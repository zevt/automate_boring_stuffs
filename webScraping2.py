import webbrowser
import requests
import shutil
import tempfile
import urllib.request
import urllib.parse
import os
from bs4 import BeautifulSoup


url = 'https://dictionary.cambridge.org/us/dictionary/english/accept?q=accept'

# response = urllib.request.urlopen(url)
# html_page = urllib.request.urlopen(url)
response = requests.get(url)
html = response.text
print(response)

# response = requests.get(url)


currentPath = os.path.curdir
filePath = os.path.join(os.path.curdir, 'accept2.html')
# file = open(filePath, 'w', )
# # file.write(html)
# file.write(html.decode('utf-8'))
# file.close()

with open(filePath, 'w', encoding='utf-8') as file:
    file.write(html)
#

# res = requests.get('https://google.com')
# print(res.content)

# param = {'q': 'accept'}
# headers_ = {'Accept-Encoding': 'identity'}
# res = requests.get('https://dictionary.cambridge.org/us/dictionary/english/accept', headers=headers_)
#
#
#
# print(res.status_code)