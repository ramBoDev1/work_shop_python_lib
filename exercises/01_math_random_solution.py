"""เฉลย Exercise 1: math + random"""

import math
import random

number = random.randint(1, 50)
root_value = math.sqrt(number)

print("สุ่มได้:", number)
print("รากที่สอง:", f"{root_value:.2f}")

if number > 25:
    print("สูง")
else:
    print("ต่ำ")
