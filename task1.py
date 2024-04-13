########################################################### ЗАДАЧА 1 

# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
#     1. Программа должна выводить данные
#     2. Программа должна сохранять данные в текстовом файле 
#     3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека) 
#     4. Использование функций. Ваша программа не должна быть линейной


def main():
    number = 1
    while number != 0:
        print("Выберите действие:\n 1. Найти контакт\n 2. Добавить контакт\n 3. Открыть телефонную книгу\n 4. Копирование контакта\n 0. Выход")
        number = int(input('>>> '))
        if number == 1:
            findContact()
        elif number == 2:
            addContact()
        elif number == 3:
            showPhoneBook()
        elif number == 4:
            copyContact()
        elif number == 0:
            break
        input("Нажмите Enter чтобы продолжить ")
            

def showPhoneBook():
    titles = ["ФАМИЛИЯ", "ИМЯ", "ОТЧЕСТВО", "ТЕЛЕФОН"]
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print(' '.join(titles))
        print()
        for line in file:
            print(''.join(line.split(';')))
            
def findContact():
    titles = ["№ ", "ФАМИЛИЯ", "ИМЯ", "ОТЧЕСТВО", "ТЕЛЕФОН"]
    searchParameter = input("Введите параметр поиска: ")
    listOfFoundContacts = []
    numberOfFoundContact = -1
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print()
        print(' '.join(titles))
        print()
        for line in file:
            line = line.split()
            for i in range(len(line)):
                for j in line[i]:
                    if j == ';':
                        line[i] = line[i].replace(';', '')
            if searchParameter in line:
                numberOfFoundContact += 1
                listOfFoundContacts.append(line)
                print(F"{numberOfFoundContact}. {' '.join(line)}")
                print('\n')
    return (listOfFoundContacts)

def addContact():
    lastName = input("Введите фамилию: ")
    firstName = input("Введите имя: ")
    middleName = input("Введите отчество: ")
    phone = input("Введите телефон: ")
    contact = {'last_name': lastName,
               'first_name': firstName,
               'middle_name': middleName,
               'phone': phone}
    
    
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        for value in contact.values():
            file.write(value)
            file.write('; ')
        file.write('\n')

def copyContact():
    listOfFoundContacts = findContact()
    numberedContactList = []
    
    if len(listOfFoundContacts) == 1:
        with open('copied_contact.txt', 'w', encoding='utf-8') as file:
            contactForWrite = '; '.join(listOfFoundContacts[0])
            file.write(contactForWrite)
        print("Контакт скопирован в новый файл")
    elif len(listOfFoundContacts) > 1:
        for i in enumerate(listOfFoundContacts):
            numberedContactList.append(i)
        numberContactForRecording = int(input("Укажите номер контакта для записи: "))
        with open('copied_contact.txt', 'w', encoding='utf-8') as file:
            for number, value in numberedContactList:
                if numberContactForRecording == number:
                    file.write('; '.join(value))
        print("Контакт скопирован в новый файл")

main()