# Python Libraries Workshop (Beginner, Thai)

ชุดเอกสารและโค้ดตัวอย่างสำหรับสอนเวิร์กช็อป 3 ชั่วโมงเรื่องการใช้ Python libraries สำหรับผู้เริ่มต้น

## โครงสร้างไฟล์
- `docs/`
  - `01_instructor_guide.md` คู่มือผู้สอน (objective, agenda, teaching flow, rubric)
  - `02_teaching_script.md` สคริปต์การสอนแบบจับเวลา
  - `03_quiz.md` แบบทดสอบพร้อมเฉลยย่อ
  - `04_setup.md` วิธีเตรียมเครื่องผู้เรียน
- `examples/`
  - `01_math_random_demo.py`
  - `02_datetime_requests_demo.py`
  - `03_pandas_matplotlib_demo.py`
  - `04_all_libraries_quick_demo.py`
- `exercises/`
  - `01_math_random_exercise.py` + `01_math_random_solution.py`
  - `02_datetime_requests_exercise.py` + `02_datetime_requests_solution.py`
  - `03_pandas_matplotlib_exercise.py` + `03_pandas_matplotlib_solution.py`
  - `04_mini_project_template.py` + `04_mini_project_solution.py`

## วิธีเริ่มใช้งาน
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## คำสั่งรันตัวอย่าง
```bash
python examples/01_math_random_demo.py
python examples/02_datetime_requests_demo.py
python examples/03_pandas_matplotlib_demo.py
python examples/04_all_libraries_quick_demo.py
```

## คำสั่งรันแบบฝึกหัด
```bash
python exercises/01_math_random_exercise.py
python exercises/02_datetime_requests_exercise.py
python exercises/03_pandas_matplotlib_exercise.py
python exercises/04_mini_project_template.py
```

ไฟล์กราฟจะถูกบันทึกในโฟลเดอร์ `outputs/` เมื่อรันไฟล์ที่มีการ plot
