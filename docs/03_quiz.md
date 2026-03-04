# Quiz: Python Libraries (Beginner)

## คำถาม
1. `pip install` ใช้ทำอะไร?
2. `import random as rd` หมายถึงอะไร?
3. `random.randint(1, 3)` มีโอกาสได้ค่า `3` หรือไม่?
4. `datetime` มักใช้แก้ปัญหาเรื่องอะไร?
5. `requests.get(url).json()` คืนค่าเป็นข้อมูลชนิดใด?
6. `pandas` เหมาะกับงานประเภทไหนมากที่สุด?
7. `matplotlib` มีหน้าที่หลักอะไร?
8. ถ้าจะใช้งานฟังก์ชันใหม่ใน docs ควรอ่านส่วนไหนก่อน?
9. เขียนโค้ด 1 บรรทัดเพื่อหาค่าเฉลี่ยคอลัมน์ `score` จาก `df`
10. ถ้าเจอ `ModuleNotFoundError` ควรตรวจอะไรเป็นอันดับแรก?

## เฉลยย่อ
1. ติดตั้ง package เพิ่มใน environment ปัจจุบัน
2. import `random` แล้วตั้งชื่อย่อเป็น `rd`
3. มีโอกาสได้ เพราะ `randint` รวมปลายทั้งสองฝั่ง
4. จัดการวันเวลา, บวก/ลบเวลา, format เวลา
5. โดยทั่วไปเป็น `dict` หรือ `list` (ตาม JSON)
6. งานตารางข้อมูล/วิเคราะห์ข้อมูลเบื้องต้น
7. วาดกราฟและแผนภาพข้อมูล
8. function signature, parameters, และ example
9. `df["score"].mean()`
10. เช็กว่า install package ใน env ที่เปิดใช้งานอยู่หรือไม่
