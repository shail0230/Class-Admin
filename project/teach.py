import sql_connect

class Teach:        
    def techar_Registration(self):
        while True:
                self.name=input("Enter Teacher Name:")
                self.a= self.name.isalpha()
                if self.a==True:
                    print("")
                    break
                else:
                    print("Only Characters are Allowed...!")
        
#Student Email:
   # def Email(self):
        while True:
                self.Email=input("Enter Teacher Email Id:")
                if (self.Email.endswith("@gmail.com")==True):
                    print(" ")
                    break
                else:
                    print("Invalid Email...!")
#Student Phone Number:
   # def number(self):
        while True: 
            self.number=(input("Enter Teacher Mobile Number:"))
            self.x=len(self.number)
            if self.x==10:
                print("")
                break
            else:
                print("Contact Digit Should be 10...")
#Student course:
   # def course(self):
        while True:    
            self.course=input("Enter Teacher's Subject:")
            if self.course.isalpha()==True:
                print("")
                break
            else:
                print("Only Characters are Allowed...!")
#Student Fees:
   # def fees(self):
        while True:
            self.slry=input("Enter Teacher Salary:")
            if self.slry.isdigit()==True:
                print("")
                break
            else:
                print("Only Number Allowed...")
        try:
            self.teacher_data()
             
        except:
            print("Error While Inserting teacher Data...")     
#Data Insert in table:
    def teacher_data(self):
        while True:
            print("Do You Want To Submit:")
            print("1.Yes 2.No")
            self.submit=int(input("Choose your option:"))
            if self.submit==1:
       
                sql = "insert into teacher(name,email,contact,course,salary) values(%s,%s,%s,%s,%s)"
                val = (self.name,self.Email,self.number,self.course,self.slry)
           
                try:
                    sql_connect.mycur.execute(sql,val)
                    sql_connect.mydb.commit()
                    print("Teacher Data Inserted...")
                    break
        
                except:
                    print("Dublicate Id...!")
                    break

            elif self.submit==2:
                print("Your Data Not Submitted...!")
                break
            else:
                print("Invalid Number...!")

    def fetch_techar_Data(self):
        r_query = "select * from teacher"
        sql_connect.mycur.execute(r_query)
        result1 = sql_connect.mycur.fetchall()
        #print(result1)
        for y in result1:
           # (r_id,r_fname,r_name1,r_mail,r_contact,r_gender,r_address)= y
            print(y)



obj=Teach()
obj.techar_Registration()
obj.fetch_techar_Data()
