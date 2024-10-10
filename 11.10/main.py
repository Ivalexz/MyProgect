class Fibonacci:
    def __init__(self, n):
        self.n=n
        self.my_list=[]

    def generate(self):
        num=1
        num2=0
        num1_old=0
        self.my_list.append(0)
        for i in range(self.n):
            num1_old=num
            num = num2
            num2+=num1_old
            self.my_list.append(num2)

    def showNumbers(self):
        print(self.my_list)

num=Fibonacci(15)
num.generate()
num.showNumbers()