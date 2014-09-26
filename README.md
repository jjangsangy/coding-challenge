## PhotoShop.py

### Part 1.

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
