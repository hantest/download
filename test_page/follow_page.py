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
# 用例：关注
# time:2018-4-27
# @HAN
#

class FollowPage(Page):

	url = "/"
	zx_list_loc = (By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div[1]/ul/li[2]")  #最新上传tab
	detail_list_loc = (By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div[2]/div[2]/div/dl[1]")
	attention_btn_loc = (By.CLASS_NAME, "attention_btn") #关注

	def zx_list(self):
		self.find_element(*self.zx_list_loc).click()

	def detail_list(self):
		self.find_element(*self.detail_list_loc).click()

	def attention_btn(self):
		self.find_element(*self.attention_btn_loc).click()


	def follow_page(self):
		''' 关注 '''
		LoginPage(self.driver).login_page()
		#点击最新上传Tab
		self.zx_list()
		self.detail_list()
		sleep(3)

		#多窗口切换
		now_handle = self.driver.current_window_handle  #获取当前窗口
		all_handle = self.driver.window_handles  #获取所有窗口

		for handle in all_handle:
			if handle != now_handle:
				self.driver.switch_to_window(handle)
				self.attention_btn()
				self.driver.get_screenshot_as_file("./img/follow_img.jpg")
				sleep(3)
