import sys
import re
WORD_RE = re.compile(r'\w+')
index = {}
print(type(WORD_RE))

with open('englishArticle.txt') as fp:
    for line_no,line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            world = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(world,[]).append(location)
            # occurrences = index.get(world,[])
            # occurrences.append(location)
            # index[world] = occurrences

for world in sorted(index, key=str.upper):
    print(world, index[world])
#print(str.upper(index['when']))
for v in index:
    print(type(v), str.upper(v))
for world in sorted(index.items(), key=lambda item:item[0]):
    print(world[0], world[1])

