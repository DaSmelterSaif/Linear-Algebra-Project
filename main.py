# Self note: Use np.array for easier matrix manipulation


import numpy as np

# Coefficients of the equations (aij)
equ_1 = []
equ_2 = []
equ_3 = []
# Constants of the equations (bi)
const = []

############ Input ############
print("Enter the 3 coefficients of 3 equations:")
print("-------------------")

for i in range(3):
    equ_1.append(float(input(f"a1{i+1}: ")))

for i in range(3):
    equ_2.append(float(input(f"a2{i+1}: ")))

for i in range(3):
    equ_3.append(float(input(f"a3{i+1}: ")))

print()
print("Enter the constants of the equations:")
print("-------------------")
for i in range(3):
    const.append(float(input(f"b{i+1}: ")))

# Construct the matrix
matrix = np.array([equ_1, equ_2, equ_3])
matrix = np.column_stack((matrix, const))

print()
print("Augmented matrix A:")
print(matrix)

############ Matrix functions ############
def gaussElimination(A):
    pass

def backSubstitution(A):
    pass

############ Row operations ############
def rowScale(A, r, k):
    pass

def rowSwap(A, r1, r2):
    pass

def rowAddScale(A, r1, r2, l):
    pass