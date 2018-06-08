# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest, sys
from .base import Page

#
# 用例：登录
# time:2018-4-25
# @HAN
#
class LoginPage(Page):

	url = "/"
	login_loc = (By.LINK_TEXT, u"登录")  #右上角登陆按钮
	login_user_loc = (By.XPATH, "//div[@class='login-part']/h3/a")  #账号登陆
	username_loc = (By.ID, "username") #账号输入框
	password_loc = (By.ID, "password") #密码输入框
	login_button_loc = (By.CLASS_NAME, "logging") #登陆按钮


	def login(self):
		self.find_element(*self.login_loc).click()

	def login_user(self):
		self.find_element(*self.login_user_loc).click()

	def username(self,username):
		self.find_element(*self.username_loc).send_keys(username)

	def password(self,password):
		self.find_element(*self.password_loc).send_keys(password)

	def login_button(self):
		self.find_element(*self.login_button_loc).click()


	# 定义登陆入口
	def login_page(self,username="nana_han",password="hannana0309"):
		''' 用户登陆 '''
		self.open()
		self.login()
		self.login_user()
		self.username(username)
		self.password(password)
		self.login_button()
		sleep(3)

