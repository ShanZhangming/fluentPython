#
l = [[1,2],2,3]
print(id(l))

temp = l*2
l[0][0] = 200
print(temp)

l *= 2
print(id(l))
l[0][0] = 100
print(l)

t = (1,2,3)
print(id(t))
t *= 2
print(id(t))

#令人难以预料的结果
t = (1, 2, [30, 40])
#t[2] += [50, 60]
print(t)

dis.dis('s[a] += b')

#############dev################
#5555
#666
