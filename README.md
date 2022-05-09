## Prediction of the most stable secondary structure for a single RNA sequence by computing its minimal free energy (MFE) according to Zuker’s algorithm.

I created a function that fills the V matrix (energies of globally optimal structures assuming (i,j)
are paired): ​ fill_Vmatrix​ and ​ ​ a function that fills the W matrix (energies of globally optimal
structures): ​ fill_Wmatrix, ​ according to Zuker’s algorithm. While the W matrix is filled, the way
that each energy value is assigned to each cell is stored in the Backtrack matrix. While the V
matrix is filled, the information if the minimum free energy is calculated because of hairpins or
because of stacking regions of (i,j) that base pair is stored in the Backtrack_V matrix.

1. Create empty matrices V, W, Backtrack, Backtrack_V of size nxn, where n: the
nucleotide count.
2. Initialization: Fill the cells of the V and W matrices underneath the 3rd diagonal
(counting from 0) ​ ​ with infinite.
3. Fill the two matrices V and W diagonally starting from the 3rd diagonal according to
Zuker’s algorithm and store information of how the filling happened in the Backtrack and
in the Backtrack_V matrices.

The Backtrack matrix shows from which cell the minimum value was calculated from, using the
following numbers:
1 : previous cell
2 : down cell
3 : V matrix
4 : k

Since there is the possibility that two energy values might be equal and minimum I also included
these cases in the Backtrack matrix:
5 : previous cell and down cell (1 and 2)
6 : previous cell and V matrix (1 and 3)
7 : previous cell and k (1 and 4)
8 : down cell and V matrix (2 and 3)
9 : down cell and k (2 and 4)
10 : V matrix and k (3 and 4)
In the Backtack_V it is stored if the minimum energy comes from a hairpin or from a stacking
region:
11 : hairpin
12 : stacking

V matrix:

![V matrix:](https://github.com/ourtheol/RNA_folding_Zuker_algo/blob/main/Pictures/Vmatrix.png)

W matrix:

![W matrix:](https://github.com/ourtheol/RNA_folding_Zuker_algo/blob/main/Pictures/Wmatrix.png)

Backtrack matrix:

The secondary structures of the given RNA sequence can be identified by the Backtrack matrix.
The following Backtrack matrix corresponds to 4 secondary structures of the given RNA sequence:

![Backtrack matrix:](https://github.com/ourtheol/RNA_folding_Zuker_algo/blob/main/Pictures/Backtrackmatrix.png)

Backtrack_V matrix:

![Backtrack_V matrix:](https://github.com/ourtheol/RNA_folding_Zuker_algo/blob/main/Pictures/Backtrack_V%20matrix.png)

Optimal folds:

![Optimal folds:](https://github.com/ourtheol/RNA_folding_Zuker_algo/blob/main/Pictures/folds.png)





