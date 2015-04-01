from __future__ import print_function
import os

class Cities:
	def __init__(self, cities_dir='cities_json'):
		self.cities_dir = cities_dir
		self.lookup_file = 'city_state_lookup.p'
		# resource of the 'states' dictionary:
		# http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/
		self.states = {
	        'AK': 'Alaska',
	        'AL': 'Alabama',
	        'AR': 'Arkansas',
	        # 'AS': 'American Samoa',
	        'AZ': 'Arizona',
	        'CA': 'California',
	        'CO': 'Colorado',
	        'CT': 'Connecticut',
	        'DC': 'District of Columbia',
	        'DE': 'Delaware',
	        'FL': 'Florida',
	        'GA': 'Georgia',
	        # 'GU': 'Guam',
	        'HI': 'Hawaii',
	        'IA': 'Iowa',
	        'ID': 'Idaho',
	        'IL': 'Illinois',
	        'IN': 'Indiana',
	        'KS': 'Kansas',
	        'KY': 'Kentucky',
	        'LA': 'Louisiana',
	        'MA': 'Massachusetts',
	        'MD': 'Maryland',
	        'ME': 'Maine',
	        'MI': 'Michigan',
	        'MN': 'Minnesota',
	        'MO': 'Missouri',
	        # 'MP': 'Northern Mariana Islands',
	        'MS': 'Mississippi',
	        'MT': 'Montana',
	        # 'NA': 'National',
	        'NC': 'North Carolina',
	        'ND': 'North Dakota',
	        'NE': 'Nebraska',
	        'NH': 'New Hampshire',
	        'NJ': 'New Jersey',
	        'NM': 'New Mexico',
	        'NV': 'Nevada',
	        'NY': 'New York',
	        'OH': 'Ohio',
	        'OK': 'Oklahoma',
	        'OR': 'Oregon',
	        'PA': 'Pennsylvania',
	        'PR': 'Puerto Rico',
	        'RI': 'Rhode Island',
	        'SC': 'South Carolina',
	        'SD': 'South Dakota',
	        'TN': 'Tennessee',
	        'TX': 'Texas',
	        'UT': 'Utah',
	        'VA': 'Virginia',
	        # 'VI': 'Virgin Islands',
	        'VT': 'Vermont',
	        'WA': 'Washington',
	        'WI': 'Wisconsin',
	        'WV': 'West Virginia',
	        'WY': 'Wyoming'}
	        
		if len(os.listdir(self.cities_dir)) != len(self.states):
			self.download_cities_info_from_web()
		if not os.path.exists(self.lookup_file):
			self.make_table_from_citi_jsons()

		self.city_map = self.load_look_up_table()

	def download_cities_info_from_web(self):

		'''
		download files from http://api.sba.gov/geodata/city_county_links_for_state_of/STATE_ABBREVIATION.json
		details of files are mentioned in the url below:
		https://www.sba.gov/about-sba/sba-performance/sba-data-store/web-service-api/us-city-and-county-web-data-api#response-json
		'''
		print('download cities info from web')
		import pathos.multiprocessing as mp
		from urllib import urlretrieve
		if not os.path.isdir(self.cities_dir):
			os.makedirs(self.cities_dir)
		def download_json(state_abbrev):
			url = 'http://api.sba.gov/geodata/city_county_links_for_state_of/{}.json'.format(state_abbrev)
			fout_name = os.path.join(self.cities_dir, '{}.json'.format(state_abbrev))
			urlretrieve(url, fout_name)

		pool = mp.Pool(processes=8)
		pool.map(download_json, self.states.keys())

	def make_table_from_citi_jsons(self):
		import json
		import pickle
		city_states = {}

		for city_file in os.listdir(self.cities_dir):
			state_abbrev = city_file[:2]
			state_full = self.states[state_abbrev].lower()
			city_states[state_full] = state_full

			city_file = os.path.join(self.cities_dir, city_file)
			with open(city_file, 'r') as fin:
				data = json.load(fin)

			for row in data:
				city_states[row['name'].lower()] = state_full

		with open(self.lookup_file, 'w') as fout:
			pickle.dump(city_states, fout)

	def load_look_up_table(self):
		import pickle
		with open(self.lookup_file, 'r') as fin:
			data = pickle.load(fin)
		# for key, val in data.items():
		# 	print(key.encode('ascii', 'ignore'), val)
		return data





if __name__ == '__main__':
	cities = Cities()
	# cities.make_table_from_citi_jsons()
	cities.load_look_up_table()
	# print(len(cities.states))
	# cities.download_cities_info_from_web()



		