import numpy as np
import h5py

N_VERTICES = 500

def generate_vertex():
    '''
    ### generatte_vertex:生成顶点

    ### 输出

    - truth: 顶点数据，包含以下字段
        - EventID: 事件ID
        - x: 顶点x坐标
        - y: 顶点y坐标
        - z: 顶点z坐标
        - p: 顶点动量
    '''
    r_in = 17710

    r = np.random.uniform(0, r_in ** 3, size = N_VERTICES) ** (1/3)
    theta = np.random.uniform(0, np.pi, size = N_VERTICES)
    phi = np.random.uniform(0, 2*np.pi, size = N_VERTICES)

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    event_id = np.arange(N_VERTICES)

    with h5py.File("data.h5", "w") as opt:
        truth = opt.create_dataset("ParticleTruth", (N_VERTICES,),
                            dtype=[("EventID", "<i4"),
                                    ("x", "<f8"),
                                    ("y", "<f8"),
                                    ("z", "<f8"),
                                    ("p", "<f8")])
        truth["EventID"] = event_id
        truth["x"] = x
        truth["y"] = y
        truth["z"] = z
        truth["p"] = np.ones(N_VERTICES) * 1.0

    print("Vertex data generated successfully.")
