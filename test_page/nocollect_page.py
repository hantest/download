# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest, sys
from .base import Page
from .collect_page import CollectPage

#
# 用例：取消收藏
# time：2018-5-28
# @HAN
#

class NocollectPage(Page):

	#取消收藏按钮
	flag_list_loc = (By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/div/div/ul/li[1]/div/div[2]/div[4]/a")

	def flag_list(self):
		self.find_element(*self.flag_list_loc).click()


	def nocollect_page(self):
		''' 取消收藏 '''
		CollectPage(self.driver).collect_page()
		self.flag_list()
		self.driver.switch_to_alert().accept()
		sleep(3)

