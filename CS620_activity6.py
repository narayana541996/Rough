#Activity 6- submitted by Lakshmi Narayana Podagatlapalli(UIN: 01087265)
import pandas as pd

df = pd.read_csv('https://www.cs.odu.edu/~sampath/courses/data/values.csv')
print('Overall dataframe: ',df)
print('\n\nNote: Couldn\'t understand if all the numbers in the series are to be rounded or just the average and mean, so rounded both.\nAverage:\n',df['factor_1'].round(2).mean().round(2),'\nStandard Deviation:\n',df['factor_1'].round(2).std().round(2))
print('\n\nRow indexes 4, 2, 5 and columns factor_1 and price in that order using iloc:\n', df.iloc[[4,2,5]][['factor_1','price']])