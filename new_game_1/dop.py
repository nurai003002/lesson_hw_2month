# from abstract import dough1
# dough1()
def sauce():
        print("ВИДЫ СОУСОВ")
        print("1 - кетчуп, 2 - сырный соус, 3 - соус Ранч, 4 - острый соус")
        sous = int(input("Выберите какой соус хотите: "))
        print(sous)
        if sous == 1:
            print(f"Тесто с кетчупом, готово")
        elif sous == 2:
            print(f"Тесто с сырный соусом, готово")
        elif sous == 3:
            print(f"Тесто с соус Ранч, готово")
        elif sous == 4:
            print(f"Тесто с острым соусом, готово")
        else:
            print("Ошибка, введите только данные числа")
        print(f"{sous}")
