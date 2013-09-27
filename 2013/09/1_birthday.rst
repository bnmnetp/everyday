The Birthday Problem
====================

Yesterday, in class, I asked the question "How many of you have the same birthday?"  We
went through the  months of the year, and if a student had a birthday in that month they
raised their hand.  When we had multiple birthdays in the month we all shouted out our day
to see if we had any matches.  I had 23 students in the classroom, and we had no matches.
Does this surprise you?  Probably not, after all there are 365 days in the year and
only 23 students in the room, so the *probability* of a match seems low,
at least at first glance.  This raises the question, what is the probability that in
any given class of 23 students there will be at least two students with a birthday on
the same day.

To answer this question we will **avoid probability theory** and use a Monte-Carlo
simulation.

.. image::  https://www.google.com/maps/vt/data=VLHX1wd2Cgu8wR6jwyh-km8JBWAkEzU4,C6PBkg2KoOZSmqU-rme02DzVOcgdKId4xVbkByyjmwAlMK1UU7nrMH7rFd1fA4rNcmKjXK-D3dborhCQ64NfUERLsWIXLbxovaCZHue0lXKdyO8NiueTnd2Ui5ZFR_zIuhCAgltNNP5wYYjZKwioTxGDaI3acRYWhiyRWxV-7PP38DIqDR31vKbS46oNo43RslkUdcQ9

Monte Carlo is known for its racing, and its casinos, James bond:  "Shaken not stirred."
Its the casino part that is important here, games of chance, and randomness.  Monaco is
the second smallest country in the world, second only to Vatican city, and is located on
the French Riviera and, in fact, is surrounded by France.

The way we will figure out the probability that 2 or more people out of 23 share a
birthday is to randomly generate 23 birthdays and see whether any of them match.  If
we  do this many many times, then the number of times we get a matching birthday,
divided by the total number of times we try gives us a good approximation of the
probability.  We will call each of these separate tests a trial.   Lets say that we try
1000 trials.  In 490 of the trials we find a duplicate birthday. So, $490/1000 = 0.49$

So, how are we going to approach this calculation.  If we were a statistician we would
go a completely different direction, but since we are computer scientists,
we are going to do a simulation.  The first question we need to ask is how are we going
to represent, and remember each of the birthdays for each class member?
**Representation** is an important aspect of problem solving,
so we'll spend a few words talking about our representation for this problem.


It would be difficult to try to represent the birthdays in normal month/day format,
so we will use an easier representation.  That is the number of the day of the year.
If we think of January 1 as day 0 (Yes, we computer scientists insist on starting at 0)
then December 31 is day 364.  So we can represent each birthday as a single integer
number.

The next representation question is how are we going to remember all of these
birthdays?  The answer is that we will use a Python list.  If you are completely new to
Python lists, you may want to look at `this chapter <http://interactivepython
.org/runestone/static/thinkcspy/Lists/lists.html>`_.  In any case we can think of a
Python list just like any list we might write down for ourselves.  If we were  going
to make up 23 birthdates and we wanted to remember them, we would write them on a
sheet of paper, one birthday per line.  A Python list is analogous to our paper list
but we will refer to each line of our list as an **entry** in a Python list.

Counting Birthdays using Count
------------------------------

Let us start out simple, and look at how we can use the ``random`` module along with a
single list method, ``append`` to construct a list of birthdays.  Here is the code:

.. activecode:: bday_1

   import random
   classSize = 23
   birthdayList = []

   for i in range(classSize):
       newBDay = random.randrange(365)
       birthdayList.append(newBDay)

   print(birthdayList)


So, now we have a list of randomly generated birthdays, but chances are that finding a
duplicate on this list is still not an easy task, even using our human powers of
observation.  It would be even worse if we used a class size of 100.  So how can we
have Python do the work for us of deciding whether there is a shared birthday on the
list.  One easy solution is to use the list ``count`` method.  All we have to do is ask
python to systematically go through the list and count the number of times each
birthday appears on the list.  If we ever find one that appears more than once then we
know we have found a duplicate.

Here's the code for this part of the problem:

.. code-block:: python

   foundDupe = False
   for num in birthdayList:
       if birthdayList.count(num) > 1:
          foundDupe = True

Now this is a very interesting pattern that you will use to solve programming problems
many times.  The pattern is:  Assume something is False, then systematically check to
see if what we assumed can be found to be True.  In this case we assume that there are
no duplicates ``foundDupe = False``,  but then we check every number on the birthday
list to see if it appears more than once.  If it does then we know our original
assumtion was wrong and we remember that by ``foundDupe = True``.

What remains to do is to wrap both the birthday list creation loop,
and the duplicate checking loop inside an outer loop that can do this experiment many
times.  Each time ``foundDupe`` is True we know we have a shared birthday,
so for a large number of trials ``foundDupe/numTrials`` gives us an estimate of the
probability that two people share the same birthday.


.. activecode:: bday_2

   import random
   classSize = 23
   numTrials = 1000
   dupeCount = 0

   for trial in range(numTrials):
       birthdayList = []
       for i in range(classSize):
           newBDay = random.randrange(365)
           birthdayList.append(newBDay)

       foundDupe = False
       for num in birthdayList:
           if birthdayList.count(num) > 1:
              foundDupe = True

       if foundDupe == True:
           dupeCount = dupeCount + 1

   prob = dupeCount / numTrials
   print("The probability of a shared birthday in a class of ", classSize, " is ", prob)


Practice
~~~~~~~~

#. Try running this program for different class sizes to see what kind of results you
   get.  How large would the class need to be in order for the probability to exceed 0.9 ?

#. Try the program above using a larger number of trials and a smaller number of trials
   Run it several each way.  What do you notice about the consistency of the answers as
   you increase the number of trials?

#. Modify the program above to print out a table of class size and probability.  You
   will need to add yet another for loop around the ``for trial in range(numTrials)``
   loop.


Counting Birthdays using Indexing
---------------------------------

Lets look at another way of keeping track of the birthdays in our class.  Rather than
keeping a list of the day numbers, lets suppose we make a list that has 365 slots.
Each of the slots in the list represents a day of the year.  In fact lets call this
list ``year``.  Now ``year[0]`` represents January 1, the first day of the year.
similarly ``year[364]`` represents December 31.  The square brackets after the list
name are the **index operator** and allow us to access the value that is stored in that
slot of the list.  For this problem we will start out with a zero in every location.
When we generate a random birthday we will update the count of birthdays on that day in
the list by one.  Lets look at the new code for generating a random birthday list using
this method.

.. activecode:: bday_3

   import random

   classSize = 23
   year = [0]*365

   for i in range(classSize):
       newBDay = random.randrange(365)
       year[newBDay] = year[newBDay] + 1

   print(year)

This approach makes it easier for us humans to quickly scan the list for a duplicate.
If we spot a number 2 or larger its easy to see that there is.  The line ``year =
[0]*365`` uses the Python repetition operator to create a list with 365 zeros.

We can continue our two phase approach to finding a duplicate birthday by simply
iterating over every number in ``year`` looking for a number larger than 1.

.. activecode:: bday_4

   import random
   classSize = 23
   numTrials = 1000
   dupeCount = 0

   for trial in range(numTrials):
       year = [0]*365

       for i in range(classSize):
           newBDay = random.randrange(365)
           year[newBDay] = year[newBDay] + 1

       foundDupe = False
       for num in year:
           if num > 1:
              foundDupe = True

       if foundDupe == True:
           dupeCount = dupeCount + 1

   prob = dupeCount / numTrials
   print("The probability of a shared birthday in a class of ", classSize, " is ", prob)


We can actually make our program much shorter, and find a duplicate in a single pass by
rearranging the code just slightly.

.. activecode:: bday_5

    import random
    classSize = 23
    numTrials = 1000
    dupeCount = 0

    for trial in range(numTrials):
       year = [0]*365
       foundDupe = False
       for i in range(classSize):
           newBDay = random.randrange(365)
           year[newBDay] = year[newBDay] + 1
           if year[newBDay] > 1:
              foundDupe = True

       if foundDupe == True:
           dupeCount = dupeCount + 1

    prob = dupeCount / numTrials
    print("The probability of a shared birthday in a class of ", classSize, " is ", prob)


Using this new representation, allows us to check for a duplicate while we are
generating the random birthdays!  This is a bit more efficient than our previous
approach.  We could make this approach even more efficient by adding a ``break``
statement right after the ``foundDupe = True`` line.  The break statement *breaks the
loop* essentially causing it to skip the rest of the class once we have determined that
there is a birthday.  Personally, I'm not a big believer in using breaks,
so I'm not going to include it in the body of the code.  I think they are confusing,
and I can never remember what exactly they break. If you know about while loops,
you could re-write the above example to get the same behavior as using a break by using
a compound condition on the while loop.  This is much more clear,
and is always my preferred way of doing things.


Calculating the Probability using.... Probability
-------------------------------------------------

Although this post has been mostly about using the Monte-Carlo simulation method to
approximate the probability of a duplicate birthday, lets look at just a tiny bit of
probability theory, and apply the *accumulator pattern* in another setting to check our
simulation.

Now, calculating the probability of a duplicate birthday may seem like a daunting task.
But what about calculating the probability that there is not a duplicate birthday?
This is actually an easier task.  Especially if we simplify the problem to a very small
class.

Let us assume that the class only has one student.  There is a 100% chance that this
person does not share a birthday since there is not anyone else in the class.  But now
lets add a second person to the class.  What are the chances that they have a different
birthday that person one?  In fact this is pretty easy, there are 364 other days in the
year so the chances are 364/365.  How about we add a third person to the class?  Now
there are 363/365 days.  To get the overall probability that there are no shared
birthdays we just multiply the individual probabilties together.  So for a class of
three the probability of no shared birthdays is 365/365 * 364/365 * 363/365 which is
.99 or a 99% chance that there are no shared birthdays among the three classmates.

The important thing is the pattern.  We can now easily calculate the probability of no
shared birthdays using a for loop.

.. activecode:: bday_7

   prob = 1.0
   classSize = 23

   for i in range(classSize):
       prob = prob * (365-i)/365

   print("probability of no shared birthdays = ", prob)

Ok, but what about the probability that there is a shared birthday?  In fact this is
quite easy as well.  Because remember that there are only two possibilities here.  1 is
that there is a shared birthday.  The other that there is not a shared birthday.  By
definition these two probabilities must add up to 1.0.  So once we have calculated the
probability that there is not a shared birthday we can easily calculate the
probability that there is as ``1 - prob``.


Practice
~~~~~~~~

#. Modify the code above to print out the probability that there is a shared birthday.

#. Modify the code above to print out a table of probabilities.

#. Modify the code above to compute the probabilities using either of the first two
   methods, along with the last method, and compare the results.  How close does our
   Monte-carlo simulation come to the value using probability theory?

