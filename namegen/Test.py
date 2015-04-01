# coding: utf-8

import pymorphy2
from WordUtils import open_json

morph = pymorphy2.MorphAnalyzer()

def test_genus_all_words():
	print("Test genus of all noun words")
	nouns = open_json("noun.json")["data"]

	for noun in nouns:
		w = noun["Word"]
		g = noun["Genus"]
		predict_g = morph.parse(w)[0].tag.gender

		pg = "none"
		if (predict_g == "masc"): pg = "m"
		if (predict_g == "femn"): pg = "f"

		if (not g == pg and pg != "none"):
			print("Word %s is incorrect, now is %s" % (w, g))



if __name__=='__main__':
	test_genus_all_words()