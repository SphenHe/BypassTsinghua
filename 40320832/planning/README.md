# planning

## 问题背景

喵喵最近在玩一款国产科幻题材沙盒建造类游戏《戴森球计划》，在该游戏中，玩家需要通过搭建自动化生产线来将各种自然资源加工制造成各种工业产品，但是，由于喵喵没有根据所需要的工业产品的产量精确地计算对各种自然资源的需求量，喵喵搭建的自动化生产线出现了各种问题，于是喵喵找到了你来帮他编写一个根据给定的工业产品的需求量计算各种自然资源的需求量的程序。

## 问题描述

与之前的作业不同，本作业希望锻炼大家阅读文档的能力。

你需要修改目录下的 `planning.py` 。该程序接受两个文件路径（文件名）作为参数，分别代表输入文件和输出文件，你需要从输入文件中读取描述各种工业产品加工过程的“化学反应方程式”、读取各工业产品的需求量，计算生产这些工业产品所需的自然资源量，并将这些自然资源需求量按照规定的格式写入输出文件。具体来说：

对于输入文件（例子参见 `data/in1.txt` ）：

1. 文件分成两部分，用一行 `Q:` 分割，在该行之前的行用于描述“反应方程式”，在该行之后的行用于描述需要的各工业产品的需求量；
2. 对于“反应方程式”部分：对于以 `#` 开头的行，是注释，直接忽略即可；对于不以 `#` 开头的行，每行代表一个“反应方程式”，例如 `2 H_2 + 1 O_2 -> 2 H_2O` 表示“生产两个单位的水 （`H_2O`）需要两个单位的氢气（`H_2`）和一个单位的氧气（`O_2`）”，即“反应方程式”被 `->` 划分为左右两边，左边为该“反应”的“反应物”，每种“反应物”前会有系数，代表需要该系数个单位的该种“反应物”，各“反应物”之间用 `+` 连接，右边为该“反应”的产物（只有一种产物），产物前会有系数，代表左边的“反应物”能生产的产物数量，为了方便大家解析这些“反应方程式”，所有符号、系数、反应物名、产物名之间都恰有一个空格，反应物名、产物名均不包含空格，系数均为正整数，且为 1 也不省略；每种产物只有一种合成方式
3. 对于“各工业产品的需求量”部分：每行包含一个产物名和对该产物的需求量（需求部分无注释），不同行的产物名可能会重复，需求量为一正整数。

对于输出文件（例子参见 `data/ans1.txt` ）：

1. 你需要读入并解析输入文件得到“反应方程式”和对工业产品的需求量，如果一种物品没有出现在任何一个“反应方程式”的右边，则称这种物品为一种“自然资源”，每种“自然资源”也可以作为一种需求出现在“各工业产品的需求量”部分；
2. 你需要根据“反应方程式”计算给定的“各工业产品的需求量”需要的每种“自然资源”的总数量，并按照给定的格式写入到输出文件中。具体来说，在计算数量的时候，你 *必须* 使用 `fractions` 模块中的 `Fraction` 类，该类实现了有理数的精确算术运算；
3. 输出文件格式要求：按照需要的总数量从高到低排列，每行输出一种“自然资源”的名字和对它需求的总数量，二者用一个空格隔开，该总数量用 `Fraction` 类默认的输出格式即可（例如 v 是 `Fraction` 类的变量，调用 `str(v)`），不需要输出需求量为零的“自然资源”。

可能会对你有帮助的文档：

1. https://docs.python.org/3/library/fractions.html
2. https://docs.python.org/3/library/functions.html
3. https://docs.python.org/3/library/stdtypes.html#list.sort
4. https://docs.python.org/3/library/sys.html#sys.argv

数据范围：

1. “反应方程式”少于或等于 100 行；
2. “各工业产品的需求量”少于或等于 201 行；
3. 所有系数均小于 500；

## 样例与评分

我们在 `data` 目录下提供了八组数据。和之前的题目一样，你可以通过 `python3 grade.py` 来进行一次的本地测评，也可以提交进行 CI 评测。此外，我们还在当前目录下提供了随机生成测试点的脚本 `gen.py` 供大家使用。

本作业会考验你代码编写的效率，如果代码运行的不够快，可能不到黑盒的满分。本题设置了 1s 的时间限制，如果超过了这个时间，评测程序会提示你超时。

用于评分的数据有两部分，一部分是助教人工构造的隐藏测例，另一部分是使用 `gen.py` 随机生成的数据，并以在助教机器上运行的正确性和时间为准。

最终分数构成为：

* 黑盒 80 分：共 8 个测例，每个 10 分；
* 白盒 20 分：参照[白盒标准](https://physics-data.meow.plus/faq/whitebox/)，并务必据实填写 honor code

助教以 deadline 前 <https://git.tsinghua.edu.cn/> 上最后一次提交为准进行评测。
