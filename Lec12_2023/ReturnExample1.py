def heightCalculator(v0):
    #v0 = 5
    g = 9.81
    t = 0.6
    y = v0*t-0.5*g*t**2
    print(y)
    return y, g, t

v0 = 5
y, g, t = heightCalculator(v0)
print(y)
print(g)
print(t)

v0 = 6
y, g, t = heightCalculator(v0)
print(y)
print(g)
print(t)

v0 = 7
y, g, t = heightCalculator(v0)
print(y)
print(g)
print(t)

# Here, we're returning multiple values from the function as individual variables, to print individually and analyse.