import requests
from bs4 import BeautifulSoup


r = requests.get('https://tuhocdohoa.vn')
page_source = BeautifulSoup(r.text, 'lxml')

title = page_source.title.text

print(title)
