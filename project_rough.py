import requests
import pandas

url = 'https://data.ct.gov/api/views/5mzw-sjtu/rows.csv?accessType=DOWNLOAD'
params = {'city': 'Norfolk'}
data = pandas.read_csv(requests.request('GET', url).text, header = 0)
print(data.tail(1))