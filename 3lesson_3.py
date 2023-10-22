# # Инкапсуляция
# class SmartPhone():
#     def __init__(self, sim_cards, battery):
#         self.__sim_cards = sim_cards
#         self.battery = battery
    
#     @property
#     def sim_cards(self):
#         return self.__sim_cards
#     @sim_cards.setter
#     def sim_cards(self, new_sim_cards):
#         self._sim_cards == new_sim_cards

#     def __info_smartphone(self):
#         print(f"Ваши сим карты {self.sim_cards}, Ваш объем батарии {self.battery}")
#     @property
#     def info_smartphone(self):
#         return self.__info_smartphone
# mi = SmartPhone(["Megacom", "O!"], 3000)
# print(mi.sim_cards)
# mi.info_smartphone()

# Множественное наследование
# class Car:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year

#     def info(self):
#         print(f"Бренд машины - {self.model}, год выпуска - {self.year}")

# class ElectricCar(Car):
#     def __init__(self, model, year, battery):
#         Car.__init__(self, model, year)
#         self.battery = battery

#     def drive(self):
#         print(f"{self.model}, едет на электричестве")
    

# class FuelCar(Car):
#     def __init__(self, model, year, fuel_bank):
#         Car.__init__(self, model, year)
#         self.fuel_bank = fuel_bank

#     def drive(self):
#         print(f"{self.model}, едет на Топливо!")

# class HybridCar(ElectricCar, FuelCar):
#     def __init__(self, model, year,  fuel_bank, battery,):
#         FuelCar.__init__(self, model, year, fuel_bank)
#         ElectricCar.__init__(self, model, year, battery)

#     def drive(self):
#         print(f"{self.model}, едет на Топливо! и на электричечтве")

# tesla = ElectricCar("Tesla Model X", 2022, 150000)
# tesla.info()
# tesla.drive()

# audi = FuelCar("Rs-8", 2018, 15)
# audi.info()
# audi.drive()

# toyota = HybridCar("Avalon", 2023, 100000, 10)
# toyota.info()
# toyota.drive()


# дз 
# №1,2,3,

# class Computer:
#     def __init__(self, cpu, memory, make_coputations):
#         self.__cpu = cpu
#         self.__memory = memory
#         self.__make_coputations = make_coputations
#     @property
#     def cpu(self):
#         return self.__cpu
#     @property
#     def memory(self):
#         return self.__memory
#     @property
#     def make_coputations(self):
#         print(f"сложение: {self.cpu + self.memory}, Деление : {self.cpu / self.memory}")
#         print(f" Умножение: {self.cpu * self.memory}, Разность: {self.cpu-self.memory}")
#         return self.__make_coputations
# result = Computer(35,5,"Результат")
# result.make_coputations

# # №4,5,6,10
# class Phone:
#     def __init__(self,sim_cards_list):
#         self.__sim_cards_list = sim_cards_list
#     @property
#     def sim_cards_list(self):
#         return self.__sim_cards_list
    
#     @sim_cards_list.setter
#     def sim_cards_list(self, sim_list):
#         self.sim_cards_list == sim_list

#     def call(self, sim_card_number, call_to_number):
#         self.sim_card_number = sim_card_number
#         self.call_to_number = call_to_number
#     def info(self):
#         if self.sim_card_number == 1:
#            print(f"Идет звонок на номер {self.call_to_number} c сим-карты - {self.sim_card_number} - Beeline")
#         elif self.sim_card_number == 2:
#             print(f"Идет звонок на номер {self.call_to_number} c сим-карты - {self.sim_card_number} - Megacom")
# booth = Phone(sim_cards_list=["Beeline", "Megacom"])
# booth.call(1, +996755750238)
# booth.info()

# # # №7,8,9,11
# class SmartPhone(Computer,Phone):
#     def __init__(self, location,cpu, memory, make_coputations,sim_cards_list):
#         Computer.__init__(self, cpu, memory, make_coputations)
#         Phone.__init__(self,sim_cards_list)
#         self.location = location
#         print(f"Маршрут постороен, от Резиденция до {self.location} займет 10 мин")

#     def add_memeory_card(self, memories):
#         self.memories = memories
#     def info_smart(self):
#         print(f"Память на вашем телефоне {self.memories}ГБ")
# local = SmartPhone("Globus",35,5,"Результат",sim_cards_list=["Beeline", "Megacom"])
# local.add_memeory_card(64)
# local.info_smart()


