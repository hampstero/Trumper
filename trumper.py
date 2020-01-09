import sys
from string import punctuation
import random
from collections import defaultdict

def trumpify(file):
	trump_list = list()
	with open(file) as file_name:
		file_list = list(file_name.read().split())
		for word in file_list:
			trump_list.append(word.lower().strip(punctuation))
	return trump_list

def dictionary1(corpus):
	limit = len(corpus)-1
	dict1_to_1=defaultdict(list)
	for index, word in enumerate(corpus):
		if index < limit:
			suffix = corpus[index+1]
			dict1_to_1[word].append(suffix)
	return dict1_to_1

def dictionary2(corpus):
	limit = len(corpus)-2
	dict2_to_1=defaultdict(list)
	for index, word in enumerate(corpus):
		if index < limit:
			key = word + ' ' + corpus[index+1]
			suffix=corpus[index+2]
			dict2_to_1[key].append(suffix)
	return dict2_to_1

def dictionary3(corpus):
	limit = len(corpus)-3
	dict3_to_1=defaultdict(list)
	
	for index, word in enumerate(corpus):
		if index < limit:
			key = word + ' ' + corpus[index+1] + ' ' + corpus[index+2]
			suffix=corpus[index+3]
			dict3_to_1[key].append(suffix)
	
	return dict3_to_1

def word_after_single(prefix,suffix_map_1):
	return suffix_map_1.get(prefix)

def word_after_double(prefix,suffix_map_2):
	return suffix_map_2.get(prefix)

def word_after_triple(prefix,suffix_map_3):
	return suffix_map_3.get(prefix)

def stupid_talk(suffix_map_1,suffix_map_2,suffix_map_3,corpus):
	speech = []
	word = random.choice(corpus)
	speech.append(word)
	word_choices = word_after_single(word,suffix_map_1)

	while (len(word_choices) == 0):
		prefix = random.choice(corpus)
		word_choices= word_after_single(prefix,suffix_map_1)

	word = random.choice(word_choices)
	speech.append(word)

	while True:

		prefix = speech[-2] + ' ' + speech[-1]
		word_choices=word_after_double(prefix,suffix_map_2)

		while (len(word_choices) == 0):
			index = random.randint(0,len(corpus)-2)
			prefix = corpus[index] + ' ' + corpus[index+1]
			word_choices=word_after_double(prefix,suffix_map_2)

		word = random.choice(word_choices)
		speech.append(word)

		if (len(speech) >= 100):
			break
		
	return speech

corpus = trumpify('speeches.txt')
dict1 = dictionary1(corpus)
dict2 = dictionary2(corpus)
dict3 = dictionary3(corpus)
speech = stupid_talk(dict1, dict2, dict3, corpus)
print(*speech, sep=' ')