import numpy as np

PHOTON_NUM = 2000

R_OUT = 19500
R_IN = 17710
R_PMT = 2540

REFRACTIVE_INDEX_WATER = 1.33
REFRACTIVE_INDEX_FLASH = 1.48

def total_reflection(info):
    '''
    ### 计算光子在墙上的反射方向

    ### 传入参数

    direction: 光子的方向向量
    wall_normal: 墙的法向量（也是光子打到墙上的位置）

    ### 返回值

    一个三维向量，表示光子的反射方向

        1. 如果全反射，则返回零向量
        2. 如果正常折射，则返回折射方向
    '''
    direction = info[3:6]
    wall_normal = info[0:3]
    critical_angle = np.arcsin(REFRACTIVE_INDEX_WATER / REFRACTIVE_INDEX_FLASH)
    cos_in = np.dot(direction, wall_normal)/(
        np.linalg.norm(direction) * np.linalg.norm(wall_normal))
    if cos_in < 0:
        return np.zeros(8)
    elif cos_in > np.cos(critical_angle):

        cos_in = np.clip(cos_in, -1, 1)
        sin_in = np.sqrt(1 - cos_in ** 2)
        sin_out = REFRACTIVE_INDEX_WATER / REFRACTIVE_INDEX_FLASH * sin_in
        sin_out = np.clip(sin_out, -1, 1)
        theta_out = np.arcsin(sin_out)

        basic_one = wall_normal / np.linalg.norm(wall_normal)
        basic_two = direction - direction @ basic_one * basic_one
        if np.linalg.norm(basic_two) > 0:
            basic_two = basic_two / np.linalg.norm(basic_two)
            new_direction = np.cos(theta_out) * basic_one + np.sin(theta_out) * basic_two

            return wall_normal[0], wall_normal[1], wall_normal[2], new_direction[0], new_direction[1], new_direction[2], info[6], info[7]
        else:
            return wall_normal[0], wall_normal[1], wall_normal[2], basic_one[0], basic_one[1], basic_one[2], info[6], info[7]
    else:
        return np.zeros(8)
