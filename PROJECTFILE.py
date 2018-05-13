import anydbm
from datetime import datetime
import getpass
print "\n***************************WELCOME****************************\n                    IIT GANDHINAGAR CANTEEN"
k=str(datetime.now())
k1=int(k[11:13]+k[14:16])
while True:


 main_password=getpass.getpass("ENTER THE PASSWORD\n")
 if main_password =='0987654321':
  print "                         ACCESS GRANTED\n"
  i=1
  c=1

  while i>0:
   balance=anydbm.open("balance.db", 'c')
   password=anydbm.open("password.db", 'c')
   print "\n\nChoose any of the options given below:\nPress1. for Registration\nPress2. for Balance Enquiry\nPress3. for Ordering"
   print "Press4. for Crediting the account\nPress5. for deleting your account from our canteen\nPress6. Switch Off"
   k=str(datetime.now())
   k1=int(k[11:13]+k[14:16])
   print "                         TIME:",k[11:16]
   a=raw_input()
   if int(a)==1:
    b=raw_input("Enter your USER_ID:\n") 
    
    d=0
 
    if b in balance.keys():
     d=d+1
   
    if d>0:
     print "THE ACCOUNT ALREADY EXISTS WITH SAME USER NAME, PLEASE TRY WITH A NEW ONE \n"
    else:
     
     e=raw_input("Enter the amount crediting in the account, the minimum balance in the account is Rs200\-\n")
     if int(e)>=200:
      b1=getpass.getpass("Enter the pass_word\n")
      password[b]=b1
      balance[b]=e
      print "NOW YOUR NEWLY OPENED ACCOUNT BALANCE IS Rs.:",balance[b]
      balance.close()
      password.close()
     else:
      print "INSUFFICIENT AMMOUNT TO REGISTER (MINIMUM BALANCE REQUIRED TO REGISTER IS Rs 200\-)\n"
 
   elif int(a)==2:
     b=raw_input("Enter your USER_ID:\n")
     b1=getpass.getpass("Enter the password:\n")
     if b in balance.keys():
      if b1 ==password[b]:
       print "YOUR BALANCE IS Rs.\n",balance[b]
      else:
       print "Invalid password"
     else:
       print "Please  first do register to our canteen and check your balance\n"
   elif int(a)==4:
    j=raw_input("Enter your USER_ID:\n")
    j1=getpass.getpass("Enter the main server password required")
    if j in balance.keys():
     if j1=='0987654321':
      credit=input("Enter the amount to be credited in your account\n")
      balance[j]=str(int(balance[j])+credit)
      print "Now your account balance is:\n",balance[j]
      balance.close()
     else:
      print "Incorrect password\n"
    else:
      print "Please  first do register to our canteen\n"
   elif int(a)==5:
    r=raw_input("Enter the  USER_ID of the account that has to be deleted\n")
    r1=getpass.getpass("Enter the password of the account\n")
    if r in balance.keys():
     if r1==password[r]:
      a1=balance[r]
      del balance[r]
      print "The remaining amount to be returned is : Rs.",a1
      balance.close()
     else:
      print "Incorrect password"
    else:
       print "The account already doesn't exist\n"
   elif int(a)==3:
    g=raw_input("Enter your USER_ID\n")
    g1=getpass.getpass("Enter the password\n")
    if g in balance.keys():
     if g1==password[g]:
      print"\n       CANTEEN MENU:\n"
      

      print"\n                   101.samosa                  -  Rs15"
      print"\n                   102.veg puf                 -  Rs15"  
      print"\n                   103.egg puf                 -  Rs20"   
      print"\n                   104.lays                    -  Rs20"   
      print"\n                   105.kurkure                 -  Rs10"    
      print"\n                   106.biscuits                -  Rs15"      
      print"\n                   107.tea                     -  Rs10"      
      print"\n                   108.onion paratha           -  Rs15"
      print"\n                   109.aloo paratha            -  Rs15"   
      print"\n                   110.egg biryani             -  Rs30"
      print"\n                   111.egg fried rice          -  Rs30"
      print"\n                   112.milk                    -  Rs10"
      print"\n                   113.coffee                  -  Rs10"   
      print"\n                   114.vada pav                -  Rs10"    
      print"\n                   115.veg cutlet              -  Rs15"     
      print"\n                   116.plain maggie            -  Rs20"     
      print"\n                   117.egg maggie              -  Rs25"       
      print"\n                   118.dahi vada               -  Rs20"       
      print"\n                   119.egg noodles             -  Rs30"         
      print"\n                   120.cool drinks             -  Rs10"
      q=dict() 
      l=[15,15,20,20,10,15,10,15,15,30,30,10,10,10,15,20,25,20,30,10] 
      for i in range(101,121):
        q[i]=l[i-101]
      h=1
      while h>0:
    
       s=input("enter the ORDER NUMBER of your item:\nTo exit ordering option enter '0'\n")  
     
       if s in range(101,121):
        f=input("enter the QUANTITY of the ITEM you want to be served: ")
    
        u=int(q[s])*int(f)
        if u<=int(balance[g]):
         balance[g]=str(int(balance[g])-u)
         print "your order will be served in a few minutes\n"
         print "Your account balance after this transaction is Rs.",balance[g]
        
        else:
         print "Insufficient balance. Please  recharge your balance and again come to ordering \n"
       
         break
       elif s==0:
        print "Exit\n"
        break
       else:
        print "Invalid Input"
     else:
       print "Incorrect password\n" 
    else:
     print"first create an account in our canteen"
    balance.close()
   elif int(a)==6:
    break
    balance.close()
   elif int(a)==9999:
    print balance.items()
   
   else:
    print "Invalid Input\n"
   password.close()
   balance.close()
 elif main_password=='10':
  break
 else:
  print "Access Denied\nplease try again or to exit press 10"
