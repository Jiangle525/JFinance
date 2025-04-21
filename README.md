# JFinance v1.0 项目简介

## 项目简介

**JFinance** 是一个使用 Python 编写的股票数据处理与基础量化分析工具，旨在为个人投资者或量化爱好者提供简洁、易用的接口，用于获取股票数据、清洗处理以及量化分析策略。


## 项目特性

- 📈 **股票数据获取**：支持从主流数据源（如 Tushare、Yahoo Finance 等）获取A股及美股历史行情数据。
- 🧹 **数据处理**：内置数据清洗、缺失值处理、复权、技术指标计算（如均线、MACD、RSI等）功能。
- 🧠 **量化分析**：支持简单的回测分析，包括动量策略、均线交叉等基础策略。
- 📊 **可视化输出**：集成 Matplotlib、Plotly 等工具，提供直观的数据可视化图表。

## 项目结构

```bash
├── README.md
├── jfinance.py
├── libs
│   ├── __init__.py
│   ├── data
│   ├── evaluation
│   ├── strategy
│   └── visualizer
└── test.ipynb
```

## 安装方式

1. 克隆本项目：

```bash
git clone https://github.com/Jiangle525/JFinance.git
cd JFinance
```

2. 安装依赖库：

```bash
pip install -r requirements.txt
```


