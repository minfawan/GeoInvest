from citis import Cities
from collections import defaultdict
import string
import bs4


class DocParser:
	def __init__(self, doc_folder='files'):
		self.doc_dir = doc_folder
		self.city_utilities = Cities()
		self.city_map = self.city_utilities.load_look_up_table()

	def process_doc(self, doc_name):
		'''
		There are two different file format: txt or htm / html.
		For files in txt format, we just read it directly.
		For files in htm format, we read its full conent with the help of extra packages.

		Find the sections below:
		item 1 business
		item 2 properties
		(item 3 legal proceedings)
		item 6 selected financial data
		item 7 managements discussion and analysis
		(item 8 financial statements)

		We need to break down the text into a list of words, and then compare every word with 
		the city / state names.
		We need to return a dictionary where its key is the full state name and its value is 
		the number of appearance of the cities in that state in the document.
		'''

		with open(doc_name, 'r') as fin:
			text = fin.read()
		if 'htm' in doc_name[-4:]:
			text = bs4.BeautifulSoup(text).text
		else:
			print('Can\'t recognize format of file: {}'.format(doc_name))
			return 

		# process on text

		text = text.lower().encode('ascii', 'ignore').translate(string.maketrans("",""), string.punctuation)
		text = self.find_sections(text)

		# if successfully identify sections in the text
		if text:
			state_count = self.city_match(text)

		return text

	def find_sections(self, text):
		i1 = text.rfind('item 1 business')
		text = text[i1:]
		# i2 = text.find('item 2 properties')
		i3 = text.find('item 3 legal proceedings')
		i6 = text.find('item 6 selected financial data')
		# i7 = text.find('item 7 managements discussion and analysis')
		i8 = text.find('item 8 financial statements')
		if i8 != -1:
			print('found section 1, 2, 6, 7')
			return text[:i3] + ' ' + text[i6:i8]
		elif i3 != -1:
			print('found section 1, 2')
			return text[:i3]
		print('no section found')
		return []
		# return [ text[:i2], text[i2:i3], text[i6:i7], text[i7:i8] ]

	def city_match(self, text):
		# initialize a hashtable to store city count
		state_count_table = self.city_utilities.init_state_count_table()
		text = text.split()
		for word in text:
			if word in self.city_map:
				state_count_table[self.city_map[word]] += 1

		# for state, count in state_count_table.items():
		# 	print('{}: {}'.format(state, count))

		return state_count_table




if __name__ == '__main__':
	doc_parser = DocParser()
	text = doc_parser.process_doc('files/1110783-000095013706011768-c08447e10vk.htm')
	# print(text)
