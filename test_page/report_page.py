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
# 功能：资源举报
# 用例：1、未下载资源举报 2、举报自己的资源 3、下载后举报 4、资源已经被举报过
# time:2018-6-1
# @HAN
#

class ReportPage(Page):

	zx_list_loc = (By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div[1]/ul/li[2]")  #最新上传tab
	detail_list_loc = (By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div[2]/div[2]/div/dl[1]")  #点击第一个资源

	report_loc = (By.ID, "download_report") #点击举报按钮

	download_no_loc = (By.ID, "download") #未下载举报框定位
	download_close_loc = (By.XPATH, "//*[@id='download']/i")  # 未下载举报框关闭按钮

	my_resource_loc = (By.LINK_TEXT, u"我的资源") #二级导航-我的资源
	my_list_loc = (By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/div/div/ul/li[1]/div/div[2]/h3/a") #上传资源TAB-第一个资源
	myself_loc = (By.ID, "myself")  #举报自己的资源弹框定位
	myself_close_loc = (By.XPATH, "//*[@id='myself']/i")  #举报自己的资源关闭按钮

	dlReport_loc = (By.ID, "dlReport")  #下载后举报弹框定位  
	dlReport_close_loc = (By.XPATH, "//*[@id='dlReport']/i")  #下载举报弹框关闭按钮


	def zx_list(self):
		self.find_element(*self.zx_list_loc).click()

	def detail_list(self):
		self.find_element(*self.detail_list_loc).click()

	def report(self):
		self.find_element(*self.report_loc).click()

	def download_no(self):
		self.find_element(*self.download_no_loc)

	def download_close(self):
		self.find_element(*self.download_close_loc).click()

	def my_resource(self):
		self.find_element(*self.my_resource_loc).click()

	def my_list(self):
		self.find_element(*self.my_list_loc).click()

	def myself(self):
		self.find_element(*self.myself_loc)

	def myself_close(self):
		self.find_element(*self.myself_close_loc).click()

	def dlReport(self):
		self.find_element(*self.dlReport_loc)

	def dlReport_close(self):
		self.find_element(*self.dlReport_close_loc).click()


	def report_notdownload_page(self):
		''' 未下载资源举报 '''
		LoginPage(self.driver).login_page()
		self.zx_list()
		self.detail_list()

		#多窗口切换
		now_handle = self.driver.current_window_handle  #获取当前窗口
		all_handle = self.driver.window_handles  #获取全部窗口句柄集合

		for handle in all_handle:
			if handle != now_handle:
				self.driver.switch_to_window(handle)  #切换到制定的页面
				self.report()
				self.download_no()
				self.driver.get_screenshot_as_file("./img/report1.jpg")
				sleep(2)
				self.download_close()


	def report_myresource_page(self):
		''' 举报自己的资源 '''
		LoginPage(self.driver).login_page()
		self.my_resource()
		self.my_list()

