"""เฉลย Exercise 3: pandas + matplotlib"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

students = pd.DataFrame(
    {
        "name": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        "score": [78, 85, 92, 66, 88, 74, 95, 81, 69, 90],
    }
)

avg_score = students["score"].mean()
max_score = students["score"].max()

print("ค่าเฉลี่ย:", round(avg_score, 2))
print("ค่าสูงสุด:", int(max_score))

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)
output_path = output_dir / "student_scores.png"

plt.figure(figsize=(8, 4))
plt.bar(students["name"], students["score"])
plt.title("Student Scores")
plt.xlabel("Student")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(output_path)
plt.close()

print(f"บันทึกกราฟแล้ว: {output_path}")
