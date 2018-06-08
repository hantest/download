# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, sys
sys.path.append("./modles")
sys.path.append("./test_page")
from models import myunit
from test_page.rank_page import RankPage

#
# 功能：排行榜
# time：2018-6-8
# @HAN
#

class Rank(myunit.MyTest):
	''' 排行榜 '''

	def test_rank(self):
		''' 排行榜 '''
		RankPage(self.driver).rank_page()

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()