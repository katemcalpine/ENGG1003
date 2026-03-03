import random

# Generating a finite list of names
a = random.choices(['Leonardo', 'Michelangelo', 'Donatello', 'Raphael'] , k=4)

print(a)
print(type(a))

# The data type changes here
print(a[0])
print(type(a[0]))