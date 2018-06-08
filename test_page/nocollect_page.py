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
# 用例：取消收藏
# time：2018-5-28
# @HAN
#

class NocollectPage(Page):

	my_favs_loc = (By.LINK_TEXT, u"我的收藏")  # 二级导航我的收藏
	flag_list_loc = (By.XPATH, "//*[@class='item uresource']/ul/li[1]/div/div[2]/div[4]/a")  #取消收藏按钮

	def my_favs(self):
		self.find_element(*self.my_favs_loc).click()

	def flag_list(self):
		self.find_element(*self.flag_list_loc).click()

	def nocollect_page(self):
		''' 取消收藏 '''
		LoginPage(self.driver).login_page()
		self.my_favs()
		self.driver.get_screenshot_as_file("./img/nocollectQ_img.jpg")
		self.flag_list()
		self.driver.switch_to_alert().accept()
		sleep(3)
		self.driver.get_screenshot_as_file("./img/nocollectH_img.jpg")