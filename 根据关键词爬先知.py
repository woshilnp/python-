import requests
from bs4 import BeautifulSoup

url = 'https://xz.aliyun.com/'
keyword = 'csrf'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html,"html.parser")

search_url = 'https://xz.aliyun.com/search'
data = {
    'type':'text',
    'keyword':keyword
}
r_r = requests.get(search_url,params=data)
r_r.encoding = 'utf-8'
r_html = r_r.text

r_soup = BeautifulSoup(r_html,"html.parser")
xz_div_list = r_soup.find_all(class_='topic-title')
xz_url_list = []

for xz_div in xz_div_list:
    xz_url = xz_div.attrs['href']
    xz_url = url + xz_url
    xz_url_list.append(xz_url + '\n')
    with open(keyword + '.txt','w') as f:
        f.writelines(xz_url_list)

print(xz_url_list)
