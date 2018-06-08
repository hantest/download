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
# 功能：评论
# 用例：1、没有下载过资源点击评论 2、资源被下载后评论 3、资源已经被评论过再次评论
# time:2018-5-24
# @HAN
#

class CommentPage(Page):  


	zx_list_loc = (By.CLASS_NAME, "tab_item")  #最新上传tab
	detail_list_loc = (By.XPATH, "//*[@class='album_detail_wrap']/dl[1]") #最新上传列表第一个资源
	direct_download_loc = (By.CLASS_NAME, "direct_download") #页面中VIP下载按钮
	vipIgnoreP_loc = (By.ID, "vipIgnoreP") #下载弹框
	vip_btn_loc = (By.ID, "vip_btn") #弹框中VIP下载按钮
	comment_top_loc = (By.XPATH, "//*[@class='dl_operate_r fr']/a[2]")  # 评论按钮
	commentbox_loc = (By.XPATH, "//*[@id='csdn_dl_commentbox']/li[2]/i[3]")  # 评价资源
	cc_body_loc = (By.ID, "cc_body") # 评论框
	btn_red_loc = (By.CLASS_NAME, "btn-red") # 提交评论按钮

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

	def comment_top(self):
		self.find_element(*self.comment_top_loc).click()

	def commentbox(self):
		self.find_element(*self.commentbox_loc).click()

	def cc_body(self):
		self.find_element(*self.cc_body_loc).send_keys("测试人员测试，看到后删除！")

	def btn_red(self):
		self.find_element(*self.btn_red_loc).click()


	def notdownload_comment_page(self):
		''' 资源未下载点击评论 '''
		LoginPage(self.driver).login_page()
		self.zx_list()
		self.detail_list()

		now_handle = self.driver.current_window_handle #获取当前窗口句柄
		all_handle = self.driver.window_handles  #获取所有窗口句柄
		for handle in all_handle:
			if handle != now_handle:
				self.driver.switch_to_window(handle)
				notdown = self.driver.find_element_by_xpath("//*[@class='cannot_com_b']/em").text
				if notdown == u"您可能没有下载过该资源":
					self.comment_top()
					self.driver.get_screenshot_as_file("./img/没有下载过点击评论.jpg")
				else:
					self.driver.close()



	def download_comment_page(self):
		''' 资源下载后评论 '''
		LoginPage(self.driver).login_page()
		self.zx_list()
		self.detail_list()

		now_handle = self.driver.current_window_handle #获取当前窗口句柄
		all_handle = self.driver.window_handles  #获取所有窗口句柄
		for handle in all_handle:
			if handle != now_handle:
				self.driver.switch_to_window(handle)
				notdown = self.driver.find_element_by_xpath("//*[@class='cannot_com_b']/em").text
				#判断资源是否下载过，没有下载则下载后评论，下载过则判断是否评论（评论过则关闭页面，没评论则进行评论）
				if notdown == u"您可能没有下载过该资源":
					self.direct_download()
					self.vipIgnoreP()
					self.driver.get_screenshot_as_file("./img/下载.jpg")
					self.vip_btn()
					sleep(2)
					self.driver.refresh()  #刷新页面
					self.comment_top()
					self.commentbox()
					self.cc_body()
					self.btn_red()
					sleep(3)
				elif notdown == u"您已经发表过评论":
					print(u"该资源已经评论过！")
					self.driver.get_screenshot_as_file("./img/已经发表过评论")
					self.driver.close()
					sleep(2)
				else:
					self.comment_top()
					self.commentbox()
					self.cc_body()
					self.btn_red()
					sleep(3)
