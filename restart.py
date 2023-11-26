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
