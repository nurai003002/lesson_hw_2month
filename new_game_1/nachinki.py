import sqlite3

connect = sqlite3.connect("players.db")
cursor = connect.cursor()
from game_db import sqlite3
def abu(user, new_nick_name):
        cursor.execute(f'''UPDATE players SET nachinki = '{user}' WHERE nick_name = "{new_nick_name}"''')
        nick_name = new_nick_name
        connect.commit()
def fillings():
    new_nick_name = input("Введите свой никнейм: ")
    print(f"\n")
    print("НАЧИНКИ")
    print("ЕСТЬ 5 ВИДОВ НАЧИКИ")
    fils_list = ("пеперони","гриб","оливка","сосиски","помидор")
    print(fils_list)
    user = input("Выберите начинку: ")
    fill_1 = "пеперони"
    fill_2 = "гриб"
    fill_3 = "оливка"
    fill_4 = "сосиски"
    fill_5 = "помидор"
    if user == 'пеперони':
        print(f"тесто с начинкой '{fill_1}' готово ")
    elif user == 'гриб':
        print(f"тесто с '{fill_2}' готово ")
    elif user == 'оливка':
        print(f"тесто с начинкой '{fill_3}' готово ")
    elif user == 'сосиски':
        print(f"тесто с начинкой '{fill_4}' готово ")
    elif user == 'помидор':
        print(f"тесто с начинкой '{fill_5}' готово ")

    abu(user,new_nick_name)



    
