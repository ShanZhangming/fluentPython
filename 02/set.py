l = ['spam', 'spam', 'eggs', 'spam']
s1 = set(l)
l2 = ['spam2', 'spam', 'eggs', 'spam']
s2 = set(l2)

print(s1 & s2)
print(type(s1&s2))