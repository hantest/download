# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest, sys
sys.path.append("./modles")
sys.path.append("./test_page")
from models import myunit
from test_page.collect_page import CollectPage

#
# 用例：收藏资源
# time:2018-4-26
# @HAN
#
class Collect(myunit.MyTest):


	def test_collect(self):
		''' 资源收藏 '''
		CollectPage(self.driver).collect_page()

	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main()