class User:
    def __init__(self, name):
        self.username = name
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawl(self, amount):
        self.balance -= amount
        if self.balance < amount:
            print("Insufficient funds to make a withdrawl")
        return self

    def transfer_money(self, other_user, amount):
        if self.balance < amount:
            print("insifficient funds to make transfer")
        else:
            self.balance -= amount
            other_user.balance += amount

    def display_user_balance(self):
        print(f"Username: {self.username}, Balance: {self.balance}")



user1 = User("Ron")
user2 = User("Missy")
user3 = User("Jason")

user1.make_deposit(100).make_deposit(50).make_deposit(300).make_withdrawl(50)
user1.display_user_balance()
user2.make_deposit(600).make_deposit(100).make_withdrawl(50).make_withdrawl(50)
user2.display_user_balance()
user3.make_deposit(1000).make_withdrawl(20).make_withdrawl(200).make_withdrawl(50)
user3.display_user_balance()


user1.transfer_money(user3, 40)

user1.display_user_balance()
user3.display_user_balance()


