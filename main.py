import sys


def sortirovka(arr):
    for i in range(len(arr)):
        low = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[low]:
                low = j
        arr[i], arr[low] = arr[low], arr[i]


def main():
    while True:
        user_input = input("\nВведите числа через пробел (или 'q' для выхода): ").strip()

        if user_input.lower() == 'q':
            print("Программа завершена.")
            break

        if not user_input:
            print("Ошибка: Ввод не может быть пустым.")
            continue

        try:
            numbers = list(map(int, user_input.split()))

            original = numbers.copy()
            sortirovka(numbers)

            print(f"Исходный массив: {original}")
            print(f"Отсортированный: {numbers}")

        except ValueError:
            print("Ошибка: Вводите только целые числа через пробел.")
            print("Пример: 5 2 8 1 9")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем.")
        sys.exit(0)
