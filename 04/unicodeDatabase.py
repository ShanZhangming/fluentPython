import unicodedata
import re

re_degit = re.compile(r'\d')

sample = sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for char in sample:
    print('U+%04x' % ord(char),
          char.center(6),
          're_dig' if re_degit.match(char) else '-',
          'is_dig' if char.isdigit() else '-',
          'is_num' if char.isnumeric() else '-',
          format(unicodedata.numeric(char), '5.2f'),
          unicodedata.name(char),
          sep = '\t'
          )