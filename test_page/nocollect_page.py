# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest, io, sys
from .base import Page
from .login_page import LoginPage
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#
# 页面：取消收藏
# time：2018-5-29
# @HAN
#

class NocollectPage(Page):

	my_favs_loc = (By.LINK_TEXT, u"我的收藏")  # 二级导航我的收藏
	flag_list_loc = (By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/div/div/ul/li[1]/div/div[2]/div[4]/a")  #取消收藏按钮

	def my_favs(self):
		self.find_element(*self.my_favs_loc).click()

	def flag_list(self):
		self.find_element(*self.flag_list_loc).click()


	def nocollect_page(self):
		''' 取消收藏 '''
		LoginPage(self.driver).login_page()
		self.my_favs()
		self.driver.get_screenshot_as_file("D:\\download\\download5\\img\\myfavs_img.jpg")  # 我的收藏页面截图
		self.flag_list()
		self.driver.switch_to_alert().accept()
		#截取当前窗口，并指定截图图片的保存位置
		self.driver.get_screenshot_as_file("D:\\download\\download5\\img\\nocollect_img.jpg")  #取消收藏资源截图
		sleep(3)

