# conding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest, sys
sys.path.append("./modles")
sys.path.append("./test_page")
from models import myunit
from test_page.nocollect_page import NocollectPage

#
# 用例：取消收藏
# time：2018-5-28
# @HAN
#

class Nocollect(myunit.MyTest):

	def test_nocollect(self):
		''' 取消收藏 '''
		NocollectPage(self.driver).nocollect_page()

		#截取当前窗口，并指定截图图片的保存位置
		self.driver.get_screenshot_as_file("D:\\download\\download5\\img\\nocollect_img.jpg")

	def dearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()

