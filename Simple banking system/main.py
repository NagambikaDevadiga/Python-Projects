class Account:
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance

    def credit(self,amt):
        self.balance+=amt
        print(f"Your account credited with Rs.{amt}")
        self.get_balance()

    def debit(self,amt):
        self.balance-=amt
        print(f"Your account debited with Rs.{amt}")
        self.get_balance()

    def get_balance(self):
        print(f"The balance is: {self.balance}")


account1=Account("12345",10000)
credit_amt=int(input("Enter the amount you want to credit: "))
account1.credit(credit_amt)
debit_amt=int(input("Enter the amount you want to debit: "))
account1.debit(debit_amt)
        