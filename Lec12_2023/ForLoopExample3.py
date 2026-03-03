import numpy as np

a = np.array([1, 2, 3])

for i in range(len(a)):
    if a[i] == 1:
        a[i] *= 2
    elif a[i] == 2:
        a[i] += 4
    else:
        a[i] += a[i-1]
        # What if we change this line to a[i+1]?

print(a)