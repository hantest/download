# coding=utf-8

from selenium import webdriver
import unittest, sys
sys.path.append("./modles")
sys.path.append("./test_page")
from models import myunit
from test_page.search_page import SearchPage

#
# 功能：首页搜索
# time：2018-6-1
# @HAN
#

class Search(myunit.MyTest):
	''' 首页-搜索 '''

	def test_search(self):
		'''' 搜索 '''
		SearchPage(self.driver).search_page()

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()