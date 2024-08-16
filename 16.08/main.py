# =======================================task1==================================

students_list = [('Alice', 28), ('Bob', 87), ('Mark', 65), ('Diana', 93), ('Max', 28), ('Margo', 41)]
stud_dictionary = {}
rep_name=[]
for value, key in students_list:
    if key in stud_dictionary:
        rep_name.append(value)
        rep_name.append(stud_dictionary[key])
        stud_dictionary[key]=rep_name
    else:
       stud_dictionary[key] = value 
       
print(stud_dictionary)
        
# print(values, keys, repeat_grade)

# stud_dict=stud_dict.fromkeys(keys, 0)
# print(stud_dict)
# for i in len(values):
    
# for key, value in stud_dict.items():
#     print(key, '-', value)

# ===================================task2=============================
stud_dict = {
    'Alice': 28, 
    'Bob': 87, 
    'Mark': 65,
    'Diana': 93, 
    'Max': 32, 
    'Margo': 41
}
my_list=[]
def avarage_grades():
    sum = 0
    for val in stud_dict.values():
        my_list.append(val)
    for i in my_list:
        sum+=i
        av=sum/len(my_list)
    print(av)
# avarage_grades()

# ===================================task3=============================

# my_tuple = (97, 79, 46, 54, 13, 2)
# sum=0
# for i in my_tuple:
#     sum+=i
# print(sum/len(my_tuple))