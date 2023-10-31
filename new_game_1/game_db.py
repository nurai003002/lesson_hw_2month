
import sqlite3

connect = sqlite3.connect("players.db")
cursor = connect.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS players (
               id INTEGER PRIMARY KEY,
               name VARCHAR (100) NOT NULL,
               nick_name VARCHAR (100) NOT NULL,
               age INTEGER NOT NULL DEFAULT 0,
               souses TEXT,
               nachinki TEXT,
               cheese TEXT

              
);""")

class Person:
    def __init__(self):
        self.name = None
        self.nick_name = None
        self.age = 0
        self.souses = None 
        self.nachinki = None
        self.cheese = None


    
    def registration(self, name, nick_name, age):  
        self.name = name
        self.nick_name = nick_name
        self.age = age
       
       
        cursor.execute(f""" INSERT INTO players (name, nick_name, age)
                        VALUES ('{name}','{nick_name}','{age}');""")
    
        connect.commit()

    def hi(self):
        print("РЕГИСТРАЦИЯ")
        print("Откройте свой личный кабинет")
        name = input("Введите ваше имя: ")
        nick_name = input("Введите ваш nick_name: ")
        age = int(input("Ваш возраст: "))
        print(f"Дорогой игрок - {name} приветсвую тебя")
        print(f"Региcтрация прошла успешно.\n")
        self.registration(name, nick_name, age)
    
   
    



# if __name__ == "__main__":
#     person = Person()
#     person.hi()