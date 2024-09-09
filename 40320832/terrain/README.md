# Terrain

## 问题背景

```text
                           _____
                 ___      / ___ \
o   ฅ(^•ﻌ•^)ฅ   ( o )    | ( o ) |
                 ---      \ --- /
                           -----

```

## 问题描述

在本作业中，你将绘图展示北京中某地区的地形、降水和风。

请先执行 `data/fetch.sh` 下载数据。推荐在校园网环境中下载，解压缩后大约 200MB。脚本中会用到 `wget` 命令和来自 `coreutils` 的 `sha256sum` 命令。如果你没有安装，可以运行以下命令：

```shell
sudo apt install coreutils wget
```

执行完成后，`data` 目录中包含有四个文件，分别对应北京的海拔数据，及某天的气候数据，以及两者的元数据。所有坐标系统都已经经过预处理，统一使用 WGS84。

使用 `utils.py` 中的 `read_data()` 函数读取数据。这一函数将会返回一个字典，包括海拔、降水、风三个数据集。每个数据集包括一个二维数组表示具体数据，一个原点的经纬度坐标，以及每个像素的长宽。

请使用 Matplotlib 绘制一幅图，要求

- 修改 `terrain.py`，使用 Python3 执行的时候输出图片到 `terrain.pdf`。
- 区域任选，但是这一范围请至少覆盖每个数据集中 200x200 个数据点。
- 包含地形、降水和风向风速信息。你可以在一张 subgraph 中绘制多层同时表示多个信息，也可以分别绘制多张 subgraph。
- 图例完全（如果使用了颜色/渐变，需要标出颜色/渐变代表的数值）
- 没有巨大的歧义，比如绘制等高线的时候，需要有办法区分山峰和低地（通过颜色、标记等）

地形和气候数据的分辨率和边界有所不同，你也许需要对数据进行一定处理，比如选定一个比数据集更稀疏网格，然后在坐标内取平均或最接近的点的值。

你也许会对以下 Matplotlib 提供的绘图方法感兴趣：

- [contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html) 和 [contourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html)
- [imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html)
- [quiver](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html) 和 [quiverkey](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiverkey.html)
- [streamplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.streamplot.html)
- [colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html)

绘图的比例、方向不做要求，但是方便你能一眼看出画的对不对，这是北京附近的每纬度:经度距离的近似值：

```
40N,116E <-> 40N,117E = 85.39 km
39.5N,116.5E <-> 40.5N,116.5E = 111.03 km
```

## 数据格式、单位

- 风速风向数据是一个二维向量场，单位是 m/s
- 降水数据是一个二维标量场，单位是 mm/h
- 地形数据是一个二维标量场，表示海拔，单位是 m

所有数据中第一个维度都是纬度，第二个纬度都是经度：

- 元数据中，原点和像素大小格式为 `(纬度, 经度)`
- 数据集中，取一点的数据需要使用 `data[纬度方向下标][经度方向下标]`

**注意**: 像素大小可能是负数，意味着沿这个方向下标增加，经度或者纬度降低。

## 样例与评测

本题目没有黑盒评测！助教将会在自己的计算机上运行你的代码，并且肉眼观察画图的结果。CI 脚本中也将运行你的代码，并将绘制的结果上传到 GitLab 中，可在 CI 运行日志中下载（一段时间后将会过期）。这次作业 CI 打绿勾只是说明成功产生了文件，不代表结果满足要求。

- 白盒
  - 代码功能：80 分，绘图满足要求，内容正确；
  - 非功能：20 分，参照[白盒标准](https://physics-data.meow.plus/faq/tutorials/whitebox/)，并务必据实填写 honor code。

本题不设置运行时间、空间限制。

数据来源于 NASA ASTER Global DEM v3 和中国气象局。数据具体来源和预处理过程见 `docs/data.md`。

助教以 deadline 前 <https://git.tsinghua.edu.cn/> 上最后一次提交为准进行评测。

## For Example

下面是助教绘制的图像，你可以参考它来绘制你的图像。

![Example](terrain-example.jpg)
