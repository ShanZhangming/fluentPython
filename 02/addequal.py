l = [[1,2],2,3]
print(id(l))

temp = l*2
l[0][0] = 200
print(temp)

l *= 2
print(id(l))
l[0][0] = 100
print(l)


