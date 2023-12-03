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

#the value of the global can be changed inside the function by refering to the variable using the glboal keyword
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)


#Phyton Data Types: here are the data types in python
#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType

#the type() function is use to get the type of a data
x = ("egg", "bread", "butter")#here is an example of a list
print(x)
print(type(x))#used the type function to get the type of data it was

#we can set a data type to what we want it to be: meaning a tuple can be made to be a list and vice versa. same thing applied for the rest of the data types
wants = ["garri", "groundnut", "indomie"]#here is a list
wants = tuple(wants)#here it's been turned to the tuple.
wants = tuple(["garri", "groundnut", "indomie"])# this and the above is same thing, it can be set to tuple by any of the two
print(wants)
print(type(wants))

#there are 3 numeric data types in python: int, float and complex
#int(integer): they are whole numbers and example include 5, -6, 4334 etc...
#float: Float can also be scientific numbers with an "e" to indicate the power of 10 
#example of float include: 35e3, 12E4, -87.7e100
#complex numbers: Complex numbers are written with a "j" as the imaginary part:
#example 3+5j, 5j, -5j
#a type can be converted form to another by using the function type
#e.g
count = 5#it is an interger here
c = float(count)#and it has been changed to a float here
print(c)
#note: you can't covert from complex num to any other number

#Random number: 
import random
print(random.randrange(1,10)) #a random num between 1 and 100 will be printed on every single trial.

import random
print(random.randrange(1,100)) # a radom num within 1 and 100 will be printed on every single trial

#casting in python basically mean converting from one data type to another, e.g from float to str, float to interger and many more
#strings
a = """i am boy and i don't even know
i school in fuoye
i stay in idofin
i have a landlord
"""#this is multiline string, and it can be printed
print(a) #printing multiline string
print(a[31]) # this will get the character at position number 31
print(a[51]) #this will get the character at position number 51

#Looping through a string 
history = "once upon a time"#declared a variable       
for x in history:# to loop through the variable, meaning to print every word in the variable
     print(x)#calling the loop

for x in "cassava":
     print(x)     
     
#Obataining the length of a string
names = "alias, fred, didier, samuel, wale"
print(len(names))
#how to check if a certain word or character in present is varible created
print("alias" in names)#checking if alias is in the variable names which should print True because it's preent in there
print("fred" in names)#checking if fred is in the variable names which should print True because it's present in there
print("Daniel" in names)#checking if Daniel is in the variable names which should print false because it's not present in there
#an if statement can also be used for same purpose, and you get assign a precise response you need it to deliver
if "alias" in names:#using an if statement to check 
     print("YES it is present!")#assigning the response i want it to give if "alias" is present
if "Mango" not in names:#using in the not in keyword to check if mango is present in names
     print("YES")   #printing YES if mango is not present in names
print("orange" not in names)#using the not in keyword without the if statement

#Slicing Strings: You can return a range of characters by using the slice syntax.
word = "A man can't be so careless to sit on his balls"
print(word[1:10])#the characters that will be returned is 1 to the 9th character
#note: first character starts from zero

#String Indexing: Use negative indexes to start the slice from the end of the string:
print(word[-8])
