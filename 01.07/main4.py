my_list = [0,0,1,4,4,-6,-2,-6,7]
minus = 0
index1 = 0
for index, i in enumerate(my_list):
    if i < 0:
        minus=i
        index1=index
print("Останній від'ємний елемент: ", minus, "Його індекс: ", index1)