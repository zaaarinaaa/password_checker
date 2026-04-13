import re

def check_password(password):
    length_ok = len(password) >= 8
    digit_ok = any(char.isdigit() for char in password)
    symbol_ok = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    return length_ok, digit_ok, symbol_ok


def password_strength(password):
    length_ok, digit_ok, symbol_ok = check_password(password)

    print("\nПроверка пароля:")

    if length_ok:
        print("✔ Длина не меньше 8 символов")
    else:
        print("✘ Пароль слишком короткий")

    if digit_ok:
        print("✔ Есть цифра")
    else:
        print("✘ Нет цифры")

    if symbol_ok:
        print("✔ Есть специальный символ")
    else:
        print("✘ Нет специального символа")


def main():
    while True:
        password = input("\nВведите пароль: ")

        if not password:
            print("Ошибка: пароль не может быть пустым")
            continue

        password_strength(password)

        again = input("\nПроверить другой пароль? (y/n): ").lower()
        if again != "y":
            print("Программа завершена.")
            break


if __name__ == "__main__":
    main()
