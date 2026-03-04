# คู่มือผู้สอน: Python Libraries Workshop (3 ชั่วโมง)

## 1) ข้อมูลคอร์ส
- กลุ่มเป้าหมาย: ผู้เริ่มต้นที่รู้พื้นฐาน Python syntax แล้ว (`if`, `for`, function)
- ระยะเวลา: 3 ชั่วโมง (180 นาที)
- ภาษา: ไทย
- เป้าหมายหลัก: ผู้เรียนเข้าใจว่า library คืออะไร, ติดตั้ง/นำเข้าได้, อ่าน docs เบื้องต้นได้, และใช้งาน `math`, `random`, `datetime`, `requests`, `pandas`, `matplotlib` ในงานจริงระดับเริ่มต้นได้

## 2) Learning Objectives
เมื่อจบคลาส ผู้เรียนจะสามารถ:
1. อธิบายความหมายของ `library`, `module`, `package` ได้
2. สร้าง virtual environment และติดตั้ง package ด้วย `pip` ได้
3. ใช้ `import` ได้ทั้งแบบปกติ, ตั้ง alias, และ `from ... import ...`
4. อ่านเอกสาร library เบื้องต้น (ดู signature, parameter, example)
5. เขียนโค้ดพื้นฐานด้วย `math`, `random`, `datetime`
6. ดึงข้อมูล JSON จาก API ด้วย `requests`
7. จัดการข้อมูลตารางด้วย `pandas`
8. วาดกราฟง่ายๆ ด้วย `matplotlib`

## 3) Agenda (180 นาที)
| เวลา | หัวข้อ | วิธีสอน |
|---|---|---|
| 00:00-00:15 | เกริ่น: library คืออะไร + เป้าหมายคอร์ส | บรรยาย + ถามตอบ |
| 00:15-00:35 | ติดตั้ง package, import, อ่าน docs | Demo |
| 00:35-01:05 | `math` และ `random` | Demo + แบบฝึกหัด |
| 01:05-01:15 | พัก | - |
| 01:15-01:45 | `datetime` และ `requests` | Demo + แบบฝึกหัด |
| 01:45-02:25 | `pandas` และ `matplotlib` | Demo + แบบฝึกหัด |
| 02:25-02:50 | Mini Project | ลงมือทำเดี่ยว/คู่ |
| 02:50-03:00 | Quiz + สรุป + Q&A | แบบทดสอบ |

## 4) Teaching Flow

### ช่วง A: ปูพื้น (35 นาที)
- อธิบายความต่าง:
  - built-in library: มาพร้อม Python (`math`, `random`, `datetime`)
  - third-party library: ต้องติดตั้งเพิ่ม (`requests`, `pandas`, `matplotlib`)
- Demo คำสั่งติดตั้ง:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- Demo import:

```python
import math
import random as rd
from datetime import datetime
```

- ฝึกอ่าน docs:
  - ให้ผู้เรียนหา: `random.randint(a, b)` คืนค่ารวม `b` หรือไม่
  - ให้ผู้เรียนหา: `pandas.DataFrame.head()` ใช้ทำอะไร

### ช่วง B: `math` + `random` (30 นาที)
- เปิดไฟล์ตัวอย่าง: `examples/01_math_random_demo.py`
- เน้นแนวคิด:
  - `math` ใช้คำนวณ
  - `random` ใช้สุ่มข้อมูล
- แบบฝึกหัด: `exercises/01_math_random_exercise.py`

### ช่วง C: `datetime` + `requests` (30 นาที)
- เปิดไฟล์ตัวอย่าง: `examples/02_datetime_requests_demo.py`
- เน้นแนวคิด:
  - จัดการเวลา/รูปแบบเวลา
  - ดึงข้อมูลจาก API แล้วอ่าน JSON
- แบบฝึกหัด: `exercises/02_datetime_requests_exercise.py`

### ช่วง D: `pandas` + `matplotlib` (40 นาที)
- เปิดไฟล์ตัวอย่าง: `examples/03_pandas_matplotlib_demo.py`
- เน้นแนวคิด:
  - DataFrame = ตารางข้อมูล
  - เริ่มจากสถิติพื้นฐาน แล้วค่อยวาดกราฟ
- แบบฝึกหัด: `exercises/03_pandas_matplotlib_exercise.py`

### ช่วง E: Mini Project (25 นาที)
- ใช้ไฟล์เริ่มต้น: `exercises/04_mini_project_template.py`
- เป้าหมาย: ดึงข้อมูลอุณหภูมิ 7 วัน, สรุปผล, วาดกราฟ
- เฉลยอ้างอิง: `exercises/04_mini_project_solution.py`

## 5) Demo ที่ควรเน้นระหว่างสอน
1. อ่าน error ให้เป็น โดยเฉพาะ `ModuleNotFoundError`
2. สื่อสารเรื่อง environment ให้ชัด: ติดตั้งผิด env = import ไม่ได้
3. เวลาทำ API call ให้ใส่ `timeout` เสมอ
4. วาดกราฟแล้วบันทึกไฟล์ด้วย `plt.savefig(...)` เพื่อกันปัญหาหน้าต่างกราฟไม่ขึ้น

## 6) Hands-on Exercises
- Exercise 1: สุ่มเลข 1-50 แล้วคำนวณรากที่สอง
- Exercise 2: ดึงรายชื่อผู้ใช้จาก API และพิมพ์เวลา ณ ตอนดึงข้อมูล
- Exercise 3: สร้าง DataFrame คะแนนนักเรียน หาค่าเฉลี่ย/ค่าสูงสุด และวาด bar chart

## 7) Mini Project Rubric (ผ่านขั้นต่ำ)
- ดึงข้อมูล API ได้
- แสดง DataFrame อย่างน้อย 5 แถว
- สร้างกราฟได้ 1 กราฟ
- เขียนสรุปผลลัพธ์สั้นๆ 2-3 ประโยค

## 8) Quiz
ใช้ไฟล์ `docs/03_quiz.md` สำหรับคำถามและเฉลย

## 9) เช็กลิสต์ก่อนเริ่มสอน
- [ ] ผู้เรียนติดตั้ง Python และเปิด terminal ได้
- [ ] สร้าง `.venv` และติดตั้ง dependency ครบ
- [ ] รันตัวอย่างไฟล์แรกได้โดยไม่ error
- [ ] อินเทอร์เน็ตพร้อมสำหรับส่วน `requests`
- [ ] เตรียมเวลาเผื่อ debug อย่างน้อย 10 นาที
