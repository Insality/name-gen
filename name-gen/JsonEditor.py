# coding: utf-8

'''
Модуль для работы с json-хранилищами данных
Позволяет просматривать и редактировать хранимые слова для генерации
'''

import os
import json

def json_editor():
	# getting list of jsons in data folder:
	jsons = filter(lambda x: x.endswith(".json"), os.listdir("./data"))
	print jsons
	pass


if __name__== '__main__':
	json_editor()