__author__ = 'BAO'
# -*- coding: utf-8 -*-

from urllib import urlencode

def generate_request_url(str):
	url_pattern = r"http://baike.baidu.com/item/"
	url = url_pattern + str
	return url;

def generate_search_url(name):
	en_name = urlencode(name)
	return r"http://baike.baidu.com/search/word?word=" + en_name

def kv_exractor(baidu_html) :
	# try:
	pass
