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
from test_page.myalbum_page import MyalbumPage

#
# 用例：专辑管理
# time：2018-5-29
# @HAN
#

class Myalbum(myunit.MyTest):


	def test_myalbum(self):
		''' 专辑管理 '''
		MyalbumPage(self.driver).myalbum_page()

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()