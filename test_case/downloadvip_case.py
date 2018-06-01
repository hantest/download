# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest, sys
sys.path.append("./modles")
sys.path.append("./test_page")
from models import myunit
from test_page.downloadvip_page import DownloadVipPage


#
# 用例：下载资源
# time:2018-5-24
# @HAN
#
class DownloadVip(myunit.MyTest):
	''' VIP下载 '''

	def test_downloady_vip(self):
		''' 页面VIP按钮 '''
		DownloadVipPage(self.driver).downloadvipy_page()

	def test_downloadg_vip(self):
		''' 跟随菜单VIP按钮 '''
		DownloadVipPage(self.driver).downloadvipg_page()

	def test_downloadx_vip(self):
		''' 相关推荐下载 '''
		DownloadVipPage(self.driver).downloadvipx_page()
		

	def tearDown(self):
		self.driver.quit()


if __name__  == "__main__":
	unittest.main()