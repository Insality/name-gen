# coding: utf-8

'''
Модуль для получения и редактирования слов (изменения падежей и окончаний)
'''

import json
import codecs
import random

DATADIR = "./data"

def get_noun():
	nouns = open_json("noun.json")["data"]
	return nouns[random.randint(0, len(nouns) - 1)]["Word"]

def get_adj():
	adjs = open_json("adj.json")["data"]
	return adjs[random.randint(0, len(adjs) - 1)]["Word"]

def get_addon():
	addons = open_json("addons.json")["data"]
	return addons[random.randint(0, len(addons) - 1)]["Word"]

def open_json(filename):
	f = codecs.open(DATADIR + "/" + filename, 'r', encoding='utf8')
	f_data = f.read()
	return json.loads(f_data)
	f.close()



if __name__=="__main__":
	for i in range(30):
		# if (random.random() > 0.5):
		print(get_adj() + " " + get_noun() + " " + get_addon())
		# else:
			# print(get_noun() + " " + get_addon())