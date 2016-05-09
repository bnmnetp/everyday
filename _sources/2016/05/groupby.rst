.. description:: A look at the itertools groupby function, makes a common iteration pattern easy.

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


Line 6 is the key part of the pattern.  While we are still working with the same group, we accumulate data.  If the key has changed, which indicates we have moved on to a new group then:

* Process the old group
* initialize the next group

Notice that it is crucial for this to work that the input data is **sorted** by month.  Otherwise we could get a real mixture of output.

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
   :datafile: salesdata

   from itertools import groupby

   with open('salesdata','r') as f
       mylist = [(line.strip().split('|')) for line  in f]

   groups = groupby(mylist, key=lambda x: x[0])
   for month, group in groups:
       saleslist = [float(x[2]) for x in group]
       total = sum(saleslist)
       average = total / len(saleslist)
       print(month, total, average)

The solution is a lot shorter, which is always nice, but more importantly it is always going to be correct.  No groups accidentally left out, no values that are incorrectly initialized or reinitialized.  However with that power there is a lot happening in those few lines that might seem pretty mysterious.  Lets start with line 4.  This transforms our file into a list of lists that looks like this::

    [['December', 'Toys', '200.3'], ['December', 'Games', '125.9'], ['December', 'Cars', '361.4'], ['January', 'Games', '450.9'], ['January', 'Cars', '229.25'], ['January', 'Toys', '22.5'], ['March', 'Games', '14.73'], ['March', 'Toys', '923.1'], ['March', 'Cars', '675.2']]

Technically this step is not needed, but it does make the rest of the code easier to follow.  The key is line 6, which creates a grouping object for us. The grouping object consists of a key, and a group of values.  The key is provided by the ``lambda`` function that simply says for each list of values, use the value at index position 0 as the key.  If you haven't used lambda functions before you could think of it as though you have written a function ``getMonth`` which takes a list as a parameter and always returns the item at index position 0.

.. code-block:: python

    def getMonth(alist):
        return alist[0]

Now line 6 would look like: ``groups = groupby(mylist, getMonth)``  This is perfectly fine, the lambda expression just makes it easier for us to create one of these little functions that we really are not going to use for anything else.  The syntax of a lambda is:  ``lambda param, param, ...: expression``  lambdas are limited to a single expression that results in a value to return.

Still confused?  Here is another example:

.. activecode:: simplegrouptuple
   :language: python3

   from itertools import groupby
   tlist = [('a',1), ('a',2), ('a',3), ('b',1), ('b',2), ('c',1), ('c',2), ('c',3), ('d',1) ]

   groups = groupby(tlist, key=lambda x: x[0])
   for key, group in groups:
    print("{}:".format(key))
    for thing in group:
        print("    {}".format(thing))

Notice that the thing printed in the loop on line 6 includes both elements of the tuple, the key and the value.  Change the print statement so that it only prints out the value using ``format(thing[1])`` to get a little nicer output.

But I want to group by category
-------------------------------

Now that we can group, you may be thinking but I want to group by the category not the month.  And you might think, hey, this is easy.  I'll just change that nifty little lambda to use the category column as the key and everything will be cool.

.. code-block:: python

   with open('salesdata', 'r') as f:
       mylist = [(line.strip().split('|')) for line in f]

   print(mylist)
   groups = groupby(mylist, key=lambda x: x[1])
   for month, group in groups:
       saleslist = [float(x[2]) for x in group]
       total = sum(saleslist)
       average = total / len(saleslist)
       print(month, total, average)

This might seem right, but you would get the following output::

    Toys 200.3 200.3
    Games 125.9 125.9
    Cars 361.4 361.4
    Games 450.9 450.9
    Cars 229.25 229.25
    Toys 22.5 22.5
    Games 14.73 14.73
    Toys 923.1 923.1
    Cars 675.2 675.2

That is definitely not what you were looking for!  The important thing to remember is that sequence of items must be sorted by the key you want to group by!  So in order to make the example above work right we need to sort ``mylist`` by the second column of values, not the first.  We can do that easily using the ``sorted`` function.

.. code-block:: python

    with open('salesdata', 'r') as f:
        mylist = sorted([(line.strip().split('|')) for line in f],
                        key=lambda x: x[1])

Here again we employ the lambda function to provide the sort key for how we want my list to be sorted.  With this small change we can get the correct report, organized by category.

Once you understand how to use it, the groupby operator is a powerful new tool for your programming toolbox.  It is cleaner, easier to understand and less error prone than the old method.
