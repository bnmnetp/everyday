Iterating over Groups of Things
===============================

There is a programming pattern, that I was taught in my first course.  The problem is this:  You are iterating over a bunch of things that are sorted, and it turns out there are groups of things.  You want to keep track of the group you are in, and after you have accumulated all of the elements in a particular group you want to do something with them.

For example, in my data structures class, we are writing a program to play the kevin bacon game.  so we have a huge file of movie,actor pairs that looks like this:

::

    Toy Soldiers (1991)|R. Lee Ermey
    Toy Soldiers (1991)|Wil Wheaton
    Toy Soldiers (1991)|Sean Astin
    Toy Soldiers (1991)|Keith Coogan
    Toy Soldiers (1991)|Andrew Divoff
    Toy Story (1995)|Don Rickles
    Toy Story (1995)|Tom Hanks
    Toy Story (1995)|Wallace Shawn
    Toy Story (1995)|Tim Allen
    Toy Story (1995)|Jim Varney
    Toy Story 2 (1999)|Tim Allen
    Toy Story 2 (1999)|Tom Hanks
    Toy Story 2 (1999)|Don Rickles

We want to make a list of all of the actors in the same movie, and then add edges between the nodes in a graph that represents a social graph of actors that have acted together.   We would like to think of it like the following:

.. code-block:: python

   toysoldiers = ['R. Lee Ermey', 'Wil Wheaton', 'Sean Astin', ...]
   Toystory = ['Don Rickles', 'Tom Hanks', 'Tim Allen', 'Jim Varney', ...]

if we had those lists made for us it would be easy.  But we need to make them by collecting all of the actors that have the same movie name on the right.

I've also been thinking about grouping things a lot as I've been preparing for my new data science classes.  In data science you often want to produce summary statistics about groups of things.  For example:

.. datafile:: salesdata

   December|Toys|200.3
   December|Games|125.9
   December|Cars|361.4
   January|Games|450.9
   January|Cars|229.25
   January|Toys|22.5
   March|Games|14.73
   March|Toys|923.1
   March|Cars|675.2

Suppose we want to see the average and total sales for each month?

::
    December: 687.6 229.2
    January: 702.65 234.22
    March: 1613.03 537.68

The usual way to do this would be

.. activecode:: totalsales
   :language: python

   f = open('salesdata','r')
   prev_month, category, sales = f.readline().strip().split('|')
   saleslist = [float(sales)]
   for line in f:
        month, category, sales = line.strip().split('|')
        if month == prev_month:
            saleslist.append(float(sales))
        else:
            total = sum(saleslist)
            average = total / len(saleslist)
            print(prev_month, total, average)
            saleslist = [float(sales)]


Line 6 is the key part of the patter.  While we are still working with the same group, we accumulate data.  If the key has changed, which indicates we have moved on to a new group then:

* Process the old group
* initialize the next group

This is an age old pattern that everyone should learn, but is a pattern that is easy to mess up, and I see lots of off by one mistakes with code like this. In fact the code as written above suffers from two problems.  I just wrote it for this posting without testing it.  As soon as I ran it I realized I had made two very common mistakes.  Can you see what they are?

.. reveal:: showmistakes

   1. Not correctly resetting ``prev_month`` we need to add the line: ``prev_month = month`` in the else clause.
   2. I have completely lost the last group!  When the for statement runs out of lines in the file, I don't get the opportunity to handle the final group!  Fixing this requires redoing the code substantially.


.. activecode:: totalsales2

   f = open('salesdata', 'r')
   prev_month, category, sales = f.readline().strip().split('|')
   saleslist = [float(sales)]
   done = False
   while not done:
       line = f.readline()
       if line:
           month, category, sales = line.strip().split('|')
       else:
           done = True
       if not done and month == prev_month:
           saleslist.append(float(sales))
       else:
           total = sum(saleslist)
           average = total / len(saleslist)
           print(prev_month, total, average)
           saleslist = [float(sales)]
           prev_month = month

Enter itertools
---------------

However, I've recently been exploring the itertools package. which offers us a completely different, and potentially much better way of handling groups by letting Python take care of the bookkeeping for grouping.

.. activecode:: totalsales
   :language: python3

   from itertools import groupby

   with open('salesdata','r') as f
       mylist = [(line.strip().split('|')) for line  in f]

   groups = groupby(mylist, key=lambda x: x[0])
   for month, group in groups:
       saleslist = [float(x[2]) for x in group]
       total = sum(saleslist)
       average = total / len(saleslist)
       print(month, total, average)

The solution is a lot shorter, which is always nice, but there is a lot happening in those few lines.  Lets start with line 4.  This transforms our file into a list of lists that looks like this::

    [['December', 'Toys', '200.3'], ['December', 'Games', '125.9'], ['December', 'Cars', '361.4'], ['January', 'Games', '450.9'], ['January', 'Cars', '229.25'], ['January', 'Toys', '22.5'], ['March', 'Games', '14.73'], ['March', 'Toys', '923.1'], ['March', 'Cars', '675.2']]

Technically this step is not needed, but it does make the rest of the code easier to follow.  The key is line 6, which creates a grouping object for us. The grouping object consists of a key, and a group of values.  The key is provided by the ``lambda`` function that simply says for each list of values, use the value at index position 0 as the key.
