#first lineo of code after restarting python from scratch
print("Hello, world!")

#python identation
if 8>2:
     print("Eight is greater than two!")#the amount of space for indention is left for the programmer to decide
     print("Eight")#you have to use the same space of indentation for the same block of code

#python variables
#variables are created when a value is assigned to it. the equals to sign is use to assign value
x = 5
y = "Hello world!"
print(x)
print(y)

#python comment
#commenting is used for incode documentations, it is started with a # and python will render it a comment
#python does not really have syntax for a multiline comment, you can add # at the begining of every line
#instead of a multiline comment, you can use a multiline string  in place of that, which is triplet quotation marks


#Python Variables
#a variable is created once a value is assigned to it
name = "Malik"
course = "computer science"
print(name)
print(course)
#Variables do not need to be declared with any particular type, and can even change type after they have been set.
Name = "shade"
Name = 5 #the variable have being changed to 5 and it was intially "shade"
print(Name)

#Casting: if a data type is to specified, it can be done by casting
number = str(5) #this will be printed as "5"
digit = float(5) #this will be printed as 5.0
figure = int(5) #this will be printed as 5

#to get the type of a variable the type() is used
number = 5
print(type(name))

#note: a string variable can be declared using a single or double quotation mark
#note: python  is case sensitive meaning a and A are not same thing
#note: python varibles
#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#A variable name cannot be any of the Python keywords

#Multiword variable name
#Camel case: every word except the first start with a capital letter e.g myVariableName
#pascal case: every word start with a capital e.g MyVariableName
#snake case: every word is separated is separted with an underscore e.g my_variable_name

#Assigning many value to mutliple variable
landlord, house, owner = "my landlord", "is the house", "owner"
print(landlord, house, owner )
print(landlord)
print(house)
#makw sure the number of variable matches the number of the values assigned

#Adding a value to multiple varible
go=out=get=it= "done"
print(go)
print(out)
print(get)
print(it)

#Unpacking a Collection
fruits= ["mango ", "apple ", "cherry"]
x,y,z=fruits
print(x,y,z)#the print() can be use to output many variables at the same time, just separate with a comma
#the plus operator can be use to output multiple variable 
print( x + y + z)
#the plus operator can be use to perfom mathematical operations too
boys = 10
girls = 22
print(boys + girls)# if you use the + operator to combine a string and an integer, it won't work, but a comma can be used to output different data types


#Global Variables: they are variables created outside a function, all example of variable above is a global variable
#global variables can be created by anyone and can be used inside and outside the function
#note: a fucntion is declared like this "def" then the function name with a bracker in front and a semicolon afterwards
# example: 
clothe = "versace"# i created this global variable so as to use it inside the function
def myfunction(): #this is the function created
     print("my clothe is " + clothe )
myfunction()    

gadget = "laptop"
def mygadgets():
     gadget = "phone"
     print("the " + gadget + " belong to me")
mygadgets()
print("the " + gadget + " belong to me")

#Global Keyboard: Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.
#If you use the global keyword, the variable belongs to the global scope

def newvariable():
     global insert 
     insert = "USB"
     print("input the " + insert)
newvariable()
print("the " + insert + " is in my hand")#when the global keyword is used, the varible can be use both inside the function and outside the function

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

