# import turtle
#
# myT = turtle.Turtle()
# myWn = turtle.Screen()
# myT.color('blue')
# myT.pensize(2)
# myT.speed(0)
# dist = 5
# myT.shape('circle')
# myT.shapesize(0.5,0.5,1)
#
# def left():
#    myT.goto(myT.xcor()-dist,myT.ycor())
#
# def right():
#    myT.goto(myT.xcor()+dist,myT.ycor())
#
# def up():
#    myT.goto(myT.xcor(),myT.ycor()+dist)
#
# def down():
#    myT.goto(myT.xcor(),myT.ycor()-dist)
#
# def quit():
#    myWn.bye()
#
# myWn.onkey(left,"a")
# myWn.onkey(right,"d")
# myWn.onkey(up,"l")
# myWn.onkey(down,"j")
# myWn.onkey(quit,"q")
# myWn.listen()
# # arrow keys are named Up, Down, Left, and Right
# turtle.mainloop()
#
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
