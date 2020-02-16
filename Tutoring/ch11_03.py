class Person:
    def __init__(self,name):
        self.name = name

class Employee(Person):
    def __init__(self,name,number):
        super().__init__(name)
        self.number = number
    def __str__(self):
        return self.name + ": " + self.number
class Boss(Person):
    def __init__(self,name,title):
        super().__init__(name)
        self.title = title

empolyee1=Employee("A","12345")
empolyee2=Employee("B","5678")
boss = Boss("C","CEO")
print(empolyee1.name)
print(empolyee1)
print(empolyee2.name)
print(boss.name)