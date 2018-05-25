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
from test_page.login_page import LoginPage

#
# 用例：登录
# time:2018-4-25
# @HAN
#
class Login(myunit.MyTest):
	
	def test_login(self):
		''' 用户登陆 '''
		
		LoginPage(self.driver).login_page()
		# 断言
		self.assertEqual(self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/dl/dt/a").text, u"nana_han", msg="fail")
		print("ok ok ok")


	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main()
