import pandas as pd

# Read in CSV
data = pd.read_csv(r'C:\Users\Student\Desktop\ENGG1003\CSVOutputExample.csv')

# Isolate columns of data by referring to their column headings
y = data['Height'].values
t = data['Time'].values


