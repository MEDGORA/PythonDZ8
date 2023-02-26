import json
import os

idContact = 0
nameOfLoadListContacts = None
nameOfNewListContacts = None
name = None
numbers = None
city = None
birthDay = None
lenListOfAttributs = 4
lastNameOfListContacts = None
BD = {}

def load(fname):
            global BD
            global idContact
            global lastNameOfListContacts
            with open(fname, 'r', encoding='utf-8') as fh:  
                BD = BD_local = json.load(fh)  
            os.system('CLS')
            print('Контакты успешно загружены, чтобы продолжить нажите клавишу Enter')
            input()
            os.system('CLS')
            lastNameOfListContacts = fname
            idContact = int(max(list(BD.keys())))
            MainMenu()
            return BD_local



def save(fname):
            with open(fname, 'w', encoding='utf-8') as fh:  
                fh.write(json.dumps(BD,
                                    ensure_ascii=False)) 
            os.system('CLS')
            print('Контакт успешно сохранен, чтобы продолжить нажите клавишу Enter')
            input()
            os.system('CLS')
            MainMenu()



def AddContact():
    os.system('CLS')
    global lenListOfAttributs
    global idContact
    global name
    global numbers
    global city
    global birthDay
    global BD
    global nameOfNewListContacts
    changeCount = False
    for i in range(lenListOfAttributs) :
        if i == 0 :
            count2 = 'имя'
            if name != None :
                print('Имя: ',name)
                count1 = 'изменить'
                changeCount = True
            else :
                count1 = 'добавить'
        elif i == 1 :
            count2 = 'номер'
            if numbers != None :
                print('Номера: ',numbers)
                count1 = 'изменить'
                changeCount = True
            else :
                count1 = 'добавить'
        elif i == 2 :
            count2 = 'город'
            if city != None :
                print('Город: ',city)
                count1 = 'изменить'
                changeCount = True
            else :
                count1 = 'добавить'
        elif i == 3 :
            count2 = 'день рождения'
            if birthDay != None :
                print('День рождения: ',birthDay)
                count1 = 'изменить'
                changeCount = True
            else :
                count1 = 'добавить'
        print(i + 1,'-',count1,count2,'контакта')
    if numbers != None :
        print('5 - добавить ещё один номер контакта')
    if changeCount == True :
        print('6 - сохранить контакт')
    print('0 - в главное меню')

    BD[idContact] = name, numbers, city, birthDay

    menuOption = int(input('Введите команду:'))
    if menuOption == 0 :
        idContact -= 1
        os.system('CLS')
        MainMenu()
    if menuOption == 1 :
        os.system('CLS')
        name = input('Введите имя контакта: ')
        AddContact()
    if menuOption == 2 :
        os.system('CLS')
        if numbers == None or len(numbers) == 1 :
            numbers = []
            numbers.append(input('Введите номер контакта: '))
            AddContact()
        else :
            count = []
            for i in range(len(numbers)) :
                print(i + 1,'-',numbers[i])
                count.append(i)
            menuOption = int(input('Выберите номер, который нужно изменить: '))
            if menuOption in count :
                for i in range(len(numbers)) :
                    if menuOption == i + 1 :
                        numbers[i] = input('Введите новый номер: ')
            else :
                while menuOption not in count:
                    menuOption = int(input('Выберите номер, который нужно изменить: '))    
    if menuOption == 3 :
        os.system('CLS')
        city = input('Введите город контакта: ')
        AddContact()
    if menuOption == 4 :
        os.system('CLS')
        birthDay = input('Введите день рождения контакта: ')
        AddContact()
    if numbers != None and menuOption == 5 :
        os.system('CLS')
        numbers.append(input('Введите ещё один номер контакта: '))
        AddContact()
    if changeCount == True and menuOption == 6 :
        if name != None and numbers!= None:
            save(nameOfNewListContacts)
            MainMenu()
        elif name == None and numbers != None:
            count3 = 'имя'
        elif name != None and numbers == None:
            count3 = 'номер'
        elif name == None and numbers == None :
            count3 = 'имя и номер'
        os.system('CLS')
        print('Вы не указали',count3,'контакта. Вы уверены, что хотите сохранить контакт?')
        print('1 - всё-равно сохранить контакт')
        print('0 - отмена')
        answer = int(input('Введите комманду: '))
        if answer == 1 :
            save(nameOfNewListContacts)
        if answer == 0 :
            AddContact()
        else :
            os.system('CLS')
            print('Вы не указали',count3,'контакта. Вы уверены, что хотите сохранить контакт?')
            print('1 - всё-равно сохранить контакт')
            print('0 - отмена')
            answer = int(input('Введите комманду: '))
    else:
        AddContact()



def MainMenu() :
    global BD
    global lastNameOfListContacts
    global idContact
    global name
    global numbers
    global city
    global birthDay
    print('Выберите пункт меню:')
    print('1 - добавить контакт')
    print('2 - изменить контакт')
    print('3 - удалить контакт')
    print('4 - поиск контакта')
    if idContact != 0 :
        print('5 - просмотр всех контактов')
    print('0 - назад')
    menuOption = int(input('Введите команду:'))
    if menuOption == 1 :
        idContact += 1
        name = None
        numbers = None
        city = None
        birthDay = None
        AddContact()
    elif menuOption == 2 :
        ChangeContact()
    elif menuOption == 3 :
        DeleteContact()
    elif menuOption == 4 :
        FindContact()
    elif idContact != 0 and menuOption == 5 :
        with open(lastNameOfListContacts, 'r', encoding='utf-8') as fh: 
            BD = BD_local = json.load(fh)  
        os.system('CLS')
        listOfKeys = list(BD.keys())
        list2 =[]
        for i in range(len(BD.keys())) :
            key = str(listOfKeys[i])
            list1 = list(BD.get(key))
            if len(list1) > 4 :
                for i in (1, -2):
                    list2.append(list1[i])
            else :
                list2 = list1[1]
            print(i + 1,'- Имя:',list1[0],', Номера:',list2,', Город:',list1[-2],', День рождения:',list1[-1])
        print('Чтобы вернуться в меню нажите клавишу Enter')
        input()
        os.system('CLS')
        MainMenu()
    elif menuOption == 0 :
        LoadMenu()
    else :
        MainMenu()



def FindContact():
    global BD
    os.system('CLS')
    print('1 - Поиск по имени')
    print('2 - Поиск по номеру')
    print('3 - Поиск по городу')
    print('4 - Поиск по дате рождения')
    print('0 - назад')
    menuOption = int(input('Выберите действие: '))
    if menuOption == 1 :
        count = 0
        os.system('CLS')
        name = input('Введите имя: ')
        listOfKeys = list(BD.keys())
        contactFind = False
        for i in range(len(BD.keys())) :
            key = str(listOfKeys[i])
            list1 = list(BD.get(key))
            if name in list1 :
                print(BD.get(key))
                count += 1
                contactFind = True
        if contactFind == True and count == 1:
            print('Контакт найден, чтобы вернуться в меню нажите клавишу Enter')
        elif contactFind == True and count > 1:
            print('Контакты найдены, чтобы вернуться в меню нажите клавишу Enter')
        else :
            print('Такого контакта нет, чтобы вернуться в меню нажите клавишу Enter')
        input()
        os.system('CLS')
        MainMenu()
    if menuOption == 2 :
        os.system('CLS')
        count = 0
        numbers = input('Введите номер: ')
        listOfKeys = list(BD.keys())
        contactFind = False
        for i in range(len(BD.keys())) :
            key = str(listOfKeys[i])
            list1 = list(BD.get(key))
            list2 = []
            for j in list1 :
                try:
                    list2.extend(j)
                except TypeError:
                    pass
            if numbers in list2 :
                print(BD.get(key))
                count += 1
                contactFind = True
        if contactFind == True and count == 1:
            print('Контакт найден, чтобы вернуться в меню нажите клавишу Enter')
        elif contactFind == True and count > 1:
            print('Контакты найдены, чтобы вернуться в меню нажите клавишу Enter')
        else :
            print('Такого контакта нет, чтобы вернуться в меню нажите клавишу Enter')
        input()
        os.system('CLS')
        MainMenu()
    if menuOption == 3 :
        count = 0
        os.system('CLS')
        city = input('Введите город: ')
        listOfKeys = list(BD.keys())
        contactFind = False
        for i in range(len(BD.keys())) :
            key = str(listOfKeys[i])
            list1 = list(BD.get(key))
            if city in list1 :
                print(BD.get(key))
                count += 1
                contactFind = True
        if contactFind == True and count == 1:
            print('Контакт найден, чтобы вернуться в меню нажите клавишу Enter')
        elif contactFind == True and count > 1:
            print('Контакты найдены, чтобы вернуться в меню нажите клавишу Enter')
        else :
            print('Такого контакта нет, чтобы вернуться в меню нажите клавишу Enter')
        input()
        os.system('CLS')
        MainMenu()
    if menuOption == 4 :
        count = 0
        os.system('CLS')
        birthDay = input('Введите день рождения: ')
        listOfKeys = list(BD.keys())
        contactFind = False
        for i in range(len(BD.keys())) :
            key = str(listOfKeys[i])
            list1 = list(BD.get(key))
            if birthDay in list1 :
                print(BD.get(key))
                count += 1
                contactFind = True
        if contactFind == True and count == 1:
            print('Контакт найден, чтобы вернуться в меню нажите клавишу Enter')
        elif contactFind == True and count > 1:
            print('Контакты найдены, чтобы вернуться в меню нажите клавишу Enter')
        else :
            print('Такого контакта нет, чтобы вернуться в меню нажите клавишу Enter')
        input()
        os.system('CLS')
        MainMenu()
    elif menuOption == 0 :
        os.system('CLS')
        MainMenu()
    else :
        FindContact()




def DeleteContact() :
    global idContact
    global name
    global numbers
    global city
    global birthDay
    os.system('CLS')
    count = []
    listOfKeys = list(BD.keys())
    for i in range(len(BD.keys())) :
        key = str(listOfKeys[i])
        print(i + 1,'-',BD.get(key))
        count.append(i)
    menuOption = int(input('Выберите контакт, который нужно удалить: '))
    if menuOption - 1 in count :
        for i in range(len(BD.keys())) :
            if menuOption == i + 1 :
                idContact = listOfKeys[i]
                list1 = list(BD.get(listOfKeys[i]))
                name = list1[0]
                if len(list1) > 4 :
                    for i in (1, -2):
                        numbers.append(list1[i])
                else :
                    numbers = list1[1]
                city = list1[-2]
                birthDay = list1[-1]
                os.system('CLS')
                print(BD.get(listOfKeys[i]))
                print('Вы уверены что хотите удалить данный контакт?')
                print('1 - да')
                print('0 - отмена')
                menuOption = int(input('Выберите действие: '))
                if menuOption == 0 :
                    os.system('CLS')
                    MainMenu()
                if menuOption == 1 :
                    BD.pop(idContact)
                    save(lastNameOfListContacts)
                else :
                   while  menuOption != 0 and menuOption != 1 :
                       menuOption = int(input('Выберите действие: '))
    else :
        while menuOption - 1 not in count:
            menuOption = int(input('Выберите контакт, который нужно удалить: '))



def ChangeContact():
    global idContact
    global name
    global numbers
    global city
    global birthDay
    os.system('CLS')
    count = []
    listOfKeys = list(BD.keys())
    for i in range(len(BD.keys())) :
        key = str(listOfKeys[i])
        print(i + 1,'-',BD.get(key))
        count.append(i)
    menuOption = int(input('Выберите контакт, который нужно изменить: '))
    if menuOption - 1 in count :
        for i in range(len(BD.keys())) :
            if menuOption == i + 1 :
                idContact = listOfKeys[i]
                list1 = list(BD.get(listOfKeys[i]))
                name = list1[0]
                if len(list1) > 4 :
                    for i in (1, -2):
                        numbers.append(list1[i])
                else :
                    numbers = list1[1]
                city = list1[-2]
                birthDay = list1[-1]
                ChangeContactMenu()
    else :
        while menuOption - 1 not in count:
            menuOption = int(input('Выберите контакт, который нужно изменить: '))



def ChangeContactMenu():
    os.system('CLS')
    global lenListOfAttributs
    global idContact
    global name
    global numbers
    global city
    global birthDay
    global BD
    global nameOfNewListContacts
    changeCount = False
    for i in range(lenListOfAttributs) :
        if i == 0 :
            count2 = 'имя'
            if name != None :
                print('Имя: ',name)
                count1 = 'изменить'
                changeCount = True
            else :
                count1 = 'добавить'
        elif i == 1 :
            count2 = 'номер'
            if numbers != None :
                print('Номера: ',numbers)
                count1 = 'изменить'
                changeCount = True
            else :
                count1 = 'добавить'
        elif i == 2 :
            count2 = 'город'
            if city != None :
                print('Город: ',city)
                count1 = 'изменить'
                changeCount = True
            else :
                count1 = 'добавить'
        elif i == 3 :
            count2 = 'день рождения'
            if birthDay != None :
                print('День рождения: ',birthDay)
                count1 = 'изменить'
                changeCount = True
            else :
                count1 = 'добавить'
        print(i + 1,'-',count1,count2,'контакта')
    if numbers != None :
        print('5 - добавить ещё один номер контакта')
    if changeCount == True :
        print('6 - сохранить контакт')
    print('0 - назад')

    BD[idContact] = name, numbers, city, birthDay

    menuOption = int(input('Введите команду:'))
    if menuOption == 0 :
        os.system('CLS')
        name = None
        numbers = None
        city = None
        birthDay = None
        LoadMenu()
    if menuOption == 1 :
        os.system('CLS')
        name = input('Введите имя контакта: ')
        ChangeContactMenu()
    if menuOption == 2 :
        os.system('CLS')
        if numbers == None or len(numbers) == 1 :
            numbers = []
            numbers.append(input('Введите номер контакта: '))
            ChangeContactMenu()
        else :
            count = []
            for i in range(len(numbers)) :
                print(i + 1,'-',numbers[i])
                count.append(i)
            menuOption = int(input('Выберите номер, который нужно изменить: '))
            if menuOption in count :
                for i in range(len(numbers)) :
                    if menuOption == i + 1 :
                        numbers[i] = input('Введите новый номер: ')
            else :
                while menuOption not in count:
                    menuOption = int(input('Выберите номер, который нужно изменить: '))    
    if menuOption == 3 :
        os.system('CLS')
        city = input('Введите город контакта: ')
        ChangeContactMenu()
    if menuOption == 4 :
        os.system('CLS')
        birthDay = input('Введите день рождения контакта: ')
        ChangeContactMenu()
    if numbers != None and menuOption == 5 :
        os.system('CLS')
        numbers.append(input('Введите ещё один номер контакта: '))
        ChangeContactMenu()
    if changeCount == True and menuOption == 6 :
        if name != None and numbers!= None:
            save(nameOfNewListContacts)
            MainMenu()
        elif name == None and numbers != None:
            count3 = 'имя'
        elif name != None and numbers == None:
            count3 = 'номер'
        elif name == None and numbers == None :
            count3 = 'имя и номер'
        os.system('CLS')
        print('Вы не указали',count3,'контакта. Вы уверены, что хотите сохранить контакт?')
        print('1 - всё-равно сохранить контакт')
        print('0 - отмена')
        answer = int(input('Введите комманду: '))
        if answer == 1 :
            save(nameOfNewListContacts)
        if answer == 0 :
            ChangeContactMenu()
        else :
            os.system('CLS')
            print('Вы не указали',count3,'контакта. Вы уверены, что хотите сохранить контакт?')
            print('1 - всё-равно сохранить контакт')
            print('0 - отмена')
            answer = int(input('Введите комманду: '))
    else:
        ChangeContactMenu()
        


def LoadMenu() :
    global nameOfLoadListContacts
    global nameOfNewListContacts
    global lastNameOfListContacts
    os.system('CLS')
    print('1 - загрузить список контактов')
    print('2 - создать новый список контактов')
    if lastNameOfListContacts != None :
        print('3 - Продолжить работу списком контактов с названием:',lastNameOfListContacts)
    print('0 - выход')
    menuOption = int(input('Введите комманду: '))
    if menuOption == 1 :
        os.system('CLS')
        nameOfLoadListContacts = input('Введите название списка контактов: ')
        nameOfLoadListContacts = nameOfLoadListContacts + '.json'
        nameOfNewListContacts = nameOfLoadListContacts
        os.system('CLS')
        load(nameOfLoadListContacts)
    elif menuOption == 2 :
        os.system('CLS')
        nameOfNewListContacts = input('Введите название нового списка контактов: ')
        nameOfNewListContacts = nameOfNewListContacts + '.json'
        os.system('CLS')
        MainMenu()
    elif lastNameOfListContacts != None and menuOption == 3 :
        os.system('CLS')
        load(lastNameOfListContacts)
    elif menuOption == 0:
        os.system('CLS')
        print('До свидания')
        exit()
    else :
        LoadMenu()




LoadMenu()