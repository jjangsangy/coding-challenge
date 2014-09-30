#!/usr/bin/env python
"""
To run this program as an executible and submit a
with a proper csv file as the first argument.

    >>> ./PhotoShop.py path/to/file

You can also supply your own python interpreter.

    >>> python3 PhotoShop.py path/to/file

"""

from __future__ import print_function

import csv
import os
import sys
import time

from threading import Thread, Event
from collections import namedtuple


Customer = namedtuple('Customer', ['name', 'photos'])


class Developer(Thread):

    """
    Developer Worker class.

    Inherits from Threading module for performing
    synchronous lock based concurrency.

    param: dev   ->  The name used to identify each thread worker instance
    param: queue ->  A Filled Task Queue ADT

    returns: None

    Note: This class is only thread safe due to the lack of a Producer.
          Once it becomes necessary to manage both reads and writes from
          the queue, it will be necessary to swap to a managed ThreadSafeQueue.
    """

    def __init__(self, name, queue):
        Thread.__init__(self)
        self.queue = queue
        self.name = name

    def run(self):
        """
        Overloading thread handler
        """
        while not self.queue.is_empty():
            client, film = self.queue.dequeue()
            wait = self.wait_time(film)

            print('Developer: [{name:6}]\t Client: {client:10} Images: {film:3} \t Time: {wait:3} sec'.format(
                name=self.name,
                film=film,
                client=client,
                wait=wait,
            ))

            sys.stdout.flush()
            time.sleep(wait/10)

    @staticmethod
    def wait_time(film):
        """Calculate the wait time for developing a roll of film"""
        leftover = film % 10
        return (film - leftover) + leftover*3


class PhotoQueue(object):

    """An abstract queue data type"""

    def __init__(self):
        self._jobs = []

    def __repr__(self):
        return '<PhotoQueue [{0}]>'.format(self.__len__())

    def __iter__(self):
        """Implement iterator protocol"""
        return reversed(self._jobs)

    def __len__(self):
        """Gets the size of the queue"""
        return len(self._jobs)

    def is_empty(self):
        if not self._jobs:
            return True
        return False

    def enqueue(self, customer):
        """Takes in a Customer and adds them to the queue."""
        return self._jobs.insert(0, customer)

    def dequeue(self):
        """Returns a customers completed job"""
        return self._jobs.pop()


def reader(filepath):
    """
    Reads from the filesystem and performs unpacking into task queue

    Parameters:
    filepath:   str -> qualified filesystem path

    Returns:
    <PhotoQueue> objects enqueued with customer information.
    """
    q = PhotoQueue()
    with open(filepath, 'rt') as fp:

        reader = csv.reader(fp)
        for row in reader:

            # Skip Incorrect Customer Submissions
            if len(row) != 2:
                print('Row {row} did not supply valid input'.format(
                    row=','.join(list(row)))
                )
                continue

            name, photos = row

            # Type Cast
            try:
                photos = int(photos)
            except ValueError:
                print('Could not convert {photos} to an integer'.format(
                    photos=photos
                    ))
                continue

            customer = Customer(name, photos)

            # Merge double entries into a single job.
            for index, entry in enumerate(q._jobs):
                if entry.name == customer.name:
                    q._jobs.remove(entry)
                    customer = entry._replace(
                        photos=(entry.photos + customer.photos)
                    )
                    q._jobs.insert(index, customer)
                    break
            else:
                q.enqueue(customer)

    return q


def main(filepath):
    """
    The Customer namedtuple is an immutible primitive data
    type managed by the Task Queue.
    """
    # Input Validation
    assert(os.path.isfile(filepath))

    taskqueue = reader(filepath)

    for worker in ('Apple', 'Google'):
        work = Developer(worker, taskqueue)
        work.start()
        time.sleep(0.1)

    try:
        while work.is_alive():
            work.join(timeout=1)
    except (KeyboardInterrupt, SystemExit):
        print('\nCtrl-C Detected: Exiting Gracefully')
        work.queue._jobs = None
        print('Waiting for threads to finish')

    return

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
