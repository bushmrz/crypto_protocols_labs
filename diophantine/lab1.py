"""
Решение диофантового уравнения первой степени с помощью расширенного алгоритма
Евклида с указанием всех промежуточных результатов.
"""


def extended_euclidean_algorithm(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    print("Начальные значения:")
    print("r =", old_r, ", s =", old_s, ", t =", old_t)
    print(" ")

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

        print("Промежуточные значения:")
        print("r =", old_r, ", s =", old_s, ", t =", old_t)
        print(" ")

    return old_r, old_s, old_t

def solve_diophantine_equation(a, b, c):
    gcd, x, y = extended_euclidean_algorithm(a, b)

    if c % gcd == 0:
        x *= c // gcd
        y *= c // gcd
        return x, y
    else:
        return "Нет решений"

a = 42
b = 30
c = 18

solution = solve_diophantine_equation(a, b, c)

print(f"Для уравнения {a}*x + {b}*y = {c}, решение:")
print(f"x = {solution[0]}, y = {solution[1]}")
