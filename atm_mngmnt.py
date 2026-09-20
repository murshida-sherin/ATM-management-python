class Bank:
    bank_name="SBI"
    
    def __init__(self,acc_no,acc_holder):
        self.acc_no=acc_no
        self.acc_holder=acc_holder
        self.balance=1000
      
    def display(self):
        print(acc1.bank_name)
        print(f"Acconut number:{self.acc_no}")
        print(f"Acconut holder:{self.acc_holder}") 
         
    def balance_enquiry(self):
        print(f"Current balance={self.balance}")
        
    def deposit(self):
        amount=float(input("enter the amount to deposit:"))
        self.balance+=amount
        print(f"Current balance after deposit={self.balance}")
        
    def withdraw(self):
        withdraw=float(input("enter the amount to withdraw:"))
        if withdraw>self.balance:
            print("Insufficient balance!")
        else:
            self.balance-=withdraw
            print(f"Current balance after withdraw={self.balance}")
  
                     
acc1=Bank("1234xxxxxxxx","Ajith")

print("1-Show details\n2-Balance Enquiry\n3-Deposit\n4-Withdraw money")

while True:
    print("==============================")
    choice=int(input("Enter your choice:"))
    if choice==1:
        acc1.display()
    elif choice==2:
        acc1.balance_enquiry()
    elif choice==3:
        acc1.deposit()
    elif choice==4:
        acc1.withdraw()
    elif choice==5:
        print("ThankYou for using this ATM!!")
        break
    else:
        print("Invalid choice!!")
        break 
print("bye")
