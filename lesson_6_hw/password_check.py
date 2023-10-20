from regestration  import*
def check_password():
    while True:
        password1 = input("Введите пароль: ")
        if len(password1) < 8:
            print("Короткий пароль!")
            return

        elif "123" in password1:
            print("Простой пароль!")
            return

        password2 = input("Введите пароль еще раз: ")
        if password1 != password2:
            print("Различаются.")
        else:
            print("Пароль создан!")
            break
