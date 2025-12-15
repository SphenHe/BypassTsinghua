'''
Sloving K_1000 u = f_1000 u

Compare the runtime between the direct solver u = K_1000\\f_1000
                        and the iterative solver u = inv(K_1000) * f_1000
'''

import numpy as np
import time

def generate_K_matrix(n):
    '''
    Write a function to generate a K matrix of size n x n.

    ## Parameters:
    - n (int): The size of the matrix.

    ## Returns:
    - K (numpy.ndarray): A n x n matrix.
    '''
    K = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i == j:
                K[i,j] = 2
            elif i == j+1 or i == j-1:
                K[i,j] = -1
    return K

# Generate the matrix K_1000
n = 1000
K_1000 = generate_K_matrix(n)

# Generate the right-hand side f_1000
f_1000 = np.random.rand(n)

# Direct solver
start = time.time()
u_direct = np.linalg.solve(K_1000, f_1000)
end = time.time()
print('Direct solver runtime:', end - start)

# Iterative solver
start = time.time()
u_iterative = np.linalg.inv(K_1000) @ f_1000
end = time.time()
print('Iterative solver runtime:', end - start)
