.. This document is Licensed Creative Commons:
   Attribution, Share Alike by Brad Miller, Luther College 2015

Event Driven Programming
========================

Well I'm looking forward to getting back to writing some of these posts again.  And I'm excited to start with an old favorite that I will now run in the browser!

Many programs that we write in introductory computer science follow a similar pattern.  Your program starts at line 1 and runs to the end on line N.  The order of events in the program is quite predictable because Python evaluates the program top to bottom left to right.  But it doesn't have to be that way.  In fact nearly all of the programs you use daily have a different pattern.

Most of the programs you use each day following the pattern of start -- wait for the user to click something -- respond to click -- repeat forever.  This makes programming much more challenging because you can't predict the order that things will happen, your program simply must respond to **events**.  When you write a program that responds to user events this is called event driven programming.

Lets look at a simple example.  Suppose we want to write a turtle program where we have the turtle respond to a mouse click in the window.  That is, whenever a user clicks in the window, the turtle will draw a line to that spot.  Notice that we don't know when or where the user will click so we cannot anticipate where to draw the lines until the user has taken an action.

The big question in event driven programming is "how do we connect an event with our program?"  The answer goes by many names, handlers, callbacks, listeners, and others.  I prefer the term **callback.**  A callback is a piece of code (a function) that is passed as a parameter to another function which is then expected to call back the passed function at some later name.

For our example we will write a callback function called ``gotopoint`` which takes two parameters: the x and y location of where the mouse was clicked.  We will pass this function as a parameter to the ``onclick`` method provided by the turtle module.  Now the turtle module knows that whenever we click the mouse it must call our ``gotopoint`` function.  Furthermore, when it calls our function it will pass it the two parameters required to provide us with the x and y location of the mouse.  Connecting a function to an event like this is referred to as **binding** a function to an event.

.. activecode:: callbackdemo

   import turtle

   # Create our turtle and screen objects
   t = turtle.Turtle()
   wn = turtle.Screen()
   wn.setup(300,300)

   # define the callback   
   def gotopoint(x, y):
       t.goto(x,y)
    
   # connect the callback with the click event and wait
   wn.onclick(gotopoint)
   wn.listen()
   turtle.mainloop()

The turtle graphics module understands three main events

* onclick(fun)
* onkey(fun,key)
* ontimer(fun,millis)
* listen()  --  tell the screen to listen for key events

.. admonition:: Try it

   Modify the program above so that it has a callback function connected to the 'q' key.  The function that should be called is You may define your own function that takes no parameters and calls ``wn.bye()`` or you may bind ``wn.bye`` directly.
   
   Try modifying the above example to use ontimer.  Have your callback function pick a random point in the window and draw a line to it every 500 milliseconds.

   
Programming Style Diversion
---------------------------

The above example is not the best in terms of design.  We cannot have the callback function accept a turtle as an argument so we have to use a global variable to keep track of the turtle.  Most people think this is bad form at a minimum, and in larger programs it certainly can cause many problems.  For small projects with a few lines of code and where everything is in one small file, global variables can be convenient.

Lets look at two solutions to the global variable problem.  The first is really quite simple, elegant, and some would say even old-fashioned.  However it illustrates a style of programming that is very common in the Javascript language, and used to be very popular in the days of Pascal.

To keep our instance of a turtle local we will encapsulate everything from our first example inside an outer function.  We'll call this function main, just because in many programming languages your program must have a main function in order to run properly.

Closures
^^^^^^^^

.. activecode:: callbacks2

   import turtle

   def main():
       t = turtle.Turtle()
       wn = turtle.Screen()
       wn.setup(300,300)
       
       def gotopoint(x, y):
           t.goto(x,y)
   
       wn.onclick(gotopoint)
       turtle.mainloop()

   main()


As you first look at this solution it might seem a bit strange to define one function inside another function.  But it is perfectly legal and has the great property that we have not created any global variables.

When we define one function inside another we are making use of a **closure**.  The simplest way to think of a closure is as a function that has a special ability to access other variables local to the scope it was created in.  So, in our case because the environment we defined ``gotopoint`` in has a variable named ``t`` it is perfectly legal for the ``gotopoint`` function to access that variable.  Just as if it was global, only it is not!  ``t`` only exists inside the scope of main.  Now main will not return until ``mainloop`` returns.  However, ``mainloop`` will never return (remember "repeat forever") unless the ``bye`` function is called.

Object Oriented
^^^^^^^^^^^^^^^

If you don't care anymore, or if you haven't been exposed to object oriented programming yet, you can skip this next solution as it is likely to confuse things for you more than it will help.  But if you have seen some object oriented programming, then our global variable problem can easily be solved by encapsulating everything we need in a class.

.. activecode:: callbacks3

   import turtle

   class Clicky:
       def __init__(self):
           self.t = turtle.Turtle()
           self.wn = turtle.Screen()
           self.wn.setup(300,300)
           self.wn.onclick(self.t.goto)
    
       def main(self):
           turtle.mainloop()

   Clicky().main()
   
If you have written your class in Python before this solution should seem pretty straightforward.  We have instance variables for the turtle and the Screen objects rather than using global variables.  

But, what happened to our ``gotopoint`` function?  We could easily have written the following:

.. code-block:: python

   def gotopoint(self, x, y):
       self.t.goto(x,y)
       
In our ``__init__`` method we would bind the gotopoint method by calling ``self.wn.onclick(self.gotopoint)``  But why bother?  The onclick method just needs a reference to a function that takes two parameters: ``x`` and ``y``.  We already have a function that does that, and it is the ``goto`` method of the turtle.  Now that you know this you can even simplify the original example by eliminating ``gotopoint`` and passing ``t.goto`` to the ``onclick`` function.


Toys from the 60's
==================

The Etch-A-Sketch was introduced by the Ohio Art Company in 1960.  As you can see from the image, it has only two knobs that control the operation of the toy.  One for moving horizontal and the other for moving vertical.  To move at a diagonal required a bit of coordination between your right and your left hands.


.. image:: ../../_static/Classic-Etch-A-Sketch.jpg

Your assignment is to write a program that mimics the etch-a-sketch.  You will need functions to handle the following events:

* go to the left by five pixels
* go to the right by five pixels
* go up five pixels
* go down five pixels
* clear the screen (use ``reset``).

If you want to get fancy you can add some additional key events to change colors.  I will post the solution in a day or two.

.. index::  event driven, event loop
