from distutils import extension
from email.policy import default
from lxml import html
import re
import json
import csv
import click
from itertools import chain
import re


file = open("men shoes.txt")
line = file.read().replace("\n", " ")
file.close()
tree = html.fromstring(html=line)
all_product = tree.xpath("//div[@class = 'cell']/ul")[0]
title = all_product.xpath(".//li/div/div[@class ='productDetail']/div/a/text()")
price = all_product.xpath(".//li/div/div[@class ='productDetail']/div/div/div/div/span/text()")
res1 = []
res2 = []

for ele in title:
    if ele.strip():
        res1.append(ele)
ree1 =[''.join(item.split()) for item in res1]
for ele in price:
    if ele.strip():
        res2.append(ele)
ree2 =[''.join(item.split()) for item in res2]
print(ree1)
print(ree2)