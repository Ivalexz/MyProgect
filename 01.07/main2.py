my_list = [1,2,3,4,5,6,-6,-5,-4,-3,-2,-1,132,456,0,0,1,4,4,-6,2,6,-7]
for index, i in enumerate(my_list):
    if i < 0:
        print("Перший від'ємний елемент: ", i, "Його індекс: ", index)
        break
