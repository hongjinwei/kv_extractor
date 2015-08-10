__author__ = 'BAO'
# -*- coding: utf-8 -*-

from http_query import get_with_auto_decode
from file_operator import save_as_resource
from file_operator import read_resource
import lxml.html
from tool import trim_word
from tool import extract_content


parser = lxml.html

#from baidu import  generate_request_url
import baidu

# resstr = get_with_auto_decode(baidu.generate_request_url("刘德华"))


def test1() :
	resstr = get_with_auto_decode(r"http://baike.baidu.com/search/word?word=%E6%B1%9F%E6%B3%BD%E6%B0%91")
	print resstr
	save_as_resource("jiang.html", resstr)


def test2() :
	xpath = '//*[@id="baseInfoWrapDom"]/div[2]/div[1]'
	content = read_resource("jiang.html")
	doc = parser.fromstring(content)

	title_list = doc.xpath('//*[@class="biTitle"]/text()')
	content_list = doc.xpath('//*[@class="biContent"]/text()')

	for index in range(len(title_list)) :
		btitle = extract_content(title_list[index].encode("utf8"))
		bcontent = extract_content(content_list[index].encode("utf8"))
		print btitle, bcontent

	print "--------------"


test2()