class Atm():
    def __init__(self, PIN):
        self.PIN = PIN
        self.uinput = input("Enter your PIN number: ")
        
        if(self.uinput != self.PIN):
            print("Incorrect Pin")

        else:
            uinput2 = self.uinput2 = input("Enter Your Bank Balance: ")
            print(uinput2)
            print(input("Enter Amount To Withdraw: "))
            print("Money Withdrawn Successfully!")

atm = Atm("1234")
