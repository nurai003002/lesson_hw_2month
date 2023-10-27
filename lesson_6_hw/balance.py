from password_check import check_password
check_password()
class Money:
    def cridet(self):
        balance = 0 
        print(f"Ваш текущий баланс: {balance} ")

        print("ПОПОЛНЕНИЕ")
        user = int(input("На сколько хотите пополнить баланс: "))
        all1 = balance + user
        print(f"Ваш баланс пополнен на {all1}сом")

        print("СНЯТИЕ")
        user_1 = int(input("Сколько хотите снять: "))
        balance = all1 - user_1
        print(f"С вашего счета списано: -{user_1} сом")
        print(f"Ваш текущий баланс: {balance} сом ")



  