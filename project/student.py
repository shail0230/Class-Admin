import sql_connect

class Stud:
    def studs(self):
        Studentinfo=int(input("\n1.Student Details \n2.Student Registration \n3.Teacher Details \n4.Teacher Registration \n5.Course Details \n6.add new Courese \n\nChoose any one option:"))
        if Studentinfo==1:
                print("Student Detalis")
            
        elif Studentinfo==2:
            print("Student Registration")
            self.student_Registration()
             
        elif Studentinfo==3:
            print("Teacher Details")
             
        elif Studentinfo==4:
            print("Teacher Registration")
            
        elif Studentinfo==5:
            print("Course Details")
            
        elif Studentinfo==6:
            print("Add new Courese")

        else:
            print("Invalid Number....!")

    def student_Registration(self):
       # print
         #Student Name:
   # def Name(self):
        while True:
                self.name=input("Enter Student Name:")
                self.a= self.name.isalpha()
                if self.a==True:
                    print("")
                    break
                else:
                    print("Only Characters are Allowed...!")
        
#Student Email:
   # def Email(self):
        while True:
                self.Email=input("Enter Student Email Id:")
                self.Email.endswith("@gmail.com")
                if (self.Email.endswith("@gmail.com")==True):
                    print(" ")
                    break
                else:
                    print("Invalid Email...!")
#Student Phone Number:
   # def number(self):
        while True: 
            self.number=(input("Enter Student Mobile Number:"))
            self.x=len(self.number)
            if self.x==10:
                print("")
                break
            else:
                print("Contact Digit Should be 10...")
#Student course:
   # def course(self):
        while True:    
            self.course=input("Enter Student Course:")
            self.c= self.course.isalpha()
            if self.c==True:
                print("")
                break
            else:
                print("Only Characters are Allowed...!")
#Student Fees:
   # def fees(self):
        while True:
            self.fees=int(input("Enter Student Fees:"))
            break
        ''' if self.fees==True:
                #print("")
                break
            else:
                print("Only Number Allowed...")'''
        try:
            self.student_data()
             
        except:
            print("Error While Inserting Student Data...")     
#Data Insert in table:
    def student_data(self):
        while True:
            print("Do You Want To Submit:")
            print("1.Yes 2.No")
            self.submit=int(input("Chose One:"))
            if self.submit==1:
       
                sql = "insert into student(name,email,contact,course,fees) values(%s,%s,%s,%s,%s)"
                val = (self.name,self.Email,self.number,self.course,self.fees)
           
                try:
                    sql1.mycur.execute(sql,val)
                    sql1.mydb.commit()
                    print("Student Data Inserted...")
                    break
        
                except:
                    print("Duplicate Id...!")
                    break

            elif self.submit==2:
                print("Your Data Not Submitted...!")
                break
            else:
                print("Invalid Number...!")

    def fetch_Student_Data(self):
        r_query = "select * from student"
        sql1.mycur1.execute(r_query)
        result1 = sql1.mycur1.fetchall()
        #print(result1)
        for y in result1:
           # (r_id,r_fname,r_name1,r_mail,r_contact,r_gender,r_address)= y
            print(y)



obj=Student()
obj.student_Registration()
obj.fetch_Student_Data()