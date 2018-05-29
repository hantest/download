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
from .downloadvip_page import DownloadVipPage


#
# 页面：下载评论
# time:2018-5-24
# @HAN
#

class CommentPage(Page):

	url = "/"
	download_top_loc = (By.XPATH, "//*[@id='download_top']/div[3]/div[2]/a[2]")  # 下载按钮
	commentbox_loc = (By.XPATH, "//*[@id='csdn_dl_commentbox']/li[2]/i[3]")  # 评价资源
	cc_body_loc = (By.ID, "cc_body") # 评论框
	btn_red_loc = (By.CLASS_NAME, "btn-red") # 提交评论按钮

	def download_top(self):
		self.find_element(*self.download_top_loc).click()

	def commentbox(self):
		self.find_element(*self.commentbox_loc).click()

	def cc_body(self):
		self.find_element(*self.cc_body_loc).send_keys("测试人员测试，看到后删除！")

	def btn_red(self):
		self.find_element(*self.btn_red_loc).click()


	def comment_page(self):
		''' 资源评论 '''
		DownloadVipPage(self.driver).downloadvip_page()
		self.driver.refresh() #刷新页面
		self.driver.get_screenshot_as_file("D:\\download\\download5\\img\\commentQ_img.jpg") #评论之前截图
		self.download_top()
		self.commentbox()
		self.cc_body()
		self.btn_red()
		self.driver.get_screenshot_as_file("D:\\download\\download5\\img\\commentH_img.jpg") #评论后截图
		sleep(3)
