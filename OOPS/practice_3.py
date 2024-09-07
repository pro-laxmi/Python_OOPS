class bank:
    def __init__(self,bal,acc) -> None:
        self.balance=bal
        self.account=acc
    def debit(self,amount):
        self.balance-=amount
        print(amount,"debited succesfully.")
        print("Total balance =",self.balance)
    def credit(self,amount):
        self.balance+=amount
        print(amount,"credited succesfully.")
        print("Total balance =",self.balance)
    def get_balance(self):
        return self.balance
balance=int(input("Enter ur balance:"))
account=int(input("Enter ur account number:"))
acc1=bank(balance,account)
method=input("Do you wanna credit/debiit:")
if method=="credit":
    amount=int(input("Enter amount to be credited:"))
    acc1.credit(amount)
elif method=="debit":
    amount=int(input("Enter amount to be debited:"))
    acc1.debit(amount)
else:
    print("OOPS!There is a typo...")