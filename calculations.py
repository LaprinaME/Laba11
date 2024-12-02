import math

# Умножение
def multiply(a, b):
    return a * b

# Деление
def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

# Вычисление расстояния между двумя точками
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Решение квадратного уравнения
def quadratic(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None  # Нет действительных корней
    elif discriminant == 0:
        return -b / (2 * a)  # Один корень
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2

# Сумма геометрической прогрессии
def geometric_sum(a, r, n):
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)
