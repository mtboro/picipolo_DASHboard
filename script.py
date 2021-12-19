import os
import glob
import json

import pandas as pd
import numpy as np

from itertools import chain
from datetime import datetime
from tkinter import Tk
from tkinter import filedialog

class Parser():

	def __init__(self, ppl):
		self.people = ppl

	@classmethod
	def __get_date(cls, timestamp_ms):
		date = datetime.fromtimestamp(timestamp_ms / 1000)
		return date.strftime("%Y.%m.%d;%X")

	@staticmethod
	def parse_json(f):
		def fix_unicode(obj):
			try:
				if isinstance(obj, str):
					return obj.encode('latin_1').decode('utf-8')

				if isinstance(obj, list):
					return [fix_unicode(o) for o in obj]

				if isinstance(obj, dict):
					return {key: fix_unicode(item) for key, item in obj.items()}
				return obj
			except:
				return obj
		return json.load(f, object_hook=fix_unicode)


	def export_to_csv(self, path, name = 'messengerData'):

		with open(path+'/'+name+'.csv', 'w', encoding='utf-8') as parsed_data:

			parsed_data.write('Nazwa;KtoWyslal;Kiedy;Godzina;Wiadomosc\n')
			for person in self.people:

				for mess in person.messages_data:
					try:
						who = mess['sender_name']
						when = Parser.__get_date(mess['timestamp_ms'])
						co = mess['content']
						row = f'{person.name};{who};{when};{co}'
					except:
						row = f'{person.name};{who};{when};Photo.'

					parsed_data.write(f'{row}\n')


class Person():
	
	def __init__(self, path):
		self.total_messages = 0
		self.is_group = False
		self.name = 'Facebook user'
		self.messages_data = []

		i = 0
		while True:
			i += 1
			file_path = f'{path}/message_{i}.json'
			if not os.path.isfile(file_path):
				break
			with open(file_path) as json_file:

				tmp = Parser.parse_json(json_file)
				self.messages_data.append(tmp['messages']) # lista list z kazdego pliku message_i

		self.name = tmp['title']
		self.messages_data = list(chain.from_iterable(self.messages_data)) # 'odlistowanie' poszczegolnych list

		if len(tmp['participants']) > 2:
			self.is_group = True

		self.total_messages = len(self.messages_data)
	

	def __repr__(self):
		return f'Kto: {self.name}, Ile: {self.total_messages}.'

def summary(ppl):
	"""
	Zwraca DataFrame'a z krótkim podsumowaniem wybranych osob oraz ich statystyk
	"""
	df = pd.DataFrame()

	for el in ppl:
		row_df = pd.DataFrame([pd.Series([el.name, el.total_messages, el.is_group])])
		df = pd.concat([row_df, df], ignore_index=True)

	df = df.set_axis(['Nazwa', 'IloscWiadomosci', 'CzyGrupa'], axis='columns')
	return df


def main():
	root = Tk()
	root.withdraw()
	path = filedialog.askdirectory()
	print(f'path: {path}')

	assert 'inbox' in os.listdir(path)

	dirs_to_all_files = glob.glob(path+"/inbox/*")

	ppl = []

	for k in dirs_to_all_files:
		person = Person(k)

		if(person.total_messages < 3): # osoby z ktorymi nie pisalismy
			continue
		ppl.append(person)



	###PODSUMOWANIE### (KROTKIE)
	print(summary(ppl))


	###PODSUMOWANIE### (DLUZSZE)

	parser = Parser(ppl)
	parser.export_to_csv(path)

	df = pd.read_csv(path+'/messengerData.csv', sep=';', on_bad_lines='skip')
	print(df.head())


	###WYBOR OSOBY###
	ciec = 'Kubuś Puchatek'

	df = df[df['Nazwa'] == ciec]


	wiadomosci = df["Wiadomosc"].tolist()
	# print(wiadomosci)

	slowa = []

	for el in wiadomosci:
		el = str(el).split()
		for el2 in el:
			slowa.append(str(el2).lower())

	mapka = {}

	for el in slowa:
		mapka.setdefault(el, 0)
		mapka[el] += 1

	###MAPA: KLUCZ - słowo, WARTOSC - ilosc###
	print(dict(sorted(mapka.items(), key=lambda item: item[1])))

if __name__ == '__main__':
	main()

