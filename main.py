# Self note: Use np.array for easier matrix manipulation


import numpy as np

# Coefficients of the equations (aij)
equ_1 = []
equ_2 = []
equ_3 = []
# Constants of the equations (bi)
const = []

############ Input ############
# Commented for debugging...

# print("Enter the 3 coefficients of 3 equations:")
# print("-------------------")

# for i in range(3):
#     equ_1.append(float(input(f"a1{i+1}: ")))

# for i in range(3):
#     equ_2.append(float(input(f"a2{i+1}: ")))

# for i in range(3):
#     equ_3.append(float(input(f"a3{i+1}: ")))

# print()
# print("Enter the constants of the equations:")
# print("-------------------")
# for i in range(3):
#     const.append(float(input(f"b{i+1}: ")))
###

### For now, use the following:
equ_1 = [2, 1, -1]
equ_2 = [-3, -1, 2]
equ_3 = [-2, 1, 2]
const = [8, -11, -3]
###

# Construct the matrix
matrix = np.array([equ_1, equ_2, equ_3])
matrix = np.column_stack((matrix, const))
matrix = matrix.astype(float)

print()
print("Augmented matrix A:")
print(matrix)

############ Row operations ############
def rowScale(A, r, k)-> None:
    A[r - 1] = (A[r - 1] * k)

def rowSwap(A, r1, r2)-> None:
    A[[r1 - 1, r2 - 1]] = A[[r2 - 1, r1 - 1]]

def rowAddScale(A, r1, r2, l)-> None:
    A[r2 - 1] += l * A[r1 - 1]

############ Matrix functions ############
def gaussElimination(A)-> None:
    # Used for all rows
    hasLeadingOne = False

    # TODO - Make it work for any number of unknowns
    # ( for i in range(len(A[0] - 1)) )

    ### Row 1 ###
    for i in range(len(A)):
        if A[i][0] == 1: # the todo
            hasLeadingOne = True
            rowSwap(A, 1, i + 1)
            break

    if not hasLeadingOne:
        rowScale(A, 1, 1/A[0][0])

    for i in range(1, len(A)): # [1, 2]
        rowAddScale(A, 1, i + 1, -A[i][0]) # the todo

    # TODO - Improve the rowAddScale part ([0, 2], [0, 1])
    # not just [1, 2]

def backSubstitution(A)-> None:
    pass

gaussElimination(matrix)
print(matrix)