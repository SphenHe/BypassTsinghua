# Field

## 问题背景

![curl cat](./curl.gif)

$`\nabla \times \text{🐈}`$

现状：猫咪找不到游戏机了

已知:

- 游戏机是电器
- 猫咪的毛可以感知电场
- 适用于猫咪的游戏机足够宏观，可以被 Maxwell Equation 精确描述
  - 猫咪没有被物理学家放入盒子中

结论：？

## 问题描述

给定某时刻的电场，以及数个点的座标，请计算这些给定点位置上的电荷密度和磁通量变化率。

为此，你需要计算场的散度和旋度，在离散存储的场中，可以通过以下方式近似计算某个空间方向上的偏导数。如果认为离散存储中相邻格点对应的实际距离是 $`d`$:

> 如果以下公式无法正确渲染，请前往 GitLab 查看。

```math
\frac{\partial F_z}{\partial x} = \frac{1}{2d}(F_z(x+1, y, z) - F_z(x-1, y, z))
```

其中 $`F_z`$ 是场的 $`z`$ 方向上的分量。

散度就是 $`F_x`$ 对 $`x`$ 的偏导数加上 $`F_y`$ 对 $`y`$ 的偏导数加上 $`F_z`$ 对 $`z`$ 的偏导数。

以此类推可以得到旋度的计算方法：

```math
(\nabla \times \mathbf{F})(x, y, z) = \frac{1}{2d} \begin{bmatrix}
  \bigl(F_z(x, y+1, z) - F_z(x, y-1, z)\bigr) - \bigl(F_y(x, y, z+1) - F_y(x, y, z-1)\bigr) \\
  \bigl(F_x(x, y, z+1) - F_x(x, y, z-1)\bigr) - \bigl(F_z(x+1, y, z) - F_z(x-1, y, z)\bigr) \\
  \bigl(F_y(x+1, y, z) - F_y(x-1, y, z)\bigr) - \bigl(F_x(x, y+1, z) - F_x(x, y-1, z)\bigr)
\end{bmatrix}
```

电荷密度等于电场强度的散度乘以介电常数。这里，我们取真空中的介电常量 `8.8541878128(13)*10^{-12} F/m`。由于本题中数据的单位都是国际单位制的基本单位，所以不用考虑单位的转换。

根据麦克斯韦方程，磁通量变化率等于电场旋度的相反数。

使用 NumPy 对矩阵进行 Slicing / Rolling 可以高效实现这类操作，通过 [Advanced indexing](https://numpy.org/doc/stable/user/basics.indexing.html#advanced-indexing) 可以同时读取多个值。为了让同学学习 NumPy 使用，本题实现中**不允许使用任何 Python 控制流语句**（如 `for`、`if`、`while` 等），否则白盒部分将**得 0 分**。

## 实现说明

请你修改 `field.py`，完成其中的函数，并将结果通过返回值返回，**本题目不通过标准输入输出进行数据传递**。请不要修改 **`main.py`**。

函数的第一个参数 `field` 是一个四维 NumPy Array，表示电场，尺寸是 `H x W x D x 3`，前三个维度分别对应 x, y, z 坐标，**最内一个维度是各个方向上的场强分量，三个元素分别对应 x, y, z 方向**。

函数的第二个参数 `query` 是一个二维 NumPy Array，表示所有查询的座标，尺寸是 `q x 3`，q 是查询数量，每行是一个坐标（三个元素分别对应 x, y, z 坐标）。**保证坐标都是整数，保证查询不落在场的边界上**。

函数的第三个参数 `d` 是一个浮点数，表示格点对应的实际距离。

你需要：以 Tuple 返回两个 NumPy Array，形状分别为 `1D: q` 和 `2D: q x 3`，内容分别是电荷密度和磁通量变化率。

所有计算过程采用国际单位制。

## 样例与评测

本题进行黑盒评测。共有 5 组测例，分别评分，总分相加。测例都在 `data` 目录下，以 Python 脚本的格式给出了输入和输出数据。评测的时候，会复制对应的测例（如 `data/1.py`）到 `data.py`，并且运行 `main.py`。

如果你想要单独测试某一个测例，例如 `3.py`，运行命令：

```shell
cp data/3.py data.py
python3 main.py
```

如果中途出错了，程序会打印错误信息；如果答案正确，那么它不会显示输出。

第一组测例在 `data/1.py` 中定义，它的输入是 $`10 \times 10 \times 10`$ 的均匀电场，每一点的电场强度都是一样的，因此电荷密度和磁通量变化率全零。

最终分数构成为：

* 黑盒 80 分：共 5 个测例，每个 16 分；
* 白盒 20 分：参照[白盒标准](https://physics-data.meow.plus/faq/whitebox/)，并务必据实填写 honor code。

助教以 deadline 前 <https://git.tsinghua.edu.cn/> 上最后一次提交为准进行评测。

本题**存在**运行时间限制。对于每个数据点，请在 1 秒内完成运行。

最终评分以在助教机器上运行的时间为准。所用电脑的 CPU 为 AMD Ryzen 7 7700。
