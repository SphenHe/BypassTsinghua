import numpy as np

DELTA = 1e-6

def sphere_ray_intersection(sphere_center, sphere_radius, ray_origin, ray_direction):
    '''
    ### sphere_ray_intersection:求解球和射线的交点

    一个计算球和射线交点的函数
    a function to calculate the intersection points of a sphere and a ray

    ### parameters:

    - sphere_center: 球心坐标，形状为(3,)，元素分别是球心的x, y, z坐标
    - sphere_center: Sphere center, shape (3,),
        where each element is the x, y, z coordinates of the sphere center

    - sphere_radius: 球的半径
    - sphere_radius: Sphere radius

    - ray_origin: 射线起点，形状为(3,)，元素分别是射线起点的x, y, z坐标
    - ray_origin: Ray origin, shape (3,),
        where each element is the x, y, z coordinates of the ray origin

    - ray_direction: 射线方向，形状为(3,)，元素分别是射线方向的x, y, z坐标
    - ray_direction: Ray direction, shape (3,),
        where each element is the x, y, z coordinates of the ray direction

    ### return:

    一个包含交点坐标的列表，如果没有交点则返回None
    a list containing the coordinates of the intersection points,
        or None if there is no intersection

    1. 如果没有交点，则返回None
    1. If there is no intersection, return None
    2. 如果有一个交点，则返回一个包含交点坐标的列表
    2. If there is one intersection,
        return a list containing the coordinates of the intersection
    3. 如果有两个交点，则返回一个包含两个交点坐标的列表
    3. If there are two intersections,
        return a list containing the coordinates of the two intersections
    '''
    # 球心坐标和半径
    cx, cy, cz = sphere_center
    r = sphere_radius

    # 射线起点和方向
    ox, oy, oz = ray_origin
    dx, dy, dz = ray_direction

    # 求解二次方程的系数 a, b, c
    a = dx**2 + dy**2 + dz**2
    b = 2 * (dx * (ox - cx) + dy * (oy - cy) + dz * (oz - cz))
    c = (ox - cx)**2 + (oy - cy)**2 + (oz - cz)**2 - r**2

    # 计算判别式
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        # 没有交点
        return None
    elif discriminant == 0:
        # 一个交点
        t = -b / (2 * a)
        intersection = ox + t * dx, oy + t * dy, oz + t * dz
        return intersection
    else:
        # 两个交点
        sqrt_discriminant = np.sqrt(discriminant)
        t1 = (-b + sqrt_discriminant) / (2 * a)
        t2 = (-b - sqrt_discriminant) / (2 * a)

        intersection1 = ox + t1 * dx, oy + t1 * dy, oz + t1 * dz
        intersection2 = ox + t2 * dx, oy + t2 * dy, oz + t2 * dz

        if t1 < DELTA:
            return intersection2
        elif t2 < DELTA:
            return intersection1
        elif t1 > t2:
            return intersection2
        else:
            return intersection1

def random_direction_vector(dim):
    '''
    ### random_direction_vector:生成随机方向向量

    ### 传入参数

    - dim: 向量的维度

    ### 返回值

    一个dim维的单位向量
    '''
    vector = np.random.randn(dim)
    norm_vector = vector / np.linalg.norm(vector)
    return norm_vector

def angle_between_vectors(v1, v2):
    '''
    ### angle_between_vectors:计算两个向量之间的夹角

    ### 传入参数

    - v1: 向量1
    - v2: 向量2

    ### 返回值

    两个向量之间的夹角，单位为度
    '''
    # 计算点积
    dot_product = np.dot(v1, v2)

    # 计算范数（长度）
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    # 计算cos(theta)
    if norm_v1 == 0 or norm_v2 == 0:
        return 0
    cos_theta = dot_product / (norm_v1 * norm_v2)

    # 计算theta，并转换为度数
    theta_radians = np.arccos(np.clip(cos_theta, -1.0, 1.0))  # 确保值在有效范围内
    theta_degrees = np.degrees(theta_radians)

    return theta_degrees
def change(pmt,info):
    x = info[:,0]
    y = info[:,1]
    z = info[:,2]
    theta = pmt[0]
    phi = pmt[1]
    pmt_r = 19500

    pmt_x = pmt_r * np.sin(theta) * np.cos(phi)
    pmt_y = pmt_r * np.sin(theta) * np.sin(phi)
    pmt_z = pmt_r * np.cos(theta)
    pmtdir = np.array([pmt_x, pmt_y, pmt_z])

    photon = np.zeros((len(x), 3))
    for i in range(len(x)):
        position = np.array([x[i], y[i], z[i]])
        photon[i][0] = (x[i]**2 + y[i]**2 + z[i]**2)**0.5
        l_pmtdir = np.linalg.norm(pmtdir)
        l_position = np.linalg.norm(position)
        photon[i][1] = np.dot(pmtdir, position) / (l_pmtdir * l_position)
        photon[i][1] = np.clip(photon[i][1], -1, 1)
        photon[i][1] = np.arccos(photon[i][1])

        photon[i][2] = info[i][3]