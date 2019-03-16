# dict = {'1':[1,2,3]}
#
# dict['1'].append(4)
# print(dict)
# dict['2'].append(4)
import collections

#以上代码会报错
dict = collections.defaultdict(list)
dict[1].append(4)
print(dict)
print(type(dict))

dict2 = {}
dict2[0] = 0
print(dict2)
#print(type(dict2[1]))
print(dict2.get(1,()))