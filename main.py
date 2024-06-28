import random
import string
password = ''
want = ''
yes = 0
while want != "-" and yes!=4:
    want = input("Хочете добавити ще один клас символів? + ТАК - НІ ")
    if want == '-':
        break
    l = int(input("Введіть довжину рядка з цим класом: "))
    if want == '+':
        yes+=1

    for i in range(1):
        symbol_class = input("Введіть клас символів з якого хочете згенерувати пароль. Великі букви - Upp, малі букви - Low, спецсимволи - Punct, цифри - Dig: ")
        if symbol_class.lower() == 'upp':
            for i in range(l):
                b = string.ascii_uppercase
                password += random.choice(b)
        if symbol_class.lower() == 'low':
            for i in range(l):
                b = string.ascii_lowercase
                password += random.choice(b)
        if symbol_class.lower() == 'punct':
            for i in range(l):
                b = string.punctuation
                password += random.choice(b)
        if symbol_class.lower() == 'dig':
            for i in range(l):
                b = string.digits
                password += random.choice(b)
        if symbol_class.lower() != 'punct' and symbol_class.lower() != 'dig' and symbol_class.lower() != 'low' and symbol_class.lower() != 'upp':
            print("Ви ввели щось не те")
print(password)