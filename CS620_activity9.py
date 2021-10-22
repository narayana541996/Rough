import pandas as pd
# Activity 9- Submitted by Lakshmi Narayana Podagatlapalli
import pandas as pd
from seaborn import violinplot

df = pd.DataFrame(pd.read_csv('https://www.cs.odu.edu/~sampath/courses/data/brfss.csv'))
df.drop('sex', axis = 1, inplace = True)
df.dropna(inplace = True)
print(df.head())
print(df['weight2'].describe())
print('25th percentile: ',df['age'].quantile(0.25),' 50th percentile: ',df['age'].quantile(),' 75th percentile: ',df['age'].quantile(0.75))
pl = violinplot(data = df)