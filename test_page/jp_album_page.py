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
	#精品专辑-点击用户名定位元素
	dl_album_btn_loc = (By.CLASS_NAME, "dl_album_btn") #顶部图片切换
	album_name_loc = (By.CLASS_NAME, "album_name") #顶部图片中用户名
	contri_name_loc = (By.CLASS_NAME, "contri_name")  #专辑贡献榜中用户名
	album_per_img_loc = (By.CLASS_NAME, "album_per_img")  #专辑首页列表用户图片
	album_per_name_loc = (By.CLASS_NAME, "album_per_name")  #专辑首页列表用户名

	def dl_album_btn(self):
		self.find_element(*self.dl_album_btn_loc).click()

	def album_name(self):
		self.find_element(*self.album_name_loc).click()

	def contri_name(self):
		self.find_element(*self.contri_name_loc).click()

	def album_per_img(self):
		self.find_element(*self.album_per_img).click()

	def album_per_name(self):
		self.find_element(*self.album_per_name).click()



	def dl_album_page(self):
		''' 顶部图片切换，点击用户名 '''

		# ****用例：点击顶部图片后，点击右侧用户名***
		LoginPage(self.driver).login_page()
		self.open()
		self.dl_album_btn()
		self.driver.get_screenshot_as_file("./img/图片切换.jpg")
		self.album_name()
		self.driver.get_screenshot_as_file("./img/顶部用户名跳转.jpg")
		sleep(3)
