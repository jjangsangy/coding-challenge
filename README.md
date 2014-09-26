## PhotoShop.py

### Part 1

This programming assignment is an exercise in OOP, flow control, and I/O.

Assume a dark room that processes photos has one person in there developing
photos. In this world, it takes the person 3 seconds to develop one photo.
However, there is a special machine that is able to process each photo in 1
second if you run exactly 10 photos through it at a time. For example, if a
customer gave this dark room 23 photos, it will take 29 seconds as opposed to
69 seconds to process. I do not expect the time adjustment to be translated to
the exact second in terms of computation time. Let's assume for the sake of
time, 1 second of photo development time = 100 ms in CPU time. Using the above
example, 29 seconds = 2.9 seconds in actual CPU time.

The photo developer can only handle one customer at a time. In other words,
each customer's batch of photos should be treated as an atomic unit. That way,
the photo developer does not mix and match different customers' photos with
other'.

When designing the solution, architect it in an object-oriented way
(e.g. Photo, Customer, Developer, and Dark Room objects). I've attached a .csv for input.
It's comma separated by the person's name and the number of photos they want
processed, e.g the first person in the file is the first customer in the queue,
and the last person is the last customer in the queue.

I expect the solution to be documented and able to run on the command line. Additionally,
I want to see the total time it takes for each person's photos to be processed
printed out. I do not care what language you choose to write it in.

### Part 2

Now, let's tweak the parameters a bit.

Assume that there are two photo developers working concurrently. Each photo
developer is still only able to handle one customer at a time. As soon as one
photo developer finishes a job, he will service the next customer in the
queue.

Also, I want you to execute flow control this time. Namely, when I run this, I
should not expect the output to be printed all out at once. In fact, I should
expect a noticeable delay between various jobs in accordance to our photo
development to actual CPU time translation scheme.

I'll explain a bit more in detail. For example, Sue and Dave are the first two
customers. Since we now have two photo developers working full-time, they can
service Sue and Dave at the same time.

Assuming both photo developers (let's call them A and B) start servicing the
first two customers at the same time, photo developer A would finish first
since Sue's photos would take 22 seconds to process whereas photo developer B
would take 27 seconds to process Dave's. Then, photo developer A would move on
to the next customer in line, which would be Kyle.

In the print out statements, I would like to see which photo developer worked
on a specific customer's photos. There might be some cases where photo
developer A will finish processing two customers' photos before photo
developer B finishes one customer's batch.

This exercise will test you on __threading__, __concurrency__, and __flow control__
(e.g. using a sleep function to control execution time). Let me know if you have any
questions.
