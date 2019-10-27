student = [["FirstName","LastName","Age","RollNumber","joinYear","Branch","PhoneNumber","Address"]]

def student_info():
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
    
def search():
    select = int(input("""
1.FullName
2.Branch(It provides count)
3.Year(It provides count)

Select above options for searching: """))


    if select == 1:
        roll = input("Enter Student Rollnumber:")
        for j in range(1,len(student)):
            if roll == student[j][3]:
                fullname = " ".join([y for x,y in enumerate(student[j]) if x<2])
                
                print("\nRoll Number: {}\nFullname:{}".format(student[j][3],fullname))


    elif select == 2:
        branch = input("Enter student branch name:").upper()
        list1 = [student[0]]
        for j in range(1,len(student)):
            if branch == student[j][5]:
                list1.append(student[j])
        for x in range(len(list1)):
            for y in list1[x]:
                print(y.ljust(15),end = "")
            print("\n")         
             
      
    elif select == 3:
        year = input("Enter year:")
        count = 0
        for j in range(1,len(student)):
            if year == student[j][4]:
                count +=1
        print("Total Student count on Year {}: {}".format(year,count))

  
while True:
    request = int(input("""
1.Add 
2.Modifiy 
3.Search
4.exit

Select above options:"""))


    if request == 1:

        while True:
            student_info()
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
        search()
    elif request == 4:
        print("THE END")
        break


 

        
        

    

        
    
    
        
    
    

