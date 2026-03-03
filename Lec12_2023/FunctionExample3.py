def heightCalculator(v0):
    #v0 = 5
    g = 9.81
    t = 0.6
    y = v0*t-0.5*g*t**2
    print(y)
    return y

v0 = 5
y = heightCalculator(v0)
print(y)

v0 = 6
y = heightCalculator(v0)
print(y)

v0 = 7
y = heightCalculator(v0)
print(y)

# If we remove v0 initialisation within the function, we can pass the value of v0 into the function as a parameter.