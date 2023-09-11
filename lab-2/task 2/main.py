import math

def expression(x):
    z = math.sqrt(2) / 2 * math.sin(1 / x) + 1
    return z

x = float(input("Введіть значення x: "))
print("Значення виразу z =", expression(x))

from mod import check_nedostat

# Приклад виклику функції
n = int(input("Введіть число n: "))
check_nedostat(n)
