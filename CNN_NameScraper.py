from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

# This program searches CNN to see how many time each candidates name has been said

# Get the html of the website
url = "https://www.cnn.com/"
html = urlopen(url)

# Using the Beautiful Soup module the html is split up into python objects
soup = BeautifulSoup(html, 'lxml')

# Name count variables NOT IN USE
Bennet = 0
Biden = 0
Booker = 0
Bullock = 0
Buttigieg = 0
Castro = 0
Blasio = 0
Delaney = 0
Gabbard = 0
Gillibrand = 0
Harris = 0
Hickenlooper = 0
Inslee = 0
Klobuchar = 0
Messam = 0
Moulton = 0
Rourke = 0
Ryan = 0
Sanders = 0
Sestak = 0
Swalwell = 0
Warren = 0
Williamson = 0
Yang = 0

dems = [	
'Bennet',
'Biden',
'Booker',
'Bullock',
'Buttigieg',
'Castro',
'Blasio', #de Blasio
'Delaney',
'Gabbard',
'Gillibrand',
'Harris',
'Hickenlooper',
'Inslee',
'Klobuchar',
'Messam',
'Moulton',
'Rourke', #O'Rourke
'Ryan',
'Sanders',
'Sestak',
'Swalwell',
'Warren',
'Williamson',
'Yang'

#These LOWERCASE
'bennet',
'biden',
'booker',
'bullock',
'buttigieg',
'castro',
'blasio', #de Blasio
'delaney',
'gabbard',
'gillibrand',
'harris',
'hickenlooper',
'inslee',
'klobuchar',
'messam',
'moulton',
'rourke', #O'Rourke
'ryan',
'sanders',
'sestak',
'swalwell',
'warren',
'williamson',
'yang'
]

dems_found = []

#print(soup.get_text()) # YAYYAYAY

uni_to_stringy = (soup.get_text()).encode('ascii','ignore')
split_pea_soup = re.split('-| |, |. |\\|: |"|/', uni_to_stringy)

#print(len(dems))
#print(split_pea_soup)

"""
while True:
	dems_count = 0
	print len(dems_found)

	if dems_count > 23:
		break
	for tester in split_pea_soup: #dems[dems_count]
		dems_found.append(dems[dems_count])
		dems_count = dems_count + 1
	print('Added One')

dems_count = 0
"""

tester = "sanders"

"""
THIS SHIT WORKS FOR SOME REASON
test_list = ['a', 'b', 'c', 'd', 'e']
test_seek = ['a', 'e', 'z']
win = []
print(test_list)
for item in range(0, (len(test_seek) - 1)):
	if test_seek[item] in test_list:
		win.append(test_seek[item])
		print(win)
"""

for person in range(0, (len(dems) - 1)):
	#print(dems[person])
	#uni_dems = unicode(dems[person], "utf-8")

	if str(dems[person]) in split_pea_soup:
		dems_found.append(dems[person])
		print(dems_found)

	#print(dems[person])
	#print(dems[person - 1])

print(dems_found)
print("Done!")