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
# 页面：退出页面
# time：2018-5-29
# @HAN
#

class LogoutPage(Page):

	logout_loc = (By.XPATH, "/html/body/div[2]/div/div/ul/li[6]/div[2]/div[6]/a")  #退出按钮

	def logout(self):
		self.find_element(*self.logout_loc).click()

	def logout_page(self):
		''' 退出 '''
		LoginPage(self.driver).login_page()
		link = self.driver.find_element_by_class_name("loginCenter") #头像悬浮
		ActionChains(self.driver).move_to_element(link).perform()
		sleep(3)
		self.driver.get_screenshot_as_file("D:\\download\\download5\\img\\logoutQ_img.jpg") #悬浮操作截取图片
		self.logout()
		self.driver.get_screenshot_as_file("D:\\download\\download5\\img\\logoutH_img.jpg") #退出操作截取图片