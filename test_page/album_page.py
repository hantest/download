# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from .base import Page
from .login_page import LoginPage

#
# 功能:专辑管理
# 用例：1、登陆download 2、点击二级导航我的资源页面 3、点击我的专辑 4、点击管理专辑 5、提交
# time：2018-5-31
# @HAN
#

class AlbumPage(Page):

	my_resource_loc = (By.LINK_TEXT, u"我的资源")
	my_album_loc = (By.LINK_TEXT, u"我的专辑")
	flag_loc = (By.CLASS_NAME, "flag") #专辑管理
	submit_btn_loc = (By.CLASS_NAME, "submit-btn")

	def my_resource(self):
		self.find_element(*self.my_resource_loc).click()

	def my_album(self):
		self.find_element(*self.my_album_loc).click()

	def flag(self):
		self.find_element(*self.flag_loc).click()

	def submit_btn(self):
		self.find_element(*self.submit_btn_loc).click()

	def album_page(self):
		''' 专辑管理 '''
		LoginPage(self.driver).login_page()
		self.my_resource()
		self.my_album()
		self.flag()

		now_handle = self.driver.current_window_handle
		all_handle = self.driver.window_handles

		for handle in all_handle:
			if handle != now_handle:
				self.driver.switch_to_window(handle)
				imgurl = "./img/"
				self.driver.get_screenshot_as_file(imgurl + "album_img.jpg")
				self.submit_btn()
				sleep(2)

