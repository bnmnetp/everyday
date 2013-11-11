A Better Way to Read the News
=============================

Once again I find myself inspired by an XKCD cartoon:

.. image:: http://imgs.xkcd.com/comics/substitutions.png

My goal for class today was to introduce Python Dictionaries.  I've often introduced dictionaries in the past by writing an english to pirate translator.   This just seemed like too much fun to pass up.

We are going to begin by looking at two ways we can translate a news article, but the key idea is the same either way.  The key is in the use of a **Map**.  A map allows us to associate one object with another.  Just like the example above.  Where the string "senator" is associated with the string "elf-lord".

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
            'elf-lord',
            'cat',
            'eating contest',
            'river spirits',
            'homestar runner',
            'is guilty and everyone knows it',
            'orc',
            'hobbit']
    



