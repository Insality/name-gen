# coding: utf-8

'''
Модуль для получения и редактирования слов (изменения падежей и окончаний)
'''

import sys
import json
import Tags
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


def change_gender(word, gender):
	p = morph.parse(word)
	if (len(p) > 0):
		if (gender=='f'):
			if word.endswith("ый") or word.endswith("ой"):
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


def generate_phrase(tag):
	noun = get_noun(tag)
	

	r = random.random()
	if (r < 0.10):
		new_word = change_gender(get_adj(tag)["Word"], noun["Genus"]) + " " + noun["Word"]
	elif (r < 0.20):
		new_word = noun["Word"] + " " + get_addon(tag)["Word"]
	else:
		new_word = change_gender(get_adj(tag)["Word"], noun["Genus"]) + " " + noun["Word"] + " " + get_addon(tag)["Word"]

	if random.random()>(0.85):
		new_word += " и %s" % get_addon(tag)["Word"]

	if random.random()>(0.90):
		new_word = change_gender(get_adj(tag)["Word"], noun["Genus"]) + " " + new_word

	return new_word

if __name__=="__main__":

	try:
		tag = sys.argv[1]
	except IndexError:
		tag = None

	if (tag != None):
		assert tag in Tags.Tags, "Incorrect tag"

	l = []
	for i in range(30):
		l.append(generate_phrase(tag))

	print('\n'.join( sorted(l, key=len) ))
