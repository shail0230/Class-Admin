import random
import smtplib
import sql_connect
import stud
import teach
import cour



class Log(stud.Stud,teach.Teach,cour.Cour):
    def userlog(self):
            self.uname_user=(input("Enter User Name:"))
            self.password_user=(input("Enter Password:"))
            

            # selecting query
            query = "SELECT * from login where uname=%s and upass=%s"
            sql_connect.mycur.execute(query,(self.uname_user,self.password_user))
            
            myresult = sql_connect.mycur.fetchall()
            print(myresult)
            for x in myresult:
                (self.id,self.username_table,self.password_table)= x
                print(self.id)
              
                if self.uname_user == self.username_table and self.password_user == self.password_table:
                    self.login_id_to_register_mail(self.id)
                else:
                    print("Username or Password incorrect")
                    

#login details 
    def login_id_to_register_mail(self,id):
        r_query = "select * from form where id=%s"
        sql_connect.mycur.execute(r_query,(id,))
        result1 = sql_connect.mycur.fetchall()
        print(result1)
        print(" ")
        for y in result1:
            (r_id,r_fname,r_lname,r_email,r_contact,r_gender,r_address)= y
            print(r_email)
            s=smtplib.SMTP('smtp.gmail.com',587)

            s.starttls()
            s.login('iamskyyadav063@gmail.com','vbogawvyrnzqqmbf')
            self.otp1 =str(random.randrange(1000,9999))
                
            s.sendmail('iamskyyadav063@gmail.com',r_email,self.otp1)

            s.quit()
            self.login_otp_Verify(self.otp1)

#Inserting data in login table:          
    def login_data(self,uname_user,password_user):
        sql = "Insert into login(uname,upass) values(%s,%s)"
        val = (uname_user,password_user)
        try:
                sql_connect.mycur.execute(sql,val)
                sql_connect.mydb.commit()
                print("Login Data Inserted...")
                #self.userlog()
                                    
        except:
                print("Something While Wrong...!")

#Student Data and Otp
    def login_otp_Verify(self,otp):
        while True:
            self.user_otp=input("Enter otp:")
            if self.user_otp==otp:
                print("Otp Verify...")

                Studentinfo=int(input("\n1.Student Details \n2.Student Registration \n3.Teacher Details \n4.Teacher Registration \n5.Course Details \n6.add new Courese \n7.Fees Details \n\nChoose any one option:"))
                if Studentinfo==1:
                    print("Student Detalis")
                    self.fetch_Student_Data()
                    
                elif Studentinfo==2:
                    print("Student Registration")
                    self.student_Registration()
                    
                elif Studentinfo==3:
                    print("Teacher Details")
                    self.fetch_techar_Data()
                    
                elif Studentinfo==4:
                    print("Teacher Registration")
                    self.techar()
                    
                elif Studentinfo==5:
                    print("Course Details")
                    self.fetch_cors_Data()
                    
                elif Studentinfo==6:
                    print("Add new Courese")
                    self.cors()
                    break

                else:
                    print("Invalid Number....!")
            else:
                print("Otp Invalide...!")

'''
o = Log()
o.userlog()
o.login_id_to_register_mail()
o.login_otp_Verify()
'''