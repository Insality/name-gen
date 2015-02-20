# coding: utf-8

'''
Модуль для работы с json-хранилищами данных
Позволяет просматривать и редактировать хранимые слова для генерации
'''

import os
import json
import Tags
import codecs

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
			genus = args[1]
			tags = args[2:]
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
			pass
		else:
			print("Неверная команда! Введите help для справки")

		command = input(">>> ")
		args = command.split(' ')[1:]
		command = command.split(' ')[0]

	# saving:
	f = codecs.open(DATADIR + "/" + jsons[index], 'w', encoding='utf8')
	f.write(json.dumps(json_data, ensure_ascii=False))
	f.close()


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
	print('exit')
	print('Сохраняет и выходит из редактирования')

def get_word_dict(word, genus, tags):
	# asserts here
	assert genus=='m' or genus=='f', "Genus is incorrect"
	assert type(tags) is list, "Tags is not a list"
	assert len(word)>0 and word.isalpha(), "Word is incorrect"

	tags = list (map(lambda x: x.title(), tags))

	for tag in tags:
		assert tag in Tags.Tags, "Tags is incorrect"

	word = {"Word": word.lower(), "Genus": genus, "Tags": tags}
	return word


if __name__== '__main__':
	json_editor()
	# print(get_word_dict("Привет", "m", [Tags.ITEM]))
