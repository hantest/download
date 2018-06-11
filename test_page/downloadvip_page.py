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


	zx_list_loc = (By.CLASS_NAME, "tab_item")  #最新上传tab
	detail_list_loc = (By.XPATH, "//*[@class='album_detail_wrap']/dl[1]") #最新上传列表第一个资源
	direct_download_loc = (By.CLASS_NAME, "direct_download") #页面中VIP下载按钮
	vip_down_loc = (By.XPATH, "//*[@class='follow_menu_r fr']/a")  #跟随菜单中的VIP下载按钮
	dl_reco_btn_loc = (By.CLASS_NAME, "dl_reco_btn")  #相关推荐立即下载
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

	def dl_reco_btn(self):
		self.find_element(*self.dl_reco_btn_loc).click()

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
				self.driver.get_screenshot_as_file("./img/downvip_y_img.jpg")
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
				js = "var q=document.body.scrollTop=100000"
				self.driver.execute_script(js)
				sleep(2)
				self.vip_down()  #点击下载按钮
				self.vipIgnoreP()  #弹出框定位
				self.driver.get_screenshot_as_file("./img/downVip_g_img.jpg")
				self.vip_btn()  #点击弹框中VIP下载按钮
				sleep(3)



	def downloadvipx_page(self):
		''' VIP下载-相关推荐 '''
		LoginPage(self.driver).login_page()
		self.zx_list()
		self.detail_list()

		#多窗口切换
		now_handlex = self.driver.current_window_handle #获取当前窗口句柄
		all_handlex = self.driver.window_handles  #获取所有窗口句柄
		for handlex in all_handlex:
			if handlex != now_handlex:
				self.driver.switch_to_window(handlex)
				#滚动条滚动
				js = "var q=document.body.scrollTop=10000"
				self.driver.execute_script(js)
				sleep(2)
				self.dl_reco_btn()  #点击下载按钮
				self.vipIgnoreP()  #弹出框定位
				self.driver.get_screenshot_as_file("./img/downVip_x_img.jpg")
				self.vip_btn()  #点击弹框中VIP下载按钮
				sleep(3)