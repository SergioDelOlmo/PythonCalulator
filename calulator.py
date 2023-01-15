operation = 0

class Operation:
    def __init__(self, a):
        self.a = a
    
    @classmethod
    def addition(self):
        sum1 = float(input("Enter the first number to sum "))
        sum2 = float(input("Enter the second one "))
        print("The sum is ", sum1 + sum2)
    
    @classmethod
    def option(self):
        stay = int(input("""What would you like to do next: 
            0 : main menu
            1 : repeat operation\n"""))
        return stay


print("WELCOME TO THE CALCULATOR")

while operation < 10:
    operation = int(input("""Select the option to execute:
    0 : main menu
    1 : addition
    2 : subtraction
    3 : multiplication
    4 : division
    5 : root
    6 : power
    7 : sin
    8 : cos
    9 : tan
    10 : exit \n"""))
    
    #Switch to handle the operation
    match operation:
        case 0 :
            operation = 0
        case 1:
            while operation > 0:
                print("You selected addition")
                Operation.addition()
                operation = Operation.option()
        case _:
            print("You selected operation: ", operation)



