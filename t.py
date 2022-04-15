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


def usage():
	global f, q, items, t

	j = 1
	items = x[0]
	t = x[j]
	f = []
	f.insert(0, 'This is too much number')
	while j < len(x):
		f.append(dict(zip(items, x[j])))
		j = j + 1
	
	while b:
		p = int(input('Enter the number of videos from 0 to 5440: '))
		if p > 5440:
			print(f[0])
			break
			
		print(f[p])
		q = f[p]
			
		print(q['link'])
		ans = str(input('Do you want to watch video? (yes or no): --> '))
		if ans == 'yes':
			webbrowser.open(q['link'], new=0, autoraise=True)
			break
		else:
			print('Okay, video is closed')
			break
def search():
	p = print(f'Search by authors\n')
	u = str(input('Name of author: '))
	w = 1
	while w < len(f):

		if u == f[w].get('author'):
			print('Found!')
			res = f[w]
			print(f[w])
			opn = input('Do you want open this video? (yes or no): ')
			if opn == 'yes':
				webbrowser.open(res['link'], new=0, autoraise=True)
			else:
				print('Okay, video is closed')
			break
		else:
			w = w + 1	
ask = input('How do you want search videos?\n 1)Author\n 2)Data Base\n Enter a number --> ')
if ask == '1':
	b = False
	usage()
	search()
else:
	b = True
	usage()






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






