import numpy as np

a = np.array([1, 2, 3])

for i in a:
    if i == 1:
        i *= 2
    elif i == 2:
        i += 4
    else:
        i += i-1

    print(i)
print(a)

# Why does printing i look different to printing a?




