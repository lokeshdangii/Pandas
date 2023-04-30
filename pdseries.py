import pandas as pd
import numpy as np

# creating empty series
ser = pd.Series()

print("Series : ",ser)

data = np.array(['l','o','k','e','s','h'])
# print("Data of array :", data)


ser = pd.Series(data)
# print("Series after passing data : ",ser)
print(ser)