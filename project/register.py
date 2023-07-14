import random
import smtplib
import sql_connect
import log

class Reg(log.Log):

    def reg(self):
        #first name
        while True:
                self.fname=input("First Name:")
                if self.fname.isalpha():
                    print(self.fname)
                    break
                else:
                    print("First Name Should be String")
    #last name
    #def nam1(self):
        while True:
                self.lname=input("Last Name:")
                self.a= self.lname.isalpha()
                if self.a==True:
                    print(self.lname)
                    break
                else:
                    print("Last Name Should be String")
#email
    #def mail(self):
        while True:
            self.email =input(" E-mail ID:")
            b=self.email.endswith("@gmail.com")
            c=self.email.endswith("@yahoo.com")
            if b==True or c==True:
                print(" ")
                break
            else:
                print("Wrong Email-ID")
            
#contact
    #def cont(self):
        while True:      
            try:
                self.contact=int(input("Contact:"))     
                if self.contact>=7000000000 and self.contact<=9999999999:
                    print("valid Contacts ")
                    break
                else:
                    print("Contact Digit Should Be 10")
            except :
                print ("Contact Should be Number")
            
#address
    #def add(self):
        self.address = input("Address:")

#gender
    #def gend(self):
        while True:
            print("1.Male \n2.Female \n3.Other")
            self.gender = int(input("Choose Your Gender:"))
            if self.gender==1:
                self.gender2 = "Male"
                print("You Have Choosen",self.gender2)
                break
            elif self.gender==2:
                self.gender2 = "Female"
                print("You Have Choosen",self.gender2)
                break
            elif self.gender==3:
                self.gender2 = "Other"
                print("You Have Choosen",self.gender2)
                break
            else:
                print("You Have Choosen Wrong Option")
                #break
        self.mail()
        self.chek_otp()
        

    def subm(self):
        while True:
            print("Do You Want To Submit ??")
            print("1.Yes \n 2.No")
            self.submit = int(input("Enter Your Choice:"))
            if self.submit==1:
                sql = "INSERT into form(fname,lname,mail,contact,gender,address) values(%s,%s,%s,%s,%s,%s)"
                val = (self.fname,self.lname,self.email,self.contact,self.gender2,self.address)           
                try:
                    sql_connect.mycur.execute(sql,val)
                    sql_connect.mydb.commit()
                    print("Data Stored Successfully")
                    
                    self.login_data(self.user_name,self.password)
                    break
                except:
                    print("Dublicate ID..")
            elif self.submit==2:
                print("Submit After Change")
                break
            else:
                print("Please Select Right Option")
                break 

    def mail(self):
    # random Password  
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
        self.password = ""
        for i in range(4):
            self.password += random.choice(characters)
            #print(password)       
            
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('iamskyyadav063@gmail.com','vbogawvyrnzqqmbf')
        self.otp =str(random.randrange(10000,99999))
        
        self.user_name=self.fname[0:3]+self.lname[0:3]
        all="Username is="+self.user_name+"\n"+"Otp is="+self.otp + "\n Password is=" + self.password
        s.sendmail('iamskyyadav063@gmail.com','shaileshyadav1109@gmail.com',all)

        s.quit()

    #check Otp:
    def chek_otp(self):
        while True:
            self.user_otp=input("Enter OTP:")
            if self.user_otp==self.otp:
                print("OTP Confirmed")
                
                self.subm()
                break
                #self.userlog()
                
            else:
                print("Invalide OTP")
'''
o = Reg()
o.reg()
o.subm()
o.mail()
o.chek_otp()
'''