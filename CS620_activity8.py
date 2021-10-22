#Activity 8 - submitted by Lakshmi Narayana Podagatlapalli(UIN: 01087265)
import math
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 100, (3,5)))
print('dataframe:\n',df)
dfsq = df.applymap(lambda x:math.sqrt(x))
print('\n\nsquare-root of each dataframe element:\n', dfsq)
print('\n\nsummation of each row:\n',dfsq.sum(axis = 1))