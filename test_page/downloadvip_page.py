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
# 用例：VIP下载
# time:2018-5-24
# @HAN
#
class DownloadVipPage(Page):

	url = "/"
	zx_list_loc = (By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div[1]/ul/li[2]")  #最新上传tab
	detail_list_loc = (By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div[2]/div[2]/div/dl[1]") #第一个资源
	direct_download_loc = (By.CLASS_NAME, "direct_download") #页面中VIP下载按钮
	vip_down_loc = (By.XPATH, "/html/body/div[22]/div/div[2]/a")  #跟随菜单中的VIP下载按钮
	vipIgnoreP_loc = (By.ID, "vipIgnoreP") #下载弹框
	vip_btn_loc = (By.ID, "vip_btn") #弹框中VIP下载按钮

	def zx_list(self):
		self.find_element(*self.zx_list_loc).click()

	def detail_list(self):
		self.find_element(*self.detail_list_loc).click()

	def direct_download(self):
		self.find_element(*self.direct_download_loc).click()

	def vip_down(self):
		self.find_element(*self.vip_down_loc).click()

	def vipIgnoreP(self):
		self.find_element(*self.vipIgnoreP_loc)

	def vip_btn(self):
		self.find_element(*self.vip_btn_loc).click()


	def downloadvipy_page(self):
		''' VIP下载-页面中 '''

		LoginPage(self.driver).login_page() #登陆
		self.zx_list()
		self.detail_list()

		#多窗口切换
		now_handle = self.driver.current_window_handle #获取当前窗口句柄
		all_handle = self.driver.window_handles  #获取所有窗口句柄
		for handle in all_handle:
			if handle != now_handle:
				self.driver.switch_to_window(handle)
				self.direct_download()  #点击下载按钮
				self.vipIgnoreP()  #弹出框定位
				self.driver.get_screenshot_as_file("./img/downvip_img.jpg")
				self.vip_btn()  #点击弹框中VIP下载按钮
				sleep(3)

	def downloadvipg_page(self):
		''' VIP下载-跟随菜单 '''

		LoginPage(self.driver).login_page()
		self.zx_list()
		self.detail_list()

		#多窗口切换
		now_handle1 = self.driver.current_window_handle #获取当前窗口句柄
		all_handle1 = self.driver.window_handles  #获取所有窗口句柄
		for handle1 in all_handle1:
			if handle1 != now_handle1:
				self.driver.switch_to_window(handle1)
				#滚动条滚动
				js = "var q=document.body.scrollTop=30000"
				self.driver.execute_script(js)
				sleep(2)
				self.vip_down()  #点击下载按钮
				self.vipIgnoreP()  #弹出框定位
				self.driver.get_screenshot_as_file("./img/downVip_img.jpg")
				self.vip_btn()  #点击弹框中VIP下载按钮
				sleep(3)



