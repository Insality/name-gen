# coding: utf-8

'''
Модуль для получения и редактирования слов (изменения падежей и окончаний)
'''

import json
import codecs
import random
import pymorphy2

DATADIR = "./data"
morph = pymorphy2.MorphAnalyzer()

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


def change_gender(word, gender):
	if (gender=='f'):
		return morph.parse(word)[0].inflect({'femn'}).word
	elif (gender=='m'):
		return morph.parse(word)[0].inflect({'masc'}).word
	return word




if __name__=="__main__":
	l = []
	for i in range(30):
		noun = get_noun()
		l.append( change_gender(get_adj()["Word"], noun["Genus"]) + " " + noun["Word"] + " " + get_addon()["Word"])
	print('\n'.join( sorted(l, key=len) ))

