# Вариант 1. Консольный калькулятор


def show(result):
    # Если число целое (например 60.0), выводим без ".0"
    if result == int(result):
        return str(int(result))
    return str(result)


print("Консольный калькулятор")
print("Операции: + - * / // % ^ (степень)")

try:
    a = float(input("Введите первое число: "))
    op = input("Введите операцию: ").strip()
    b = float(input("Введите второе число: "))
except ValueError:
    print("Ошибка: нужно вводить числа!")
    exit()

if op == "+":
    print("Результат:", show(a + b))
elif op == "-":
    print("Результат:", show(a - b))
elif op == "*":
    print("Результат:", show(a * b))
elif op == "/":
    if b == 0:
        print("Ошибка: деление на ноль!")
    else:
        print("Результат:", show(a / b))
elif op == "//":
    if b == 0:
        print("Ошибка: деление на ноль!")
    else:
        print("Результат:", show(a // b))
elif op == "%":
    if b == 0:
        print("Ошибка: деление на ноль!")
    else:
        print("Результат:", show(a % b))
elif op == "^":
    if a == 0 and b < 0:
        print("Ошибка: ноль нельзя возвести в отрицательную степень!")
    elif a < 0 and b != int(b):
        print("Ошибка: результат не является вещественным числом!")
    else:
        print("Результат:", show(a ** b))
else:
    print("Ошибка: неизвестная операция!")
