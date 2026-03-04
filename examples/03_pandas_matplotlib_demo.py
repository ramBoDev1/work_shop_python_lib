"""Demo: ใช้ pandas และ matplotlib"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def build_sales_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "day": [1, 2, 3, 4, 5, 6, 7],
            "sales": [120, 150, 90, 170, 200, 180, 210],
        }
    )


def summarize(df: pd.DataFrame) -> None:
    print("== summary ==")
    print(df)
    print("ค่าเฉลี่ยยอดขาย:", round(df["sales"].mean(), 2))
    print("ยอดขายสูงสุด:", int(df["sales"].max()))


def plot_sales(df: pd.DataFrame) -> None:
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "daily_sales_line.png"

    plt.figure(figsize=(8, 4))
    plt.plot(df["day"], df["sales"], marker="o")
    plt.title("Daily Sales")
    plt.xlabel("Day")
    plt.ylabel("Sales")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print(f"บันทึกกราฟแล้ว: {output_path}")


if __name__ == "__main__":
    sales_df = build_sales_dataframe()
    summarize(sales_df)
    plot_sales(sales_df)
