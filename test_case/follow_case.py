# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
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
	''' 关注 '''

	def test_follow(self):
		''' 关注 '''
		FollowPage(self.driver).follow_page()
		self.assertEqual(self.driver.find_element_by_xpath("//*[@id='personal_wrap']/dd/p[1]/span").text, u"已关注")

	def test_not_follow(self):
		''' 取消关注 '''
		FollowPage(self.driver).not_follow_page()
		self.assertEqual(self.driver.find_element_by_class_name("person_add_focus").text, "关注")

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()