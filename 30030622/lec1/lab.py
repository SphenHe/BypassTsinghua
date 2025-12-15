'''
HW1: Leature 1 Four Special Matrices Pre MMDA Spring 25
'''

import numpy as np

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

def coding_lab_1(n):
    '''
    Write a function to generate special matrices K, C, T, B of any input size n.

    ## Parameters:
    - n (int): The size of the matrix.

    ## Returns:
    - K (numpy.ndarray): A K matrix of size n x n.
    - C (numpy.ndarray): A C matrix of size n x n.
    - T (numpy.ndarray): A T matrix of size n x n.
    - B (numpy.ndarray): A B matrix of size n x n.
    '''
    # Generate the K matrix
    K = generate_K_matrix(n)
    # Generate the C matrix
    C = K.copy()
    C[-1, 0] = -1
    C[0, -1] = -1
    # Generate the T matrix
    T = K.copy()
    T[0, 0] = 1
    # Generate the B matrix
    B = T.copy()
    B[-1, -1] = 1
    return K, C, T, B

def coding_lab_2(n, spring_constant, masses, g):
    '''
    Solve the fixed-free spring-mass system for displacement with 100 masses connected by 100 springs.
    Uses the stiffness matrix K and force vector f, and applies boundary conditions.

    ## Parameters:
    - n (int): Number of masses (and springs).
    - spring_constant (float): Spring constant.
    - masses (numpy.ndarray): Masses at each node.
    - g (float): Gravitational acceleration.

    ## Returns:
    - u (numpy.ndarray): Displacement vector for the spring-mass system.
    '''
    # Generate the stiffness matrix K for a spring-mass system
    K = generate_K_matrix(n)
    K = K * spring_constant

    # Generate the force vector f for a spring-mass system
    f = masses * g

    # Apply boundary conditions(Fixed-free)
    K = K[1:, 1:]
    f = f[1:]

    # Solve the system
    u = np.linalg.solve(K, f)

    return u

def main():
    '''
    Main function to test or run the functions/codes.
    '''
    # Run the coding_lab_1 function
    n = int(input('Enter the size of the matrix: '))
    K, C, T, B = coding_lab_1(n)
    print(f'K matrix of size {n} x {n}:')
    print(K)
    print(f'C matrix of size {n} x {n}:')
    print(C)
    print(f'T matrix of size {n} x {n}:')
    print(T)
    print(f'B matrix of size {n} x {n}:')
    print(B)

    # Run the coding_lab_2 function
    n = 100
    spring_constants = np.ones(n)
    masses = np.ones(n)
    g = 9.81
    u = coding_lab_2(n, spring_constants, masses, g)
    print('Displacement vector:')
    print(u)

if __name__ == '__main__':
    main()