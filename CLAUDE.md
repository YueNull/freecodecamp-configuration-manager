# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库用途

freeCodeCamp **Scientific Computing with Python** 认证的个人学习记录。每个 Lab 是一个独立子文件夹，命名格式为 `NN_lab-name/`，包含 `main.py`（实验代码）和 `README.md`（说明）。

## 运行某个 Lab

```bash
cd 01_user-configuration-manager
python main.py
```

无需安装任何依赖，所有 Lab 均使用 Python 3 标准库。

## 添加新 Lab 的规范

1. 新建文件夹 `NN_lab-name/`（编号两位数，如 `02_`）
2. 在其中创建 `main.py` 和 `README.md`
3. 在根目录 `README.md` 的目录表格中追加一行

## 代码约定

- 所有函数均以 `settings_dict`（`dict`）作为第一个参数，直接修改并返回描述操作结果的字符串
- key 和 value 在写入前统一转为小写（`.lower()`）
- 每个 `main.py` 底部的 `if __name__ == "__main__":` 块用于本地演示，不属于 freeCodeCamp 测试范围
