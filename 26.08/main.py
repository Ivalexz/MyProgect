import os.path
name='tasks.txt'

while True:
    print('Виберіть команду:')
    users_input=int(input('1 - додати завдання, 2 - вивести поточний список завдань, 3 - видалити файл, 4 - завершити '))

    if users_input == 1:
        with open(name, "a") as file1:
            list_input=input(('Введіть нове завдання: '))
            file1.write(list_input)
            file1.write(' ')

  
    if users_input == 2:
        try:
            with open(name, "r") as file1:
                print(file1.read())
    
        except FileNotFoundError:
            with open(name, "a") as file1:
                print("Файл порожній")


    if users_input == 3:
        try:
            os.remove(name)
            print("Файл видалено")
    
        except FileNotFoundError:
                print("Неможливо видалити неіснуючий файл")
        
    if users_input == 4:
        break