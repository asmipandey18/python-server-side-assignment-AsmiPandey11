#create a program that takes a list of student names and stores them in a file.Then read the file and display the contents.

num_students = int(input("Input the number of students"))

student = []
for i in range(num_students):
    name=str(input("Enter the name of student"))
    student.append(name)

filename = "student.txt"
with open(filename,"w") as file:
    for name in student:
        file.write(f"{name}\n") 

print("\nStudent name are written successfully to file")

print("\nReading from the file")

with open(filename,"r") as file:
    contents=file.read()
    print(contents)