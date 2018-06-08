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
# 用例：收藏资源
# time:2018-5-28
# @HAN
#
class CollectPage(Page):


		zx_list_loc = (By.CLASS_NAME, "tab_item")  #最新上传tab
		detail_list_loc = (By.XPATH, "//*[@class='album_detail_wrap']/dl[1]") #最新上传列表第一个资源
		favorite_loc = (By.ID, "favorite")  #收藏按钮
		dl_lock_loc = (By.ID, "dl_lock") #收藏弹出框
		my_favorite_loc = (By.XPATH, "//*[@id='dl_lock']/h4/a") #弹框中我的收藏

		def zx_list(self):
			self.find_element(*self.zx_list_loc).click()

		def detail_list(self):
			self.find_element(*self.detail_list_loc).click()
		
		def favorite(self):
			self.find_element(*self.favorite_loc).click()

		def dl_lock(self):
			self.find_element(*self.dl_lock_loc)

		def my_favorite(self):
			self.find_element(*self.my_favorite_loc).click()


		def collect_page(self):
			''' 资源收藏 '''
			LoginPage(self.driver).login_page()
			self.zx_list()
			self.detail_list()

			#多窗口切换
			now_handle = self.driver.current_window_handle  #获取当前窗口
			all_handle = self.driver.window_handles  #获取全部窗口句柄集合
			for handle in all_handle:
				if handle != now_handle:
					self.driver.switch_to_window(handle)  #切换到指定的页面
					self.favorite()
					self.dl_lock()
					self.my_favorite()
					sleep(3)