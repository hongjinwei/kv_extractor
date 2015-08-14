__author__ = 'BAO'
# -*- coding: utf-8 -*-

from file_operator import save_as_resource
from file_operator import  read_resource
from http_query import get_with_auto_decode
from urlparse import urljoin
import urllib2
from lxml import html
parser = html


def search(keyword):
	url = "https://en.wikipedia.org/w/index.php?search=" + keyword + "&title=Special%3ASearch&go=Go";
	response = urllib2.urlopen(url)
	print dir(response)
	html = response.read()
	url = response.geturl()
	print(url)
	return html


def wiki_content_extractor(wiki_page, homeurl):
	doc = parser.fromstring(wiki_page)
	ans = {}

	try:
		ans['title'] = doc.xpath("//h1[@id='firstHeading' and @class='firstHeading']/text()")[0]
	except:
		ans['title'] = ""

	try:
		con = doc.xpath("//div[@id='mw-content-text' and @class='mw-content-ltr']")[0]
		ans['content'] = con.xpath('string(.)')
		rel_links =[]
		links = con.xpath("//p/a")
		for link in links:
			try:
				rel_links.append(urljoin(homeurl, link.attrib['href']))
			except:
				pass

		ans['rel_link'] = rel_links
	except:
		ans['content'] = ""
		ans['rel_link'] = []

	try:
		pass
	except:
		ans['link'] = []

	return ans


def relative_content_extractor(rel_link):
	page = get_with_auto_decode(rel_link)
	doc = parser.fromstring(page)
	relative_content = doc.xpath("//div[@id='mw-content-text' and @class='mw-content-ltr']")[0].xpath('string(.)')
	return relative_content


def test1():
	url = "https://en.wikipedia.org/w/index.php?search=obama&title=Special%3ASearch&go=Go"
	html_page = get_with_auto_decode(url)
	print html_page
	save_as_resource("wiki/obama.html", html_page)
	return html_page


def test2():
	content = read_resource("/wiki/obama.html")
	doc = html.fromstring(content)
	# title = doc.xpath("//h1[@id='firstHeading' and @class='firstHeading']/text()")[0]
	con = doc.xpath("//div[@id='mw-content-text' and @class='mw-content-ltr']")[0]
	info = con.xpath("//p/a")

	# print dir(info[0])

	for e in info:
		print(e.attrib['href'])


if __name__ == "__main__":
	# test2()
	result = wiki_content_extractor(read_resource("/wiki/obama.html"), "https://en.wikipedia.org/wiki/Barack_Obama")
	print result
	print relative_content_extractor(result['rel_link'][0])
	# search("hello")