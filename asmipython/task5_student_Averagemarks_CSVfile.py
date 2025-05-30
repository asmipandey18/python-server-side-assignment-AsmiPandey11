#Write python code to read from a CVS file of student marks and calculate average.
import csv
total_marks=0
student_count=0

with open("studentmarks.csv","r") as file:
    data=csv.DictReader(file)

    for row in data:
        marks = float(row['marks'])
        total_marks += marks
        student_count +=1
average = total_marks / student_count
print(f"\nAverage marks of students:{average}")        
