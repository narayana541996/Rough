#Activity 10 - Submitted by Lakshmi Narayana Podagatlapalli (01087265)
import pandas as pd

def systematic_sampling(df, step):
    return df[::3]

heights = [159, 171, 158, 162, 162, 177, 160, 175, 168, 171, 178, 178, 173, 177, 164]
heights.sort()
print(heights)
data = {'h' : heights}
df = pd.DataFrame(data)
print(systematic_sampling(df, 3))
