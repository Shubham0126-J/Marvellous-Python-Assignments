class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self._department = department 
        self.__salary = salary 

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"department: {self._department}")
        print(f"salary: {self.__salary}")

    def get_salary(self):
        return self.__salary

emp = Employee("ABC", "IT", 60000)

print("Public: ", emp.name)

print("Protected: ", emp._department)

print("Private: ", emp.get_salary() )

print("\nEmployee_datails: ")
emp.show_details()