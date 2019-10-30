import os
import pickle

student = [["RollNumber","FirstName","LastName","Age","joinYear","Branch","PhoneNumber","Address"]]


def student_info():
    First_Name = input("First Name of Student:").upper()
    Last_Name = input("Last Name of Student:").upper()
    Age = int(input("Student Age :"))
    Roll_Number = r_number()
    join_Year = int(input("Join Year :"))
    Branch = input("Branch Name:").upper()
    Phone_no = p_number()
    Address = input("Address:")
    
    for x in range(len(student)):
        l = [str(Roll_Number),First_Name,Last_Name,str(Age),str(join_Year),Branch,str(Phone_no),Address]
        if student[x][0] == Roll_Number or (student[x][1] + student[x][2]) == (First_Name+Last_Name):
            print("\nExisting student have same roll number {}".format(Roll_Number))
            break
        elif student[x][1] + student[x][2] == First_Name+Last_Name:
            print("\nStudent Name:{} \tRollNumber:{} \tBranch :{} \tYear :{}\nIs already existed in our records".format((First_Name+Last_Name),student[x][0],student[x][5],student[x][4]))
            break
            
    else:
        student.append(l)

def r_number():
    while True:
        value = input("Enter with in 7 digits for Roll Number:")
        try:
            if isinstance(int(value),int):
                if len(value)<7:
                    return value
                
        except ValueError:
            continue
            
         
        else:
            print("7 Digits only")
def p_number():
    while True:
        value = input("Enter 10 digits Phone Number:")
        if len(value)==10:
            return value
         
        else:
            print(" 10 Digits are mandatory ")
    
            
                        
def search():
    select = int(input("""
1.FullName
2.Branch(It provides count)
3.Year(It provides count)

Select above options for searching: """))


    if select == 1:
        roll = input("Enter Student Rollnumber:")
        for j in range(1,len(student)):
            if roll == student[j][0]:
                fullname = " ".join([y for x,y in enumerate(student[j]) if (1<= x <3)])
                print("\nRoll Number: {}\nFullname:{}".format(student[j][0],fullname))


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

        if not os.path.exists("C:\\Users\\SHANKAR REDDY\\Desktop\\listfile.txt"):
            with open('listfile.txt', 'wb') as filehandle:
                pickle.dump(student, filehandle)
        elif os.path.exists("C:\\Users\\SHANKAR REDDY\\Desktop\\listfile.txt"):
            with open("C:\\Users\\SHANKAR REDDY\\Desktop\\listfile.txt", 'rb') as filehandle:
                my_list = pickle.load(filehandle)
                for x in range(len(student)):
                    for y in range(len(my_list)):
                        if my_list[y][0]==student[x][0] and my_list[y][1] == student[x][1] and my_list[y][2] == student[x][2]:
                            break
                    else:
                        
                        my_list.append(student[x])    
                print(my_list)
                with open('listfile.txt', 'ab') as filehandle:
                    pickle.dump(my_list, filehandle)
            
            
            
##        for x in range(len(student)):
            
##            for y in student[x]:
##                if not os.path.exists("C:\\Users\\SHANKAR REDDY\\Desktop\\listfile.txt"):
##                    with open('listfile.txt', 'wb') as filehandle:
                        
##                        for listitem in y:
##                            filehandle.write(y.ljust(15))
##                    file = open("C:\\Users\\SHANKAR REDDY\\Desktop\\Text.txt","w")
##                    file.write(y.ljust(15))
##                elif os.path.exists("C:\\Users\\SHANKAR REDDY\\Desktop\\Text.txt"):
##                    places = []
##                    with open('listfile.txt', 'r') as filehandle:
##                        for line in filehandle:
##                            currentPlace = line[:-1]
##                            places.append(currentPlace)
                  
##                    file = open("C:\\Users\\SHANKAR REDDY\\Desktop\\Text.txt","a")
##                    file.write(y.ljust(15))
##            file.write("\n")        
                    
##                print(y.ljust(15),end = "")
##            print("\n")
            
    elif request == 2:
        continue
    elif request == 3:
        search()
    elif request == 4:
        print("THE END")
##        file.close()
        break


 

        
        

    

        
    
    
        
    
    

