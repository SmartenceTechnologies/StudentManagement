students_details = ["fname", "lname", "branch", "roll_no", "age"]

def students_managment(student_details):
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    branch = input("Enter branch: ")
    roll_no = input("Enter roll_no: ")
    age = input("Enter age: ")
    details = [fname, lname, branch, roll_no, age]
    students_details.append(details)
print(students_managment(students_details))




n = int(input("Enter total number of students: "))
l = []
count = 0
while count < n:
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    roll_no = input("Enter roll no: ")
    age = input("Enter age: ")
    count += 1
    t = [name, branch, roll_no, age]
    l.append(t)
print(l)




    
