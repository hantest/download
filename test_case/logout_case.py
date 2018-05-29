# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest, sys
sys.path.append("./modles")
sys.path.append("./test_page")
from models import myunit
from test_page.logout_page import LogoutPage

#
# 用例：退出
# time：2018-5-29
#

class Logout(myunit.MyTest):
	''' 退出 '''
	
	def test_logout(self):
		''' 退出 '''
		LogoutPage(self.driver).logout_page()

	def dearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()

