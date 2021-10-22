#Activity 14 - submitted by Lakshmi Narayana Podagatlapalli(01087265)
import pandas

df = pandas.read_json(r'https://www.cs.odu.edu/~sampath/courses/data/books.json')
df = pandas.json_normalize(df['books'])
#to print the entire rows of books written by Addy Osmani
print(df[df['author'] == 'Addy Osmani'])
#To print only titles of the books written by Addy Osmani
print(df['title'][df['author'] == 'Addy Osmani'])