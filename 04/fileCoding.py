open('cafe.txt', 'w', encoding='utf_8').write('café')

fp = open('cafe.txt')
print(fp)
print(open('cafe.txt').read())

fp = open('cafe.txt', 'w', encoding='utf_8')
fp.write('café')
fp.close()

import os
print(os.stat('cafe.txt').st_size)

fp2 = open('cafe.txt')
print(fp2)
print(fp2.encoding)
print(fp2.read())
fp2.close()

fp3 = open('cafe.txt', encoding='utf_8')
print(fp3)
print(fp3.read())
fp3.close()

fp4 = open('cafe.txt', 'rb')
print(fp4)
print(fp4.read())
fp4.close()
