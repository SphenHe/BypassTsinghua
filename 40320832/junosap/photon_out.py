import numpy as np
import h5py as h5

R_OUT = 19500
R_IN = 17710
R_PMT = 254
V = 299.8 #单位mm/ns
REFRACTIVE_INDEX_WATER = 1.33
V = V / REFRACTIVE_INDEX_WATER

pmt_num = 100

def photon_out(info, geo_file):
    '''
    location: np.array([x, y, z])
    direction: np.array([x, y, z])
    output:一维向量len（pmt_num），有输出的pmt对应位置会有时间，没有输出的则没有时间
    输入位置，方向
    输出channelid，time
    '''
    location = info[0:3]
    direction = info[3:6]

    if direction[0] == 0 and direction[1] == 0 and direction[2] == 0:
        channelid = -1
        time = -1
        return channelid, time

    with h5.File(geo_file, "r") as geo:
        channels = geo['Geometry']['ChannelID'][0:pmt_num]
        theta = geo['Geometry']['theta'][0:pmt_num] / 180 * np.pi
        phi = geo['Geometry']['phi'][0:pmt_num]/ 180 * np.pi
        pmt = np.zeros((len(channels), 3))
        pmt[:, 0] = R_OUT * np.sin(theta) * np.cos(phi)
        pmt[:, 1] = R_OUT * np.sin(theta) * np.sin(phi)
        pmt[:, 2] = R_OUT * np.cos(theta)

    #读取pmt位置信息
    a_vector = pmt - location
    b_vector = direction
    a_length = np.linalg.norm(a_vector, axis=1)
    b_length = np.linalg.norm(b_vector)
    cos_theta = np.dot(a_vector, b_vector) / (a_length * b_length)
    cos_theta = np.clip(cos_theta, -1, 1)
    sin_theta = np.sqrt(1 - cos_theta ** 2)
    out_to_pmt = np.linalg.norm(a_vector, axis=1)
    distance = out_to_pmt * sin_theta
    #计算出光子到pmt的距离
    right_theta = np.where(cos_theta > 0)
    right_distance = np.where(distance < R_PMT)
    right = np.intersect1d(right_theta, right_distance)

    if len(right) == 0:
        channelid = -1
        time = -1
        return channelid, time

    #筛选出符合条件的pmt
    length = np.ones(len(channels)) * 20000
    length_a = np.ones(len(channels)) * 20000
    length_b = np.ones(len(channels)) * 20000
    length_a[right] = np.sqrt(out_to_pmt[right] ** 2 - distance[right] ** 2)
    length_b[right] = np.sqrt(R_PMT ** 2 - distance[right] ** 2)
    length[right] = length_a[right] - length_b[right]
    #计算出光子到pmt的距离
    channelid = np.argmin(length)
    time = length[channelid] / V

    return channelid, time
