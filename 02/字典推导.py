DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
    ]

country_code = {country:code for country,code in DIAL_CODES}
print(country_code)
a = dict(one = 1, two = 2, three = 3)
print(a)
b = {'one':1, 'two':2, 'three':3}
print(b)
c = dict(zip(['a','b','c'], [1,2,3]))
print(c)
d = dict({'one':1, 'two':2, 'three':3})
print(d)
e = dict([('three',3), ('one',1,), ('two',2)])
print(e)