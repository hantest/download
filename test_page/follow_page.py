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
# 用例：关注、取消关注
# time:2018-4-27
# @HAN
#

class FollowPage(Page):


	zx_list_loc = (By.CLASS_NAME, "tab_item")  #最新上传tab
	detail_list_loc = (By.XPATH, "//*[@class='album_detail_wrap']/dl[1]") #最新上传列表第一个资源
	attention_btn_loc = (By.CLASS_NAME, "attention_btn") #关注
	head_loc = (By.CLASS_NAME, "head") #右侧用户头像
	person_add_focus_loc = (By.CLASS_NAME, "person_add_focus") #个人中心取消关注按钮


	def zx_list(self):
		self.find_element(*self.zx_list_loc).click()

	def detail_list(self):
		self.find_element(*self.detail_list_loc).click()

	def attention_btn(self):
		self.find_element(*self.attention_btn_loc).click()

	def head(self):
		self.find_element(*self.head_loc).click()

	def person_add_focus(self):
		self.find_element(*self.person_add_focus_loc).click()



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
				fllow = self.driver.find_element_by_class_name("attention_btn").text
				if fllow == u"关注":
					self.attention_btn()
					self.driver.get_screenshot_as_file("./img/follow_img.jpg")
				else:
					self.driver.get_screenshot_as_file("./img/follow_img1.jpg")
				sleep(3)



	def not_follow_page(self):
		''' 取消关注 '''
		LoginPage(self.driver).login_page()
		self.zx_list()
		self.detail_list()
		sleep(3)

		#多窗口切换
		now_handle = self.driver.current_window_handle  #获取当前窗口
		all_handle = self.driver.window_handles  #获取所有窗口
		for handle in all_handle:
			if handle != now_handle:
				self.driver.close() #关闭第一个窗口
				self.driver.switch_to_window(handle)
				fllow = self.driver.find_element_by_class_name("attention_btn").text
				if fllow == u"关注":
					self.attention_btn()
					self.driver.get_screenshot_as_file("./img/follow_img.jpg")
					self.head()
					handles = self.driver.window_handles #获取所有的窗口
					for handle1 in handles:
						if handle1 != self.driver.current_window_handle:
							self.driver.close()
							self.driver.switch_to_window(handle1)
							sleep(3)
							self.person_add_focus()
							self.driver.get_screenshot_as_file("./img/关注后取消.jpg")
							sleep(3)
				else:
					self.head()
					handles = self.driver.window_handles #获取所有的窗口
					for handle1 in handles:
						if handle1 != self.driver.current_window_handle:
							self.driver.close()
							self.driver.switch_to_window(handle1)
							sleep(3)
							self.person_add_focus()
							self.driver.get_screenshot_as_file("./img/取消关注.jpg")
							sleep(3)
