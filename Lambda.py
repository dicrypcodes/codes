x = lambda y,z,a : y + z + a
print(x(100, 20, 10))


y = lambda f,g,h : f+g*h
print(y(3,2,4))

def four_times(m):
    return lambda v : v * m

fourth = four_times(3)
third = four_times(2)
print(fourth(2))
print(third(2))


G = lambda g,h : g * h
print(G(2,3))

def lam(y):
    return lambda b: b * y
small = lam(4)
print(small(6))


def myfunc(n):
    return lambda b: b + n
    
intro = myfunc("James")
print(intro(" Mr"))


"""def modifyUser(user):
    return lambda title: title + user


modifier = modifyUser("James")

print(modifier("Mr "))"""


def myname():
    intro = "my name is Daniel"
    print(intro)
myname()   


def foo():
    return "food"

def baz():
    return foo


print(baz()())


def company(name):
    profile = "Mr " + name
    return profile
user = company("Abdul")
def trial():
    #global user
    print(user)
trial()    




x = "A white one"
def new():
    x = "a red one"
    description = "The ball is " + x
    print(description)
new()
print(x)



def classifier(identify):
    return lambda age : identify + age

description = classifier("my name is Daniel i am ")
print(description("19"))
 