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