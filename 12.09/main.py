class Math:
    @staticmethod
    def plus(number1,number2):
        print(f'Сума введених чисел: {number1+number2}')
        
    def minus(number1,number2):
        print(f'Різниця введених чисел: {number1-number2}')
        
    def multiplication(number1,number2):
        print(f'Добуток введених чисел: {number1*number2}')
        
    def division(number1,number2):
        if number2!=0:
            print(f'Частка введених чисел: {number1/number2}')
        else:
            print("Ділити на нуль неможливо")
        
number1=int(input("Введіть перше число: "))
number2=int(input("Введіть друге число: "))
operation=input("Введіть операцію: */+-")
if operation=='+':
    Math.plus(number1,number2)
elif operation=='-':
    Math.minus(number1,number2)
elif operation=='*':
    Math.multiplication(number1,number2)
elif operation=='/':
    Math.division(number1,number2)
else:
    print("Ви ввели щось не те")