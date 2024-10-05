from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self, name, model, power_level=0):
        self.name = name
        self.model = model
        self.power_level = power_level

    @abstractmethod
    def perform_task(self):
        pass

    def show_info(self):
        print(f"Name {self.name}, model {self.model}, power level {self.power_level}")

    def charge(self, charge):
        self.charge = charge
        if charge <= 100:
            print(f"Старий заряд: {self.power_level}")
            self.power_level += charge
            print(f"Новий заряд: {self.power_level}")
        else:
            print('Максимальна кількість збільлення - 100')


class WorkerRobot(Robot):
    def __init__(self, name, model, power_level, tool, my_file='WorkerRobot.txt'):
        super().__init__(name, model, power_level)
        self.tool = tool
        self.my_file=my_file

    def __enter__(self):
        self.my_file=open(self.my_file, 'w')
        return self.my_file

    def perform_task(self):
        if self.power_level >= 10:
            self.power_level -= 10
            print(f"Завдання виконується з інструментом {self.tool}. Заряд: {self.power_level}")
        else:
            print("У вас недостатньо заряду")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.my_file:
            self.my_file.close()
        if exc_type:
            print(f" Щось не те: {exc_type}")
            return True


class DefenseRobot(Robot):
    def __init__(self, name, model, power_level, weapon):
        super().__init__(name, model, power_level)
        self.weapon = weapon

    def perform_task(self):
        if self.power_level >= 15:
            self.power_level -= 15
            print(f"Захисне завдання виконується зі зброєю {self.weapon}. Заряд: {self.power_level}")
        else:
            print("У вас недостатньо заряду")
    def __del__(self):
        print("об'єкт очищено")


class ServiceRobot(Robot):
    def __init__(self, name, model, power_level, service_type):
        super().__init__(name, model, power_level)
        self.service_type = service_type

    def perform_task(self):
        if self.power_level >= 5:
            self.power_level -= 5
            print(f"Надається послуга: {self.service_type}. Заряд: {self.power_level}")
        else:
            print("У вас недостатньо заряду")
    def __del__(self):
        print("об'єкт очищено")


worker = WorkerRobot("Bob", "X1", 10, "wrench")
worker.charge(20)
worker.show_info()
worker.perform_task()

with worker as file1:
    file1.write(f"Name: {worker.name}, power level: {worker.power_level}")

print()
defence = DefenseRobot("Defender", "Z3", 20, "laser")
defence.charge(30)
defence.show_info()
defence.perform_task()
print()
service = ServiceRobot("Helper", "S2", 25, "cleaning")
service.charge(15)
service.show_info()
service.perform_task()