#Activity 5 - submitted by Lakshmi Narayana Podagatlapalli(UIN: 01087265)
import pandas as pd
import random
import numpy as np

RandomNumbers = pd.Series([random.randint(0,50) for i in range(10)])
RandomNumbers.index.name = 'idx'
RandomNumbers.name = 'Random Numbers'
print(RandomNumbers)
sqrs = np.square(RandomNumbers)
print('\n\nsquares:\n',sqrs)
print('\n\nodd indices of squares:\n',sqrs[RandomNumbers.index % 2 == 1])
print('\n\nnumbers <400 (without index):\n',sqrs[sqrs < 400].values)
print('\n\nnumbers <400 (without index) converted to a list:\n', list(sqrs[sqrs < 400]))