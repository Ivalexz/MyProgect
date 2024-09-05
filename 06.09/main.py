# =======================task1=====================
# class Person:
#     def __init__(self, name, surmane, age):
#         self.name=name
#         self.surname=surname
#         self.age=age
        
#     def showInfo(self):
#         print(f"name = {self.name}, surname = {self.surname}, age = {self.age}")

# try:       
#     name=input("Введіть ім'я: ")
#     surname=input("Введіть прізвище: ")
#     age=int(input("Введіть вік: "))
#     obj1= Person(name, surname, age)
#     obj1.showInfo()
# except ValueError:
#     print("Ви ввели щесь не те. Спробуйте ще раз")

# ============================task2==========================
class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
        
    def rectangleArea(self):
        area=self.width*self.height
        print(f"Площа прямокутника: {area}")
        
    def rectanglePerimetry(self):
        perimetry=self.width+self.height
        print(f"Периметр прямокутника: {perimetry}")
        
    def showInf(self):
        print(f"Ширина = {self.width}, висота = {self.height}")

try:   
    width=int(input("Введіть ширину прямокутника: "))
    height=int(input("Введіть висоту прямокутника: "))

    rect1=Rectangle(width, height)
    rect1.rectangleArea()
    rect1.rectanglePerimetry()
    rect1.showInf()
     
except ValueError:
    print("Ви ввели щесь не те. Спробуйте ще раз")