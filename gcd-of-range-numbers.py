def gcd_of_range_numbers(L: str, R: str) -> str:
    if (L > R):
        return "Число начала диапазона, не может быть больше числа конца диапазона"

    if (L == R):
        return L

    return 1

L = input('Введите число начала диапазона: ')
R = input('Введите число конца диапазона: ')
print(gcd_of_range_numbers(L, R))
