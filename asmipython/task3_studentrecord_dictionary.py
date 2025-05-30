#Implement a program to store student records (name,roll,marks,contact number) using a dictionary.
#a. provide menu options to add, search,and display students.
students=[]
def add_student():
    print("\nEnter the student deatils:")
    records={}
    records['name']= input("Input the name")
    records['roll']= int(input("Input the roll number"))
    records['marks']= float(input("Input the marks number"))
    records['contact']= input("Input the contact number")
    students.append(records)
    print("Student records are added.\n")

def search_student():
    rollno = int(input("Enter the roll number to search:"))
    found = False 
    for stu in students:
        if stu['roll']== rollno:
            print("\nStudent record found:")
            print("{:<15}{:<15}{:<15}{:<15}\n".format("Name","Roll","Marks","Contact"))
            print("{:<15}{:<15}{:<15}{:<15}\n".format(stu['name'],stu['roll'],stu['marks'],stu['contact']))
            found = True
            break
        if not found:
            print("Student with this roll number is not found.\n")

def display_students():
    if not students:
        print("No student records to display.\n")
        return
    print("student records are: \n")
    print("{:<15}{:<15}{:<15}{:<15}\n".format("Name","Roll","Marks","Contact"))
    for stu in students:
        print("{:<15}{:<15}{:<15}{:<15}\n".format(stu['name'],stu['roll'],stu['marks'],stu['Contact']))

while True:
    print("1. Add Student")
    print("2. Search Student by Roll Number")
    print("3. Display All Student")
    print("4. Exit")

    option = input("Enter your choice from 1 to 4:")

    if option == '1':
        add_student()
    elif option == '2':
        search_student()    
    elif option == '3':
        display_students()
    elif option == '4':
        print("Exiting") 
        break
    else:
        print("Invalid choice. Please enter number from 1 to 4.\n")   

