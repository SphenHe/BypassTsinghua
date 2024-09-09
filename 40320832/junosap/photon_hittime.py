import numpy as np

# 常数
# Constants
N_PMT = 100  # Number of PMTs
N_VERTICES = 500

TAU_D = 10
TAU_L = 5

INTEGRAL_FACTOR = 1500


C = 3e8  # Speed of light in vacuum in m/s

# 计算单个顶点的击中时间
# Calculate hit times for a single vertex_locations
def calculate_hit_time(vertex_locations, pmt_locations):
    '''
    ### calculate_hit_time:计算单个顶点的击中时间
    a function to calculate the hit time of the PMT for a single vertex:一个计算单个顶点的PMT击中时间的函数

    ### parameters:参数

    vertex_locations: 顶点位置，形状为(N_VERTICES, 3)，其中每一行的元素是顶点的位置坐标
    vertex_locations: Vertex locations, shape (N_VERTICES, 3),
        where each row is the coordinates of the vertex

    pmt_locations: PMT位置，形状为(N_PMT, 4)，其中每一行的第一个元素是PMT的通道号，后三个元素是PMT的位置坐标
    pmt_locations: PMT locations, shape (N_PMT, 4),
        where the first element of each row is the channel ID of the PMT,
        and the rest three elements are the coordinates of the PMT

    ### return:返回值

    times: 击中时间，形状为(N_PMT,)
    times: Hit times, shape (N_PMT,)
    '''
    distances = np.linalg.norm(pmt_locations - vertex_locations, axis=1)
    times = (distances / 1000) / C * 1e9  # Convert distances to meters, then to time in ns
    return times

# 模拟非齐次泊松采样的时间分布
# Simulate inhomogeneous Poisson sampling
def simulate_inhomogeneous_poisson_sampling(required_quantity):
    '''
    ### simulate_inhomogeneous_poisson_sampling:模拟非齐次泊松采样的时间分布
    a function to simulate the time distribution of inhomogeneous Poisson sampling:
    一个模拟非齐次泊松采样的时间分布的函数

    ### parameters:参数

    required_quantity: 所需的时间数量
    required_quantity: The required number of times

    ### return:返回值

    times: 时间，形状为(required_quantity,)
    times: Times, shape (required_quantity,)
    '''
    if required_quantity > 1:
        times = []
        while len(times) < required_quantity:
            t = np.random.exponential(TAU_D)  # 初始猜测时间
            acceptance_prob = INTEGRAL_FACTOR * np.exp(-t/TAU_D) * (1 - np.exp(-t/TAU_L))
            if np.random.rand() < acceptance_prob:
                times.append(t)
        return np.array(times)
    elif required_quantity == 1:
        while True:
            t = np.random.exponential(TAU_D)  # 初始猜测时间
            acceptance_prob = INTEGRAL_FACTOR * np.exp(-t/TAU_D) * (1 - np.exp(-t/TAU_L))
            if np.random.rand() < acceptance_prob:
                return t
    else:
        raise ValueError("required_quantity must be a positive integer")
