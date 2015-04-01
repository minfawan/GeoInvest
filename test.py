# # ########################## lxml test ###############################
# from lxml import etree
# with open('files/1110783-000095013706011768-c08447e10vk.htm', 'r') as fin:
# 	tree = etree.parse(fin)




# import html2text

# with open('files/1110783-000095013706011768-c08447e10vk.htm', 'r') as fin:
# 	html2text.html2text(fin.read())

import bs4
with open('files/1110783-000095013706011768-c08447e10vk.htm', 'r') as fin:
	soup = bs4.BeautifulSoup(fin)
	with open('test.txt', 'w') as fout:
		fout.write(soup.text.encode('ascii', 'ignore'))









# # ########################## download test ###############################
# url = 'http://www.sec.gov/Archives/edgar/data/66740/000110465915009560/a15-1770_110k.htm'
# import os
# test_folder = 'test_folder'
# if not os.path.isdir(test_folder):
# 	os.makedirs(test_folder)

# # python 2
# import urllib
# import sys

# def report(blocknr, blocksize, size):
#     current = blocknr*blocksize
#     sys.stdout.write("\r{0:.2f}%".format(100.0*current/size))


# def downloadFile(url):
#     print "\n",url
#     fname = url.split('/')[-1]
#     fname = os.path.join(test_folder, fname)
#     print fname
#     urllib.urlretrieve(url, fname, report)

# downloadFile(url)






# import wget
# file_name = url.split('/')[-1]
# file_name = os.path.join(test_folder, file_name)
# print file_name
# file_name = wget.download(url, out=file_name, bar=wget.bar_thermometer)







# import requests
# import sys
# def requests_download(link, file_name):
# 	with open(file_name, "wb") as f:
# 	        print "Downloading %s" % file_name
# 	        response = requests.get(link, stream=True)
# 	        total_length = response.headers.get('content-length')

# 	        if total_length is None: # no content length header
# 	            f.write(response.content)
# 	        else:
# 	            dl = 0
# 	            total_length = int(total_length)
# 	            for data in response.iter_content():
# 	                dl += len(data)
# 	                f.write(data)
# 	                done = int(50 * dl / total_length)
# 	                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
# 	                sys.stdout.flush()


# file_name = url.split('/')[-1]
# file_name = os.path.join(test_folder, file_name)
# requests_download(url, file_name)


########################## timeit test ###############################

# import timeit
# # from timeit import timeit


# s = ['some weird string' for i in range(1000)]
# def stupid_function(x):
# 	x += 'another weird string'
# 	return x


# # timeit('[stupid_function(x) for x in s]')
# # timeit('map(stupid_function, s)')
# t1 = timeit.Timer('map(stupid_function, s)',
#         'from __main__ import stupid_function, s').timeit(number=100)

# t2 = timeit.Timer('for x in s: stupid_function(x)', 
# 				'from __main__ import stupid_function, s').timeit(number=100)

# print t1
# print t2