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
from test_page.download_page import DownloadPage

class Download(myunit.MyTest):
	''' 普通用户下载 '''

	def test_download1(self):
		''' 积分不足有剩余C币 '''
		DownloadPage(self.driver).downloadHasC_page()
		
	def test_download2(self):
		''' 资源大于0，积分和C币等于0 '''
		DownloadPage(self.driver).downloadNoJC_page()
		self.assertEqual(self.driver.find_element_by_xpath("//*[@id='noVipNoEnoughPNoC']/div[3]/span/a").text, u"积分和C币不足，点我赚C币吧！", msg="fail")

	def test_download3(self):
		''' 下载自己的资源 '''
		DownloadPage(self.driver).download_my_page()
		self.assertEqual(self.driver.find_element_by_xpath("//*[@id='personal_wrap']/dd/a").text, u"cpongo4", msg="fail")

	def test_download4(self):
		''' 资源/积分/C币 == 0 '''
		DownloadPage(self.driver).download_JC_page()
		self.assertEqual(self.driver.find_element_by_xpath("//*[@id='noVipZeroP']/div[3]/div[1]/a").text, u"点击完成任务获取下载码", msg="fail")


	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()