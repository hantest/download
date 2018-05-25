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
from test_page.comment_page import CommentPage

#
# 用例：下载评论
# time:2018-5-24
# @HAN
#

class Comment(myunit.MyTest):

	def test_comment(self):
		''' 资源评论 '''
		CommentPage(self.driver).comment_page()

	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main()