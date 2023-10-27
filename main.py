class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age =age

    def set_position(self, position):
        self.position = position

    def set_salary(self, salary):
        self.salary = salary

    def printer(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.salary)

employee1 = Employee("Andriy", 23, "Manager", 50000)

employee1.printer()