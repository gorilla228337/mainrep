import math

ITERATIONS = 10


def hyperbolic_cosine(x):
    """
    Вычисляет гиперболический косинус через ряд Тейлора.

    Аргументы:
    x -- значение

    Возвращаемое значение:
    Значение гиперболического косинуса.

    Исключения:
    Нет.

    Примеры использования:
    >>> hyperbolic_cosine(1)
    1.5430806348152437
    """
    result = 0
    for n in range(ITERATIONS):
        result += (x ** (2 * n)) / math.factorial(2 * n)
    return result


def binomial_series(x, m):
    """
    Вычисляет биномиальный ряд для (1 - x)^m.

    Аргументы:
    x -- значение
    m -- степень

    Возвращаемое значение:
    Значение биномиального ряда.

    Исключения:
    Нет.

    Примеры использования:
    >>> binomial_series(0.5, 3)
    0.125
    """
    result = 1
    term = 1
    for n in range(1, ITERATIONS):
        term *= (m - n + 1) / n * (-x)
        result += term
    return result


def cosine(x):
    """
    Вычисляет косинус через ряд Тейлора.

    Аргументы:
    x -- значение угла в радианах

    Возвращаемое значение:
    Значение косинуса.

    Исключения:
    Нет.

    Примеры использования:
    >>> cosine(math.pi)
    -1.0
    """
    result = 0
    for n in range(ITERATIONS):
        result += ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
    return result

def main():
    while True:
        print("Выберите функцию:")
        print("1. Гиперболический косинус")
        print("2. Биномиальный ряд")
        print("3. Косинус")
        print("4. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            x = float(input("Введите значение x: "))
            print("Результат:", hyperbolic_cosine(x))
        elif choice == '2':
            x = float(input("Введите значение x: "))
            m = float(input("Введите значение m: "))
            print("Результат:", binomial_series(x, m))
        elif choice == '3':
            x = float(input("Введите значение x (в радианах): "))
            print("Результат:", cosine(x))
        elif choice == '4':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
