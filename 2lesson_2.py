# основные принципы ооп

# class Shoes: 

#     def __init__(self, name, color, size):
#         self.name = name
#         self.color = color
#         self.size = size
#     def info(self):
#         print(f"Название - {self.name}, Цвет - {self.color}, Размер - {self.size}")
# class Loropiano(Shoes):
#     def __init__(self, name, color, size, heel = 4):
#         Shoes.__init__(self, name, color, size)
#         self.heel = heel
# shoes = Shoes("Loropiano", "Brown", 38)
# shoes.info()

# lofer = Loropiano("Лофер", "Beige", 37)
# lofer.info()
# print(lofer.heel)
    

# class Feathered():
#     def __init__(self, name, size, age):
#         self.name = name
#         self.size = size
#         self.age = age

#     def speak():
#         pass


# class Cuckoo(Feathered):
#     def __init__(self, name, size, age):
#         Feathered.__init__(self, name, size, age)
#     def speak(self):
#         print("ку-ку")

# class Pigeon(Feathered):
#     def __init__(self, name, size, age):
#         Feathered.__init__(self, name, size, age)
#     def speak(self):
#         print("кур-кур")

# class Chiken(Feathered):
#     def __init__(self, name, size, age):
#         Feathered.__init__(self, name, size, age)
#     def speak(self):
#         print("ку-ка-ре-ку")
    
# cuckoo = Cuckoo("Чирика", "15см ", 2)
# pigeon = Pigeon("Рика", "13см ", 3)
# chiken = Chiken("Желтый", "30см", 1)
# cuckoo.speak()
# pigeon.speak()
# chiken.speak()





    # def __init__(self, color, size):
    #     self.color = color
    #     self.size = size
    # def info(self):
    #     print(f"Цвет - {self.color}, Размер - {self.size}")
    
    
# дз
# №1,2
# class Person:
#     def __init__(self, fullname, age, is_married):
#         self.fullname = fullname
#         self.age = age
#         self.is_married = is_married
#     def introduce_myself(self):
#       print(f"Имя - {self.fullname}, Возраст - {self.age}, Женат(а) - {self.is_married}")
# inptroduce = Person("Нурай", 15, "Нет")
# inptroduce.introduce_myself()
  # №3,8
# class Student(Person):
#     def __init__(self, fullname, age, is_married):
#             Person.__init__(self, fullname, age, is_married)
#             self.grades = {}
#     def half(self,lesson,scoure):
#         self.grades[lesson] = scoure

#     def total(self):
#         avarage = sum(self.grades.values()) // len(self.grades)
#         print(f" Средний балл: {avarage}")
       

# result = Student("Нурай", 15, "Нет")
# result.half("Алгебра",100)
# result.half("Русский язык",80)
# result.total()


# # №4,5,6,7
# class Teacher(Person):
#     def __init__(self, fullname, age, is_married,experience,salary):
#         Person.__init__(self, fullname, age, is_married)
#         self.experience = experience
#         self.salary = salary     

#     def sal(self):
#         for i in range(self.experience):
#             self.salary += 3000
#         print(f"{self.fullname}, Ваша зарплата: {self.salary}")
# result = Teacher("Нурай", 15, "Нет",3,30000)
# result.sal()
        



        


        
