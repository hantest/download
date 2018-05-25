# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from time import sleep

#
# 用例：收藏资源、取消收藏
# time:2018-4-26
# @HAN
#
class Collect(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()  #浏览器全屏显示
		self.base_url = "https://download.csdn.net"
		sleep(3)


	def test_collect(self):
		''' 资源收藏 '''
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_xpath("/html/body/div[2]/div/div/ul/li[5]/a[1]").click()
		driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/h3/a").click()
		driver.find_element_by_id("username").send_keys("nana_han")
		driver.find_element_by_id("password").send_keys("Hannana0309!")
		driver.find_element_by_class_name("logging").click()
		sleep(3)


		#点击最新上传Tab
		driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div/div[1]/ul/li[2]").click()
		driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div/div[2]/div[2]/div/dl[1]").click()
		sleep(3)

		#多窗口切换
		now_handle = driver.current_window_handle  #获取当前窗口
		print(now_handle)  #输出当前窗口句柄
		all_handle = driver.window_handles  #获取全部窗口句柄集合
		print(all_handle)  #输出全部句柄

		for handle in all_handle:
			if handle != now_handle:
				print(handle)
				driver.switch_to_window(handle)  #切换到制定的页面
				driver.find_element_by_id("favorite").click()
				driver.find_element_by_id("dl_lock")
				driver.find_element_by_xpath("//*[@id='dl_lock']/h4/a").click()
				sleep(3)



	def test_Nocollect(self):
		''' 取消收藏 '''

		driver = self.driver
		driver.get(self.base_url + "/my/favs")
		driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/h3/a").click()
		driver.find_element_by_id("username").send_keys("nana_han")
		driver.find_element_by_id("password").send_keys("Hannana0309!")
		driver.find_element_by_class_name("logging").click()
		sleep(3)

		driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/div/div/ul/li[1]/div/div[2]/div[4]/a").click()
		driver.switch_to_alert().accept()
		sleep(5)

	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main()