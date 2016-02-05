.. This document is Licensed Creative Commons:
   Attribution, Share Alike by Brad Miller, Luther College 2015

Etch Solution
=============

Here is the first attempt at a solution to make a simple etch a sketch program using events and the turtle.  It has the same global variable issues as our first mouse click program yesterday, but it will work.  

Lets start by looking at a general outline of the program, as that is a good example of the way that many event driven programs operate.

1.  Initialize the turtle and the window objects
2.  Set up colors and speeds and initialize a couple of constants
3.  Write the callback functions to handle the events we want to handle.
4.  Bind our callback functions to the events.
5.  Enter the event loop


.. activecode:: etcheasy

   import turtle

   myT = turtle.Turtle()
   myWn = turtle.Screen()
   myT.color('blue')
   myT.pensize(2)
   myT.speed(0)
   dist = 2
   myT.shape('circle')

   def left():
      myT.goto(myT.xcor()-dist,myT.ycor())

   def right():
      myT.goto(myT.xcor()+dist,myT.ycor())

   def up():
      myT.goto(myT.xcor(),myT.ycor()+dist)

   def down():
      myT.goto(myT.xcor(),myT.ycor()-dist)

   def quit():
      myWn.bye()

   myWn.onkey(left,"a")
   myWn.onkey(right,"d")
   myWn.onkey(up,"l")
   myWn.onkey(down,"j")
   myWn.onkey(quit,"q")
   myWn.listen()

   turtle.mainloop()


The solution above is done to very closely approximate the real etch-a-sketch.  Your left hand moves the point left and right while your right hand moves the point up and down.  Drawing a diagonal line is quite tedious!  Of course with a keyboard to work with we can really improve our drawing experience.  You could modify the program above to use the arrow keys on your keyboard.  "Up" and "Down" could allow the turtle to go forward and backward, while "Left" and "Right" could turn the turtle by a few degrees.  You may also want to improve the program by adding some key events to allow your users to select a color for the turtle.   You could also add a reset key that would erase the current picture.


Just for the sake of completeness for you object oriented programmers following along, here is a version that encapsulates our Etch-a-Sketch inside a class.

.. activecode:: etchfinal

   import turtle

   class Etch(turtle.Turtle):
      def __init__(self):
          turtle.Turtle.__init__(self)
          self.myWn = turtle.Screen()
          self.color('blue')
          self.pensize(2)
          self.speed(0)
          self.dist = 5
          self.myWn.onkey(self.up,"l")
          self.myWn.onkey(self.down,"j")
          self.myWn.onkey(self.left,"a")
          self.myWn.onkey(self.right,"d")
          self.myWn.onkey(self.quit,"q")
          self.myWn.listen()

      def up(self):
          self.goto(self.xcor(),self.ycor()+self.dist)

      def down(self):
          self.goto(self.xcor(),self.ycor()-self.dist)

      def left(self):
          self.goto(self.xcor()-self.dist,self.ycor())   

      def right(self):
          self.goto(self.xcor()+self.dist,self.ycor())   

      def quit(self):
          self.myWn.bye()

      def main(self):
          turtle.mainloop()

   if __name__ == '__main__':
      etch = Etch()
      etch.main()

The above solution is actually a great example of using inheritance.  In the previous post we had a simple class that made a turtle and stored it away as an instance variable.  In this case we don't need an instance variable because we are Making our Etch object a subclass of Turtle.  This means that an Etch object can do everything a regular turtle can do but we are giving it some specialized behavior.  In particular we are redefining the behavior of ``up,`` ``down,`` ``left,`` and ``right.`` 

