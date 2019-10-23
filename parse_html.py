import os
from os import path
from bs4 import BeautifulSoup
import re

def refine(data):
    return re.sub('[\\s\\n\\t]+', ' ', data)

def main():
    file = open(os.path.join(os.path.curdir, 'accept.html'), 'r', encoding='utf-8')

    acceptSoup = BeautifulSoup(file.read().encode('utf-8'))
    sense_body = acceptSoup.select('.sense-body')

    sense_file = open(path.join(path.curdir, 'accept_sense.html'), 'w', encoding='utf-8')

    content = {}

    for item in sense_body:
        definitions = item.select('div.def')
        s = definitions[0].text.strip(' \n\t')
        s = refine(s)
        if len(s) > 0:
            sense_file.write('sense: ' + s + '\n')
            examples = item.select('div.examp')
            for ex in examples:
                s = ex.text.strip(' \n\t')
                if len(s) > 0:
                    sense_file.write('   example: ' + s + '\n')

    sense_file.close()


main()

