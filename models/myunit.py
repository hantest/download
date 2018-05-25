# coding=utf-8

from selenium import webdriver
import unittest
from time import sleep


class MyTest(unittest.TestCase):

	'''下载首页'''
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()  #浏览器全屏显示
		self.base_url = "http://download.csdn.net"
		sleep(5)

	def teatDown(self):
		self.driver.quit()