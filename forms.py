import requests
from urllib import urlretrieve
# from urllib.request import urlretrieve
import bs4
import csv
import sys
import os
import re
import pathos.multiprocessing as mp
# import multiprocessing as mp



out_dir = 'files'
if not os.path.isdir(out_dir):
	os.makedirs(out_dir)

urls = [ 'http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000040545&type=10-K&dateb=&owner=exclude&count=40', 
		'http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000051143&type=10-K&dateb=&owner=exclude&count=40',
		'http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000066740&type=10-K&dateb=&owner=exclude&count=40',
		'http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000108772&type=10-K&dateb=&owner=exclude&count=40',
		'http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001110783&type=10-K&dateb=&owner=exclude&count=40'
		]


def is_valid_file(url):
	return '.' in url[url.rfind('/')+1: ]


def visit_entry(entry):
	cells = entry.find_all('td')
	row = [cell.text.strip() for cell in cells]
	form_link = 'http://www.sec.gov' + cells[1].a['href']
	return form_link
	# download_10k_form(form_link)


def download_10k_form(url):
	r = requests.get(url)
	soup = bs4.BeautifulSoup(r.text)
	table = soup.find('table', {'class': 'tableFile'})

	file_link = 'http://www.sec.gov' + \
		table.find_all('tr')[1].find('a')['href']

	if is_valid_file(file_link):
		fout_name = '-'.join(file_link.split('/')[-3:])
		fout_name = os.path.join(out_dir, fout_name)
		print('retrieving {}'.format(fout_name))
		urlretrieve(file_link, fout_name)

	else:
		print('no file found at: {}'.format(url))







pool = mp.Pool(processes=4)


for url in urls:
	print('start visiting url: {}'.format(url))
	r = requests.get(url)
	soup = bs4.BeautifulSoup(r.text)
	# fout_name = 'companies_list.csv'
	print('finished loading url')
	table_entries = soup.find('table', {'class': 'tableFile2'}).find_all('tr')
	form_links = list(map(visit_entry, table_entries[1:]))

	print('Finished getting form links')
	pool.map(download_10k_form, form_links)



# testing only 
# url = 'http://www.sec.gov/Archives/edgar/data/40545/000004054510000010/0000040545-10-000010-index.htm'
# download_10k_form(url)