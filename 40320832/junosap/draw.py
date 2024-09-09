import h5py as h5
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pmt_num = 100

# 该类在测试时会用到，请不要私自修改函数签名，后果自负
class Drawer:
    def __init__(self, data, geo):
        self.simtruth = data["ParticleTruth"]
        self.petruth = data["PETruth"]
        self.geo = geo["Geometry"]

    def draw_vertices_density(self, fig, ax):
        '''画出顶点密度'''
        #7/31 齐天下，画出顶点密度
        vertices = self.simtruth
        r = np.sqrt(vertices['x'][:]**2 + vertices['y'][:]**2 + vertices['z'][:]**2)
        n = np.zeros(50)
        for i in range(50):
            n[i] = np.sum(r < (i+1) * 17710 / 50) / (4/3 * np.pi * (i+1) ** 3)
        plt.plot(np.arange(50), n)
        ax.set_xlabel('Radius (17710/50m)')
        ax.set_ylabel('Density')
        ax.set_title('Vertex Density vs Radius')
        ax.grid(True)

    def draw_pe_hit_time(self, fig, ax):
        '''画出光子击中时间'''
        #画出PE的击中时间直方图
        # 获取光子击中时间
        hit_times = self.petruth['PETime'][:]
        # 仅绘制时间在 0.00 到 0.02 之间的数据
        hit_times = hit_times[(hit_times >= 0) & (hit_times <= 300)]
        # 创建更细的 bins，例如 200 个 bins
        bins = np.linspace(0, 300, 200)
        # 绘制直方图
        ax.hist(hit_times, bins=bins, color='blue', alpha=0.75)
        ax.set_xlabel('Hit Time (ns)')
        ax.set_ylabel('Counts')
        ax.set_title('Distribution of Photon Hit Times')
        ax.grid(True)
        print("Updated histogram of PE hit time to focus on 0 to 300 ns range with finer bins.")



    def draw_probe(self, fig, ax):
        '''画出探测器响应函数'''
        #7/31 齐天下，画出探测器响应函数
        with h5.File("geo.h5", "r") as geo:
            theta = geo['Geometry']['theta'][0:pmt_num] / 180 * np.pi
            phi = geo['Geometry']['phi'][0:pmt_num] / 180 * np.pi
            pmt = np.zeros((len(theta), 3))
            pmt[:, 0] = 19500 * np.sin(theta) * np.cos(phi)
            pmt[:, 1] = 19500 * np.sin(theta) * np.sin(phi)
            pmt[:, 2] = 19500 * np.cos(theta)

        # 从模拟数据中提取顶点信息
        vertices = self.simtruth
        pe_truth = self.petruth
        # 计算每个顶点到球心的距离，并归一化到[0,1]        
        r = np.zeros(len(pe_truth))
        eventid = pe_truth['EventID'][:]
        channelid = pe_truth['ChannelID'][:]
        r[:] = np.sqrt(vertices['x'][eventid[:]]**2 + vertices['y'][eventid[:]]**2 + vertices['z'][eventid[:]]**2) / 17710
        
        # 计算顶点与对应pmt的夹角
        dir_v = np.zeros((len(pe_truth), 3))
        dir_pmt = np.zeros((len(pe_truth), 3))
        dir_v[:, 0] = vertices['x'][eventid[:]]
        dir_v[:, 1] = vertices['y'][eventid[:]]
        dir_v[:, 2] = vertices['z'][eventid[:]]
        dir_pmt[:] = pmt[channelid[:]]
        theta = np.zeros(len(pe_truth))
        theta[:] = np.arccos(np.sum(dir_v[:] * dir_pmt[:], axis=1) / (np.linalg.norm(dir_v, axis=1) * np.linalg.norm(dir_pmt, axis=1)))

        r_new = np.zeros(2*len(pe_truth))
        theta_new = np.zeros(2*len(pe_truth))
        r_new[0:len(pe_truth)] = r
        r_new[len(pe_truth):] = r
        theta_new[0:len(pe_truth)] = theta
        theta_new[len(pe_truth):] = 2*np.pi - theta

        r = r_new
        theta = theta_new

        # 创建二维直方图，范围为r:[0,1]和theta:[0, 2*np.pi]
        hist, r_edges, theta_edges = np.histogram2d(r, theta, bins=[100, 100], range=[[0, 1], [0, 2*np.pi]])
        
        # 对数化直方图数据，加1避免log(0)
        hist = np.log10(hist + 1)
        
        # 获取r和theta的中心值
        r_centers = (r_edges[:-1] + r_edges[1:]) / 2
        theta_centers = (theta_edges[:-1] + theta_edges[1:]) / 2
        
        # 创建极坐标网格
        R, T = np.meshgrid(r_centers, theta_centers)

        # 选择颜色映射
        cmap = plt.get_cmap('viridis')
        
        # 在调用pcolormesh之前关闭网格
        ax.grid(False)
        
        # 绘制极坐标热图
        c = ax.pcolormesh(T, R, hist.T, cmap=cmap, shading='auto')
        
        # 设置颜色条
        cbar = fig.colorbar(c, ax=ax, label='PE (log scale)')
        cbar.set_ticks([0, 1, 2])
        cbar.set_ticklabels(['$10^0$', '$10^1$', '$10^2$'])
        
        # 设置极坐标网格和标签
        ax.set_rticks([0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_rlabel_position(-22.5)  # 将半径标签移到y轴正方向
        
        # 设置角度标签
        ax.set_xticks(np.linspace(0, 2*np.pi, 8, endpoint=False))
        ax.set_xticklabels(['0', '$\\pi/4$', '$\\pi/2$', '$3\\pi/4$', 
                            '$\\pi$', '$5\\pi/4$', '$3\\pi/2$', '$7\\pi/4$'])
        
        # 设置标题和其他属性
        ax.set_title('Probe Function R(r, θ)')
        ax.set_theta_zero_location("N")  # 设置0度在北方（顶部）
        ax.set_theta_direction(-1)  # 设置角度逆时针方向
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # 添加径向网格线
        ax.plot([0, np.pi], [0, 1], 'k:', linewidth=1)
        ax.plot([np.pi/2, 3*np.pi/2], [0.6, 0.6], 'k--', linewidth=1)
        
        # 设置图像范围
        ax.set_ylim(0, 1)


if __name__ == "__main__":
    import argparse

    # 处理命令行
    parser = argparse.ArgumentParser()
    parser.add_argument("ipt", type=str, help="Input simulation data")
    parser.add_argument("-g", "--geo", dest="geo", type=str, help="Geometry file")
    parser.add_argument("-o", "--output", dest="opt", type=str, help="Output file")
    args = parser.parse_args()

    # 读入模拟数据
    data = h5.File(args.ipt, "r")
    geo = h5.File(args.geo, "r")
    drawer = Drawer(data, geo)

    # 画出分页的 PDF
    with PdfPages(args.opt) as pp:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        drawer.draw_vertices_density(fig, ax)
        pp.savefig(figure=fig)

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        drawer.draw_pe_hit_time(fig, ax)
        pp.savefig(figure=fig)

        # Probe 函数图像使用极坐标绘制，注意 x 轴是 theta，y 轴是 r
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, projection="polar", theta_offset=np.pi / 2)
        drawer.draw_probe(fig, ax)
        pp.savefig(figure=fig)
