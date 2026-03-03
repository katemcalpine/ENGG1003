import numpy as np
import pandas as pd

v0 = 5
g = 9.81

# Initialise arrays. Multidimentional arrays also work.
t = np.linspace(0, 1, 1001)
y = v0*t-0.5*g*t**2

# Turn arrays into Pandas DataFrame
time_dataframe = pd.DataFrame({'Time': t})
height_dataframe = pd.DataFrame({'Height': y})

# Concatenate DataFrames. axis=1 stacks vertically, axis=0 stacks horizontally
data = pd.concat([time_dataframe, height_dataframe], axis=1)

# Export to CSV. Remove indexing and set column titles (headers).
data.to_csv(r'C:\Users\Student\Desktop\ENGG1003\CSVOutputExample.csv', index=False, header=True)