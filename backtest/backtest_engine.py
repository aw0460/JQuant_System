import pandas as pd
import os

def run_backtest(df: pd.DataFrame, initial_cash=100000):
    """简易回测引擎"""
    df['return'] = df['close'].pct_change()
    df['strategy_return'] = df['signal'].shift(1) * df['return']
    df['equity_curve'] = (1 + df['strategy_return']).cumprod() * initial_cash

    total_return = df['equity_curve'].iloc[-1] / initial_cash - 1
    max_drawdown = ((df['equity_curve'].cummax() - df['equity_curve']) / df['equity_curve'].cummax()).max()

    return df, total_return, max_drawdown


def save_report(total_return: float, max_drawdown: float, save_path="docs/report.txt"):
    """保存回测结果报告"""
    os.makedirs("docs", exist_ok=True)
    with open(save_path, "w", encoding="utf-8") as f:
        f.write("回测结果报告\n")
        f.write("=====================\n")
        f.write(f"总收益率: {total_return:.2%}\n")
        f.write(f"最大回撤: {max_drawdown:.2%}\n")
    print(f"回测报告已保存至 {save_path}")


def save_backtest_results(df: pd.DataFrame, save_path="docs/backtest_results.csv"):
    """保存完整回测数据到 CSV"""
    os.makedirs("docs", exist_ok=True)
    df.to_csv(save_path, index=False, encoding="utf-8-sig")
    print(f"回测数据已保存至 {save_path}")
