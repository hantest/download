# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest, sys
from .base import Page
from .login_page import LoginPage

#
# 功能：首页搜索
# time：2018-6-1
# @HAN
#

class SearchPage(Page):

	keywords_input_loc = (By.CLASS_NAME, "keywords")  #搜索输入框
	keywords_btn_loc = (By.ID, "keywords")  #搜索按钮
	zxsc_list_loc = (By.LINK_TEXT, u"最新上传")  #最新上传TAB
	zdxz_list_loc = (By.LINK_TEXT, u"最多下载")  #最多下载TAB

	def keywords_input(self):
		self.find_element(*self.keywords_input_loc).send_keys("java")

	def keywords_btn(self):
		self.find_element(*self.keywords_btn_loc).click()

	def zxsc_list(self):
		self.find_element(*self.zxsc_list_loc).click()

	def zdxz_list(self):
		self.find_element(*self.zdxz_list_loc).click()

	def search_page(self):
		LoginPage(self.driver).login_page()
		self.keywords_input()
		self.keywords_btn()
		sleep(2)
		self.driver.get_screenshot_as_file("./img/search_img.jpg")
		self.zxsc_list()
		self.zdxz_list()

