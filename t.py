import csv
from collections import Counter
import json
import webbrowser

with open('data.csv') as File:
	reader = csv.reader(File)

	global x
	x = list(reader)
	
	ath = []
	ath_2 = []
	i = 1
	while i < len(x):
		g = x[i]
		ath.append(g[1])
		i = i + 1


def duplicate():
    for key,val in Counter(ath).items():
        print(key,val)
        if val == 2:
        	ath_2.append([key, val])
        else:
        	continue


#p = int(input('Enter the number of videos from 0 to 5440: '))


def usage(index):
	global f, q
	j = 1
	prices = x[0]
	t = x[j]
	f = []
	while j < len(x):
		f.append(dict(zip(prices, x[j])))
		j = j + 1
	print(f[index])
	q = f[index]
	print(q['link'])
	ans = str(input('Do you want to watch video? (yes or no): --> '))
	if ans == 'yes':
		webbrowser.open(q['link'], new=0, autoraise=True)
	else:
		print('Okay, video is closed')
usage(12)
print(q.values())

t = x[0]
def search():
	p = print(f'Search by {t}\n')
	print("1 - title\n2 - author\n3 - date")
	u = int(input('Item: '))
	if u == 1:
		tit = str(input('Name of title: '))
	if u == 2:
		a = str(input("Name of author: "))
		print(q['author'])
	if u == 3:
		dat = int(input("Date: "))
