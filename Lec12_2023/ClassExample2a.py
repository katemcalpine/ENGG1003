import numpy as np

class Circle:
    # For other languages, we would have to
    # declare the variable 'radius' to be used here.

    def circumference(self):
        C = 2 * np.pi * self.radius
        return C

    def area(self):
        A = np.pi * self.radius**2
        return A


# Keep in mind that for other languages, the Class
# name may need to be the same as the filename.

