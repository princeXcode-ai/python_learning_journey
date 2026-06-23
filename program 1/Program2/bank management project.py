import json
import random
import string
from pathlib import Path


class bank:
    database= 'data.json'
    data=[]
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
                
        else:
            print("no such file exist")
            
    except Exception as err:
        print(f"an exception is form of {err}")   

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(bank.data))
    
    @classmethod
    def __accountgenerate(cls):
        alpha =random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return"".join(id)
        

    
    def createaccount(self):
        info ={
            "name": input("tell your name:- "),
            "age" : int(input("tell your age:- ")),
            "email": input("tell your email:- "),
            "pin": int(input("tell your pin:- ")),
            "accountno.": bank.__accountgenerate(),
            "balance": 0
        }
        if info['age']< 18 or len(str(info['pin'])) !=  4:
            print("sorry you can't create your account")
            
        else:
            print("account has been created successfully")
            for i in info:
                print(f"[{i} : {info[i]}]")
            print("please note down your account number")
            
            bank.data.append(info)
            bank.__update()
    
    def depositemoney(self):
        accnumber= input("please tell your account no:- ")
        pin =int(input("please tell your pin as well as:- "))
        
        userdata =[i for i in  bank.data if i ['accountno.']== accnumber and i['pin']== pin]
        
        if userdata == False:
            print("soory no data found")
            
        else:
            amount = int(input("how much you want to deposite:- "))
            if amount > 10000 or amount < 0:
                print ("sorry the amount is too much you can deposite below 10000 and above 0")
            
            else:
                userdata[0]['balance'] += amount
                bank.__update()
                print("Amount deposited successfully")
                
                
                
    def withdrawmoney(self):
        accnumber= input("please tell your account no:- ")
        pin =int(input("please tell your pin as well as:- "))
        
        userdata =[i for i in  bank.data if i ['accountno.']== accnumber and i['pin']== pin]
        
        if userdata == False:
            print("soory no data found")
            
        else:
            amount = int(input("how much you want to withdraw:- "))
            if userdata[0]['balance'] < amount:
                print("sorry you don't have that much money")
                
            
            else:
                userdata[0]['balance'] -= amount
                bank.__update()
                print("Amount withdrew successfully")
                
                
    def showdetails(self):
        accnumber= input("please tell your account no:- ")
        pin =int(input("please tell your pin as well as:- "))
        
        userdata =[i for i in  bank.data if i ['accountno.']== accnumber and i['pin']== pin]
        print("Your information are :- \n\n\n")
        
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")
        

    def updatedetails(self):
        accnumber= input("please tell your account no:- ")
        pin =int(input("please tell your pin as well as:- "))
        
        userdata =[i for i in  bank.data if i ['accountno.']== accnumber and i['pin']== pin]
        
        if userdata== False:
            print("no such data found")
            
        else:
            print("You cannot change the age ,account no and balance")
            
            print ("Fill the details for change or leave it empty if no change")
            
            newdata = {
                "name" : input("please tell new name or press enter:"),
                "email" : input("please tell your new email or press enter to skip :"),
                "pin" : input ("enter new pin or press enter to skip: ")
            }
            
            if newdata["name"] =="":
                newdata ["name"] = userdata[0]['name']
                
            if newdata["email"] =="":
                newdata ["email"] = userdata[0]['email']
                
            if newdata["pin"] =="":
                newdata ["pin"] = userdata[0]['pin']
                
            
            newdata['age'] = userdata[0]['age']
            
            newdata['accountno.'] = userdata[0]['accountno.']
            newdata['balance'] = userdata[0]['balance']
            
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
                
                
            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
                    
            bank.__update()
            print("datials successfully")
                
    def delete(self):
        accnumber= input("please tell your account no:- ")
        pin =int(input("please tell your pin as well as:- "))
        
        userdata =[i for i in  bank.data if i ['accountno.']== accnumber and i['pin']== pin]
        
        if userdata == False:
            print("sorry no such data exist")
            
        else :
            check = input("press y for deleting your account or press x:- ")
               
            
        
                
                
                
    
user=bank()
print("press 1 for creating an account")
print("press 2 for deposititing the money in bank")
print("press 3 for withdrawing the money")
print("press 4 for detials")
print("press 5 for upadatingthe details")
print("press 6 for deleting your bank account")

check=int(input("tell your response :- "))

if check == 1:
    user.createaccount()
    
if check ==2:
    user.depositemoney()
    
if check == 3:
    user.withdrawmoney()
    
if check == 4:
    user.showdetails()
    
if check == 5:
    user.updatedetails()
    
if check ==6:
    user.delete()