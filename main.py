import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}


url = "http://ke.kabupro.jp/code/8601.htm"
response = requests.get(url, headers=headers)  # get url contents
response.encoding = response.apparent_encoding
bs_obj = BeautifulSoup(response.text, 'html.parser')  # parse with beautifulsoup
table = bs_obj.find("table", class_="Quote")  # get the link tables

print(table)

