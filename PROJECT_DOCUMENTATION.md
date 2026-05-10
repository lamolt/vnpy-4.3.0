# VeighNa 项目文档

## 项目概述

**VeighNa** (vnpy) 是一套基于Python的开源量化交易系统开发框架，目前版本 **4.3.0**。该项目在开源社区持续贡献下已成长为多功能量化交易平台，用户涵盖私募基金、证券公司、期货公司等金融机构。

- **官网**: https://www.vnpy.com
- **GitHub**: https://github.com/vnpy/vnpy
- **文档**: https://www.vnpy.com/docs/cn/index.html
- **论坛**: https://www.vnpy.com/forum/
- **许可证**: MIT

## 支持环境

- **操作系统**: Windows 11+ / Windows Server 2022+ / Ubuntu 22.04 LTS+
- **Python版本**: 3.10+ (推荐3.13)
- **架构**: 64位

---

## 核心目录结构

```
vnpy-4.3.0/
├── .github/                 # GitHub配置
│   ├── CODE_OF_CONDUCT.md   # 社区行为准则
│   ├── ISSUE_TEMPLATE.md    # Issue模板
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── SUPPORT.md
│   └── workflows/           # CI/CD工作流
│       └── pythonapp.yml
├── docs/                    # 项目文档(Sphinx)
│   ├── conf.py
│   ├── index.rst
│   ├── community/           # 社区文档
│   │   ├── app/             # 交易应用文档
│   │   ├── info/            # 资讯信息文档
│   │   └── install/         # 安装指南
│   └── elite/               # Elite版本文档
│       ├── extension/
│       ├── info/
│       └── strategy/
├── examples/                # 示例代码
│   ├── alpha_research/      # AI量化研究示例(Jupyter Notebook)
│   ├── candle_chart/
│   ├── cta_backtesting/
│   ├── data_recorder/
│   ├── download_bars/
│   ├── portfolio_backtesting/
│   ├── spread_backtesting/
│   └── ...
├── tests/                   # 测试代码
│   └── test_alpha101.py
├── vnpy/                    # 核心源代码
│   ├── __init__.py
│   ├── alpha/               # AI量化模块 (4.0新增)
│   ├── chart/               # K线图表模块
│   ├── event/               # 事件驱动引擎
│   ├── rpc/                 # 跨进程通讯
│   └── trader/              # 交易核心引擎
│       ├── engine.py        # 主引擎
│       ├── gateway.py       # 接口网关基类
│       ├── object.py        # 数据对象
│       ├── constant.py      # 常量定义
│       ├── converter.py     # 转换器
│       ├── database.py      # 数据库接口
│       ├── datafeed.py      # 数据服务接口
│       ├── app.py           # 应用基类
│       ├── ui/              # UI界面
│       └── locale/          # 国际化
├── .gitignore
├── CHANGELOG.md             # 变更日志
├── LICENSE                 # MIT许可证
├── README.md               # 中文说明
├── README_ENG.md           # 英文说明
├── pyproject.toml          # 项目配置
├── install.bat             # Windows安装脚本
├── install.sh              # Ubuntu安装脚本
└── install_osx.sh         # macOS安装脚本
```

---

## 核心模块详解

### 1. vnpy.alpha - AI量化模块 (4.0版本新增)

面向AI量化策略的一站式多因子机器学习策略开发、投研和实盘交易解决方案。

| 子模块 | 文件 | 说明 |
|--------|------|------|
| **dataset** | 因子特征工程模块 |
| | `cs_function.py` | 横截面函数 |
| | `ts_function.py` | 时间序列函数 |
| | `math_function.py` | 数学运算函数 |
| | `ta_function.py` | 技术指标函数 |
| | `processor.py` | 数据处理器 |
| | `template.py` | 数据集模板 |
| | `utility.py` | 工具函数 |
| | `datasets/alpha_101.py` | WorldQuant Alpha 101因子集 |
| | `datasets/alpha_158.py` | Alpha 158因子集(源于Qlib) |
| **model** | 预测模型训练模块 |
| | `template.py` | 模型基类 |
| | `models/lasso_model.py` | Lasso回归模型 |
| | `models/lgb_model.py` | LightGBM梯度提升树 |
| | `models/mlp_model.py` | 多层感知机神经网络 |
| **strategy** | 策略投研开发 |
| | `template.py` | 策略模板 |
| | `backtesting.py` | 回测引擎 |
| | `strategies/equity_demo_strategy.py` | 股票策略示例 |
| **lab.py** | 投研流程管理(集成数据、模型、信号、回测) |
| **logger.py** | 日志记录 |

### 2. vnpy.chart - K线图表模块

高性能Python K线图表，支持大数据量显示和实时数据更新。

| 文件 | 说明 |
|------|------|
| `axis.py` | 坐标轴 |
| `base.py` | 基础组件 |
| `item.py` | 图表项 |
| `manager.py` | 图表管理 |
| `widget.py` | 图表窗口部件 |

### 3. vnpy.event - 事件驱动引擎

简洁易用的事件驱动引擎，作为事件驱动型交易程序的核心。

| 文件 | 说明 |
|------|------|
| `engine.py` | 事件引擎实现 |

### 4. vnpy.rpc - 跨进程通讯

跨进程通讯标准组件，用于实现分布式部署的复杂交易系统。

| 文件 | 说明 |
|------|------|
| `client.py` | RPC客户端 |
| `server.py` | RPC服务端 |
| `common.py` | 公共定义 |

### 5. vnpy.trader - 交易核心引擎

核心交易框架，包含所有交易相关的基础设施。

| 文件/目录 | 说明 |
|-----------|------|
| `engine.py` | 主引擎(MainEngine) |
| `gateway.py` | 接口网关基类 |
| `object.py` | 数据对象(订单、持仓等) |
| `constant.py` | 常量定义(方向、类型等) |
| `converter.py` | 数据转换器 |
| `database.py` | 数据库接口 |
| `datafeed.py` | 数据服务接口 |
| `app.py` | 应用基类 |
| `event.py` | 事件定义 |
| `logger.py` | 日志引擎 |
| `optimize.py` | 参数优化 |
| `setting.py` | 配置管理 |
| `utility.py` | 工具函数 |
| `ui/` | Qt图形界面 |
| `locale/` | 国际化资源 |

---

## 功能特点

### 交易接口 (Gateway)

支持国内外多种交易接口：

**国内市场**:
- CTP、CTP Mini、CTP证券
- 飞马、恒生UFT、易盛
- 顶点HTS、顶点飞创
- 中泰XTP、华鑫奇点
- 东证OST、东方财富EMT
- 飞鼠、金仕达黄金
- 融航、杰宜斯等

**海外市场**:
- Interactive Brokers (IB)
- 易盛9.0外盘
- 直达期货

### 量化应用 (App)

- **cta_strategy**: CTA策略引擎
- **cta_backtester**: CTA回测模块
- **spread_trading**: 价差交易
- **option_master**: 期权交易
- **portfolio_strategy**: 组合策略
- **algo_trading**: 算法交易
- **script_trader**: 脚本策略
- **paper_account**: 本地仿真
- **chart_wizard**: K线图表
- **portfolio_manager**: 组合管理
- **rpc_service**: RPC服务
- **data_manager**: 数据管理
- **data_recorder**: 行情记录
- **excel_rtd**: Excel RTD
- **risk_manager**: 风险管理
- **web_trader**: Web服务

### 数据库适配

**SQL类**: SQLite、MySQL、PostgreSQL

**NoSQL类**: DolphinDB、TDengine、MongoDB

### 数据服务

RQData、迅投研、MultiCharts、TuShare、Wind、同花顺iFinD、天勤TQSDK、掘金、polygon

---

## 安装方式

**Windows**:
```bash
install.bat
```

**Ubuntu**:
```bash
bash install.sh
```

**macOS**:
```bash
bash install_osx.sh
```

---

## 依赖项

**核心依赖**:
- PySide6 >= 6.8.2.1
- pyqtgraph >= 0.13.7
- qdarkstyle >= 3.2.3
- numpy >= 2.2.3
- pandas >= 2.2.3
- ta-lib >= 0.6.4
- deap >= 1.4.2
- pyzmq >= 26.3.0
- plotly >= 6.0.0
- tqdm >= 4.67.1
- loguru >= 0.7.3
- nbformat >= 5.10.4
- tzlocal >= 5.3.1

**AI模块额外依赖** (可选):
- polars >= 1.26.0
- scipy >= 1.15.2
- scikit-learn >= 1.6.1
- lightgbm >= 4.6.0
- torch >= 2.6.0
- pyarrow >= 19.0.1
- alphalens-reloaded >= 0.4.5

---

## 版本历史

### v4.3.0 (当前版本)
- 新增WorldQuant Alpha 101因子特征数据集
- 多个模块升级适配4.0版本
- 多项bug修复

### v4.2.0
- 重构vnpy_riskmanager模块(插件式设计)
- 新增vnpy_polygon数据服务
- 升级CTP API到6.7.11

### v4.1.0
- 新增ETF类型支持
- 增加遗传算法优化函数
- 完成4.0版本模块升级适配

---

## 贡献代码

1. 创建Issue讨论较大改动
2. Fork项目仓库
3. 从dev分支创建feature分支
4. 修改后提交PR到dev分支
5. 遵守代码规范:
   - 使用`ruff check .`检查代码样式
   - 使用`mypy vnpy`进行类型检查

---

*文档生成时间: 2026/05/09*
