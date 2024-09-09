# Simple Fluid

```diff
- 提交时间：2024/7/13 03:59:50
+ 提交时间：2024/7/12 01:06:27
```

## 问题背景

前提：猫咪走丢了

已知：

![Fluid](docs/liquid.jpg)

结论：？

## 问题描述

你需要进行代码填空，完成一个简单的二维不可压缩流体模拟程序。你需要完成的代码功能大致包括：

1. 从 `input.json` 读取输入，调用提供好的接口，初始化模拟环境（设置格点数量，边界条件，模拟参数等）
2. 实现以上初始化接口的具体逻辑。
3. 完成每个时间片内的模拟逻辑，更新格点上的流体速度和压强，溶质的浓度。
4. 模拟一定步数后，将每个格点的流体速度，溶质的浓度输出到 `output.hdf5` 文件中。

模板代码位于 `fluid.example.py`，请先将其重命名为 `fluid.py`，随后将其中标有 `# TODO` 的部分替换为相应的代码。算法详细说明位于 `docs/algorithm.pdf`， `TODO` 注释中带有的**编号**和 `docs/algorithm.pdf` 中的**章节号**对应，请仔细阅读。

输入输出格式说明见 `docs/file.md`。

**注意！**本题如果你的程序执行成功了，Action 的状态就会是通过（对勾）。这不意味着你拿到了满分。请查看 Action Build Log 来了解具体获得的分数。

## 依赖

默认情况下，模板代码会根据每个时间片的模拟结果输出一个 GIF 文件。这需要一个额外的依赖，可以通过以下方式安装：

```bash
# Debian
$ sudo apt install python3-pil

# Gentoo Prefix on macOS
$ emerge -avt dev-python/pillow
```

如果你不需要 GIF 输出，请将代码开头 `ENABLE_GIF` 变量的值改为 `False`。

GIF 文件的内容不会参与评测。

## 样例与评测

本题进行黑盒评测。共有 5 组输入，对于每组输入，我们对 `dyes` 和 `velocity` 数据集进行**逐点**比较，如果你的程序输出的值是 $r$，助教所写的模拟得到对应的值是 $r\_std$，那么这个点给分比例 `(0, 1]` 如下：

```python
THRESHOLD = 0.01
def scoring(r, r_std):
  ratio = abs(r - r_std) / max(abs(r_std), 1e-5)

  if ratio < THRESHOLD:
    return 1
  return 0.1 ** ((ratio - THRESHOLD) / (1 - THRESHOLD))
```

也就是如果相对误差在 Threshold = 1% 以内给 100% 的分数，相对误差在 100% 的时候给 10% 的分数。最后 `velocity` 数据集的平均得分站一半分数，`dyes` 数据集的平均得分占一半分数。

**注意！**本题如果你的程序执行成功了，Action 的状态就会是通过（对勾）。这不意味着你拿到了满分。请查看 Action Build Log 来了解具体获得的分数。

在本地执行评测并输出分数请执行 `scripts/grade.sh`

本题分数构成为：

- 黑盒: 按上述方法计算。
- 白盒: 代码风格与 Git 使用 20 分（包括恰当注释、合理命名、提交日志等）。

本题不设置运行时间、空间限制。

助教以 deadline 前 GitHub 上最后一次提交为准进行评测。

## 调试
在 `data` 目录中有数个 `animation.*.gif` 文件，这是标程输出的 GIF。请注意，标程采取的 GIF 压缩算法和速度可能和 PIL 有微妙的不同，所以如果 GIF 有一点点差距，可能你的输出和标准答案是完全一致的。

在 https://lab.cs.tsinghua.edu.cn/physics-data/fluid/steps.1.tar.gz 压缩文件中有 `input.1.json` 输入对应的，各步中各变换之后标程的场的内容。例如 `23.advection.hdf5` 代表在 step=23 时，Advection 之后的场的内容。额外的，`23.before.hdf5` 代表 step=23 的模拟刚开始时（splat 之后）的场的内容。这些数据也许有助于你调试。具体的输出的位置见标程的源码。

最后，在 `data/std` 目录中有 C++ 写的标程，可以用来对照你的实现，或者生成更多输出。相关信息请阅读 `data/std/README.md`。
