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
# 页面：二级导航-排行榜
# time：2018-6-8
# @HAN
#

class RankPage(Page):

	rank_list_loc = (By.LINK_TEXT, u"排行榜")

	def rank_list(self):
		self.find_element(*self.rank_list_loc).click()


	def rank_page(self):
		''' 排行榜 '''
		LoginPage(self.driver).login_page()
		self.rank_list()
		self.driver.get_screenshot_as_file("./img/排行榜.jpg")