import time  # 時刻に関するさまざまな関数を使用するためのパッケージ
import pandas as pd  # データ解析を容易にする機能を提供する
import requests  # WEBスクレイピングでHTMLファイルからデータを取得するのに使われる
from bs4 import BeautifulSoup  # 取得したHTMLファイルをさらに解析するライブラリ
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

url = "http://ke.kabupro.jp/code/8604.htm"
dfs = pd.read_html(url)
print(len(dfs))
table = dfs[1][2:-1]
#print(table)

response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, 'html.parser')

table_for_link = soup.find('table', class_="Quote")


links = []
names = []
for tr in table_for_link.find_all("tr"):
    trs = tr.find_all("td", class_="CellBrownName")
    for each in trs:
        try:
            link = each.find('a')['href']
            links.append(link)
            name = each.text
            names.append(name)
            filename = os.path.join(r'C:\\Users\Ray94\OneDrive\桌面\20210701', str(name) + '.pdf')
            with open(filename, 'wb') as f:
                f.write(requests.get(str(link)).content)
                time.sleep(3)
        except:
            pass

print(links)

table['Link'] = links
Result = pd.DataFrame(table)
print(Result)

Result.to_csv(r"C:\\Users\Ray94\OneDrive\桌面\20210706\Result.csv", mode='a', index=False, header=None, encoding="utf-8_sig")

