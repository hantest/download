# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest
from .base import Page
from .login_page import LoginPage

#
# 用例：退出
# time：2018-5-31
# @HAN
#

class LogoutPage(Page):

	logout_loc = (By.XPATH, "/html/body/div[2]/div/div/ul/li[6]/div[2]/div[6]/a")  #退出按钮

	def logout(self):
		self.find_element(*self.logout_loc).click()

	def logout_page(self):
		''' 退出 '''
		LoginPage(self.driver).login_page()
		link = self.driver.find_element_by_class_name("loginCenter")
		ActionChains(self.driver).move_to_element(link).perform()
		sleep(2)
		imgurl = "./img/"
		self.driver.get_screenshot_as_file(imgurl + "logputQ_img.jpg")
		self.logout()
		self.driver.get_screenshot_as_file(imgurl + "logoutH_img.jpg")