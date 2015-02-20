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
	return nouns[random.randint(0, len(nouns) - 1)]

def get_adj():
	adjs = open_json("adj.json")["data"]
	return adjs[random.randint(0, len(adjs) - 1)]

def get_addon():
	addons = open_json("addons.json")["data"]
	return addons[random.randint(0, len(addons) - 1)]

def open_json(filename):
	f = codecs.open(DATADIR + "/" + filename, 'r', encoding='utf8')
	f_data = f.read()
	return json.loads(f_data)
	f.close()



if __name__=="__main__":
	l = []
	for i in range(30):
		l.append(get_adj()["Word"] + " " + get_noun()["Word"] + " " + get_addon()["Word"])
	print('\n'.join( sorted(l, key=len) ))

