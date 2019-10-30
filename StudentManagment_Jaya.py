students_details = [["fname", "lname", "branch", "roll_no", "age", "year"]]

def students_managment():
    n = int(input("Enter total no of students: "))
    count = 0
    while count < n:
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        branch = input("Enter branch: ")
        roll_no = input("Enter roll_no: ")
        age = input("Enter age: ")
        year = input("Enter a year: ")
        count += 1
        details = [fname, lname, branch, roll_no, age, year]
        students_details.append(details)
students_managment()
print(students_details)

for i in range(len(students_details)):
    for j in range(len(students_details[i])):
        print(students_details[i][j], end=" ")
    print()    


'''
for details in students_details:
    print("      ".join(details))
'''
    
def search(student_details):
    n = int(input("Enter an index number: "))
    return [item[n] for item in students_details]
print(search(students_details))    




n = int(input("Enter total number of students: "))
students_details = [["Nmae", "Branch", "Roll_no", "Age", "Year"]]
count = 0
while count < n:
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    roll_no = input("Enter roll no: ")
    age = input("Enter age: ")
    year = input("Enter a year: ")
    count += 1
    t = [name, branch, roll_no, age, year]
    students_details.append(t)
print("students_details: ", students_details)

for i in range (len(students_details)):
    for j in range(len(students_details[i])):
        print(students_details[i][j], end=" ")
    print()    

def search(students_details):
    n = int(input("Enter an index number: "))
    return [item[n] for item in students_details]
print(search(students_details))






    
