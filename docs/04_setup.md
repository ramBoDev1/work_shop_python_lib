# วิธีเตรียมเครื่องสำหรับเวิร์กช็อป

## 1) ตรวจ Python
```bash
python --version
```
แนะนำ Python 3.10 ขึ้นไป

## 2) สร้าง Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3) ติดตั้งไลบรารีที่ใช้ในคลาส
```bash
pip install -r requirements.txt
```

## 4) ทดสอบ import เบื้องต้น
```bash
python -c "import math, random; import datetime; import requests, pandas, matplotlib; print('ready')"
```

ถ้าเห็นคำว่า `ready` แปลว่าพร้อมเรียน
