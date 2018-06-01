# conding=utf-8

from selenium import webdriver
import unittest, sys
sys.path.append("./modles")
sys.path.append("./test_page")
from models import myunit
from test_page.report_page import ReportPage

#
# 功能：举报
# time：2018-6-1
# @HAN
#

class Report(myunit.MyTest):
	''' 举报 '''

	def test_report1(self):
		''' 未下载举报 '''
		ReportPage(self.driver).report_notdownload_page()

	


	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()