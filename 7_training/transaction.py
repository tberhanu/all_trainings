class Account():
    max_withdrawal = 2000

    def __init__(self, curr_dep):

        self.curr_dep = curr_dep

    def deposit(self, amt):
        self.curr_dep = self.curr_dep + amt

    def withdraw(self, amt):
        if amt > 2000:
            print("Amount exceed the limit")
        else:
            self.curr_dep = self.curr_dep - amt

class ATM(Account):

    def __init__(self, username, password, curr_dep):
        super().__init__(curr_dep)
        self.username = username
        self.password = password

    def authenticate(self, username, password):

        return True

class Main():
    atm  = ATM("username", "password", 5200)
    atm.deposit(111)
    print(atm.curr_dep)
    atm.withdraw(6300)
    print(atm.curr_dep)


