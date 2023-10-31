import sqlite3

connect = sqlite3.connect("players.db")
cursor = connect.cursor()
from game_db import sqlite3
def  abu(user, new_nick_name):
        cursor.execute(f'''UPDATE players SET cheese = '{user}' WHERE nick_name = "{new_nick_name}"''')
        nick_name = new_nick_name
        connect.commit()
def ches():
    new_nick_name = input("Введите свой никнейм: ")
    print(f"\n")
    print("Вот и последний этап ")
    print("мацарелла, классический, сыр с плесенью, сулугуни")
    user = input("Добавьте сыр: ")
    if user == 'мацарелла':
         print("Хороший выбор")   
    elif user == 'классический':
         print("Хороший выбор")
    elif user == 'сыр с плесенью':
         print("странный выбор")
    elif user == 'сулугуни':
         print("Хороший выбор")
    abu(user, new_nick_name)
            
def last():
          print("ПОСЛЕДНИЙ ЭТАП")
          user = input("введите 'в печь' чтобы завершить: ")
          if user == 'в печь':
               print("ПИЦЦА ГОТОВО! ")

def choice():
     while True:
          choice = input("хотите приготовить еще? 'да', 'нет': ")
          if choice == "нет":
               print(f'Мы принили ваш заказй')
               break     
          elif choice == "да":
                    print(f"\n")
                    from begin import dough1
                    dough1()
                    from sous import sauce
                    sauce()
                    from nachinki import fillings
                    fillings()                
                    
                    
                      
                                    
        
            

            
    