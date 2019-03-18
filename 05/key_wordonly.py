def tag(name, cls=None, *content,  **attrs):
	"""生成一个或多个HTML标签"""
	if cls is not None:
		attrs['class'] = cls
	if attrs:
		attr_str = ''.join(' %s="%s"' % (attr, value)
						   for attr, value
						   in sorted(attrs.items()))
	else:
		attr_str = ''
	if content:
		return '\n'.join('<%s%s>%s</%s>' %
						 (name, attr_str, c, name) for c in content)
	else:
		return '<%s%s />' % (name, attr_str)

print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
		  'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))

def f(a, *, b):
	return a, b

print(f(1,b=2))