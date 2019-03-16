s = 'café你好'
for string  in s:
    print(string)
print(type(s))

en = s.encode('utf8')
print(type(en))
print(en)
de = en.decode('utf8')
print(de)

fp = open('chineseText.txt', encoding='utf-8')
for line in fp.readlines():
    print(line)

s_array = bytearray(en)
for byte in s_array:
    print(byte)