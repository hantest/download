# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest, sys
from .base import Page
from .login1_page import LoginPage

#
# 功能：普通用户下载
# 用例：1、资源分=0，积分/C币=0，获取验证码  2、下载自己上传的资源不扣除积分  3、资源分>0,积分/C币=0，开通VIP
# 		3、资源=0，积分/C币>0  4、资源分>0,积分/C币>0
# time：2018-6-11
# @HAN
#

class DownloadPage(Page):
	''' 普通用户下载 '''
	zx_list_loc = (By.CLASS_NAME, "tab_item")  #最新上传tab
	detail_list_loc = (By.XPATH, "//*[@class='album_detail_wrap']/dl[1]") #最新上传列表第一个资源
	ym_direct_download_loc = (By.XPATH, "//*[@class='dl_download dl_pdf']/a[2]")  #页面立即下载按钮
	noVipZeroP_loc = (By.ID, "noVipZeroP")  # 0积分资源定位框
	noVipNoEnoughPHasC_loc = (By.ID, "noVipNoEnoughPHasC")  # 积分不足有剩余C币定位框(测试账号cpongo8)
	dl_down_btn_loc = (By.LINK_TEXT, u"确认下载")  # 弹框中的确认下载按钮

	def zx_list(self):
		self.find_element(*self.zx_list_loc).click()

	def detail_list(self):
		self.find_element(*self.detail_list_loc).click()

	def ym_direct_download(self):
		self.find_element(*self.ym_direct_download_loc).click()

	def noVipNoEnoughPHasC(self):
		self.find_element(*self.noVipNoEnoughPHasC_loc)

	def dl_down_btn(self):
		sekf.find_element(*self.dl_down_btn).click()

	def download_page(self):
		''' 积分不足有剩余C币 '''
		LoginPage(self.driver).login_page(username="cpongo8",password="abc123")
		self.zx_list()
		sleep(2)
		self.detail_list()
		sleep(3)






