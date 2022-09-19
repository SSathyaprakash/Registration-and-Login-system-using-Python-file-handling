#Registration and Login system using Python, file handling
import csv
def Email_Check(Email):
 special_char="!#$%^&*()-+?_=,<>/"
 num=["1","2","3","4","5","6","7","8","9","0"]
 if ("@" in Email) and Email.count("@")==1:
   if ("." in Email) and Email.count(".")==1: 
      if  Email.index(".")-Email.index("@")!=1:
         if Email.index(".") >Email.index("@"):
             if Email.index("@")>1 and Email.count(" ")==0 :
                 if Email[0] not in num and  Email[0] not in special_char and Email[len(Email)-1]!=".":
                    return 1
                 else:
                     print("Email_Id should not start with special characters and numbers and ending should not be \".")
             else:
                 print("Email_Id should not Start with @ and should have no Space in it")
         else:
             print(" Email should have @ and followed by .")
      else:
         print("Email should not have . immediate next to @")
   else:
       print("Email should have @ and followed by .")
 else:
    print("Email Id should have @ before Domine ")
###################################################################

def Password_Check(Password):
 special_char="!#$%^&*()-+?_=,<>/@."
 num=["1","2","3","4","5","6","7","8","9","0"]
 d=[i for i in Password if i in num]
 sp=[j for j in Password if j in special_char]
 lc=[k for k in Password if k.islower()==True]
 uc=[l for l in Password if l.isupper()==True]
 if len(d)>0 and len(sp)>0 and len(lc)>0 and len(uc)>0:
    return 1
 else:
    print("Invalid Password")    
################################################################
import pandas as pd

def login():
 Email=input("Enter your Email_id : ").lower()
 df=pd.read_csv("Crediantial.csv")
 df.set_index('email',inplace=True)
 try: 
   if len(df.loc[Email])==1:
       
       Password=input("Enter your Password : ")
       df=pd.read_csv("Crediantial.csv")
       df.set_index('email',inplace=True)
       if df.loc[Email,'password']==Password:
               print("Login in Sucessfully")
       else:
           print("Wrong Password")
 except KeyError:
     
     A=input("Email Id Not registered, if you what to register press Y else N  :")
     if A=="Y":
         Registration()
#################################################################
def forget_password():
    Email=input("\nEnter the Email_ID/Username :").lower()
    with open("Crediantial.csv","r") as f:
        r = csv.reader(f)
        for i in r:
            if Email==i[0]:
                A=int(input("\n1 to display old Password \n2 for set new password \n:"))
                if A==1:
                    print('Emaili = ',i[0])
                    print('Password= ', i[1])
                elif A==2:
                    with open("Crediantial.csv","w") as f:
                       w=csv.writer(f) 
                       w.writerow([Email,Password_Check(Password)])
            else:
                A=input("Email Id Not registered, if you what to register press Y else N  :")
                if A=="Y":
                    Registration()
                    
                else:
                    break
                        
        


##################################################################
def Registration():
   Email=input("\n\nEnter the Email_ID/Username: ").lower()
   if Email_Check(Email)==1:
      Password=input("\nPlease enter the  Password: ")
      if Password_Check(Password)==1:
       df = pd.DataFrame({'email': [Email],
                       'password': [Password]})
       print(df)
       df.to_csv("crediantial.csv",mode="a",index=False,header=False)
       print("Registered Sucessfully")
           

###########################################
Start=int(input("\nEnter 1 for Login \nEnter 2 for Register \nEnter 3 for Forget Password\n:"))
if Start==1:
    login()

elif Start==2:
    Registration()
elif Start==3:
    forget_password()
else:
    print("Wrong Entry please re-try")