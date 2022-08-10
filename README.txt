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