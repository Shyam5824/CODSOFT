print("\t\tCALCULATOR")
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if(y==0):
        return "Error!Division by zero"
    else:
        return x/y
print("Select operation:\n 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n")
choice=input("Enter choice(1/2/3/4):")
x=float(input("Enter first number:"))
y=float(input("Enter first number:"))
if(choice=='1'):
    print(x,"+",y,"=",add(x,y))
elif(choice=='2'):
    print(x,"-",y,"=",subtract(x,y))
elif(choice=='3'):
    print(x,"*",y,"=",multiply(x,y))
elif(choice=='4'):
    print(x,"/",y,"=",divide(x,y))
else:
    print("Invalid input")



