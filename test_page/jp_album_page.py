# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest
from .base import Page
from .login_page import LoginPage

#
# 页面：精品专辑页面
# time：2018-6-5
# @HAN
#

class JpalbumPage(Page):

	url = "/album"
	#精品专辑-顶部元素定位
	dl_album_btn_loc = (By.CLASS_NAME, "dl_album_btn") #顶部图片切换
	album_name_loc = (By.CLASS_NAME, "album_name") #顶部图片中用户名

	def dl_album_btn(self):
		self.find_element(*self.dl_album_btn_loc).click()

	def album_name(self):
		self.find_element(*self.album_name_loc).click()

	def dl_album_page(self):
		''' 顶部图片切换，点击用户名 '''
		# 用例：点击顶部图片后，点击右侧用户名
		LoginPage(self.driver).login_page()
		self.open()
		self.dl_album_btn()
		self.driver.get_screenshot_as_file("./img/图片切换.jpg")
		self.album_name()

		all_handle = self.driver.window_handles
		now_handle = self.driver.current_window_handle
		for handle in all_handle:
			if handle != now_handle:
				self.driver.switch_to_window(handle)
				self.driver.get_screenshot_as_file("./img/顶部用户名跳转.jpg")
				sleep(3)


	#精品专辑-专辑贡献榜
	contri_cur_loc = (By.XPATH, "//*[@class='contri']/span[1]") #总榜
	contri_btn_loc = (By.XPATH, "//*[@class='contri']/span[2]")  #年榜
	contri_name_loc = (By.XPATH, "//*[@class='album_contri_c album_contri_c_show']/li[1]/label/a[2]")  #专辑贡献榜中用户名

	def contri_cur(self):
		self.find_element(*self.contri_cur_loc).click()

	def contri_btn(self):
		self.find_element(*self.contri_btn_loc).click()

	def contri_name(self):
		self.find_element(*self.contri_name_loc).click()


	def album_gx_page(self):
		''' 专辑贡献榜 '''
		#用例：进入精品专辑TAB页，切换年榜点击用户名，切换总榜点击用户名
		LoginPage(self.driver).login_page()
		self.open()
		self.contri_btn() #年榜
		sleep(2)
		self.driver.get_screenshot_as_file("./img/年榜.jpg")
		self.contri_name()
		sleep(5)
		all_handle = self.driver.window_handles
		now_handle = self.driver.current_window_handle
		for handle in all_handle:
			if handle == now_handle:
				self.driver.switch_to_window(handle)
				self.contri_cur()  #总榜
				sleep(3)
				self.driver.get_screenshot_as_file("./img/总榜.jpg")
				self.contri_name()
				sleep(3)



	#精品专辑-首页列表
	album_per_img_loc = (By.CLASS_NAME, "album_per_img")  #专辑首页列表用户图片
	album_per_name_loc = (By.CLASS_NAME, "album_per_name")  #专辑首页列表用户名

	def album_per_img(self):
		self.find_element(*self.album_per_img_loc).click()

	def album_per_name(self):
		self.find_element(*self.album_per_name_loc).click()

	def album_my_page(self):
		''' 点击用户头像或用户名跳转到个人中心 '''
		LoginPage(self.driver).login_page()
		self.open()
		self.album_per_img()
		sleep(3)

		now_handle = self.driver.current_window_handle
		all_handle = self.driver.window_handles
		for handle in all_handle:
			if handle == now_handle:
				self.driver.switch_to_window(handle)
				self.album_per_name()
				sleep(2)