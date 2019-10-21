import pprint
import pyperclip
import re
import os


students = {
    'john': {
        'id': 123,
        'name': 'John'
    },
    'peter': {
        'id': 234,
        'name': 'Peter'
    },
}

phonePattern = re.compile(r'(.+)(\d\d\d-\d\d\d-\d\d\d\d)')

matchPhone = phonePattern.search('my phone number is: 214-336-4959 and 214-507-0102')
group = matchPhone.group()
print(group)


path = os.path.join('usr', 'bin', 'spam')

print(path)
print(os.path.abspath(os.path.curdir))
print(os.path.curdir)

filePath = os.path.join(os.path.curdir, 'toeic.txt')
print(filePath)
file = open(filePath)

# content = file.read()

s = re.sub('\\s+', ' ', 'abc    d')
print(s)
