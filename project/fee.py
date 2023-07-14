import stud
import sql_connect
import datetime
import smtplib
import random
#import PyPDF2
from email.mime.multipart import MIMEMultipart
#from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage



from fpdf import FPDF


class Fee(stud.Stud):
    def fee(self):
        self.r_email=input("Enter your email:")
        #if(self.r_email==self.Email):

        query = "SELECT * from student where email=%s"
        sql_connect.mycur.execute(query,(self.r_email,))
        
        myresult = sql_connect.mycur.fetchall()
        #print(myresult)

        for x in myresult:
                (self.id,self.name,self.email,self.contact,self.course,self.total_fees,self.paid_fees,self.bal_fees)= x
                print(self.total_fees,"   ",self.paid_fees,"   ",self.bal_fees)

        self.fees=int(input("Enter Your Fees:"))
        if(self.fees<=self.total_fees):
            self.paid_fees=self.paid_fees + self.fees
            self.bal_fees=self.total_fees-self.paid_fees
            print(self.total_fees,"   ",self.paid_fees,"   ",self.bal_fees)

            sql="update student set paid_fees=%s,bal_fees=%s where email=%s" 
            val=(self.paid_fees,self.bal_fees,self.r_email)
            sql_connect.mycur1.execute(sql,val)
            sql_connect.mydb.commit()
        else:
             print("Issue In Fees Please Check Database")

    def pdf(self): 
        ct = datetime.datetime.now()
        z = ct.strftime("%d%m%y_%H_%M_%S")
        a = ("Shail"+z+".pdf")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('helvetica', size=20)
        pdf.cell(200,10,txt="Sailesh",align='C')
       
        #print(a)
        pdf.output(a)


        msg = MIMEMultipart()
        msg.attach(MIMEText(open("C:/Users/91897/Shail280423_10_51_57.pdf").read()))

        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('iamskyyadav063@gmail.com','vbogawvyrnzqqmbf')
        #self.otp =str(random.randrange(10000,99999))
        
        #self.user_name=self.fname[0:3]+self.lname[0:3]
        #all="Username is="+self.user_name+"\n"+"Otp is="+self.otp + "\n Password is=" + self.password
        s.sendmail('iamskyyadav063@gmail.com','shaileshyadav1109@gmail.com',msg.as_string())

        s.quit()
        




        # creating a pdf file object
        #pdfFileObj = open("Shail280423_10_51_57.pdf", 'rb')
        
        # creating a pdf reader object
        #pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
        # printing number of pages in pdf file
        #print(pdfReader.numPages)
        
        # creating a page object
        #pageObj = pdfReader.getPage(0)
        
        # extracting text from page
        #print(pageObj.extractText())
        
        # closing the pdf file object
        #pdfFileObj.close()
'''
        yr=dt.strftime("%Y")
        yr1=dt.strftime("%m")
        yr2=dt.strftime("%d")
        t = dt.strftime("%H:%M:%S")

        x = str(yr + yr1 + yr2)+".pdf"
        print(x)
        print(type(x))
        
        print(t)
        print(yr)
        print(yr1)
        print(yr2)
        print(t+yr+yr1+yr2)
        #print(str(dt))
        #print(type(dt))
        #print(dt.timestamp())
        '''
        
        

        

        
              

o = Fee()
#o.fee()
o.pdf()
        

