def egcd(a, b):
    """Расширенный алгоритм Евклида для нахождения x, y: ax + by = gcd(a, b)"""
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


def modinv(a, m):
    """Обратное по модулю: нахождение a^-1 mod m"""
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Обратный элемент не существует')
    else:
        return x % m


def chinese_remainder_theorem(a, m):
    """Реализация китайской теоремы об остатках"""
    M = 1
    x = 0
    result = {"M": None, "intermediate_results": [], "solution": None}

    for modulus in m:
        M *= modulus

    for i in range(len(a)):
        Mi = M // m[i]
        yi = modinv(Mi, m[i])
        x += a[i] * Mi * yi
        result["intermediate_results"].append({"Mi": Mi, "yi": yi, "calculation": f"{a[i]} * {Mi} * {yi}"})

    x %= M
    result["M"] = M
    result["solution"] = x

    return result


# Пример данных
a = [13, 16, 19]  # Остатки
m = [3, 5, 7]  # Модули

# Выполнение КТО
chinese_remainder_theorem_result = chinese_remainder_theorem(a, m)
print(chinese_remainder_theorem_result)
