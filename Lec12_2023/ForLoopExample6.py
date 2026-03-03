import numpy as np

a = np.array([1, 2, 3])

# Use a counter to navigate indexes
counter = 0

for i in a:
    if i == 1:
        a[counter] *= 2
    elif i == 2:
        a[counter] += 4
    else:
        a[counter] += a[counter-1]

    counter += 1

    print(i)
print(a)

# Why does printing i look different to printing a?

