# Декомпозиция - разделение кода по модулям 

# from calculator import add,sub  #точечный импорт

# print(add(2,2))
# print(sub(10,2))

# import calculator #Импорт модуля

# print(calculator.sub(10,5))
# print(calculator.add(10,5))


# from calculator import* #

# print(add(2,2))
# print(sub(10,2))
      

from abstract import Person
class People(Person):
    def __str__(self):
        return f"Имя: {self.name}"



people = People("Нурай",15)
print(people)

