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
from test_page.album_page import AlbumPage

#
# 用例：专辑管理
# time：2018-5-29
# @HAN
#

class Album(myunit.MyTest):


	def test_album(self):
		''' 专辑管理 '''
		AlbumPage(self.driver).album_page()

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()