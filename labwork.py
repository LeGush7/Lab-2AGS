import csv
from random import *
from lxml import etree


bibl = []
with open('books-en.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    for row in csvreader:
        bibl.append(row)

# первое задание
countlen30 = 0
for i in range(1, len(bibl)):
    if len(bibl[i][1]) > 30:
        countlen30 += 1
print(countlen30)

# второе задание
name = input('Введите автора: ').lower()
books = set()
for x in range(1, len(bibl)):
    if bibl[x][2].lower() == name:
        books.add(bibl[x][1])
print('\n'.join(list(books))) if len(books) != 0 \
    else print('Произведения автора отсутствуют')

# третье задание
randbook = []
for i in range(20):
    randbook.append(bibl[randint(1, len(bibl))])
numofstr = 1
with open('listbooks.txt', 'w'):
    pass
listofbooks = open('listbooks.txt', 'a+')
for i in range(20):
    listofbooks.write(f'''
{numofstr}. {randbook[i][2]}. {randbook[i][1]} - {randbook[i][3]}''')
    numofstr += 1
listofbooks.close()

# четвёртое задание
values = []
charcodes = []
doc = etree.parse('currency.xml')
root = doc.getroot()
for element in root.findall('.//CharCode'):
    charcodes.append(element.text)
for element in root.findall('.//Value'):
    values.append(element.text)
print(charcodes)
print(values)
