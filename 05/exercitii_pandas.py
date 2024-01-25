import pandas as pd
import numpy as np

# lista = [10, 20, 30, 40, 50]

# series = pd.Series(lista)

# print(series)

# array_date = np.array([10, 20, 30, 40, 50])
#
# series = pd.Series(array_date)
# print(series)

# dict_date = {
#     "a": 10,
#     "b": 20,
#     "c": 30,
#     "d": 40,
#     "e": 50
# }
#
# series = pd.Series(dict_date)
# print(series)

data = {
    'nume': ['nume1', 'nume2', 'nume3'],
    'randomInfo': ['randomInfo1', 'randomInfo2', 'randomInfo3']
}

df = pd.DataFrame(data)
# df.set_index('nume', inplace = True)
# print(df.loc['nume1'])

df.to_csv('new.csv')