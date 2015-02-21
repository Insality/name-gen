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

def get_noun(tag=None):
	nouns = open_json("noun.json")["data"]

	if (tag != None):
		nouns = list( filter(lambda x: tag in x["Tags"], nouns))

	return nouns[random.randint(0, len(nouns) - 1)]

def get_adj(tag=None):
	adjs = open_json("adj.json")["data"]

	if (tag != None):
		adjs = list( filter(lambda x: tag in x["Tags"], adjs))

	return adjs[random.randint(0, len(adjs) - 1)]

def get_end():
	end = open_json("endings.json")["data"]
	return end[random.randint(0, len(end) - 1)]

def get_adj_to_addon(addon, tag=None):
	addon_tags = morph.parse(addon)[0].tag
	case = addon_tags.case
	number = addon_tags.number
	gender = addon_tags.gender

	adj = get_adj(tag)["Word"]
	result = ""
	try:
		result = morph.parse(adj)[0].inflect({case, number, gender}).word
	except AttributeError:
		# При любой ошибке можно вернуть пустое слово
		result = ""
	return result

def get_addon(tag=None):
	addons = open_json("addons.json")["data"]

	if (tag != None):
		addons = list( filter(lambda x: tag in x["Tags"], addons))

	return addons[random.randint(0, len(addons) - 1)]

def open_json(filename):
	f = codecs.open(DATADIR + "/" + filename, 'r', encoding='utf8')
	f_data = f.read()
	return json.loads(f_data)
	f.close()

def stem_noun(noun):
	max_chars = 9
	nl = len(noun)
	if (nl < max_chars):
		max_chars = nl
	if (nl <= 4):
		return noun
	return noun[:random.randint(3, max_chars)]

def change_gender(word, gender):
	p = morph.parse(word)
	if (len(p) > 0):
		if (gender=='f'):
			if word.endswith("ый") or word.endswith("ой") or word.endswith("ий"):
				word = word[:-2] + "ая"
				return word
			# если неполучилось
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
