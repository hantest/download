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
from .downloadvip_page import DownloadVipPage

#
# 功能：资源举报
# 用例：1、未下载资源举报 2、举报自己的资源 3、下载后举报，被举报后再次举报 4、举报后直接点击取消
# time:2018-6-1
# @HAN
#

class ReportPage(Page):

	zx_list_loc = (By.XPATH, "//ul[@class='tab_list clearfix']/li[2]")  #最新上传tab
	detail_list_loc = (By.XPATH, "//*[@class='tab_page tab2_con']/div/dl[1]") #最新上传列表第一个资源

	report_loc = (By.ID, "download_report") #点击举报按钮

	download_no_loc = (By.ID, "download") #未下载举报框定位
	download_close_loc = (By.XPATH, "//*[@id='download']/i")  # 未下载举报框关闭按钮

	my_resource_loc = (By.LINK_TEXT, u"我的资源") #二级导航-我的资源
	my_list_loc = (By.XPATH, "//*[@class='item uresource']/ul/li[1]/div/div[2]/h3/a") #上传资源TAB-第一个资源
	myself_loc = (By.ID, "myself")  #举报自己的资源弹框定位
	myself_close_loc = (By.XPATH, "//*[@id='myself']/i")  #举报自己的资源关闭按钮

	dlReport_loc = (By.ID, "dlReport")  #下载后举报弹框定位 
	report_type_loc = (By.ID, "report_type") #举报类型
	report_option_loc = (By.XPATH, "//*[@id='report_type']/option[3]")  # 选额举报类型
	report_description_loc = (By.ID, "report_description")  #详细原因
	btn_submit_loc = (By.ID, "btn_submit")  #提交按钮
	cancel_loc = (By.XPATH, "//*[@id='reportform']/div[2]/button[1]")  #取消按钮
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

	def report_type(self):
		self.find_element(*self.report_type_loc).click()

	def report_option(self):
		self.find_element(*self.report_option_loc).click()

	def report_description(self):
		self.find_element(*self.report_description_loc).send_keys("测试人员测试，看到会删除！！")

	def btn_submit(self):
		self.find_element(*self.btn_submit_loc).click()

	def cancel(self):
		self.find_element(*self.cancel_loc).click()

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
				self.driver.close()
				self.driver.switch_to_window(handle)  #切换到制定的页面
				self.report()
				self.download_no()
				self.driver.get_screenshot_as_file("./img/report1.jpg")
				sleep(2)
				#self.download_close()



	def report_myresource_page(self):
		''' 举报自己的资源 '''

		LoginPage(self.driver).login_page()
		self.my_resource()
		self.my_list()

		#多窗口切换
		now_handle = self.driver.current_window_handle  #获取当前窗口
		all_handle = self.driver.window_handles  #获取全部窗口句柄集合
		for handle in all_handle:
			if handle != now_handle:
				self.driver.switch_to_window(handle)  #切换到制定的页面
				self.report()
				self.myself()
				self.driver.get_screenshot_as_file("./img/myself.jpg")
				sleep(2)
				self.myself_close()



	def report_not_modify_page(self):
		''' 举报不修改内容，直接点击取消 '''

		DownloadVipPage(self.driver).downloadvipy_page()
		self.report()
		self.dlReport()
		sleep(3)
		self.cancel()
		self.driver.get_screenshot_as_file("./img/举报取消.jpg")

	
	'''
	def report_download_page(self):
		#下载资源后举报,已经被举报过再次举报

		DownloadVipPage(self.driver).downloadvipy_page()
		self.report()
		self.dlReport()
		self.report_type()
		self.report_option()
		self.report_description()
		self.driver.get_screenshot_as_file("./img/dlReport.jpg")
		self.btn_submit()
		sleep(2)
		self.driver.switch_to_alert().accept()
		self.report()
		self.btn_submit()
		self.driver.get_screenshot_as_file("./img/已经举报过.jpg")
		self.driver.switch_to_alert().accept()
		sleep(2)
	'''