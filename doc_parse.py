from citis import Cities
import unicodedata
import sys
import string
import bs4


class DocParser:
	def __init__(self, doc_folder='files'):
		self.doc_dir = doc_folder
		self.city_map = Cities().city_map

	def process_doc(self, doc_name):
		'''
		There are two different file format: txt or htm / html.
		For files in txt format, we just read it directly.
		For files in htm format, we read its full conent with the help of extra packages.

		Find the sections below:
		item 1 business
		item 2 propertiets
		(item 3 legal proceedings)
		item 6 consolidated financial data
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

		return text



if __name__ == '__main__':
	doc_parser = DocParser()
	print(doc_parser.process_doc('files/1110783-000095013706011768-c08447e10vk.htm'))
