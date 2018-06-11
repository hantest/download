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

	def test_download(self):
		''' 积分不足有剩余C币 '''
		DownloadPage(self.driver).download_page()