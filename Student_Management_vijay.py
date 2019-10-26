##import xlsxwriter as xlsx
##
##workbook = xlsx.Workbook("Student_list.xlsx")
##worksheet = workbook.add_worksheet("Year 2005")
def student_info(num_student):
    student = [["FirstName","LastName","Age","RollNumber","joinYear","Branch","PhoneNumber","Address"]]
    for i in range(num_student): #range(1,3) 1,2

    
        First_Name = input("First Name of Student:").upper()
        Last_Name = input("Last Name of Student:").upper()
        Age =int(input("Student Age :"))
        Roll_Number = input("Roll Number of Student:")
        join_Year = int(input("Join Year :"))
        Branch = input("Branch Name:").upper()
        Phone_no = int(input("Enter Phone Number:"))
        Address = input("Address:")
        l = [First_Name,Last_Name,str(Age),Roll_Number,str(join_Year),Branch,str(Phone_no),Address]
        student.append(l)
        
    return student

def search(student):
    select = int(input("""Select below options for searching:
                                    1.FullName
                                    2.Branch(It provides count)
                                    3.Year(It provides count):"""))
    if select == 1:
        roll = input("Enter Student Rollnumber:")
        for j in range(1,len(student)):
            if roll == student[j][3]:
                fullname = " ".join([y for x,y in enumerate(student[j]) if x<2])
                
                return fullname
    elif select == 2:
        branch = input("Enter student branch name:").upper()
        
        list1 = [student[0]]
        for j in range(1,len(student)):
            if branch == student[j][5]:
                list1.append(student[j])
        res = " ".join(list1)
        
        return res
    
    elif select == 3:
        year = int(input("Enter year:"))
        count = 0
        for j in range(1,len(student)):
            if year == student[j][4]:
                count +=1
        return count

def formate_list(x):
    for x in range(len(student)):
        for y in student[x]:
            print(y.ljust(15),end = "")
    print("\n")

        
    
    
##while True:
##    num_student = input("Enter Number of students:")
##    if not num_student.isdigit():
##        try:
##            num_student = int(num_student)
##           
##        except ValueError as a:
##            print(a)
##            continue
##    elif int(num_student)> 0:
##        break
while True:
    request = int(input("""Select below options:
                                        1.Add 
                                        2.Modifiy 
                                        3.Search
                                        4.exit:"""))


    if request == 1:

        while True:
            student = student_info(1)
            req_student = input("Do you want to enter more student data(YES/NO):").upper()
            if req_student == "YES":
                continue
            else:
                break
        for x in range(len(student)):
            for y in student[x]:
                print(y.ljust(15),end = "")
            print("\n")
            
    elif request == 2:
        continue
    elif request == 3:
        result = search(student)
        print(result)
    elif request == 4:
        print("THE END")
        break

        
 

        
        
        

        
    
##row = 0
##col = 0
##for x in range(len(student)):
##    for FirstName,LastName,Age,RollNumber,joinYear,Branch,PhoneNumber,Address in [student[x]]:
##        worksheet.write(row,col,FirstName)
##        worksheet.write(row,col+1,LastName)
##        worksheet.write(row,col+2,Age)
##        worksheet.write(row,col+3,RollNumber)
##        worksheet.write(row,col+4,joinYear)
##        worksheet.write(row,col+5,Branch)
##        worksheet.write(row,col+6,PhoneNumber)
##        worksheet.write(row,col+7,Address)
##        row +=1
##workbook.close()    
    
    
    
##    for x in range(len(student)):
##        for y in student[x]:
##            print(y.ljust(15),end = "")
##        print("\n")
        
    
##    l = t.split()
##    le = len(l)
##    while le>0:
##        for j in l:
##            print(j.rjust(15),end="")
##            le= le-1    
##result = search(student)
##print(result)

    

        
    
    
        
    
    

