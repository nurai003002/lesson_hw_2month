class Person:
    def regist(self):
        print("begin")
    print("РЕГИСТРАЦИЯ")  
    print("Откройте cвой кабинет")
    name = input("Введите ваше Ф.И.: ")
    age = int(input("Ваш возраст: "))
                                                                                        
    def info(self):

        print("Регистрация прошла успешно!")
        print(f"здравствуйте {self.name}, пожалуйста запомните свой пин-код: {pincode}")
        print("Кабинет создан")
    
while True:
        pincode = input("Создайте пин-код: ")
        if len(pincode) != 4:
                print("пинкод должен содержать только 4 символа:")
        else:
            break 
result = Person()
result.regist()
result.info()

