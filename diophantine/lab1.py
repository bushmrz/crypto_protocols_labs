"""
Решение диофантового уравнения первой степени с помощью расширенного алгоритма
Евклида с указанием всех промежуточных результатов.
"""


def extended_euclid(a, b):
    """
    Расширенный алгоритм Евклида для нахождения x, y таких, что ax + by = gcd(a, b),
    возвращает gcd(a, b), x, y и промежуточные результаты.
    """
    if a == 0:
        return (b, 0, 1, [(b, 0, 1)])
    else:
        gcd, x1, y1, intermediates = extended_euclid(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        intermediates.append((gcd, x, y))
        return (gcd, x, y, intermediates)


def solve_diophantine(a, b, c):
    """
    Решает диофантово уравнение ax + by = c и выводит промежуточные результаты.
    """
    gcd, x, y, intermediates = extended_euclid(a, b)

    # Проверяем, делится ли c на НОД(a, b) для определения возможности решения уравнения.
    if c % gcd == 0:
        # Масштабируем решение, чтобы получить конечные x и y для ax + by = c
        x *= c // gcd
        y *= c // gcd
        return f"Уравнение {a}x + {b}y = {c} имеет решение: x = {x}, y = {y}", intermediates
    else:
        return "Уравнение не имеет решения", intermediates


# Пример данных
a, b, c = 37, 11, 1
print(solve_diophantine(a, b, c))
