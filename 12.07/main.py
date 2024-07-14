import random
# ================================№1============================
def  random_list():
    my_list=[]
    for i in range(10):
        my_list.append(random.randint(-50,100))
    print("Згенерований список: ", my_list)
    return(my_list)


def max_min():
    rand=random_list()
    rand.sort()
    max_num=rand[9]
    print("Максимальне число у списку: ", max_num)
    min_num=rand[0]
    print("Мінімальне число у списку: ",min_num)

# max_min()

# ==============================№2==============================
def random_word():
    game_list=['камінь', 'ножиці', 'папір']
    rand_word=random.choice(game_list)
    return rand_word

def word():
    my_word=input("Виберіть: камінь, ножиці чи папір ")
    return my_word.lower().strip()

def start():
    choise=input("Введіть 'comp', щоб почати гру з комп`ютера, 'player', щоб почати з себе: ")
    if choise.lower().strip() == 'player':
        game_player()
    if choise.lower().strip() == 'comp':
        game_comp()
    else:
        print("Ви ввели щось не те")
        
def game_player():
    my_word=word()
    rand_word=random_word()
    game_list=['камінь', 'ножиці', 'папір']
    if my_word == game_list[0] and rand_word == game_list[0] or my_word == game_list[1] and rand_word == game_list[1] or my_word == game_list[2] and rand_word == game_list[2]:
        print("Нічия")
        print("Ви обрали: ", my_word)
        print("Комп'ютер обрав: ", rand_word)
    if my_word == game_list[0] and rand_word == game_list[1] or my_word == game_list[1] and rand_word == game_list[2] or my_word == game_list[2] and rand_word == game_list[0]:
        print("Ви виграли!")
        print("Ви обрали: ", my_word)
        print("Комп'ютер обрав: ", rand_word)
    if my_word == game_list[1] and rand_word == game_list[0] or my_word == game_list[2] and rand_word == game_list[1] or my_word == game_list[0] and rand_word == game_list[2]:
        print("Виграв комп'ютер")
        print("Ви обрали: ", my_word)
        print("Комп'ютер обрав: ", rand_word)
    if my_word not in game_list:
        print("Ви ввели щось не те")

def game_comp():
    rand_word=random_word()
    print("Комп'ютер зробив свій вибір")
    my_word=word()

    game_list=['камінь', 'ножиці', 'папір']
    if my_word == game_list[0] and rand_word == game_list[0] or my_word == game_list[1] and rand_word == game_list[1] or my_word == game_list[2] and rand_word == game_list[2]:
        print("Нічия")  
        print("Комп'ютер обрав: ", rand_word)
        print("Ви обрали: ", my_word)
    if my_word == game_list[0] and rand_word == game_list[1] or my_word == game_list[1] and rand_word == game_list[2] or my_word == game_list[2] and rand_word == game_list[0]:
        print("Ви виграли!")
        print("Комп'ютер обрав: ", rand_word)
        print("Ви обрали: ", my_word)
    if my_word == game_list[1] and rand_word == game_list[0] or my_word == game_list[2] and rand_word == game_list[1] or my_word == game_list[0] and rand_word == game_list[2]:
        print("Виграв комп'ютер")
        print("Комп'ютер обрав: ", rand_word)
        print("Ви обрали: ", my_word)
    if my_word not in game_list:
        print("Ви ввели щось не те")

start()