# coding: utf-8

'''
Модуль для работы с json-хранилищами данных
Позволяет просматривать и редактировать хранимые слова для генерации
'''

import os
import json
import Tags
DATADIR = "./data"

def json_editor():
	# getting list of jsons in data folder:
	jsons = list( filter(lambda x: x.endswith(".json"), os.listdir(DATADIR)) )
	# print(type(jsons))
	print("Доступные файлы:")
	for index, filename in enumerate(jsons):
		print("%s: %s" % (index, filename))

	# index = raw_input("Enter file to open (index): ")
	index = 0
	print("Открываю %s" % jsons[index])
	f = open(DATADIR + "/" + jsons[index])
	f_data = f.read()
	json_data = json.loads(f_data)
	f.close()

	print("Введите команду, help для справки")

	command = input(">>> ")
	args = command.split(' ')[1:]
	command = command.split(' ')[0]

	while (command != "exit"):
		if (command == "help"):
			print_help()
		elif (command == "add"):
			pass
		elif (command == "list"):
			pass
		elif (command == "rm"):
			pass
		else:
			print("Неверная команда! Введите help для справки")

		command = input(">>> ")
		args = command.split(' ')[1:]
		command = command.split(' ')[0]

def print_help():
	print()
	print("help - эта информация")
	print()
	print("add $word $genus $part $tags")
	print("word: русское слово, genus: род слова (m - мужской, f- женский)")
	print("tags: тэги. Список возможных тэгов: %s " % ", ".join(Tags.Tags))
	print()
	print("rm $word")
	print("word: слово, которое необходимо удалить")
	print()
	print('list')
	print('Выводит список слов')

def get_word_dict(word, genus, tags):
	# asserts here
	assert genus=='m' or genus=='f', "Genus is incorrect"
	assert type(tags) is list, "Tags is not a list"
	assert len(word)>0 and word.isalpha(), "Word is incorrect"

	word = {"Word": word.lower(), "Genus": genus, "Tags": tags}
	return word


if __name__== '__main__':
	json_editor()
	# print(get_word_dict("Привет", "m", [Tags.ITEM]))
