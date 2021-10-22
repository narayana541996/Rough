#Activity 11 - submitted by Lakshmi Narayana Podagatlapalli(01087265)
import pandas as pd

df = pd.DataFrame(pd.read_csv('https://www.cs.odu.edu/~sampath/courses/data/brfss.csv'))
print(df)
df.drop(columns = 'sex', axis = 1, inplace = True)
print(df)
redata = df.apply(lambda series: ((series - series.min())/ (series.min() - series.max())))
redata.boxplot()
print(redata)