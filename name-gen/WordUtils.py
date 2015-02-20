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
	p = morph.parse(word)
	if (len(p) > 0):
		if (gender=='f'):
			try:
				result = p[0].inflect({'femn'}).word
				if result.endswith("ую"):
					result = result[:-2] + "ая"
				return result
			except AttributeError:
				return word
		elif (gender=='m'):
			# return p[0].inflect({'masc'}).word
			return word
	return word


def generate_phrase():
	noun = get_noun()
	new_word = change_gender(get_adj()["Word"], noun["Genus"]) + " " + noun["Word"] + " " + get_addon()["Word"]

	if random.random()>(0.85):
		new_word += " и %s" % get_addon()["Word"]

	if random.random()>(0.90):
		new_word = change_gender(get_adj()["Word"], noun["Genus"]) + " " + new_word

	return new_word

if __name__=="__main__":
	l = []
	for i in range(30):
		l.append(generate_phrase())

	print('\n'.join( sorted(l, key=len) ))
