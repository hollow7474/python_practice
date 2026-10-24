# Вариант 1. Консольный калькулятор (несколько операций подряд)


def show(result):
    # Если число целое (например 60.0), выводим без ".0"
    if result == int(result):
        return str(int(result))
    return str(result)


def calculate(a, op, b):
    """Возвращает результат или выбрасывает ValueError с текстом ошибки."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op in ("/", "//", "%"):
        if b == 0:
            raise ValueError("деление на ноль!")
        if op == "/":
            return a / b
        if op == "//":
            return a // b
        return a % b
    if op == "^":
        if a == 0 and b < 0:
            raise ValueError("ноль нельзя возвести в отрицательную степень!")
        if a < 0 and b != int(b):
            raise ValueError("результат не является вещественным числом!")
        return a ** b
    raise ValueError("неизвестная операция!")


def ask_continue():
    while True:
        answer = input("Хотите выполнить ещё одну операцию? (да/нет): ").strip().lower()
        if answer == "да":
            return True
        if answer == "нет":
            return False
        print("Ошибка: введите «да» или «нет».")


print("Консольный калькулятор")
print("Операции: + - * / // % ^ (степень)")

while True:
    try:
        a = float(input("Введите первое число: ").replace(",", "."))
        op = input("Введите операцию: ").strip()
        b = float(input("Введите второе число: ").replace(",", "."))
    except ValueError:
        print("Ошибка: нужно вводить числа!")
    else:
        try:
            print("Результат:", show(calculate(a, op, b)))
        except ValueError as error:
            print("Ошибка:", error)
        except OverflowError:
            print("Ошибка: число слишком большое!")

    if not ask_continue():
        break

print("Работа программы завершена.")
