# coding=utf-8

from selenium import webdriver
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
	''' 用户登录 '''
	
	def test_login(self):
		''' 用户登陆 '''
		
		LoginPage(self.driver).login_page()

		#截取当前窗口，并指定截图图片的保存位置
		imgurl = "./img/"
		self.driver.get_screenshot_as_file(imgurl + "login_img.jpg")
		# 断言
		self.assertEqual(self.driver.find_element_by_class_name("user_name").text, u"my_profession", msg="fail")

	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main()
