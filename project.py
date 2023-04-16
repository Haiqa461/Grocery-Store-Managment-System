items = dict({1: 'Bread', 2:  'Rice', 3: 'Soap', 4:  'Sugar', 5:  'Tea', 6:  'Snacks', 7:  'Milk', 8:  'Eggs', 9:  'Oil', 10:  'Flour'})
prices = dict({1: 120, 2: 880, 3: 50, 4: 100, 5: 150, 6: 30, 7: 90, 8: 100, 8: 900, 10: 70})
qu=dict({1: 42, 2: 60, 3: 100, 4: 55, 5: 90, 6: 15, 7: 36, 8: 80, 9: 50, 10: 5})
di = dict(zip(items,prices)) 

def file():
    fgl=open("C:\Grocery Store Management System\listcus.txt","r")
    print(fgl.read())
    fgl.close
    return
def item_list():
    st=open("C:\Grocery Store Management System\List.txt")
    print(st.read())
    st.close
    return
# cashier login function 
def cashier ():
  print("Want to login as a cashier ")
  signin=input(" (1)Yes    (2)No   \n")
  if signin=="1":
   for i in range(3):
    Username=input("Enter Username: ")
    password=input("Enter Password: ")
    if Username=="sabeen@gmail.com" and  password=="7654":
     print(" \n  processing data.....")
     print(" **** CASHIER VERIFIED **** ")
     print(" View items and prices list ")
     file()
     print("Cashier's profile activated")
     print("HAVE A NICE EXPERIENCE")
     break
    elif print("INCORRECT PASSWORD "):
        
     return
 
# customer's shopping calculations 
def calcuation():
                        for x in range(4):
                            i=input("    Enter Item No: ")
                            if i=="1":                            
                                q=int(input("    Enter Quantity: " )) 
                                c=120*q
                                print("    GROCERY STORE")
                                print("    Bread:120 \n ")
                                print("    Total:",c)
                                print("    Bill is Checked by Cashier  \n \n  ")
                                print("    **THANK YOU FOR SHOPING WITH US**")
                            elif i=="2":
                                q=int(input("    Enter Quantity: " )) 
                                c=80*q
                                print("    GROCERY STORE")
                                print("    Rice:80 \n ")
                                print("    Total:",c)
                                print("    Bill is Checked by Cashier  \n \n  ")
                                print("    **THANK YOU FOR SHOPING WITH US**")
                            elif i=="3":
                                q=int(input("    Enter Quantity: " )) 
                                c=110*q
                                print("    GROCERY STORE")
                                print("    Sof Drinks:110 \n ")
                                print("    Total:",c)
                                print("    Bill is Checked by Cashier  \n \n  ")
                                print("    **THANK YOU FOR SHOPING WITH US**")
                            elif i=="4":
                                q=int(input("    Enter Quantity: " )) 
                                c=100*q
                                print("    GROCERY STORE")
                                print("    Sugar:100 \n ")
                                print("    Total:",c)
                                print("    Bill is Checked by Cashier  \n \n  ")
                                print("    **THANK YOU FOR SHOPING WITH US**")
                            elif i=="5":
                                q=int(input("    Enter Quantity: " )) 
                                c=150*q
                                print("    GROCERY STORE")
                                print("    tea:150 \n ")
                                print("    Total:",c)
                                print("    Bill is Checked by Cashier  \n \n  ")
                                print("    **THANK YOU FOR SHOPING WITH US**")
                            elif i=="6":
                                q=int(input("    Enter Quantity: " )) 
                                c=30*q
                                print("    GROCERY STORE")
                                print("    Snaks:30 \n ")
                                print("    Total:",c)
                                print("    Bill is Checked by Cashier  \n \n  ")
                                print("    **THANK YOU FOR SHOPING WITH US**")
                            elif i=="7":
                                q=int(input("    Enter Quantity: " )) 
                                c=90*q
                                print("    GROCERY STORE")
                                print("    Milk:90 \n ")
                                print("    Total:",c)
                                print("    Bill is Checked by Cashier  \n \n  ")
                                print("    **THANK YOU FOR SHOPING WITH US**")
                            elif i=="8":
                                q=int(input("    Enter Quantity: " )) 
                                c=100*q
                                print("    GROCERY STORE")
                                print("    Eggs:100 \n ")
                                print("    Total:",c)
                                print("    Bill is Checked by Cashier  \n \n  ")
                                print("    **THANK YOU FOR SHOPING WITH US**")
                            elif i=="9":
                                q=int(input("    Enter Quantity: " )) 
                                c=900*q
                                print("    GROCERY STORE")
                                print("    Oil:900 \n ")
                                print("    Total:",c)
                                print("    Bill is Checked by Cashier \n \n  ")
                                print("    **THANK YOU FOR SHOPING WITH US**")
                            elif i=="10":
                                q=int(input("    Enter Quantity: " )) 
                                c=700*q
                                print("    GROCERY STORE")
                                print("    Flour:700 \n ")
                                print("    Total:",c)
                                print("    Bill is Checked by Cashier  \n \n  ")
                                print("    **THANK YOU FOR SHOPING WITH US**")
                        print("**********************************************") 
                        return     
# OWNER PART 
    
print("                WELCOME TO GLOSSARY STORE                    ")

print("SELECT         ")
print("     1.OWNER       2.CASHIER         3.CUSTOMER  ")

login=input("Enter number ")
if login=="1":
    name=input("Enter Name: ")
    vcode=input("Enter password: ")
    if name=="Haiqa" and vcode=="255":
        print(" Verification succeed ")
        print(" This store is on yours commmand Owner \n You can manage  items here  ")
        print(" SELECT ")
        print("1.See Items     2.Add any Item \n   3.Edit Prices   4.Increase/Decrease Stock " )
        entr=input(" Enter number: ")
        if entr=="1":
            item_list()      
                   
        if entr =="2":
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
           add1=input(" Want to add any item    \n  1.Yes  \n  2.No ")
    
           if add1=="1":
               add1=input(" Enter item: ")
               addp1=input(" Add price of item: ")
               items.update({11: add1})
               prices.update({11: addp1})
               print(items)
               print(prices)
               add2=input("Want to add another item  \n enter number \n 1.Yes  2.No  ")
               if add2=="1":
                   add2=input("Enter item: ")
                   addp2=input("Add price of item ")
                   items.update({12: add2})
                   prices.update({12: addp2})
                   print(items)
                   print(prices)
                   add3=input("Want to add another item \n enter number \n 1.Yes  2.No   ")
                   if add3=="1":
                       add3=input("Enter item: ")
                       addp3=input("Add price of item ")
                       items.update({13: add3})
                       prices.update({13: addp3})
                       print(items)
                       print(prices)
                       print("*****Entered*****")
# ---------------------------------------------------------------------------------------------------------------------
        elif entr=='3':
             ri=input("Do you want to remove the item  \n  Yes    No  \nv   ")
             if ri=="Yes":
                 item_list()
                 print("Operation performed")
                 r=input("Enter item number:  ")
                 if r=="1":
                    f=open("C:\Grocery Store Management System\l1.txt","r")
                    print(f.read())
                    f.close()
                    print("Changes saved ")
                 elif r=="2":
                    f=open("C:\Grocery Store Management System\l2.txt","r")
                    print(f.read())
                    f.close()
                    print("changes saved ")
                 elif r=="3":
                    f=open("C:\Grocery Store Management System\l3.txt","r")
                    print(f.read())
                    f.close()
                    print("changes saved ") 
                 elif r=="4":
                    f=open("C:\Grocery Store Management System\l4.txt","r")
                    print(f.read())
                    f.close()
                    print("changes saved ") 
                 elif r=="5":
                    f=open("C:\Grocery Store Management System\l5.txt","r")
                    print(f.read())
                    f.close()
                    print("changes saved ") 
                 elif r=="6":
                    f=open("C:\Grocery Store Management System\l6.txt","r")
                    print(f.read())
                    f.close()
                    print("changes saved ")
                 elif r=="7":
                    f=open("C:\Grocery Store Management System\l7.txt","r")
                    print(f.read())
                    f.close()
                    print("changes saved ") 
                 elif r=="8":
                    f=open("C:\Grocery Store Management System\l8.txt","r")
                    print(f.read())
                    f.close()
                    print("changes saved ") 
                 elif r=="9":
                    f=open("C:\Grocery Store Management System\l9.txt","r")
                    print(f.read())
                    f.close()
                    print("changes saved ") 
                 elif r=="10":
                    f=open("C:\GroceryStore Management System\l10.txt","r")
                    print(f.read())
                    f.close()
                    print("CHANGES SAVED  ")
# ----------------------------------------------------------------------------------------------------------------------- 
        elif entr=="4":
                 inc=input("  You want to change the quantity of items    ")
                 if inc=="Yes":
                      item_list()
                      q=input("Enter item no.  ")
                      qq= input("Enter quantity  ")
                      if q=="1":
                         qu.update({1: qq})
                         print(" quantity changed")
                         print(qu)
                      elif q=="2":
                          qu.update({2: qq})
                          print(" quantity changed")
                          print(qu)
                      elif q=="3":
                          qu.update({3: qq})
                          print(" quantity changed")
                          print(qu)
                      elif q=="4":
                          qu.update({4: qq})
                          print(" quantity changed")
                          print(qu)
                      elif q=="5":
                          qu.update({5: qq})
                          print(" quantity changed")
                          print(qu)
                      elif q=="6":
                          qu.update({6: qq})
                          print(" quantity changed")
                          print(qu)
                      elif q=="7":
                          qu.update({7: qq})
                          print(" quantity changed")
                          print(qu)
                      elif q=="8":
                          qu.update({8: qq})
                          print(" quantity changed")
                          print(qu)
                      elif q=="9":
                          qu.update({9: qq})
                          print(" quantity changed")
                          print(qu)
                      elif q=="10":
                          qu.update({10: qq})
                          print(" quantity changed")
                          print(qu)
                 if inc=="No":
                       print(" Systemm Closed  ")      
        else: 
                 print("  MANAGEMNENT HANDLED     ")
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
# CASHIER PART 
elif login=="2":
   cashier()             
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# CUSTOMER PART
elif login=="3":
    print("       Welcome to Glossary Store Customer Service App         ")
    logcus=input(" Which type of Service you Want \n  (1)CREATE ACCOUNT \n  (2)LOGIN     ")
    if logcus=="1":
        name=input("Enter your name  ")
        ph_no=input("Enter your phone number  ")
        
        print(" A verification code sent to you on this ph number  \n  please wait....     ")
        print(" code=8753 ")
        pin=int(input("Enter verification code:  "))
        if pin==8753: 
          print("  Processing Data ......  ")
          print(" *****VERIFIED**** ")
          file()
          calcuation()
        else:
            print(" unvalid password ")             
     #----------------------------------------------------------------------------------------------       
    if logcus=="2":
       name=input("Enter name ")
       password=input("Enter password  ")
       print("  Account Accessed   ")
       seiitems={"Bread","Rice","Soap","Sugar","Tea","Snacks","Milk","Eggs","Oil","Flour"}
       search=input("    Search Item:  ")
       seei=search in seiitems
       print(search,seei)
       print(" \n    DO YOU WANT TO BUY SOMETHING: ")
       buy=input("    1.YES     2.NO   \n")
       if buy=="1":
            file()
            calcuation()
       else: 
           print("    ...GOOD BYE...   ")
           

