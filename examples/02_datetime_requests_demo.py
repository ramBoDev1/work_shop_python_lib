"""Demo: ใช้ datetime และ requests"""

from datetime import datetime, timedelta

import requests


def run_datetime_demo() -> None:
    print("== datetime demo ==")
    now = datetime.now()
    next_week = now + timedelta(days=7)
    print("เวลาปัจจุบัน:", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("อีก 7 วัน:", next_week.strftime("%Y-%m-%d"))


def run_requests_demo() -> None:
    print("\n== requests demo ==")
    url = "https://jsonplaceholder.typicode.com/todos/1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        print("title:", data.get("title"))
        print("completed:", data.get("completed"))
    except requests.RequestException as exc:
        print("เรียก API ไม่สำเร็จ:", exc)


if __name__ == "__main__":
    run_datetime_demo()
    run_requests_demo()
