"""เฉลย Exercise 2: datetime + requests"""

from datetime import datetime

import requests


def main() -> None:
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        print("เรียก API ไม่สำเร็จ:", exc)
        return

    users = response.json()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"ดึงข้อมูลเมื่อ: {now}")

    print("รายชื่อผู้ใช้ 5 คนแรก")
    for user in users[:5]:
        print("-", user.get("name"))


if __name__ == "__main__":
    main()
