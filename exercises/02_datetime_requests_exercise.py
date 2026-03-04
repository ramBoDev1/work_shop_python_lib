"""Exercise 2: datetime + requests

โจทย์:
1) ดึงข้อมูลจาก https://jsonplaceholder.typicode.com/users
2) แสดงชื่อผู้ใช้ 5 คนแรก
3) แสดงเวลาปัจจุบันกำกับผลลัพธ์
"""

from datetime import datetime

import requests


def main() -> None:
    # TODO: เรียก API และเก็บผลลัพธ์ JSON ลงใน users
    users = []

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"ดึงข้อมูลเมื่อ: {now}")

    print("รายชื่อผู้ใช้ 5 คนแรก")
    # TODO: loop แสดงชื่อ 5 คนแรก จาก key: name


if __name__ == "__main__":
    main()
