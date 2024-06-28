import random
sproba = 0
num = random.randint(0,101)
while True:
    user_num = int(input("Вгадайте число: "))
    if user_num < num:
        print("загадкове число більше")
        sproba +=1
    if user_num > num:
        print("загадкове число менше")
        sproba +=1
    if user_num == num:
        print("Ви вгадали!")
        sproba +=1
        print(sproba)