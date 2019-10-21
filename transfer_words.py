import re
import os


filePath = os.path.join(os.path.curdir, 'toeic.txt')
print(filePath)
file = open(filePath)

# content = file.read()
# print(content)

lines = file.readlines()
collect = {}

for line in lines:
    if '==' in line:
        s = re.sub('\\s+', ' ', line.split('==')[0].strip().lower())
        collect[s] = collect.setdefault(s, 0) + 1

# pprint.pprint(collect)
wordList = list(collect.keys())

outputFilePath = os.path.join(os.path.curdir, 'toeic_words.txt')

outputFile = open(outputFilePath, 'a')

# wordList.sort()

for word in wordList:
    outputFile.writelines(word + '\n')
    # outputFile.write(word)

file.close()
outputFile.close()





