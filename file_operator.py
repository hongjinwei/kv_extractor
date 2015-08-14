__author__ = 'BAO'
# -*- coding: utf-8 -*-

import sys
import os


def is_exist(path):
	return os.path.exists(path)


def is_file(src):
	return os.path.isfile(src)


def cur_file_dir():
	path = sys.path[0]
	#判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
	if os.path.isdir(path):
		return path
	elif os.path.isfile(path):
		return os.path.dirname(path)


directory = cur_file_dir() + "/resources/"
if not os.path.isdir(directory):
	os.mkdir(directory)


def save_as_resource(filename, content):
	content = content.encode('utf8')
	paths = filename.split("/")
	print paths
	real_filename = paths[-1]
	abspath = directory
	for i in range(len(paths) - 1):
		print i
		path = paths[i]
		if path == '':
			continue
		abspath = directory + path + "/"
		print abspath
		if not os.path.isdir(abspath):
			print "mkdir"
			os.mkdir(abspath)

	# print abspath
	f = abspath + real_filename
	fp = open(f, 'w')
	try:
		fp.write(content)
	except Exception, e:
		print Exception,e
	finally:
		fp.close()


def append_to_resource(filename, content):
	f = directory + filename
	fp = open(f, 'a')
	try:
		fp.write(content)
	except Exception, e:
		print Exception,e
	finally:
		fp.close()


def read_resource(filename):
	f = directory + filename
	fp = open(f, 'r')
	return fp.read()


def clean_page(html_page):
	pass

if __name__ == "__main__":
	print(cur_file_dir())
	# save_as_resource("test.txt", "aaa!")
	# append_to_resource("test.txt","bbb!")
	print read_resource("test.txt")