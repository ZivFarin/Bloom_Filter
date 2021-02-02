# Bloom Filters

#### This is assignment 14 from the [Data Structures & Intro to Algorithms](https://www.openu.ac.il/courses/20407.htm) course in [The Open University of Israel](https://www.openu.ac.il/).
#### (More about [the 'Bloom Filter' hashing method](https://en.wikipedia.org/wiki/Bloom_filter))

## Code Files:

- #### main
First, it hashes into a bloom filter the strings of the 'DB_FILE',
Then, checks which of the strings in 'CHECK_FILE' is recognized as a part of 'DB_FILE'

- #### stats_sim
Simulates two *disjointed* sets of strings,
Makes the same check made in the 'main file',
and prints a statistical analysis about the amount of mistakes made in the simulation.
(Mistakes = false-positive calls)



## Text Files:

- #### M.M.N 14.docx
The assignment main doc.

- #### "All" and "even"
Used as default inputs to be used by "main.py".

- #### More Checks *(folder)*:
Contains more inputs for "main.py".
