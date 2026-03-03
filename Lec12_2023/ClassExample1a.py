import numpy as np

class Circle:
    def __init__(self, r):
        self.radius = r

    def circumference(self):
        C = 2 * np.pi * self.radius
        return C

    def area(self):
        A = np.pi * self.radius**2
        return A


# Keep in mind that for other languages, the Class
# name may need to be the same as the filename.



