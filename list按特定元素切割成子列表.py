with open(r'C:\Users\Ray94\Downloads\記事_豆乳.txt','r', encoding='UTF-8') as f:
    lines = f.readlines()
strs = []
for line in lines:
    strs.append(line)
from itertools import groupby
i = (list(g) for _, g in groupby(strs, key=' 印刷対象にする\n'.__ne__))
number = 0
print(number)
all = [a + b for a, b in zip(i, i)]
import pandas as pd
number = 0
for each in all:
    number += 1
    print(number)
    with open(r"C:\Users\Ray94\Downloads\豆乳記事\\" + str(number) + ".txt", 'w', encoding='utf-8') as f1:
        for item in each[:-1]:
            f1.write(item)
