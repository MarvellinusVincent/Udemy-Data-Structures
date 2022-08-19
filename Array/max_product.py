import numpy as np

array = np.array([10 ,24 ,16 ,43 ,50 ,15 ,34 ,51 ,46 ,17 ,11 ,12 ,30 ,5 ,27])

def maxproduct(arr):
    arr.sort()
    print (arr[-1] * arr[-2])



maxproduct(array)