from __future__ import print_function

import csv
import sys
import time

from threading import Thread
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

    def __init__(self, dev, queue):
        Thread.__init__(self)
        self.dev = dev
        self.queue = queue

    def run(self):
        """
        Overloading thread handler
        """
        while not self.queue.is_empty():

            client, film = self.queue.dequeue()
            wait = self.wait_time(film)

            print('Developer: [{name:6}]\t Client: {client:10} Images: {film:3} \t Time: {wait:3} sec'.format(
                name=self.dev,
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
            name, photos = row
            q.enqueue(Customer(name, int(photos)))

    return q


def main(filepath):
    """
    The Customer namedtuple is an immutible primitive data
    type managed by the Task Queue.
    """
    taskqueue = reader(filepath)

    for worker in ('Apple', 'Google'):
        work = Developer(worker, taskqueue)
        work.start()

    return


if __name__ == '__main__':

    main(sys.argv[1])
