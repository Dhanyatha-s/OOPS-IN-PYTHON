class Account:
    def __init__(self, balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("total balance:", self.get_balance())

    def credit(self, amount):
        self.balance +=amount
        print("Rs", amount, "was Credited")
        print("total balance:", self.get_balance())


    def get_balance(self):
        return self.balance

acc1 = Account(10000,123456)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(140000)
acc1.debit(10000)
