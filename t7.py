class Employee:
    def __init__(self, surname, position, salary):
        self.surname = surname
        self.position = position
        self.salary = salary

class Enterprise_employee(Employee):
    def __init__(self, surname, position, salary, rating):
        super().__init__(surname, position, salary)
        self.rating = rating

employees = [
    Enterprise_employee("Aliyev", "Developer", 1000, 70),
    Enterprise_employee("Ismoilov", "Manager", 1500, 80),
    Enterprise_employee("Muminov", "Designer", 1200, 95),
    Enterprise_employee("Olimov", "Engineer", 1100, 55),
    Enterprise_employee("Saidov", "Analyst", 1300, 85)
]

def increase_salary(employee):
    if 60 <= employee.rating < 75:
        employee.salary *= 1.2
    elif 75 <= employee.rating < 90:
        employee.salary *= 1.4
    elif 90 <= employee.rating <= 100:
        employee.salary *= 1.6

for employee in employees:
    increase_salary(employee)
    print(f"{employee.surname}: {employee.position}, New_salary: {employee.salary}")
