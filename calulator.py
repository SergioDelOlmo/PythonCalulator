import numpy as np
factors = np.zeros(2) #[0,0]
operation = 0

class Operation:
    def __init__(self, a):
        self.a = a
    
    @classmethod
    def addition(self):
        factors[0] = float(input("Enter the first number to sum: "))
        factors[1] = float(input("Enter the second one: "))
        print("The sum is: ", np.sum(factors))
    
    @classmethod
    def subtraction(self):
        factors[0] = float(input("Enter the minuend: "))
        factors[1] = float(input("Enter the subtrahend: "))
        print("The subtraction equals to: ", factors[0]-factors[1])

    @classmethod
    def multiplication(self):
        factors[0] = float(input("Enter the first factor: "))
        factors[1] = float(input("Enter the second factor: "))
        print("The product equals to: ", np.prod(factors))
    
    @classmethod
    def division(self):
        factors[0] = float(input("Enter the numerator: "))
        factors[1] = float(input("Enter the denominator: "))
        print("The division equals to: ", factors[0]/factors[1])
    
    @classmethod
    def root(self):
        factors[0] = float(input("Enter the base: "))
        factors[1] = float(input("Enter the root: "))
        print("The root equals to: ", factors[0]**(1/factors[1]))
    
    @classmethod
    def power(self):
        factors[0] = float(input("Enter the base: "))
        factors[1] = float(input("Enter the exponent: "))
        print("The result equals to: ", factors[0]**(factors[1]))
    
    @classmethod
    def sin(self):
        factors[0] = float(input("Enter the argument (x): "))
        print("The sin(x) equals to: ", np.sin(factors[0]))
    
    @classmethod
    def cos(self):
        factors[0] = float(input("Enter the argument (x): "))
        print("The cos(x) equals to: ", np.cos(factors[0]))
    
    @classmethod
    def tan(self):
        factors[0] = float(input("Enter the argument (x): "))
        print("The tan(x) equals to: ", np.sin(factors[0])/np.cos(factors[0]))
    
    @classmethod
    def option(self):
        stay = int(input("""What would you like to do next? 
            0 : main menu
            1 : repeat operation\n"""))
        return stay

print("WELCOME TO THE CALCULATOR!")

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
                print("You selected addition.")
                Operation.addition()
                operation = Operation.option()
        case 2:
            print("You selected subtraction")
            while operation > 0:
                Operation.subtraction()
                operation = Operation.option()
        case 3:
            print("You selected multiplication")
            while operation > 0:
                Operation.multiplication()
                operation = Operation.option()
        case 4:
            print("You selected division")
            while operation > 0:
                Operation.division()
                operation = Operation.option()
        case 5:
            print("You selected root")
            while operation > 0:
                Operation.root()
                operation = Operation.option()
        case 6:
            print("You selected power")
            while operation > 0:
                Operation.power()
                operation = Operation.option()
        case 7:
            print("You selected sin(x)")
            while operation > 0:
                Operation.sin()
                operation = Operation.option()
        case 8:
            print("You selected cos(x)")
            while operation > 0:
                Operation.cos()
                operation = Operation.option()
        case 9:
            print("You selected tan(x)")
            while operation > 0:
                Operation.tan()
                operation = Operation.option()
        case _:
            print("You selected operation: ", operation)



