Rolling the Dice
================

.. figure:: dice.jpg
   :caption: Image used under Creative Commons SA (https://www.flickr.com/photos/tomitapio/)

A die makes a nice example of a simple object that we can model with a Python class.  We have a couple of simple instance variables, such as the the possible values (number of sides) and the current value.  A Die object also has one simple method -- ``roll``.  This method will simply get a new current value for the die.

.. activecode:: die1
   :language: python

    import random

    random.seed(42)

    class MSDie:
        def __init__(self, num_sides):
            self.num_sides = num_sides
            self.roll()

        def getValue(self):
            return self._value

        def roll(self):
            self._value = random.randrange(self.num_sides) + 1
            return self._value

        def __str__(self):
            return str(self._value)

    d = MSDie(6)
    for i in range(5):
        d.roll()
        print(d)


This simple example gives us a lot to explore:

* How can I protect the value of the die?
* What is ``__str__`` all about?
* What if I want to have a dice with 10, Jack, Queen, King, Ace, Joker as the values?
* How come I always get the same sequence of numbers when I run the example above?
* How does this random stuff really work?  When I am programming where do these random numbers come from?
