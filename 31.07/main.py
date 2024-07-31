def first():
    my_dictionary = {
    "name" : "Sasha",
    "age" : 15,
    "class" : 9
    }
    k=input("Введіть ключ: ")
    for key in my_dictionary:
        if k in key:
            print('True')
    
# first()

def second():
    key_list=[]
    my_dictionary = {
    "name" : "Stas",
    "sport" : "soccer",
    "age" : '16',
    "number" : '10',
    "class" : '10'
    }
    v=input("Введіть значення: ")
    for key in my_dictionary:
        if my_dictionary[key] == v:
            key_list.append(key)
    print(key_list)
    
# second()
    
    
def third():
    my_dictionary = {
    "ім'я" : "-",
    "прізвище" : "Іванчук",
    "вік" : 15,
    "факультет" : "-"
    }
    
    name_value=input("Введіть ім'я: ")
    faculty_value=input("Введіть факультет: ")
    
    my_dictionary = {
    "ім'я" : name_value,
    "прізвище" : "Іванчук",
    "вік" : 15,
    "факультет" : faculty_value
    }
    
    for key, value in my_dictionary.items():
        print(f"{key}: {value}")
        
    new_value=input("Введіть середній бал: ")
    
    my_dictionary ["середній бал"] = new_value
    
    for key, value in my_dictionary.items():
        print(f"{key}: {value}")
        
# third()