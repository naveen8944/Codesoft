def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a/b
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Number can't be divided by Zero")
def percent(a,b):
    try:
        return a%b
    except ZeroDivisionError:
        print("Number can't Be zero!"+"change the value of the right operand.")
print("Enter any operations\n"\
      "1.Addition\n"\
      "2.Substraction\n"\
       "3.Multiplication\n"\
       "4.Division\n"\
        "5.Percentage\n") 
option = int(input("Select any operations form 1,2,3,4,5:"))
a1 = int(input("Enter any number:"))
b1 = int(input("Enter any second number:"))
if option==1:
    print(a1,"+",b1,"=",add(a1,b1))
elif option==2:
    print(a1,"-",b1,"=",sub(a1,b1))
elif option==3:
    print(a1,"*",b1,"=",multiply(a1,b1))
elif option==4:
    print(a1,"/",b1,"=",divide(a1,b1))
elif option==5:
    print(a1,"%",b1,"=",percent(a1,b1))
else:
    print("Invalid input")