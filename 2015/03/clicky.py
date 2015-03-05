import turtle

class Clicky:
    def __init__(self):
        self.t = turtle.Turtle()
        self.wn = turtle.Screen()
        self.wn.onclick(self.t.goto)
    
    def main(self):
        turtle.mainloop()

Clicky().main()

