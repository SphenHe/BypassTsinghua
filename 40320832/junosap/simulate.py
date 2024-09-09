import argparse
import h5py as h5
import numpy as np

import vertex_generation
import vertex_simulation

pmt_num = 100

# 处理命令行
parser = argparse.ArgumentParser()
parser.add_argument("-n", dest="n", type=int, help="Number of events")
parser.add_argument("-g", "--geo", dest="geo", type=str, help="Geometry file")
parser.add_argument("-o", "--output", dest="opt", type=str, help="Output file")
args = parser.parse_args()

# 读入几何文件
with h5.File(args.geo, "r") as geo:
    channels = geo['Geometry']['ChannelID'][0:pmt_num]
    theta = geo['Geometry']['theta'][0:pmt_num] / 180 * np.pi
    phi = geo['Geometry']['phi'][0:pmt_num] / 180 * np.pi

    pmt_channels = geo['Geometry']['ChannelID'][0:pmt_num]
    pmt_locations = np.array([
        channels, np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)
        ]).T

# 生成顶点数据
# Generate vertex data
vertex_generation.generate_vertex()

# 模拟光子运输
# Simulate photon transport
vertex_simulation.simulate(args.geo, args.opt)
