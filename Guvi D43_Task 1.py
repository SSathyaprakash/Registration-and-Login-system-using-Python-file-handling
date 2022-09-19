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
                 print("Email_Id should not Start with \"@\" and should have no Space in it")
         else:
             print(" Email should have \"@\" and followed by \".\" ")
      else:
         print("Email should not have . immediate next to \"@\"")
   else:
       print("Email should have \"@\" and followed by \".\"")
 else:
    print("Email Id should have \"@\" before Domine ")
###################################################################

def Password_Check(Password):
 special_char="!#$%^&*()-+?_=,<>/@."
 num=["1","2","3","4","5","6","7","8","9","0"]
 d=[i for i in Password if i in num]
 sp=[j for j in Password if j in special_char]
 lc=[k for k in Password if k.islower()==True]
 uc=[l for l in Password if l.isupper()==True]
 if len(d)>0 and len(sp)>0 and len(lc)>0 and len(uc)>0 and len(Password)>5 and len(Password)<16:
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
               print("\nLogin in Sucessfully")
       else:
           print("\nWrong Password")
 except KeyError:
     
     A=input("\nEmail Id Not registered, if you what to register press Y else N  :")
     if A=="Y":
         Registration()
#################################################################
def forget_password():
 import pandas as pd
 print("You Have Opted Forget Password")
 Email=input("\nEnter the Email ID : ").lower()
 df=pd.read_csv("Crediantial.csv")
 df.set_index('email',inplace=True)
 try:
  if len(df.loc[Email])==1:
   print(df.loc[Email])
   A=input("\nDo you like to reset password if Yes Enter \"Y\" else press any key : ").lower()
   if A=="y":
    print("\nPassword length should be 6-16 \nMust have minimum one special character\none digit,\none uppercase,\none lowercase character")
    Password=input("\nEnter your new password : ")
    if Password_Check(Password)==1:
     df.loc[Email,'password']=Password
     df.to_csv("Crediantial.csv")
     print("\nPassword Reset Sucessful ")
    else:
        print("Invalid Password formet")
 except KeyError:
    B=input("\nEmail Id not registered press \"Y\" for regristration :").lower()
    if B=="y":
        print("\nRegrestration Started ")
        Registration()
        
##################################################################
def Registration():
   Email=input("\n\nEnter the Email_ID: ").lower()
   df=pd.read_csv("Crediantial.csv")
   df.set_index('email',inplace=True)
   try: 
     if len(df.loc[Email])==1:
       A=input("Email already Registered press \'Y\' for Login \npress \"N\" for forget password : ").lower()
       if A=="y":
           login()
       elif A=="n":
           forget_password()
   except KeyError:
       
        print("\nNote \*\nPassword length should be 6-16 \nMust have minimum one special character\none digit,\none uppercase,\none lowercase character")
        Password=input("\nPlease enter the  Password: ")
        if Password_Check(Password)==1:
          df = pd.DataFrame({'email': [Email],
                       'password': [Password]})
       
          df.to_csv("crediantial.csv",mode="a",index=False,header=False)
          print("\nRegistered Sucessfully")
   

###########################################
Start=int(input("\nEnter 1 for Login \nEnter 2 for Register \nEnter 3 for Forget Password\n:"))
if Start==1:
    login()
elif Start==2:
    Registration()
elif Start==3:
    forget_password()
else:
    print("\nWrong Entry please Retry")