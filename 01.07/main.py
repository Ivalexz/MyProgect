my_list = [1,2,3,4,5,6,-6,-5,-4,-3,-2,-1,132,456,0,0,1,4,4,-6,2,6,-7]
plus = 0
minus = 0
nul = 0
for i in my_list: 
    if i >0:
        plus+=1
    if i == 0:
        nul+=1
    if i <0:
        minus+=1
print('Кількість додатніх елементів: ', plus)
print('Кількість від`ємних елементів: ', minus)
print('Кількість нулів: ', nul)