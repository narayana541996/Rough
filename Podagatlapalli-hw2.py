# CS620
# HW2
# @author:Lakshmi Narayana Podagatlapalli (UIN: 01087265)
import pandas

####################################################################Exercise 1
print('Exercise 1 -\n\n')
url = 'https://www.cs.odu.edu/~sampath/courses/data/earthquakes.csv'
df = pandas.read_csv('https://www.cs.odu.edu/~sampath/courses/data/earthquakes.csv')
print('Read CSV data into df dataframe.')

#############################################################################Exercise 2
print('\n\nExercise 2 -\n\nShape: ',df.shape,'\n columns: ',df.columns,'\nSample of first five: ',df.head())

#############################################################################Exercise 3
print('\n\nExercise 3 -\n\nunique values: ',list(pandas.unique(df['alert'])))
#  Write a comment with other alert values available consulting the USGS API documentation for the alert field:

# Limit to events with a specific PAGER alert level. The allowed values are:
# alertlevel=green
# Limit to events with PAGER alert level "green".
# alertlevel=yellow
# Limit to events with PAGER alert level "yellow".
# alertlevel=orange
# Limit to events with PAGER alert level "orange".
# alertlevel=red
# Limit to events with PAGER alert level "red".

##########################################################################Exercise 4
print('\n\nExercise 4 -\n\n',df[['title', 'time']][100:106])

##########################################################################Exercise 5
mags = [col for col in df.columns if col.startswith('mag')]
for c in ['title', 'parsed_place', 'time']:
    mags.append(c)
short_df = df[mags]
print('\n\nExercise 5 - df with mag-columns, title, parsed_place, time\n\n\n',short_df)

###########################################################################Exercise 6
print('\n\nExercise 6 -\n\n\n', short_df[['parsed_place', 'mag']][short_df['mag'] > 6.0])

############################################################################Exercise 7
print('\n\nExercise 7 -\n\n\n', df[['parsed_place','mag']][(df.alert == 'red') & (df.tsunami == 1)])

############################################################################Exercise 8
print('\n\nExercise 8 - percentile:\n\n\n',df['mag'][(df.parsed_place == 'Japan') & (df.magType == 'mb')].quantile(q = 0.9))

##############################################################################Exercise 9
print('\n\nExercise 9 - Summary statistics:\n\n\n',df[df.parsed_place == 'California'].describe())

##############################################################################Exercise 10
df.insert(loc = len(df.columns), column = 'ring_of_fire', value = False)
for place in ['Bolivia', 'Chile', 'Ecuador', 'Peru', 'Costa Rica', 'Guatemala', 'Mexico', 'Japan', 'Philippines', 'Indonesia','New Zealand','Antarctic', 'Canada', 'Fiji', 'Alaska', 'Washington', 'California', 'Russia', 'Taiwan', 'Tonga','Kermadec Islands']:
    df['ring_of_fire'][df.parsed_place == place] = True
print('\n\nBonus Exercise 10 -\n\n\n', df)