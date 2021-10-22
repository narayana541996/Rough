#activity 7 - submitted by Lakshmi Narayana Podagatlapalli(UIN: 01087265)
#Activity 7 - submitted by Lakshmi Narayana Podagatlapalli(UIN: 01087265)
import numpy as np
import pandas as pd

arr = np.random.randint(1, 100,(3,5))
print('array:\n',arr)
df = pd.DataFrame(arr, index = ['a', 'b', 'c'])
print('\n\ndataframe:\n',df)
tdf = df.transpose()
tdf[tdf < 40] = 0
print('\n\nTransposed dataframe with values less than 40 set to 0:\n',tdf)