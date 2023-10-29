import sqlite3

connect = sqlite3.connect("list_doctors.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS hospital (
               id INTEGER PRIMARY KEY,
               profation TEXT NOT NULL,
               surname VARCHAR (100) NOT NULL,
               name VARCHAR (160) NOT NULL,
               age INTEGER NOT NULL DEFAULT 0,            
               experience INTEGER NOT NULL DEFAULT 0,
               salary INTEGER NOT NULL DEFAULT 0,
               is_active BOOLEAN NOT NULL DEFAULT FALSE
)              
""")


class WorkHospital:
    def __init__(self):
        self.surname = None
        self.name = None
        self.age = 0
        self.profation = 0
        self.experience = 0
        self.salary = 0 
        self.is_active = False

    def registration(self, surname, name, age, profation):
        self.surname = surname
        self.name = name 
        self.age = age 
        self.profation = profation
        
        cursor.execute(f""" INSERT INTO hospital  (profation,surname, name, age, experience , salary, is_active)
                       VALUES (' {profation}', '{surname}','{name}','{age}', 0,0, True); """) 
        connect.commit()


    def work_experience(self, exper):
            cursor.execute(f""" UPDATE hospital SET experience = experience + {exper} WHERE name = '{self.name}'""")
            self.experience += exper
            connect.commit()
       

    def take(self, salary_all):
        cursor.execute(f""" UPDATE hospital SET salary = salary + {salary_all} WHERE name = '{self.name}'""")
        self.salary += salary_all
        connect.commit()

    def minus(self, salary_all):
        cursor.execute(f""" UPDATE hospital SET salary = salary - {salary_all} WHERE name = '{self.name}'""")
        self.salary -= salary_all
        connect.commit()
    

  

    def main(self):
        while True:
            print("1 - Регистрация, 2 - Ввести опыт работы , 3 - Пополнить деньги , 4 - Снятие денег , 5 - выйти ")
            commands = int(input("Выберите команду: "))
            if commands == 1:
                print("РЕГИСТРАЦИЯ")
                profation = input("Ваша должность в больнице: ")
                surname = input("Введите вашу фамилию: ")
                name = input("Введите ваше имя: ")
                age = int(input("Введите ваш возраст: "))
                print("Регистрация прошла")
                self.registration(surname, name, age, profation)

            elif commands == 2:
                if self.profation:
                    print("ОПЫТ РАБОТЫ")
                    salary_all = int(input("Введите опыт работы: "))
                    self.work_experience(salary_all)
                else:
                    print("Пройдите регистрацию")
                
            elif commands == 3:
                print("ПОПОЛНЕНИЕ")
                salary_all = int(input("Введите сумму: "))
                self.take(salary_all)

            elif commands == 4:
                    print("ВЫВЕСТИ ДЕНЬГИ")
                    salary_all = int(input("Введите сумму: "))
                    self.minus(salary_all)

            elif commands == 5:
                break  

            else:
                print("1 - Регистрация, 2 - Ввести опыт работы , 3 - Вывести деньги , 4 - выйти, 5 - выйти ")
                commands = int(input("Выберите команду: "))

work = WorkHospital() 
work.main()



            



                

            



            

    



