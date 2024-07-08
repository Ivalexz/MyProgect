def tabl():
    num = int(input("Введіть число: "))
    for i in range(11):
        print(num, "x", i, "=", num*i)
# tabl()

def length():
    a=0
    string=input('Введіть рядок: ')
    for i in string:
        a+=1
    print(a)
# length()

def change():
    a=''
    my_str=input('Введіть рядок: ')
    for i in my_str:
        if i in my_str.lower():
            a+=i.upper()
        if i in my_str.upper():
            a+=i.lower()
    print(a)
# change()

def middle():
    num1=int(input("Введіть число: "))
    num2=int(input("Введіть число: "))
    num3=int(input("Введіть число: "))
    print("Середнє значення: ", (num1+num2+num3)/3)

# middle()

def max():
    num1=int(input("Введіть перше число: "))
    num2=int(input("Введіть друге число: "))
    num3=int(input("Введіть третє число: "))
    if num1>num2 and num1>num3:
        print("Перше число є найбільшим", num1)
    if num2>num1 and num2>num3:
        print("Друге число є найбільшим", num2)
    if num3>num2 and num1<num3:
        print("Третє число є найбільшим", num3)
    if num1==num2 or num2==num3 or num3==num1:
        print("Серед чисел є однакові")

# max()