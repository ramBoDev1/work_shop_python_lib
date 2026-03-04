"""Exercise 3: pandas + matplotlib

โจทย์:
1) สร้าง DataFrame คะแนนนักเรียน 10 คน
2) หาค่าเฉลี่ยและคะแนนสูงสุด
3) วาด bar chart คะแนนแล้วบันทึกไฟล์ภาพ
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# TODO: เติมข้อมูลให้ครบ 10 คน
students = pd.DataFrame(
    {
        "name": ["A", "B", "C", "D", "E"],
        "score": [78, 85, 92, 66, 88],
    }
)

# TODO: หาค่าเฉลี่ยและคะแนนสูงสุด
avg_score = 0
max_score = 0

print("ค่าเฉลี่ย:", avg_score)
print("ค่าสูงสุด:", max_score)

# TODO: วาด bar chart แล้ว save เป็น outputs/student_scores.png
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)
