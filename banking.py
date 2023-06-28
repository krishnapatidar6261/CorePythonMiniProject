def Banker():
    print("*"*50)
    print("Welcome to Banker's App")    
    print("*"*50)
    
    while True:
            print("Operation Menu: ")
            print("        1) Add Customer")
            print("        2) View Customer")
            print("        3) Search Customer")
            print("        4) Total Ammount in Bank")
            print("        5) Exit")

            Bchoose=int(input("Enter Choice: "))

            if Bchoose==1:
                
                acL=[]
                while True:        
                        acN=int(input("Enter Account Number: "))
                        if acN not in acL:
                            acL.append(acN)
                            break
                        else:
                            print("Account Number is Already Exist Please Choose another Account Number")
                            
                
            elif Bchoose==2:

                with open("Cus.txt","r") as f:
                    
                    ac=int(input("Enter Account Number: "))
                    dic=eval(f.read())
                    print(dic.get(ac))
                    
            elif Bchoose==3:
                search=int(input("Enter Account Number For Search: "))
                
                with open("Cus.txt","r") as f:
                   dic=eval(f.read())
                   
                   print("Account Number: ",search,"is found deatial is: ",dic.get(search))
            
            elif Bchoose==4:
                with open("Cus.txt","r") as f:
                    dic=eval(f.read())
                    l=[]
                    
                    for i in dic:
                        l.append(dic[i]["Balance"])
                    
                    total=0
                    for i in l:
                        total+=i
                    print("Bank Total Balane is: ",total)
                    
            elif Bchoose==5:
                break
            else:
                print("Invalid Choice")
                

def customerr():
    print("WElcome to Customer's App")
    print("Operation Menu:") 
    print("            1) Withdraw Ammount")                 
    print("            2) Deposite Ammount")                 
    print("            3)View Balance")  
    
    Cchoice=int(input("Enter Choice: "))
    
    if Cchoice==1:
        with open("Cus.txt","r")as f:
            dic=eval(f.read())
            l=[]
            for i in dic:
                l.append(i)
                
            ac=int(input("Enter Your account number for withdraw: "))
            
            if ac in l:
                withdraw=int(input("Enter Ammount to Withdraw: "))
                totalBal=dic[ac]["Balance"]
                if withdraw<=totalBal:
                    totalBal-=withdraw
                    print("Now your total Ammount is: ",totalBal)
                else:
                    print("Withdraw Ammount is greater than total Ammount")
            else:
                print("Account Not Found")
        with open("Cus.txt","w")as f:
                f.write(str(dic))
                
                
            
    elif Cchoice==2:
        with open("Cus.txt","r")as f:
            dic=eval(f.read())
            l=[]
            for i in dic:
                l.append(i)
                
            ac=int(input("Enter Your account number for Diposite: "))
            
            if ac in l:
                withdraw=int(input("Enter Ammount to Diposite: "))
                totalBal=dic[ac]["Balance"]
                
                totalBal+=withdraw
                print("Now your total Ammount is: ",totalBal)
                
            else:
                print("Account Not Found")
                
        with open("Cus.txt","w")as f:
                f.write(str(dic))
        
    elif Cchoice==3:
         with open("Cus.txt","r")as f:
            dic=eval(f.read())
            l=[]
            for i in dic:
                l.append(i)
                
                        
            if ac in l:
                
                totalBal=dic[ac]["Balance"]
                print("Now your total Ammount is: ",totalBal)
                
            else:
                print("Account Not Found")
    else:
        print("Invalid Choice")
        
print("*"*50)
print("Welcome to Python Bnak Mnagement System")
print("*"*50)

print("Select Your Role")
print("1) Banker")
print("2) Customer")
print("3) Exit")

print("*"*50)

choose=int(input("Choose your Role: "))

if choose==1:
    Banker()
    
elif choose==2:
    customerr()

else:
    print("Invalid Choice")