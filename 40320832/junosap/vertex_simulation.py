import numpy as np
import h5py
from tqdm import tqdm

import utils
import photon_move
import photon_reflection
import photon_hittime
import photon_out

PHOTON_NUM = 2000
N_VERTICES = 500

LIGHT_SPEED = 300

REFRACTIVE_INDEX_WATER = 1.33
REFRACTIVE_INDEX_FLASH = 1.48

def save_to_hdf5(file_name, EventID,channelID, PETime):
    '''
    ### save_to_hdf5:将数据保存到对应的hdf5文件中

    ### 传入参数

    - file_name: 文件名
    - data: 数据

    ### 返回值

    无，将数据保存到对应的文件中
    '''
    # 读取已有的数据
    with h5py.File(file_name, "r") as f:
        old_EventID = f["ParticleTruth"]["EventID"]
        old_x = f["ParticleTruth"]["x"]
        old_y = f["ParticleTruth"]["y"]
        old_z = f["ParticleTruth"]["z"]
    with h5py.File(file_name, "w") as f:
        old_truth = f.create_dataset("ParticleTruth", (N_VERTICES,),
                            dtype=[("EventID", "<i4"),
                                    ("x", "<f8"),
                                    ("y", "<f8"),
                                    ("z", "<f8"),
                                    ("p", "<f8")])
        old_truth["EventID"] = old_EventID
        old_truth["x"] = old_x
        old_truth["y"] = old_y
        old_truth["z"] = old_z
        old_truth["p"] = np.ones(N_VERTICES) * 1.0
        truth = f.create_dataset("PETruth", (len(channelID),),
                            dtype=[("EventID", "<i4"),
                                    ("ChannelID", "<i4"),
                                    ("PETime", "<f8")])
        truth["EventID"] = EventID
        truth["ChannelID"] = channelID
        truth["PETime"] = PETime

def simulate(geo, opt):
    '''
    ### simulate:模拟光子运输

    ### 传入参数

    - geo: 几何文件
    - opt: 输出文件
    - ParticleTruth: 顶点数据

    ### 返回值

    无，将结果直接写入对应的文件
    '''
    eventID = []
    channelID = []
    PETime = []
    with h5py.File("data.h5", "r") as inp:
        ids = inp["ParticleTruth"]["EventID"]
        xs = inp["ParticleTruth"]["x"]
        ys = inp["ParticleTruth"]["y"]
        zs = inp["ParticleTruth"]["z"]

    print("Start to generate the photon information")

    theta_ = np.random.uniform(0, np.pi, N_VERTICES * PHOTON_NUM)
    phi_ = np.random.uniform(0, 2 * np.pi, N_VERTICES * PHOTON_NUM)
    theta_ = theta_.reshape(N_VERTICES, PHOTON_NUM)
    phi_ = phi_.reshape(N_VERTICES, PHOTON_NUM)
    info = np.zeros((N_VERTICES, PHOTON_NUM, 8))
    xs = xs.reshape(len(xs), 1)
    ys = ys.reshape(len(ys), 1)
    zs = zs.reshape(len(zs), 1)
    xs = np.tile(xs, PHOTON_NUM)
    ys = np.tile(ys, PHOTON_NUM)
    zs = np.tile(zs, PHOTON_NUM)
    info[:, :, 0] = xs
    info[:, :, 1] = ys
    info[:, :, 2] = zs
    info[:, :, 3] = np.sin(theta_) * np.cos(phi_) * LIGHT_SPEED / REFRACTIVE_INDEX_FLASH
    info[:, :, 4] = np.sin(theta_) * np.sin(phi_) * LIGHT_SPEED / REFRACTIVE_INDEX_FLASH
    info[:, :, 5] = np.cos(theta_) * LIGHT_SPEED / REFRACTIVE_INDEX_FLASH
    info[:, :, 6] = 0
    info[:, :, 7] = 0

    print("Start to simulate the photon transport 1")

    result = np.apply_along_axis(photon_move.move_photon,2,info[:,:,0:7])
    info[:,:,6] += result[:,:,6]
    info[:,:,0:3]  = result[:,:,0:3]

    print("Start to simulate the photon reflection")

    new_direction = np.apply_along_axis(photon_reflection.total_reflection,2,info[:,:,0:8])
    info[:,:,0:8] = new_direction[:,:,0:8]

    print("Start to calculate the hit")

    newinfo = np.apply_along_axis(photon_out.photon_out,2,info[:,:,0:6],geo)
    newtime = newinfo[:,:,1]
    newchannelID = newinfo[:,:,0]
    print("Start to save the result")

    info[:,:,6] += newtime
    info[:,:,7] = newchannelID

    print("Start to add the hit time")

    for i in range(N_VERTICES):
        for j in range(PHOTON_NUM):
            info[i,j,6] = info[i,j,6] + photon_hittime.simulate_inhomogeneous_poisson_sampling(1)

    print("Start to save the result to the file")

    eventID = []
    channelID = []
    PETime = []
    for i in range(N_VERTICES):
        for j in range(PHOTON_NUM):
            if info[i,j,7] != -1:
                eventID.append(ids[i])
                channelID.append(info[i,j,7])
                PETime.append(info[i,j,6])

    print("ok")

    save_to_hdf5(opt, eventID, channelID, PETime)
