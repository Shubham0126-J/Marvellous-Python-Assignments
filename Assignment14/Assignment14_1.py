class Employee:
    def __init__(self, name, emp_id, salary):
        self.Name = name
        self.Emp_id = emp_id
        self.Salary = salary

    def display_details(self):
        print(f"Name : {self.Name}, ID:{self.Emp_id}, Salary:{self.Salary}")

emp1 = Employee("Rohit", 101, 50000)

emp1.display_details()