# coding: utf-8

import sys
import Tags
import random
from WordUtils import *

def print_help():
	print("Синтаксис: PhraseGen [Тег] [Число]")
	print("Доступные теги %s и All - для генерации без учета тегов" % (", ".join(Tags.Tags)))
	print("По умолчанию число фраз - 30")

def generate_boss(noun):
	new_word = noun["Word"].title()

	title = ""
	if (random.random()<0.5):
		title = ", " + get_noun(Tags.CREATURE)["Word"] + " " + get_addon(Tags.CREATURE)["Word"]
	else:
		title = " " + get_adj()["Word"]

	new_word += title

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

	new_word.replace("  ", " ")

	return new_word



if __name__=="__main__":
	tag = None
	try:
		tag = sys.argv[1]
		if (tag == "All"):
			tag = None
	except IndexError:
		print_help()
		exit()

	phrase_count = 30
	try:
		phrase_count = int(sys.argv[2])
	except ValueError:
		print("Неправильное число фраз")
		exit()
	except IndexError:
		pass


	if (tag != None):
		assert tag in Tags.Tags, "Incorrect tag"

	l = []
	for i in range(phrase_count):
		l.append(generate_phrase(tag))

	print('\n'.join( sorted(l, key=len) ))