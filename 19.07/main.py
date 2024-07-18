def List():
    my_list=['asd', '1', 'qwe', 'iop','4.56', 'cvb', '938']
    el=input("Введіть елемент: ")
    if el.lower().strip() not in my_list:
        raise ValueError("такого елемента немає у списку")
    if el.lower().strip() in my_list:
        return el
    
# try:
#     List()

# except ValueError as mes:
#     print("Ви ввели щось не те, ", mes)

def Delete():
    my_list=['abd', '1', '3.14', 'rfg', '95', 'elm']
    print(my_list)
    el=input("Введіть елемент, який хочете забрати: ")
    new_el=el.lower().strip()
    
    if new_el not in my_list:
        raise ValueError("ви не можете видалити неіснуючий елемент")
    if new_el in my_list:
        my_list.remove(new_el)
        return my_list
        
# try:
#     Delete()

# except ValueError as e:
#     print("Ви ввели щось не те, ", e)

def pair():
    num=int(input("Введіть парне число: "))
    
    if num %2 != 0:
        raise ValueError("це число не є парним")
    if num %2 == 0:
        return num
        
# try:
#     pair()

# except ValueError as message:
#     print("Ви ввели щось не те, ", message)