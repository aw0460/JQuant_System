import matplotlib.pyplot as plt
import pandas as pd
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 确保 docs 目录存在
os.makedirs("docs", exist_ok=True)

def plot_equity_curve(df: pd.DataFrame, save_path="docs/equity_curve.png"):
    """资金曲线"""
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['equity_curve'], label="策略净值")
    plt.title("策略回测资金曲线")
    plt.xlabel("日期")
    plt.ylabel("资金")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)  # 保存图片
    plt.close()  # 关闭图像，避免重复显示

def plot_signals(df: pd.DataFrame, save_path="docs/signals.png"):
    """K线 + 策略信号"""
    plt.figure(figsize=(14, 6))
    plt.plot(df['date'], df['close'], label="收盘价", alpha=0.7)
    plt.plot(df['date'], df['ma_short'], label="MA短期")
    plt.plot(df['date'], df['ma_long'], label="MA长期")

    buy_signals = df[df['signal'] == 1]
    sell_signals = df[df['signal'] == -1]
    plt.scatter(buy_signals['date'], buy_signals['close'], marker="^", color="g", label="买入", alpha=0.8)
    plt.scatter(sell_signals['date'], sell_signals['close'], marker="v", color="r", label="卖出", alpha=0.8)

    plt.title("双均线策略信号")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)  # 保存图片
    plt.close()
