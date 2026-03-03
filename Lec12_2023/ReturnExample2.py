def heightCalculator(v0):
    #v0 = 5
    g = 9.81
    t = 0.6
    y = v0*t-0.5*g*t**2
    print(y)
    return y, g, t

v0 = 5
values = heightCalculator(v0)
print(values[0])
print(values[1])
print(values[2])

v0 = 6
values = heightCalculator(v0)
print(values[0])
print(values[1])
print(values[2])

v0 = 7
values = heightCalculator(v0)
print(values[0])
print(values[1])
print(values[2])

# Here, we're returning multiple values from the function as a tuple, to print individually and analyse.