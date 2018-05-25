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
from test_page.follow_page import FollowPage


#
# 用例：关注
# time:2018-4-27
# @HAN
#

class Follow(myunit.MyTest):

	def test_follow(self):
		''' 关注 '''
		FollowPage(self.driver).follow_page()


	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main()