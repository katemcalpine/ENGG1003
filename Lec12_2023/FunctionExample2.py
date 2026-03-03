
def heightCalculator():
    v0 = 5
    g = 9.81
    t = 0.6
    y = v0*t-0.5*g*t**2
    print(y)
    return y

v0 = 6
y = heightCalculator()
print(y)

v0 = 7
y = heightCalculator()
print(y)

# Why doesn't this work?
# How can we fix it?

# v0 is overwritten with a new value within the function.