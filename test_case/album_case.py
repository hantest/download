# coding=utf-8

from selenium import webdriver
import unittest, sys
sys.path.append("./modles")
sys.path.append("./test_page")
from models import myunit
from test_page.album_page import AlbumPage

#
# 功能：专辑管理-编辑（不修改内容直接提交）
# time：2018-5-31
# @HAN
#

class Album(myunit.MyTest):
	''' 专辑管理-编辑 '''

	def test_album(self):
		''' 专辑管理 '''
		AlbumPage(self.driver).album_page()

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()