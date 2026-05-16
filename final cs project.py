print("----------------------------------------------")
print("\t Bank Management System")
print("----------------------------------------------")

import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="1234")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists bank2")
mycursor.execute("use bank2")
mycursor.execute("create table if not exists login"
                 "(admin varchar(25) not null,password varchar(25) not null)")
mycursor.execute("create table if not exists bank_master(acc_no int not null, name varchar(25) not null,"
                 "city varchar(25) not null, pin int not null,balance int not null)")
mycursor.execute("create table if not exists sno(no int not null, temp int not null)")
mydb.commit()
j=0
mycursor.execute("select*from login")
for i in mycursor:
    j=1
if(j==0):
    mycursor.execute("insert into login values('admin','ng')")
    mydb.commit()
z=0
mycursor.execute("select*from sno")
for i in  mycursor:
    z=1
if(z==0):
    mycursor.execute("insert into sno values(0,0)")
    mydb.commit()


while True:
    print("1. Login")
    print("2. Exit")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        password=input("Enter password: ")
        mycursor.execute("select * from login")
        for i in mycursor:
            admin,passs=i
        if(password==passs):
            print("Successfully login.....")
            print("1.Create Account")
            print("2.Deposit Money")
            print("3.Withdraw Money")
            print("4.Display")
            print("5.Delete Account")
            print("6.Exit")
        
            ch2=int(input("Enter your choice: "))
            if(ch2==1):
                name=input("Enter your Name:")
                city=input("Enter your city: ")
                pin=int(input("Enter PIN:"))
                balance=0
                mycursor.execute("select * from sno")
                for i in mycursor:
                    no,temp=i
                no+=1
                mycursor.execute("insert into bank_master values('"+str(no)+"','"+name+"','"+city+"','"+str(pin)+"','"+str(balance)+"')")
                mydb.commit()
                print("Successfilly Done...")


            elif(ch2==2):
                account=int(input("Enter Account Number: "))
                amount=int(input("Enter Amount: "))
                mycursor.execute("select * from bank_master where acc_no='"+str(account)+"'")
                for i in mycursor:
                    acc,name,city,pin,balance=i
                balance=balance+amount
                mycursor.execute("update bank_master set balance='"+str(balance)+"' where acc_no='"+str(account)+"'")
                mydb.commit()
                print("Successfully Deposited...")


            elif(ch2==3):
                account=int(input("Enter account number: "))
                amount=int(input("Enter amount: "))
                mycursor.execute("select * from bank_master where acc_no='"+str(account)+"'")
                for i in mycursor:
                    acc,name,city,pin,balance=i
                balance=balance-amount
                if(balance<0):
                    print("Not Having Sufficient Amount")
                    continue
                mycursor.execute("update bank_master set balance='"+str(balance)+"' where acc_no='"+str(account)+"'")
                mydb.commit()
                print("Successfully Withdraws...")


            elif(ch2==4):
                account=int(input("Enter your account number: "))
                mycursor.execute("select * from bank_master where acc_no='"+str(account)+"'")
                for i in mycursor:
                    acc,name,city,pin,balance=i
                print(f"Account --> {acc}")
                print(f"Name --> {name}")
                print(f"City --> {city}")
                print(f"balance--> {balance}")


            elif(ch2==5):
                account=int(input("Enter Account Number To be Deleted "))
                mycursor.execute("delete from bank_master where acc_no='"+str(account)+"'")
                print("Account Terminated Successfully...")

            elif(ch2==6):
                break

        else:
            print("Wrong Password")
