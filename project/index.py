import random
import smtplib
import sql_connect
import register
import log

class ind(register.Reg,log.Log):
    def __init__(self):
        while True:
            print("1.Register \n2.Login \n3.Exit")
            
            a = int(input("Choose Your Option:"))
            if a==1:
                self.reg()
                #break

            elif a==2:
                self.userlog()
                break

            elif a==3:
                exit()

            else:
                print("Choose right option!!!")

o=ind()

