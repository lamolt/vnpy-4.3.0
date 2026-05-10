"""
VeighNa Trader 启动脚本 - 包含CTP接口和CTA策略模块
"""
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp

from vnpy_ctp import CtpGateway
from vnpy_ctastrategy import CtaStrategyApp
from vnpy_ctabacktester import CtaBacktesterApp


def main():
    """Start VeighNa Trader with CTP and CTA modules"""
    qapp = create_qapp("vnpy")

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)

    # 添加CTP交易接口
    main_engine.add_gateway(CtpGateway)

    # 添加CTA策略应用
    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(CtaBacktesterApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()