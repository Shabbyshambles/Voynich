Tasks done:
DL of v101 of Voynich Manuscript
Wrote code to read in manuscript and clean it of metadata
(could metadata be valuable? return to analyze after initial tests)
Wrote code to get feature vector and Laplacian representation of character graph, wherein nodes are characters and how often
they come after or before other characters is the edges
Identified most common characters used

Tasks to do:
Clean up code
Come up with way to analyze graph for anomalies.(walk the graph, perhaps?)
Find other languages from similar time periods and locations and create graphs and features etc.


Notes:
The transliteration of the Voynich manuscript has been conducted by multiple people into multiple alphabets. 
The most complete one I can find is "Voynich101" or v101, so that is what I will use as a first pass
Ideally we will test on all transliterations, as different transliterations are subjective about certain details, such as:
spacing, character difference/handwriting quirks, punctuation.

The most commonly used character, ".", is most commonly used with the character "9". It in fact represents 14584/17439 uses
paired with the character. This indicates that these characters are joined in very close harmony, one perhaps modiying the other
in traditional Arabic language style. There are suggestions by experts that the text is meant to be a translation of Hebrew or Arabic,
languages scholars would have been able to read and write in that location at that time. This is for me strong evidence of this
theory. No doubt others have noticed similar patterns in their own analysis and this is the basis for the idea.
Still, the fact that there are so many unique or nearly-unique characters is fascinating. 
Is this a quirk of the handwriting, such that the characters are examples of commonly used characters but interpreted incorrectly
in the transliteration? What characters are they used alongside? Hebrew contains 22 unique characters, and this text contains ~175,
so I doubt it could be that, even if hebrew has characters that alter other characters. Unless each unique alteration is contained 
within its own character, but then why would the previously indicated pair be so closely related if they were not modifying?
Perhaps they represent the most common vowel and consonant sound, and that explains it? "Is", or some such? There are certainly outsize use of 
"." beyond its use alongside "9", but little use of "9" without ".", which is also fascinating. Perhaps it indicates some term peculiar to the
subject matter, but of supreme importance to it? For instance, if it were a treatise on plants one would expect the word plant to be often used 
and thus "a" and "n" would recieve greater relationship than normal.
What is the next most used character, and how often is THAT used without "."?  



Current approach:
The idea is to model strings of words as graphs and examine them for patterns.
We use a Laplacian where each character represents a node, each seperate instance of one letter connecting to another letter is considered an "edge"
Each characters usage in the text will be its "node feature".

Modeling sentences as graphs of probabilities, can a GNN crack the Voynich Manuscript if trained on grammars of other languages 
present in the same region and time period

Tasks:
Build a simple GNN to gain familiarity with the methodology using toy examples and easy graphs

Research era and location of discovery of Voynich Manuscript

Any languages found in that era/location that have known translations available online?

DL Voynich Manuscript full text transliteration

Clean transliteration of metadata

Concerns:
What if Manuscript text is not the location of its information? There exist pictures and other qualities that may be used to
convey information.

What if it uses a cypher to obscure grammatical elements? 