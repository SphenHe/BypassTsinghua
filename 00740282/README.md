# 计算机程序设计基础（python）

2023-2024学年夏季学期-00740282-计算机程序设计基础（python）-乔林-已完结

## 仓库介绍

`乔Python` 小学期作业。。。

## 作业列表

- 请查阅 [problems.md](problems.md) 或 [problems.pdf](problems.pdf)

## 运行环境

- OS: OpenSUSE Tumbleweed 20240822 x86_64
- Python: 3.11.9
  - numpy 1.26.4

可以使用以下命令安装 numpy 1.26.4

```shell
pip install numpy==1.26.4
```

或者在项目根目录下运行以下命令

```shell
pip install -r requirements.txt
```

## 文档结构

> 注：每个 Chapter 中的 Python 文件可能会互相引用，请不要随意删除文件或改变文件名。

整个 Repo 分为多个 Chapter，每个 Chapter 下有多个题目。每个题目对应一个 Python 文件。每个 Chapter 的题目完成后，会有一个 `report.md` 和 `report.pdf` 文件，用于记录题目的解答思路和结果。

```shell
❯ tree
.
├── chapter1
│   ├── chapter1_1.py
│   ├── chapter1_2.py
│   ├── chapter1_3.py
│   ├── ...
│   ├── report.md
│   └── report.pdf
├── chapter2
│   ├── chapter2_1.py
│   └── ...
├── ...
├── problems.md
├── problems.pdf
├── README.md
└── requirements.txt

```
