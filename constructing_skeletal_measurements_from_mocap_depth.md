### Notes from November 16

# From Motive
Constructing skeletal measurements from Motive
* manually find skeleton in T pose
* randomly sample 20 other frames
Compute skeletal measurements via distances between labeled nodes: details are in [HERE], for variables [xyz]


# From RGB inferred pose/skeleton
More directly comparable

Compute skeletal measurements


# Ideal table we want to create

Data collection mode | tape measure | RGB frame 1 | RGB frame avg | depth camera | mocap etc.

where for each row, how each skeletal measurement is defined: 

body measurement | description of measurement | process to infer that measurement in this data and where it is saved | etc. |...
standing height | feet to head with tape measure | difference between x and y calculated via this input processed through this | etc.
biachromial breadth | ... | ... | 
