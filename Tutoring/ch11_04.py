class Manager:
    def __init__(self,name,salary,bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def getSalary(self):
        return self.salary + self.bonus

    def __repr__(self):
        return "name: "+self.name+" Salary: "+str(self.salary)+" Bonus: "+str(self.bonus)

kim=Manager("kim",3000,300)
print(kim)
