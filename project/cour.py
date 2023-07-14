import sql_connect

class Cour:
    def cour(self):
        self.cname=input("Enter Course name:")
        self.ctime=input("Enter course Duration:")
        self.cfees=input("Enter course Fees:")

    def cour_data(self):
        while True:
            print("Do You Want To Submit:")
            print("1.Yes \n2.No")
            self.submit=int(input("Choose your option:"))
            if self.submit==1:
       
                sql = "insert into course(name,duration,fees) values(%s,%s,%s)"
                val = (self.cname,self.ctime,self.cfees)
           
                try:
                    sql_connect.mycur.execute(sql,val)
                    sql_connect.mydb.commit()
                    print("Course Data Inserted...")
                    break
        
                except:
                    print("Duplicate Id...!")

            elif self.submit==2:
                print("Your Data Not Submitted...!")
                break
            else:
                print("Invalid Number...!")


    def fetch_cors_Data(self):
        r_query = "select * from course"
        sql_connect.mycur.execute(r_query)
        result1 = sql_connect.mycur.fetchall()
        #print(result1)
        for y in result1:
           # (r_id,r_fname,r_name1,r_mail,r_contact,r_gender,r_address)= y
            print(y)

o = Cour()
o.cour()
o.cour_data()
o.fetch_cors_Data()