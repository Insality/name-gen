# coding: utf-8

'''
Модуль для работы с json-хранилищами данных
Позволяет просматривать и редактировать хранимые слова для генерации
'''

import os
import json
import Tags
import codecs
from WordUtils import get_word_dict

DATADIR = "./data"

def json_editor():
	# getting list of jsons in data folder:
	jsons = list( filter(lambda x: x.endswith(".json"), os.listdir(DATADIR)) )
	# print(type(jsons))
	print("Доступные файлы:")
	for index, filename in enumerate(jsons):
		print("%s: %s" % (index, filename))

	index = int( input("Enter file to open (index): "))
	# index = 0
	print("Открываю %s" % jsons[index])
	f = codecs.open(DATADIR + "/" + jsons[index], 'r', encoding='utf8')
	f_data = f.read()
	json_data = json.loads(f_data)
	f.close()

	print("Файл загружен, число слов %i" % len(json_data["data"]))
	print("Введите команду, help для справки")

	command = input(">>> ")
	# command = "add безысхощжность m Item Location"
	args = command.split(' ')[1:]
	command = command.split(' ')[0]

	while (command != "exit"):
		if (command == "help"):
			print_help()

		elif (command == "add"):
			word = args[0]
			try:
				genus = args[1]
				tags = args[2:]
			except IndexError:
				genus = "m"
				tags = []
			remove_word(args[0], json_data)
			try:
				cur_word = get_word_dict(word, genus, tags)
				json_data["data"].append(cur_word)
				print("Добавлено %s" % cur_word['Word'])
			except AssertionError:
				print("Неправильный формат слова")

		elif (command == "list"):
			word_list = []
			for word in json_data["data"]:
				word_list.append(word["Word"])
			print(", ".join( sorted(word_list)))

		elif (command == "rm"):
			remove_word(args[0], json_data)

		else:
			print("Неверная команда! Введите help для справки")

		command = input(">>> ")
		args = command.split(' ')[1:]
		command = command.split(' ')[0]

	# saving:
	f = codecs.open(DATADIR + "/" + jsons[index], 'w', encoding='utf8')
	f.write(json.dumps(json_data, ensure_ascii=False))
	f.close()

def remove_word(word, json_data):
	for tup in json_data["data"]:
		if tup["Word"] == word:
			json_data["data"].remove(tup)
			print("Удалено %s" % word)
			break

def print_help():
	print()
	print("help - эта информация")
	print()
	print("add $word $genus $tags")
	print("word: русское слово, genus: род слова (m - мужской, f- женский)")
	print("tags: тэги. Список возможных тэгов: %s " % ", ".join(Tags.Tags))
	print("Пример: add Слово m Item Location")
	print()
	print("rm $word")
	print("word: слово, которое необходимо удалить")
	print()
	print('list')
	print('Выводит список слов')
	print()
	print('exit')
	print('Сохраняет и выходит из редактирования')


if __name__== '__main__':
	json_editor()
	# print(get_word_dict("Привет", "m", [Tags.ITEM]))
