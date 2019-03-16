from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
print(floats2[-1])
print(floats == floats2)

a = [[1,2,3],4]
#b = a.__deepcopy__()
#print(b)
#b[0][0] = -1
print(a)