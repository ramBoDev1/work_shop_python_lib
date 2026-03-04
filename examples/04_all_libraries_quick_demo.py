"""Quick demo: รวมการใช้ทุกไลบรารีในไฟล์เดียว"""

import math
import random
from datetime import datetime

import pandas as pd
import requests


def main() -> None:
    print("sqrt(81) =", math.sqrt(81))
    print("random 1-10 =", random.randint(1, 10))
    print("time now =", datetime.now().strftime("%Y-%m-%d %H:%M"))

    todo = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10).json()
    print("todo title =", todo["title"])

    df = pd.DataFrame({"name": ["A", "B", "C"], "score": [80, 90, 75]})
    print("mean score =", df["score"].mean())


if __name__ == "__main__":
    main()
