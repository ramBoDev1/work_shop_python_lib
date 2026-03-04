"""Demo: ใช้ math และ random สำหรับผู้เริ่มต้น"""

import math
import random


def run_math_demo() -> None:
    print("== math demo ==")
    number = 49
    print(f"sqrt({number}) = {math.sqrt(number):.2f}")
    print(f"pi (4 ตำแหน่ง) = {math.pi:.4f}")
    print(f"ceil(4.2) = {math.ceil(4.2)}")
    print(f"floor(4.8) = {math.floor(4.8)}")


def run_random_demo() -> None:
    print("\n== random demo ==")
    dice = random.randint(1, 6)
    color = random.choice(["red", "green", "blue"])
    print(f"ทอยลูกเต๋าได้: {dice}")
    print(f"สุ่มสีได้: {color}")

    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)
    print(f"shuffle list: {numbers}")


if __name__ == "__main__":
    run_math_demo()
    run_random_demo()
