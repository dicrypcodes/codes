x = "my name is daniel"
y = " left coding for a little while"
z = " but i am back and stronger now!"
print(x + y + z)


def classifier(identify):
    return lambda age : identify + age

description = classifier("my name is ")
print(description("19"))
 