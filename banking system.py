
class acount:
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no

    def dabit(self,amount):
        self.balance -= amount
        print("Rs", amount, "was dabited")
        print("balance is",self.get_bal())

    def credited(self,amount):
            self.balance += amount
            print("Rs", amount, "was cradited")
            print("balance is",self.get_bal())

    def get_bal(self):
         return self.balance

acc1 = acount(10000, 12345)
acc1.dabit(500)
acc1.credited(1000)
     