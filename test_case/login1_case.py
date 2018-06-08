# coding=utf-8

from selenium import webdriver
import unittest, random, sys
sys.path.append("./modles")
sys.path.append("./test_page")
from models import myunit
from test_page.login1_page import LoginPage

#
# 用例：登录
# time:2018-4-25
# @HAN
#
class Login(myunit.MyTest):
	''' 用户登录 '''
	

	def login_verify(self,username="",password=""):
		LoginPage(self.driver).login_page(username,password)

	def test_login1(self):
		''' 用户名、密码为空 '''
		self.login_verify()
		self.assertEqual(self.driver.find_element_by_id("error-message").text, u"请输入用户名！")
		self.driver.get_screenshot_as_file("./img/login_empty.jpg")


	def test_login2(self):
		''' 用户名正确，密码为空 '''
		self.login_verify(username="cpongo1")
		self.assertEqual(self.driver.find_element_by_id("error-message").text, u"请输入密码！")
		self.driver.get_screenshot_as_file("./img/login_paw_empty.jpg")


	def test_login3(self):
		''' 用户名为空，密码正确 '''
		self.login_verify(password="abc123")
		self.assertEqual(self.driver.find_element_by_id("error-message").text, u"请输入用户名！")
		self.driver.get_screenshot_as_file("./img/login_username_empty.jpg")


	def test_login4(self):
		''' 用户名与密码不匹配 '''
		character = random.choice("abcdefghijk")  #随机取一个字符
		username = "cpongo" + character  #随机一个字符与cpongo进行拼接
		self.login_verify(username=username, password="abc123")
		self.assertEqual(self.driver.find_element_by_id("error-message").text, u"帐户名或登录密码不正确，请重新输入")
		self.driver.get_screenshot_as_file("./img/login_user_paw_error.jpg")


	def test_login5(self):
		''' 用户名密码正确 '''
		self.login_verify(username="cpongo8",password="abc123")
		self.assertEqual(self.driver.find_element_by_class_name("user_name").text, u"cpongo8", msg="fail")
		self.driver.get_screenshot_as_file("./img/login_ture.jpg")


	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main()
