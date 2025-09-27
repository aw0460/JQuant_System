from backtest.backtest_engine import run_backtest, save_report, save_backtest_results
from visualization.plot_results import plot_equity_curve, plot_signals
from strategies.moving_average import moving_average_strategy
import akshare as ak
import pandas as pd


def main():
    # 1. 获取数据
    df = ak.stock_zh_index_daily(symbol="sh000300")  # 沪深300
    df = df.reset_index()
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    df = df[['date', 'open', 'high', 'low', 'close', 'volume']]

    # 2. 策略
    df = moving_average_strategy(df)

    # 3. 回测
    df, total_return, max_drawdown = run_backtest(df)

    print(f"总收益率: {total_return:.2%}, 最大回撤: {max_drawdown:.2%}")

    # 4. 保存报告 & 数据
    save_report(total_return, max_drawdown)
    save_backtest_results(df)

    # 5. 可视化并保存图片
    plot_equity_curve(df)
    plot_signals(df)

    # 6. 自动更新 README
    update_readme(total_return, max_drawdown)

    print("🎉 所有回测结果已保存至 docs/ 并更新 README.md")



def update_readme(total_return, max_drawdown):
    """自动更新 README.md 文件，插入最新回测结果"""
    readme_path = "README.md"
    content = f"""
# 📈 JQuant System

这是一个个人量化金融系统，用于分析中国A股数据（示例：沪深300）。

## 🔹 最新回测结果
- 总收益率: {total_return:.2%}  
- 最大回撤: {max_drawdown:.2%}  

## 📊 策略资金曲线
![equity_curve](docs/equity_curve.png)

## 📌 策略买卖点信号
![signals](docs/signals.png)

## 📂 回测结果文件
- [回测报告 (report.txt)](docs/report.txt)  
- [完整回测数据 (backtest_results.csv)](docs/backtest_results.csv)  
    """

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content.strip())

    print("✅ README.md 已更新！")


if __name__ == "__main__":
    main()
