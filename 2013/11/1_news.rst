A Better Way to Read the News
=============================

Once again I find myself inspired by an XKCD cartoon:

.. image:: http://imgs.xkcd.com/comics/substitutions.png

My goal for class today was to introduce Python Dictionaries.  I've often introduced dictionaries in the past by writing an english to pirate translator.   This just seemed like too much fun to pass up.

We are going to begin by looking at two ways we can translate a news article, but the key idea is the same either way.  The key is in the use of a **Map**.  A map allows us to associate one object with another.  Just like the example above, where the string "senator" is associated with the string "elf-lord".

The outline for our translator is as follows:  For each of the strings on the left side of the arrow, we want to search the article, and replace those strings with the strings on the right hand side of the arrow.

So, the question is how do we represent a map in Python?  Here is one example of how we might do it using lists, and the idea of "parallel construction."  Lets make a list called ``boring_news`` to keep track of the words on the left, and another list called ``xkcd`` to keep track of the words on the right.

::

    boring_news  =  ['witnesses',
                     'allegedely',
                     'new study',
                     'rebuilt',
                     'space',
                     'google glass',
                     'smartphone',
                     'electric',
                     'senator',
                     'speaker',
                     'car',
                     'election',
                     'congressional leaders',
                     'homeland security',
                     'could not be reached for comment',
                     'republican',
                     'democrat']

    xkcd = ['dudes I know',
            'kinda probably',
            'tumblr post',
            'avenge',
            'spaace',
            'virtual boy',
            'pokedex',
            'atomic',
            'elf-lord',
            'high elf-lord',
            'cat',
            'eating contest',
            'river spirits',
            'homestar runner',
            'is guilty and everyone knows it',
            'orc',
            'hobbit']
    

Now to map a word in the ``boring_news`` list to a word in the ``xkcd`` list, we simply need to find the index of the word in ``boring_news`` and then retrieve the word from ``xkcd``.

In keeping with the simple example from above lets write a function that can take one word as a parameter, find the word in ``boring_news`` and return the word from ``xkcd``.

.. activecode:: news_1

    boring_news  =  ['witnesses',
                     'allegedely',
                     'new study',
                     'rebuilt',
                     'space',
                     'google glass',
                     'smartphone',
                     'electric',
                     'senator',
                     'speaker',
                     'car',
                     'election',
                     'congressional leaders',
                     'homeland security',
                     'could not be reached for comment',
                     'republican',
                     'democrat']

    xkcd = ['dudes I know',
            'kinda probably',
            'tumblr post',
            'avenge',
            'spaace',
            'virtual boy',
            'pokedex',
            'atomic',
            'elf-lord',
            'elf-lord',
            'cat',
            'eating contest',
            'river spirits',
            'homestar runner',
            'is guilty and everyone knows it',
            'orc',
            'hobbit']

    def changeWord(word):
        if word in boring_news:
            idx = boring_news.index(word)
            return xkcd[idx]
        else:
            return word


    print(changeWord('senator'))
    print(changeWord('python'))

Now lets suppose we have a news article that reads as follows:

    Senator johnson was caught stealing a smartphone on election night.  witnesses say that he allegedly took the smartphone from a kindly old lady while she was washing her electric car. republican and democrat congressional leaders have vowed to hold hearings.  Senator johnson could not be reached for comment.

.. tabbed:: translate_tabs

   .. tab:: Question
   
      See if you can write the code to translate the above news article into xkcd speak.
      
      .. actex:: trans_q1
      
   .. tab:: Solution
   
      Lets think about solving this problem in the following way:
      
      1.  We have some boring news text.
      2.  We have a list of words that we can use to "spice up" our news.
      3.  We want to replace the boring words in the original news article with the spicier versions.
      
      Here are some things we know how to do:
      
      1.  We know how to replace a particular substring by another using the ``replace`` method.
      2.  We know how to iterate over a list of objects.
      3.  We know that quite often we can use the computer's speed to just do the same boring repetitive job over and over again.
      
      So, the solution to our problem can be stated as follows:  For each word in ``boring_news`` replace try to replace the ``boring_news`` string in the news article with the ``xkcd`` string.
      
      .. activecode:: trans_soln1

         boring_news  =  ['witnesses',
                          'allegedely',
                          'new study',
                          'rebuilt',
                          'space',
                          'google glass',
                          'smartphone',
                          'electric',
                          'senator',
                          'speaker',
                          'car',
                          'election',
                          'congressional leaders',
                          'homeland security',
                          'could not be reached for comment',
                          'republican',
                          'democrat']

         xkcd = ['dudes I know',
                 'kinda probably',
                 'tumblr post',
                 'avenge',
                 'spaace',
                 'virtual boy',
                 'pokedex',
                 'atomic',
                 'elf-lord',
                 'elf-lord',
                 'cat',
                 'eating contest',
                 'river spirits',
                 'homestar runner',
                 'is guilty and everyone knows it',
                 'orc',
                 'hobbit']

         article = '''Senator johnson was caught stealing a smartphone on election
         night.  witnesses say that he allegedly took the smartphone from a kindly old
         lady while she was washing her electric car. republican and democrat
         congressional leaders have vowed to hold hearings.  Senator johnson could not be reached for comment.'''

         def translateNews(article, boringWords, funWords):
             article = article.lower()
             for idx in range(len(boringWords)):
                 article = article.replace(boringWords[idx],funWords[idx])
             return article

         print(translateNews(article,boring_news,xkcd))

This parallel construction solution works, in fact, it works quite well for our small
example, but in larger, real world problems it can be quite slow to search through a list
to find a particular word.  There is a better way.

This better way involves the Python object known as a `dictionary
<http://interactivepython.org/runestone/static/thinkcspy/Dictionaries/dictionary.html>`_
.  Python
dictionaries
provide a general purpose way to do mapping.     Just like our parallel lists mapped
from one word to another a Python dictionary provides us with with that same
capability, only faster and a little easier than using two lists.   In fact the Python
dicionary is a general purpose mapper that allows you to associate a **key** with a
**value**.  A key can be any immutable Python object, and a value can be any Python
object at all.  Very often a key will be a string.

We can represent that XKCD word map we've been using a Python dictionary,
and some familiar indexing notation.

.. activecode:: dict_map1

   wordMap = {}
   wordMap['witnesses'] = 'dudes I know'
   wordMap['allegedly'] = 'kinda probably'

   print(wordMap['witnesses'])


The string inside the square brackets is the key, and the string on the right hand side
of the assignment statement is the value.  Notice that in the final line we can look
up a key and get its value to print by just using the square bracket notation.  There
is also a dictionary method you can use called ``get``.   These two things are the
same:  ``wordMap['witnesses']``  and  ``wordMap.get('witnesses')``  Using one or the
other is largely a matter of personal taste.  I prefer the square brackets since they
are consistent with the notation used to index into strings or lists.


Since we already have two lists with all
the values typed in, we don't need to retype the entire dictionary.  Lets create a
dictionary from our two initial lists as follows:


.. activecode:: dict_map2

    boring_news  =  ['witnesses',
                     'allegedely',
                     'new study',
                     'rebuilt',
                     'space',
                     'google glass',
                     'smartphone',
                     'electric',
                     'senator',
                     'speaker',
                     'car',
                     'election',
                     'congressional leaders',
                     'homeland security',
                     'could not be reached for comment',
                     'republican',
                     'democrat']

    xkcd = ['dudes I know',
            'kinda probably',
            'tumblr post',
            'avenge',
            'spaace',
            'virtual boy',
            'pokedex',
            'atomic',
            'elf-lord',
            'elf-lord',
            'cat',
            'eating contest',
            'river spirits',
            'homestar runner',
            'is guilty and everyone knows it',
            'orc',
            'hobbit']

    wordMap = {}
    for idx in range(len(boring_news)):
        key = boring_news[idx]
        value = xkcd[idx]
        wordMap[key] = value



Now using the newly created dictionary see if you can re-write the program to translate
the entire news article.  Just add it to the bottom of the activecode box above.  When
you have tried it on your own, then click the show button below to reveal the solution
and a few comments.


.. reveal:: myreveal

   .. activecode:: newtrans

      def translateNews(article, translationDict):
          for key in translationDict:
              article = article.replace(key,translationDict[key])
          return article


   For purposes of illustration lets look at another way to write this same function:

   ::

      def translateNews(article, translationDict):
          for key,value in translationDict.items():
              article = article.replace(key,value)
          return article


If this is your first time using Python dictionaries I suggest you take a few minutes
to read through the chapter on dictionaries `here <http://interactivepython
.org/runestone/thinkcspy/Dictionaries/dictionaries.html>`_.


In my next post we'll look at a program that can automatically retrieve a story from
the web and translate the article for you.
