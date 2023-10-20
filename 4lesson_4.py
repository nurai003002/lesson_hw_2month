# # Магические методы - dunder методы 
# #начинаются "__  __" - двумя нижнеми подчеркиваниями
# class Car:
#     def __init__(self, model, year, wheels):
#         self.model = model
#         self.year = year
#         self.wheels = wheels
#     def info(self):
#         print(f"Марка машины {self.model}, год выпуска {self.year}, колесо- {self.wheels}")

#     def __str__(self): # __str__ == print
#        return f"Марка машины {self.model}, год выпуска {self.year}, колесо-{self.wheels} - магический метод, "
    

#     # магические действия для арифметических действий

#     def __add__(self, other): #__add__ == сложение ("+")
#        new_year =  self.year + other.year
#        return Car(self.model, new_year, self.wheels)
    
#     def __sub__(self, other): #__sub__ == вычитание ("-")
#        new_wheels =  self.wheels - other.wheels
#        return Car(self.model, self.year ,new_wheels)

#     def __mul__(self, other): #__mil__ == Умножение ("*")
#        new_wheels =  self.wheels * other.wheels
#        return Car(self.model, self.year ,new_wheels)
    
#     def __floordiv__(self, other): #__floordiv__ == деление ("//")
#        new_wheels =  self.wheels // other.wheels
#        return Car(self.model, self.year ,new_wheels)
    
#     def __bool__(self, other): #__floordiv__ == деление ("//")
#        new_wheels =  self.wheels // other.wheels
#        return Car(self.model, self.year ,new_wheels)
    
#      # Магические методы для операторов сравнения

#     def __gt__(self, other):
#        return self.year > other.year
#     def __lt__(self, other):
#        return self.year < other.year
       
#     def __eq__(self,other):
   #     return self.year == other.year
    
   #  def __ne__(self,other):
   #     return self.year != other.year
   #  def __ge__(self,other):
   #     return self.year >= other.year
   #  def __le__(self,other):
   #     return self.year <= other.year

# car1 = Car("BMW - f90", 2021, 4)
# car2 = Car("BMW - f6", 2023, 4) 

# # Арифметические действия 
# print(car1+car2)
# print(car1-car2)
# print(car1*car2)
# print(car1//car2)
#  # car.info() #Если вызвать без магического метода выйдет путь


# # операторы сравнения
# print(car1>car2) # Больше чем ">"
# print(car1<car2) # Меньше чем "<"
# print(car1==car2) # Равно "=="
# print(car1!=car2) # Неравняется "!="
# print(car1>=car2) # Больше или равно ">"
# print(car1<=car2) # Меньше или равно ">"

# class ElectricCar(Car):
#     def __init__(self, model, year,wheels , battery):
#         Car.__init__(self, model, year, wheels)
#         self.battery = battery

#     def __str__(self):
#         return super().__str__() + f"Заряд батареи {self.battery}"

# electriccar = ElectricCar("Avalon", 2020, 4, 1000)
# print(electriccar)




# # дз
# class Computer:
#    def __init__(self, cpu, memory):
#       self.cpu = cpu
#       self.memory = memory
#    def __add__(self, other_num):
#       result = self.memory + other_num.memory
#       return f"Резултат сложения: {result}"
    
#    def __sub__(self, other_num):
#       result1 = self.memory - other_num.memory
#       return f"Резултат вычитания: {result1}"
   
#    def __floordiv__(self, other_num):
#       result2 = self.memory // other_num.memory
#       return f"Резултат деления: {result2}"
   
#    def __mul__(self, other_num):
#       result3 = self.memory * other_num.memory
#       return f"Резултат умножения: {result3}"

# computer = Computer("Кпу", 34)
# computers = Computer("Кпa", 2)
# print(computer + computers)
# print(computer - computers)
# print(computer // computers)
# print(computer * computers)


# class Phone:
#    def __init__(self,sim_cards_list):
#       self.sim_cards_list = sim_cards_list 

#    def __call__(self,sim_card_number,call_to_number):
#       self.sim_card_number = sim_card_number
#       self.call_to_number = call_to_number

#    def __str__(self):
#         if self.sim_card_number == 1:
#            return f"Идет звонок на номер {self.call_to_number} c сим-карты - {self.sim_card_number} - Beeline"
         
#         elif self.sim_card_number == 2:
#             return f"Идет звонок на номер {self.call_to_number} c сим-карты - {self.sim_card_number} - Megacom"

# booth = Phone(["Beeline", "Megacom"])
# booth(2, +996771244745)
# print(booth)

# class SmartPhone(Computer, Phone):
#    def __init__(self,use_gps , location,cpu, memory,sim_cards_list):
#       Computer.__init__(self,cpu, memory)
#       Phone.__init__(self,sim_cards_list)
#       self.use_gps = use_gps
#       self.location = location
#       print(f"Маршрут постороен, от {self.use_gps} до {self.location} займет 10 мин")
   
#    def add_memeory_card(self, memories):
#         self.memories = memories
#    def __call__(self):
#         print(f"Память на вашем телефоне {self.memories}ГБ")
# result = SmartPhone("Резиденция", "Globus","Кпу", 35,["Beeline", "Megacom"] )
# result.add_memeory_card(38)
# result()





 






      





