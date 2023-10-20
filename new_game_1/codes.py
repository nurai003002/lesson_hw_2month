from dop import sauce
sauce()
def fillings():

    print("НАЧИНКИ")
    print("ЕСТЬ 5 ВИДОВ НАЧИКИ")
    fils_list = ("пеперони","гриб","оливка","сосиски","помидор")
    print(fils_list)
    fill_user = input("Выберите начинку: ")
    fill_1 = "пеперони"
    fill_2 = "гриб"
    fill_3 = "оливка"
    fill_4 = "сосиски"
    fill_5 = "помидор"
    if fill_user == 'пеперони':
        print(f"тесто с начинкой '{fill_1}' готово ")
    elif fill_user == 'гриб':
        print(f"тесто с '{fill_2}' готово ")
    elif fill_user == 'оливка':
        print(f"тесто с начинкой '{fill_3}' готово ")
    elif fill_user == 'сосиски':
        print(f"тесто с начинкой '{fill_4}' готово ")
    elif fill_user == 'помидор':
        print(f"тесто с начинкой '{fill_5}' готово ")

    



    
