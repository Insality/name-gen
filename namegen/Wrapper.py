# coding: utf-8

import sys
import random
from PhraseGen import generate_phrase


def print_help():
	print("Синтаксис: Wrapper noun m|f [Тег]")
	print("Доступные теги %s и All - для генерации без учета тегов" % (", ".join(Tags.Tags)))


if __name__=="__main__":
	tag = None
	try:
		tag = sys.argv[3]
		if (tag == "All"):
			tag = None
	except IndexError:
		print_help()
		exit()

	noun = {"Word": sys.argv[1], "Genus": sys.argv[2]}

	phrase = generate_phrase(tag, noun=noun)

	sys.stdout.write(phrase)
