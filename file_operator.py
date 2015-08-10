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


def save_as_resource(filename, content):
	content = content.encode('utf8')
	f = directory + filename
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

if __name__ == "__main__":
	print(cur_file_dir())
	# save_as_resource("test.txt", "aaa!")
	# append_to_resource("test.txt","bbb!")
	print read_resource("test.txt")