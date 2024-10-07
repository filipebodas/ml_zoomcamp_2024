import numpy as np

u = np.array([2, 4, 5, 6])
v = np.array([1, 0, 0, 2])

u.shape[0]

# Multiplication 
## vector-vector
def vector_multiplication(u, v):
    assert u.shape[0] == v.shape[0] # guarantees both arrays have the same size
    
    n = u.shape[0]
    result = 0
    
    for i in range(n):
        result = result + u[i] * v[i]

    return result


vector_multiplication(u,v)

'''the same result can be achieve with:'''
u.dot(v)

## Matrix-vector multiplication
U = np.array([
    [2, 4, 5, 6],
    [1, 2, 1, 2],
    [3, 1, 2, 1]
])

v = np.array([1, 0.5, 2, 1])


def matrix_vector_multiplication(U, v):
    assert U.shape[1] == v.shape[0] #columns of matrix must match rows of vector
    
    number_rows = U.shape[0]
    
    result = np.zeros(number_rows)
    
    for i in range(number_rows):
        result[i] = vector_multiplication(U[i], v) 
    
    return result

matrix_vector_multiplication(U, v)
U.dot(v)

## matrix-matrix multiplication
V = np.array([
    [1, 1, 2],
    [0, 0.5, 1],
    [0, 2, 1],
    [2, 1, 0]
])

def matrix_matrix_multiplication(U, V):
    assert U.shape[1] == V.shape[0]
    
    num_rows = U.shape[0]
    num_cols = V.shape[1]
    
    result = np.zeros((num_rows, num_cols))
    
    for i in range(num_cols):
        vi = V[:, i]
        Uvi = matrix_vector_multiplication(U, vi)
        result[:, i] = Uvi
    
    return result

matrix_matrix_multiplication(U, V)
U.dot(V)


# Identity Matrix
I = np.eye(3)
I

V
V.dot(I)

# Matrix Inverse
### Only square matrizes have inverses

V[[0, 1, 2]] # get the first 3 rows of matrix V
Vs = V[[0, 1, 2]]
Vs

np.linalg.inv(Vs) # compute the matrix inverse of V square matrix

Vs_inv = np.linalg.inv(Vs)
Vs_inv

Vs_inv.dot(Vs)
