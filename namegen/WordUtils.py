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
	# lenght_to_strip = len(noun)/2
	nl = len(noun)
	if (nl <= 4):
		return noun
	return noun[:random.randint(int(nl/2), nl-2)]

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

def generate_boss(noun):
	new_word = noun["Word"] + ", "

	titul = ""
	titul = get_noun(Tags.CREATURE)["Word"] + " " + get_addon(Tags.CREATURE)["Word"]

	new_word += titul

	return new_word

def generate_phrase(tag):
	noun = get_noun(tag)


	# Создаем имя уникального босса и заавершаем генерацию тут
	noun_name = noun["Word"]
	if (tag==Tags.CREATURE and random.random() < 0.2):

		noun_name = stem_noun(noun["Word"]) + get_end()["Word"]
		noun["Genus"] = "m"
		noun["Word"] = noun_name
		return generate_boss(noun)


	new_word = ""

	addon_first = get_addon(tag)["Word"]
	if (random.random() < 0.2):
		addon_first = get_adj_to_addon(addon_first, tag) + " " + addon_first

	addon_second = get_addon(tag)["Word"]
	if (random.random() < 0.2):
		addon_second = get_adj_to_addon(addon_second, tag) + " " + addon_second

	adj_first = change_gender(get_adj(tag)["Word"], noun["Genus"])
	adj_second = change_gender(get_adj(tag)["Word"], noun["Genus"])

	r = random.random()
	if (r < 0.10):
		new_word = noun["Word"] + " " + addon_first
	elif (r < 0.20):
		new_word = adj_first + " " + noun["Word"]
	else:
		new_word = adj_first + " " + noun["Word"] + " " + addon_first

	if random.random()>(0.85) and r < (0.10):
		new_word += " и %s" % addon_second

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
