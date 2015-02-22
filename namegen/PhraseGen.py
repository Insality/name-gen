# coding: utf-8

import sys
import Tags
import random
from WordUtils import *

def print_help():
	print("Синтаксис: PhraseGen [Тег] [Число]")
	print("Доступные теги %s, Boss и All - для генерации без учета тегов" % (", ".join(Tags.Tags)))
	print("По умолчанию число фраз - 30")

def generate_boss():
	noun = get_noun(Tags.CREATURE)
	noun_name = stem_noun(noun["Word"]) + get_end()["Word"]
	noun["Genus"] = "m"
	noun["Word"] = noun_name

	new_word = noun["Word"].title()

	title = ""
	# Name, [adj] noun [addon]
	if (random.random()<0.5):
		n = get_noun(Tags.CREATURE)
		title = n["Word"]
		r = random.random()
		if (r < 0.4):
			title = change_gender(get_adj(Tags.CREATURE)["Word"], n["Genus"]) + " " + title
		elif (r <0.8):
			title += " " + get_addon(Tags.CREATURE)["Word"]
		else:
			title = change_gender(get_adj(Tags.CREATURE)["Word"], n["Genus"]) + " " + title + " " + get_addon(Tags.CREATURE)["Word"]

		title = ", " + title
	else:
		# Name adj
		title = " " + get_adj()["Word"]

	new_word += title

	return new_word

def generate_phrase(tag, noun=None):
	if (noun == None):
		noun = get_noun(tag)


	new_word = ""

	addon_first = get_addon(tag)["Word"]
	addon_first_added = False
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
		addon_first_added = True
	elif (r < 0.20):
		new_word = adj_first + " " + noun["Word"]
	else:
		new_word = adj_first + " " + noun["Word"] + " " + addon_first
		addon_first_added = True

	if random.random()>(0.85):
		if (addon_first_added):
			new_word += " и"
		new_word += " " + addon_second

	if random.random()>(0.90):
		new_word = change_gender(get_adj(tag)["Word"], noun["Genus"]) + " " + new_word

	new_word = new_word.replace("  ", " ")

	return new_word



if __name__=="__main__":
	boss_mode = False
	tag = None
	try:
		tag = sys.argv[1]
		if (tag == "All"):
			tag = None
		if (tag == "Boss"):
			boss_mode = True
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
		if (boss_mode):
			l.append(generate_boss())
		else:
			l.append(generate_phrase(tag))

	print('\n'.join( sorted(l, key=len) ))