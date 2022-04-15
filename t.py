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

def openvd(st, source):
	st = True
	while st:
		ans = str(input('Do you want to watch video? (yes or no): --> '))
		if ans == 'yes':
			webbrowser.open(source.get('link'), new=0, autoraise=True)
			st = False
		else:
			print('Okay, video is closed')
			st = False

def usage(b):
	global f, q, items, t

	j = 1
	items = x[0]
	t = x[j]
	f = []
	f.insert(0, 'This is too much number')
	while j < len(x):
		f.append(dict(zip(items, x[j])))
		j = j + 1
	
	while b: # use it only for data base
		p = int(input('Enter the number of videos from 0 to 5440: '))
		if p > 5440:
			print(f[0])
			break
			
		print(f[p])
		
		q = f[p]		
		print(q['link'])
		openvd(True, q)
		b = False


def search_keys():
	sk = print('Search by key words')
	ser = str(input('Key word: '))

	m = 1 # in all data
	n = 0 # in string

	ar_kw = []
 
	while m < len(f):
		obj = f[m].get('title')
		string = obj.split()
		count = 0
		while count < len(string):
			if ser == string[count]:
				ar_kw.append(f[m])
				count = count + 1
			else:
				count = count + 1
		m = m + 1	

	cn = 1
	while cn < len(ar_kw):
		print(f'{cn}', ar_kw[cn])
		cn = cn + 1
	num_video = int(input('Enter the number of these videos: '))
	print(ar_kw[num_video])
	openvd(True, ar_kw[num_video])


def search():
	p = print('Search by authors\n')
	u = str(input('Name of author: '))
	w = 1
	while w < len(f):

		if u == f[w].get('author'):
			print('Found!')
			res = f[w]
			print(f[w])
			openvd(True, f[w])
			break
		else:
			w = w + 1	
ask = input('How do you want search videos?\n 1)Author\n 2)Data Base\n 3)Key words\n Enter a number --> ')
if ask == '1':

	usage(False)
	search()

if ask == '2':
	usage(True)
if ask == '3':
	usage(False)
	search_keys()







# TO DO
def categories():
	pass

# def duplicate():
#     for key,val in Counter(ath).items():
#         print(key,val)
#         if val == 2:
#         	ath_2.append([key, val])
#         else:
#         	continue






