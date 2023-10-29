# OOП  -> объектно-орентированное программирование
# DRY -> Don't repeat yourself

# class Car:
#     # атрибут класса
#     # model = "Mersedes" 
#     # wheels = 4

#     #   __init__ - конструктор
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
   
#     def info(self):
#      print(f"Модель машины = {self.model}, Год выпуска = { self.year}, Цвет машины = {self.color}")



# lexus = Car("es-350", 2023, "black")
# mersedes = Car("cls", 2020, "black")
# lexus.info()
# mersedes.info()
         

# class Cow:
#    def make_sound(self):
#       print("муууу!")

# cow = Cow()
# cow.make_sound()

# class Airplane:
#     def __init__(self, model, year, max_speed, capacity):
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed  
#         self.capacity =  capacity
#         self.is_flying = False
#         self.odometer = 0

#     def take_off(self):
#         self.is_flying = True
#         print("Самолет взлетел")

#     def fly(self, distance):
#         if self.is_flying:
#             self.odometer += distance
#             print(f"Наш самолет пролетел {distance}км")
#         else:
#             print(f"Сначало выполните взлет ")
    
#     def land(self):
#         self.is_flying = False
#         print(f"Наш самолет приземлился ")



#     def info_about_plane(self):
#         print(f"Модель самолета = {self.model} ")
#         print(f"Год выпуска = {self.year} ")
#         print(f"Скорость = {self.max_speed} ")
#         print(f"Вмещаемость = {self.capacity} ")
#         print(f"Пройденная дистанция = {self.odometer}км ")


# plane = Airplane("AH-4", 1982, 1200, 250)  
# plane.take_off()
# plane.fly(1000)
# plane.fly(2000) 
# plane.land()
# plane.info_about_car()


# booing = Aircar("747",2000, 2000, 2)
# booing.take_off()

# дз 
# № 1
# class Fruits:
#     def __init__ (self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight
#     def info(self):
#         print(f"Фрукт: {self.name}, Цвет: {self.color}, Вес: {self.weight}")
       
# apple = Fruits("Apple", "red", 4)
# cherry = Fruits("Cherry", "red", 5)
# banana = Fruits("Banana", "yellow", 1)
# apple.info()
# cherry.info()
# banana.info()
    
# # № 2

   
# class Car:
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.city = "Bishkek"
#     def info(self):
#         print(f"Машина - {self.model} едет в  -{self.city}")
# car = Car("Nissan Renault", 2018, "Dark-Blue")
# car.info()


# # доп.задание
# # № 1
# class Car:
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.city = "Bishkek"
#         self.fuel = 0
#         self.odometer = 0
#         self.is_driving = True
#         self.is_driving_leter = False
#         print(f"Машина - {self.model} едет в город {self.city}")

#     def car_start(self):
#         self.is_flying = True
#         print("Машина поехала")
    
 
#     def fuels(self, refuel):
#         if self.is_driving_leter:
#             self.fuel = refuel
#             print(f"Сначало пополните бак ")
#         elif refuel <= 0:
#             print("Наполните бак")
#         elif refuel > 40:
#             print("Можно только до 40 литров")
        
#         leter =  refuel * 10
#         print(f"Бак наполнен на {refuel} литров")
#         print(f"Дистанция {leter} км данная вам за ваш бензин ")

#     def driving(self, distance):
#         if distance >= 400:
#             print("Максимальная дистация 400 км")
#         elif self.is_driving:
#             self.odometer += distance
#             print(f"Вы прошли {distance}км")
#             gas = distance / 10
#         else:
#              print(f"Вы истратили {gas} литров бензина")
     
         
    
#     def land(self):
#         self.is_flying = False
#         print(f"Машина на месте ")


#     def info_about_car(self):
#         print(f"Модель  = {self.model} ")
#         print(f"Год выпуска = {self.year} ")
#         print(f"Цвет = {self.color} ")
#         print(f"Пройденная дистанция = {self.odometer}км ")


# car = Car("Nissan Renault", 2018, "Dark-Blue")  
# car.car_start()
# car.fuels(40)
# car.driving(38) 
# car.land()
# car.info_about_car()



# # основные концепции ооп
# class Car:   
#     def __init__(self, model, year, color):
#         self.model = model 
#         self.year = year 
#         self.color = color
#         self.fuel = 0
    
#     def refuel(self, re): 
#        self.re = re
#        if self.re == 40: 
#            print("Вы заправились")
#            self.fuel =+ 40
#        elif self.re != 40:
#            print("можно заправить только 40 литров")
           
#     def drive(self,city, distance):
#         self.city = city
#         self.distance = distance 
#         if self.distance == 400 and self.fuel == 40: 
#             print(f"Машина -{self.model} {self.year} года, {self.color} цвета едет в {self.city} c дистанцией {self.distance}км ") 
#         elif self.distance != 400:
#             print("На одной заправке можно проехать только 400 км")
                    
# Cart = Car("Nissan", 2020, "dark-blue") 
# Cart.refuel(40)
# Cart.drive("Bishkek", 400)