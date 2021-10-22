#Activity4 - submitted by Lakshmi Narayana Podagatlapalli(UIN: 01097265)
import numpy as np
arr = np.arange(12).reshape(4, 3)
boo = np.array([True, False, False, True])
print(np.sum(arr[:, 1][boo]))
#print(arr[::3,1])