__author__ = 'BAO'
# -*- coding: utf-8 -*-


def trim_word(word):
	return word.replace(" ", "")


def is_chinese(uchar):
	try:
		uchar = uchar.decode("utf8")
	finally:
		return u'\u4E00' <= uchar <= u'\u9FFF'


def is_content(uchar) :
	try:
		uchar = uchar.decode("utf8")
	finally:
		#中文
		if u'\u4E00' <= uchar <= u'\u9FFF':
			return True
		#数字
		elif u'\u0030' <= uchar <= u'\u0039':
			return True
		#英文
		elif u'\u0041' <= uchar <= u'\u005a' or u'\u0061' <= uchar <= u'\u007a':
			return True
		else:
			return False


def is_english(uchar):
	uchar = uchar.decode("utf8")
	return u'\u0041' <= uchar <= u'\u005a' or u'\u0061' <= uchar <= u'\u007a'


def extract_chinese(sentence):
	sentence = sentence.decode("utf8")
	return "".join([c for c in sentence if is_chinese(c)])


def extract_content(sentence):
	sentence = sentence.decode("utf8")
	ans = "".join([c for c in sentence if is_content(c)])
	return ans.encode("utf8")


def _show_character(sentence):
	try:
		sentence = sentence.decode("utf8")
	finally:
		print [c for c in sentence]


