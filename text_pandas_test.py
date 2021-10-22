import pandas as pd

df = pd.read_fwf('https://www.census.gov/construction/bps/txt/tb3u201901.txt', skiprows = 9)
print(df)