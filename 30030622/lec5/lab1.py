import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import spsolve

def f(x):
    return (18 * np.pi * x) ** 2 * np.sin(9 * np.pi * x ** 2) - 18 * np.pi * np.cos(9 * np.pi * x ** 2)

def solve_finite_difference(n):
    h = 1.0 / (n + 1)  # Grid spacing
    x = np.linspace(h, 1 - h, n)  # Interior grid points

    # Construct finite difference matrix K efficiently using sparse storage
    from scipy.sparse import diags
    diagonals = [-2 * np.ones(n), np.ones(n-1), np.ones(n-1)]
    K = diags(diagonals, [0, -1, 1], format='csc') / h**2

    # Compute right-hand side vector F
    F = f(x)

    # Solve for u using sparse solver
    u = spsolve(K, F)

    return x, u

def convergence_analysis():
    ns = [10, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 10000]
    errors = []
    hs = []

    # Reference solution using u = sin[9*Pi*x^2] with boundary conditions
    x_ref = np.linspace(0, 1, 1000)
    u_ref = np.sin(9 * np.pi * x_ref ** 2)
    u_ref[0] = 0  # Boundary condition at x=0
    u_ref[-1] = 0  # Boundary condition at x=1

    for n in ns:
        x, u = solve_finite_difference(n)
        u_interp = np.interp(x_ref, x, u)
        error = np.linalg.norm(u_interp - u_ref, np.inf)
        errors.append(error)
        hs.append(1.0 / (n + 1))

    # Plot error vs h
    plt.figure()
    plt.loglog(hs, errors, '-o', label='Numerical error')
    plt.loglog(hs, np.array(hs)**2, '--', label='$O(h^2)$ reference')
    plt.xlabel('Grid spacing h')
    plt.ylabel('Error norm')
    plt.legend()
    plt.title('Convergence of Finite Difference Method')
    plt.grid()
    plt.savefig('convergence.pdf')
    plt.show()

if __name__ == "__main__":
    convergence_analysis()