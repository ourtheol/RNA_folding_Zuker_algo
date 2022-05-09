"""
Created on Mon Mar 23 18:39:26 2020

@author: Ourania Theologi

Prediction of the most stable secondary structure for a single RNA sequence by 
computing its minimal free energy (MFE) according to Zuker’s algorithm.
"""
import numpy as np
import pandas as pd

RNA = 'AAUACUCCGUUGCAGCAU'
size = len(RNA)
WC_bond = -4
GU_bond = 0
other_bond = 4       
 
#fills the V matrix (energies of globally optimal structures assuming (i,j) are paired)    
def fill_Vmatrix(row,col):
    if ((RNA[row] == 'A' and RNA[col] == 'U') or
        (RNA[row] == 'U' and RNA[col] == 'A') or
        (RNA[row] == 'C' and RNA[col] == 'G') or
        (RNA[row] == 'G' and RNA[col] == 'C')
        ):
        E1 = WC_bond + (col-row+1)   
        E2 = WC_bond + W[row+1,col-1]
        V[row,col] = min(E1, E2)
        
        if V[row,col] == E1:
            Backtrack_V[row,col] = 11
        if V[row,col] == E2:
            Backtrack_V[row,col] = 12
        if (V[row,col] == E1 and V[row,col] == E2):
            Backtrack_V[row,col] = 13
    elif ((RNA[row] == 'G' and RNA[col] == 'U') or
          (RNA[row] == 'U' and RNA[col] == 'G')
          ):
        E1 = GU_bond + (col-row+1)    
        E2 = GU_bond + W[row+1,col-1]
        V[row,col] = min(E1, E2)
        if V[row,col] == E1:
            Backtrack_V[row,col] = 11
        if V[row,col] == E2:
            Backtrack_V[row,col] = 12
        if (V[row,col] == E1 and V[row,col] == E2):
            Backtrack_V[row,col] = 13
    else:
        E1 = other_bond + (col-row+1)
        E2 = other_bond + W[row+1,col-1]
        V[row,col] = min(E1, E2)
        if V[row,col] == E1:
            Backtrack_V[row,col] = 11
        if V[row,col] == E2:
            Backtrack_V[row,col] = 12
        if (V[row,col] == E1 and V[row,col] == E2):
            Backtrack_V[row,col] = 13
    return V[row,col]


#fills the W matrix (energies of globally optimal structures)
def fill_Wmatrix(row,col):
    cut_in_k = []
    for k in range(row+2,col):
        cut_in_k.append(W[col,k] + W[k-1,row])
                    
    E1 = W[row,col-1]    #the previous cell
    E2 = W[row+1,col]    #the underneath cell    
    E3 = V[row,col]      #look at V matrix
    E4 = min(cut_in_k)   #2 bulges                            
    W[row,col] = min(E1, E2, E3, E4)

    if W[row,col] == E1:
        Backtrack[row,col] = 1
    if W[row,col] == E2:
        Backtrack[row,col] = 2
    if W[row,col] == E3:
        Backtrack[row,col] = 3
    if W[row,col] == E4:
        Backtrack[row,col] = 4

    if (W[row,col] == E1 and W[row,col] == E2):
        Backtrack[row,col] = 5
    if (W[row,col] == E1 and W[row,col] == E3):
        Backtrack[row,col] = 6
    if (W[row,col] == E1 and W[row,col] == E4):
        Backtrack[row,col] = 7
    if (W[row,col] == E2 and W[row,col] == E3):
        Backtrack[row,col] = 8
    if (W[row,col] == E2 and W[row,col] == E4):
        Backtrack[row,col] = 9
    if (W[row,col] == E3 and W[row,col] == E4):
        Backtrack[row,col] = 10

    return W[row,col]
                


# Create empty matrix
W = np.zeros((size,size))    
V = np.zeros((size,size))
Backtrack = np.zeros((size,size))
Backtrack_V = np.zeros((size,size))      

# Initialization: j + 3 > i => V (i,j) = W(i,j) = inf
for row in range(size):
    for col  in range(size):
        if col - row < 3:
            W[row,col] = np.inf
            V[row,col] = np.inf     

for n in range(3,len(RNA)+1):
    for row in range(size-n):
        for col in range(size):
            if row+n == col:
                fill_Vmatrix(row,col)
                fill_Wmatrix(row,col)
            
print(V)
print(W)
print(Backtrack)
df1 = pd.DataFrame.from_records(W)
df2 = pd.DataFrame.from_records(V)
df3 = pd.DataFrame.from_records(Backtrack)
df4 = pd.DataFrame.from_records(Backtrack_V)
df1.to_excel("W.xlsx")
df2.to_excel("V.xlsx")
df3.to_excel("Backtrack.xlsx")
df4.to_excel("Backtrack_V.xlsx")   
