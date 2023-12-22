def add(a,b):
    return a + b
def sub(a,b):
    return a -b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a/b

def calculator():
    print("1. add")
    print("2. sub")
    print("3. multiply")
    print("4. divide")
    choice = input("(enter a number from 1 to 4): ")
    num1= int(input("enter the first number: " ))
    num2= int(input("enter the second number: "))
    if choice == "1":
        result = add(num1,num2)
        print("answer", result)
    if choice == "2" :
        result = sub(num1, num2)
        print("answer", result)
    if choice == "3" :
        result = multiply(num1, num2)
        print("answer", result)
    if choice == "4" :
        result= divide(num1,num2)
        print("answer", result)
    else:
        return "not valid"
    
calculator()    
   
    
    
    
    
