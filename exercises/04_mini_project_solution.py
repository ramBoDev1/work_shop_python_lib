"""เฉลย Mini Project: สรุปอุณหภูมิ 7 วัน"""

import math
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import requests


def fetch_weather() -> dict:
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=13.7563&longitude=100.5018"
        "&daily=temperature_2m_max,temperature_2m_min"
        "&forecast_days=7&timezone=Asia%2FBangkok"
    )
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    return response.json()


def main() -> None:
    data = fetch_weather()
    daily = data["daily"]

    df = pd.DataFrame(
        {
            "time": pd.to_datetime(daily["time"]),
            "temp_max": daily["temperature_2m_max"],
            "temp_min": daily["temperature_2m_min"],
        }
    )

    print("ตัวอย่างข้อมูล:")
    print(df.head())

    avg_max = df["temp_max"].mean()
    avg_min = df["temp_min"].mean()

    # ใช้ math.floor/ceil เพื่อโชว์การประยุกต์ math กับข้อมูลจริง
    print(f"avg temp max: {avg_max:.2f} C (floor={math.floor(avg_max)})")
    print(f"avg temp min: {avg_min:.2f} C (ceil={math.ceil(avg_min)})")

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "weather_7_days.png"

    plt.figure(figsize=(9, 4))
    plt.plot(df["time"], df["temp_max"], marker="o", label="Max Temp")
    plt.plot(df["time"], df["temp_min"], marker="o", label="Min Temp")
    plt.title("Bangkok: 7-Day Temperature Forecast")
    plt.xlabel("Date")
    plt.ylabel("Temperature (C)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print(f"บันทึกกราฟแล้ว: {output_path}")


if __name__ == "__main__":
    main()
