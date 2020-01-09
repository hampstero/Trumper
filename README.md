# Trumper
A Markov chain analysis based Python script that takes Donald Trump's speeches as training data and outputs new speeches.

The program uses text data from https://github.com/ryanmcdermott/trump-speeches/blob/master/speeches.txt

There are several versions of the program. The numbering following the program title is the depth of the Markov chain ex. trumper2.py uses
the previous two words to generate a new list of words to choose from. The versions that don't use integer numbering follow a pattern
based on the numbering written for example 2.5 alternates between using the previous two words and the previous three words to generate a new word.

Based on code Impractical Python projects : playful programming activities to make you smarter / Lee Vaughan chapter 9.
