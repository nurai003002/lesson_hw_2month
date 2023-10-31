import sqlite3

connect = sqlite3.connect("players.db")
cursor = connect.cursor()
from game_db import sqlite3
def abu(user, new_nick_name):
        cursor.execute(f'''UPDATE players SET souses = '{user}' WHERE nick_name = "{new_nick_name}"''')
        nick_name = new_nick_name
        connect.commit()
def sauce():
        new_nick_name = input("Введите свой никнейм: ")
        print("\n")
        print("ВИДЫ СОУСОВ")
        print(" кетчуп, сырный соус,  соус Ранч, острый соус")
        user = input("Выберите какой соус хотите: ")
        if user == "кетчуп":
            print(f"Тесто с кетчупом, готово")
        elif user == "сырный соус":
            print(f"Тесто с сырный соусом, готово")
        elif user == "соус ранч":
            print(f"Тесто с соус ранч, готово")
        elif user == "острый соус":
            print(f"Тесто с острым соусом, готово")
        else:
            print("Ошибка, введите только данные числа")
        abu(user, new_nick_name)
        
