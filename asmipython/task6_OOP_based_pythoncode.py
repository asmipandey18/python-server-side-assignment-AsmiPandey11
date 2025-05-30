#Develop a simple OOP-based python class student with attributes like name,roll number,and marks. Implement methods to input and display details.
class Student:
    def __init__(self):
        self.name = ""
        self.roll_number = ""
        self.marks = 0.0

    def input_details(self):
        self.name = input("Enter the student name:")
        self.roll_number = input("Enter the roll number:")
        self.marks = input("Enter the marks:")

    def display_details(self):
        print("\nStudent Details:")
        print(f"Name:{self.name}")
        print(f"Roll Number:{self.roll_number}")
        print(f"marks:{self.marks}")

student1 = Student()
student1.input_details()
student1.display_details()




    