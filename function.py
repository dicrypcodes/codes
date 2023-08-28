def name_list(*names):
    print("my name is" + names[1])
name_list(" Dan", " Bush", " Denjeloux")    

def my_function(child3, child2, child1):
  print("The youngest child is " + child1)
  print("The laziest child is " + child3)
  print("The smartest of his child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function(**kid):
  print("His last name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_country(country = "Nigeria"):
   print("I am from " + country)
my_country("Ghana")
my_country("Maldevis")
my_country() 
my_country("Japan")  


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def my_foods(fruits):
   for x in fruits:
      print(x)
fruits = {"japan": "apple", "Nigeria": "Orange", "US": "mushroom"}
my_foods(fruits)


def my_math(x):
   if x < 10:
      return x * 5
   elif x >= 10:
      return x + 5
print(my_math(15))  
print(my_math(14)) 
print(my_math(13))
print(my_math(9))
print(my_math(8))

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

   
