import numpy as np

constVacuumPermittivity = 8.8541878128e-12

def calculateChargeDensity(field, query, d):
    '''
    Calculate the charge density at a given point in the field

    $$\\frac{\\partial F_z}{\\partial x} =
            \\frac{1}{2d}(F_z(x+1, y, z) - F_z(x-1, y, z))$$

    ### Inputs:
        - field: A 4d NumPy array representing the electric field
        - query: A 2d NumPy array with shape `q x 3` representing `q` queries
        - d: A float number representing unit distance in the grid

    ### Outputs:
        - chargeDensity: A NumPy array with shape `q`
          representing the charge density at each query point
    '''

    x, y, z = query[:, 0], query[:, 1], query[:, 2]

    dExdx = (field[x + 1, y, z, 0] - field[x - 1, y, z, 0]) / (2 * d)
    dEydy = (field[x, y + 1, z, 1] - field[x, y - 1, z, 1]) / (2 * d)
    dEzdz = (field[x, y, z + 1, 2] - field[x, y, z - 1, 2]) / (2 * d)

    chargeDensity = constVacuumPermittivity * (dExdx + dEydy + dEzdz)

    return chargeDensity

def calculateMagneticFluxChangeRate(field, query, d):
    '''
    Calculate the magnetic flux change rate at a given point in the field

    $$(\\nabla \\times \\mathbf{F})(x, y, z) = \\frac{1}{2d} \\begin{bmatrix}
    \\bigl(F_z(x, y+1, z) - F_z(x, y-1, z)\\bigr) - \\bigl(F_y(x, y, z+1) - F_y(x, y, z-1)\\bigr)
    \\bigl(F_x(x, y, z+1) - F_x(x, y, z-1)\\bigr) - \\bigl(F_z(x+1, y, z) - F_z(x-1, y, z)\\bigr)
    \\bigl(F_y(x+1, y, z) - F_y(x-1, y, z)\\bigr) - \\bigl(F_x(x, y+1, z) - F_x(x, y-1, z)\\bigr)
    \\end{bmatrix}$$

    ### Inputs:
        - divValue: A 3d NumPy array representing the divergence of the electric field
        - query: A 2d NumPy array with shape `q x 3` representing `q` queries
        - d: A float number representing unit distance in the grid

    ### Outputs:
        - magneticFluxChangeRate: A NumPy array with shape `q x 3`
          representing the magnetic flux change rate at each query point
    '''
    x, y, z = query[:, 0], query[:, 1], query[:, 2]

    rotEx = ((field[x, y + 1, z, 2] - field[x, y - 1, z, 2]) - \
            (field[x, y, z + 1, 1] - field[x, y, z - 1, 1])) / (2 * d)
    rotEy = ((field[x, y, z + 1, 0] - field[x, y, z - 1, 0]) - \
            (field[x + 1, y, z, 2] - field[x - 1, y, z, 2])) / (2 * d)
    rotEz = ((field[x + 1, y, z, 1] - field[x - 1, y, z, 1]) - \
            (field[x, y + 1, z, 0] - field[x, y - 1, z, 0])) / (2 * d)

    magneticFluxChangeRate = - np.array([rotEx, rotEy, rotEz]).T

    return magneticFluxChangeRate

def compute(field, query, d):
    """
    Arguments:
        field: A 4d NumPy array representing the electric field
        query: A 2d NumPy array with shape `q x 3` representing `q` queries
        d: A float number representing unit distance in the grid
    Returns:
        Two NumPy arrays with shape `q` and `q x 3`
    """
    chargeDensity = calculateChargeDensity(field, query, d)
    magneticFluxChangeRate = calculateMagneticFluxChangeRate(field, query, d)
    return chargeDensity, magneticFluxChangeRate
