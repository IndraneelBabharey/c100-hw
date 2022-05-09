class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
     
    def check_balance(self):
        print("Your balance is : 100$")
    
    def cashwidthdrawal(self,amount):
        new_amount = 100 - amount
        print("You have withdrawn " + str(amount) + ". Your remaining balance is "+ str(new_amount))

def main():
    name = input("hello what is your name")
    print("hello, " + name)
    cardnumber = input("Insert your card number:- ")
    pin = input("Enter your pin number:- ")
    new_user =  Atm(cardnumber,pin)

    print("Choose your activity ")
    print("1) Balance Inquriy ")
    print("2) Withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("Enter the amount: "))
        new_user.withdrawl3(amount)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()