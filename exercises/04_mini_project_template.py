"""Mini Project Template: สรุปอุณหภูมิ 7 วัน

สิ่งที่ต้องทำ:
1) ดึงข้อมูลพยากรณ์อากาศรายวันจาก Open-Meteo
2) แปลงข้อมูลเป็น DataFrame
3) แสดงตารางอย่างน้อย 5 แถว
4) คำนวณค่าเฉลี่ยอุณหภูมิสูงสุด
5) วาดกราฟอุณหภูมิและบันทึกไฟล์ภาพ
"""

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

    # TODO: สร้าง DataFrame จาก data["daily"] โดยมีคอลัมน์
    # time, temperature_2m_max, temperature_2m_min
    df = pd.DataFrame()

    # TODO: แปลงคอลัมน์ time เป็น datetime

    print("ตัวอย่างข้อมูล:")
    print(df.head())

    # TODO: คำนวณค่าเฉลี่ย temperature_2m_max แล้วพิมพ์ออกมา

    # TODO: วาด line chart temp max/min แล้ว save เป็น outputs/weather_7_days.png
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)


if __name__ == "__main__":
    main()
