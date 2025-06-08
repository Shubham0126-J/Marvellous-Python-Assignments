class Student:
    school_name = "NESB"

    def __init__(self, name, roll_no):
        self.Name = name
        self.Roll_no = roll_no

    def display(self):
        print(f"Student_name : {self.Name}, Roll_no :{self.Roll_no} and school_name:{Student.school_name}")


set1 = Student("Shubham", 101)
set1.display()

Student.school_name = "ABCD"

set1.display()