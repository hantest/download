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
# 页面：VIP下载
# time:2018-5-24
# @HAN
#
class DownloadVipPage(Page):

	url = "/"
	zx_list_loc = (By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div[1]/ul/li[2]")  #最新上传tab
	detail_list_loc = (By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div[2]/div[2]/div/dl[1]") #第一个资源
	direct_download_loc = (By.CLASS_NAME, "direct_download") #页面中VIP下载按钮
	vipIgnoreP_loc = (By.ID, "vipIgnoreP")
	vip_btn_loc = (By.ID, "vip_btn")

	def zx_list(self):
		self.find_element(*self.zx_list_loc).click()

	def detail_list(self):
		self.find_element(*self.detail_list_loc).click()

	def direct_download(self):
		self.find_element(*self.direct_download_loc).click()

	def vipIgnoreP(self):
		self.find_element(*self.vipIgnoreP_loc)

	def vip_btn(self):
		self.find_element(*self.vip_btn_loc).click()


	def downloadvip_page(self):
		''' VIP用户下载资源 '''

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
				sleep(2)
				self.driver.get_screenshot_as_file("D:\\download\\download5\\img\\downloadVipQ_img.jpg")
				self.vip_btn()  #点击弹框中VIP下载按钮
				self.driver.get_screenshot_as_file("D:\\download\\download5\\img\\downloadVipH_img.jpg")
				sleep(3)

