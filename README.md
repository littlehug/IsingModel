Version: python2


# IsingModel
The Ising Model in Python

We have four sets of code in Python:

1. regular2D.py
This runs a 1 or 2D square grid Ising Model using the Metropolis algorithm. Variables are adjusted
inside the file. For a 1D model, set either n or m to 1.

2. HexagonalLattice.py
This runs a 2D hexagonal grid Ising Model using the Metropolis algorithm. This is what is referred to
as "triangular" in the assignment. Since each cell has six neighbors,
we decided to call it hexagonal rather than triangular.

3. lattice.py
This creates a lattice of arbitrary dimensions, filling it with -1 and 1 randomly. It also contains the functions that act on this lattice. 

4. metropolisModule.py
This should run a "square" Ising Model of arbitrary size and
dimension using the Metropolis algorithm. It draws in lattice.py
Usage: [Time steps] [TEMPERATURE] [Length in Dimension 1]
[Length in Dimension 2]....

5. wolffModule.py
This draws on lattice.py and runs a sqaure Ising Model using the Wolff
Algorithm. The usage is the same as lattice.py, though "time steps"
isn't meaningful in this case. Instead, the code runs through 10,000
iterations and outputs the initial and final configurations of the
grid.

We have 3 Mathematica Notebooks:

1. DataAnalysis.nb
This is what was used to generate all of the plots in the
report. Since data was saved as temporary files (because each run of
large grids generated ~30MB of data), plots will not be automatically
regenerated.

2. MathematicaPrototype.nb
This is what Anna made to understand how the algorithm worked.

3. HexagonalLattice.nb
This is what Anna made to understand what changes when we change the
geometry. 

Finally, IsingModelReport.pdf is included. 
