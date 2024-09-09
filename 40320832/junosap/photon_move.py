import numpy as np

import utils

R_OUT = 19500
R_IN = 17710

def move_photon(photon):
    '''
    ### move_photon:移动光子

    ### 传入参数

    - photon: 光子的位置和方向，飞行时间

    ### 返回值

    一个七维向量，表示光子的新位置（3），方向（3），飞行时间
    '''
    # read the photon information
    x, y, z = photon[0:3]
    px, py, pz = photon[3:6]

    v = np.linalg.norm(np.array([px, py, pz]))
    # move the photon
    result = []
    new_location = utils.sphere_ray_intersection((0, 0, 0), R_IN, (x, y, z), (px, py, pz))
    result[0:3] = new_location[0:3]
    result[3:7] = photon[3:7]
    # update the distance and time
    distance = np.linalg.norm(np.array(result[0:3]) - np.array([x, y, z]))
    result[6] += distance / v

    return result
