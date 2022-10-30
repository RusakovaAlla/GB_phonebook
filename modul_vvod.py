def get_info():
    info = [[], []]
    last_name = input('Введите фамилию: ')
    while len(last_name) < 1:
        last_name = input('Это обязательное поле, пустым нельзя оставить. Введите фамилию: ')
    info[0].append(last_name)
    info[0].append(input('Введите имя: '))
    valid = False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info[1].append(phone_number)
    info[1].insert(0, input('Тип номера: '))
    info[0].append(input('Укажите пол: '))
    info[0].append(input('Укажите дату рождения: '))
    info[0].append(input('Введите описание: '))

    return info


#print(get_info())
