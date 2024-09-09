# 数据相关说明

## 数据来源

风速、风向、降水、温度、气压：

> 中国地面气象站逐小时观测资料
>
> 中国气象局 国家气象信息中心

高程数据：

> ASTER Global Digital Elevation Model v3
>
> NASA/METI/AIST/Japan Space Systems, and U.S./Japan ASTER Science Team
>
> https://doi.org/10.5067/ASTER/ASTGTM.003

## 预处理

ASTER GDEM 高程数据提供的下载格式是沿经纬度网格切分成了 1x1 度的 GeoTIFF。预处理使用了 gdal 拼成了一张大的 GeoTIFF。

中国气象局提供的气象数据中，降水和风速风向分别经过了插值。降水采用的插值方法是 SciPy 提供的 `scipy.interpolate.griddata`，曲线是连续三次曲线 (2D Clough-Tocher)。

风向风速采用的插值方法是 RBF 插值，选取基函数保证插值结果的散度为 0。具体的方法和基函数见 [arXiv:1102.4852](https://arxiv.org/abs/1102.4852)
