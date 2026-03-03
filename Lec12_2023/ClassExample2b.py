from ClassExample2a import Circle

Circle1 = Circle()
# For other languages, we declare 'radius' within the Class,
# so we can update the value of the copy here.
Circle.radius = 3

y = Circle1.circumference()
print(y)
y = Circle1.area()
print(y)

Circle2 = Circle()
Circle.radius = 4

y = Circle2.circumference()
print(y)
y = Circle2.area()
print(y)

