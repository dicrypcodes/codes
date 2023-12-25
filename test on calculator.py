def addition(a,b):
    return a + b
def substraction(a,b):
    return b - a
def multiplication(a,b):
    return a * b
def division(a,b):
    return a/b

def calculator():
    print("Simple calculator")
    print("1. Add")
    print("2. Sub")
    print("3. Multiply")
    print("4. Divide")
    choice = input("1,2,3,4: ")
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))

    if choice == "1" :
        sum = addition(num1,num2)
        print(sum)
    if choice == "2" :
        sub = substraction(num2,num1)
        print(sub)
    if choice == "3" :
        multiply = multiplication(num1,num2)
        print(multiply)
    if choice == "4" :
        divide = division(num1,num2)
        print(divide)
    elif choice != 1 or 2 or 3 or 4 :
        print("invalid input")
calculator()        


        

