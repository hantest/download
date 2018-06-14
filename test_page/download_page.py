# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest, sys
from .base import Page
from .login1_page import LoginPage

#
# 功能：普通用户下载
# 用例：1、资源分=0，积分/C币=0，获取验证码  2、下载自己上传的资源不扣除积分  3、资源分>0,积分/C币=0，开通VIP
# 		3、资源=0，积分/C币>0  4、资源分>0,积分/C币>0
# time：2018-6-11
# @HAN
#

class DownloadPage(Page):
	''' 普通用户下载 '''
	zx_list_loc = (By.XPATH, "//ul[@class='tab_list clearfix']/li[2]")  #最新上传tab
	detail_list_loc = (By.XPATH, "//*[@class='tab_page tab2_con']/div/dl[1]") #最新上传列表第一个资源
	ym_direct_download_loc = (By.XPATH, "//*[@id='download_top']/div[4]/a[2]")  #页面立即下载按钮
	noVipZeroP_loc = (By.ID, "noVipEnoughP")  # 资源=0，积分/C币=0  
	task_loc = (By.XPATH, "//*[@id='noVipZeroP']/div[3]/div[1]/a") #双0用户，点击完成任务获取下载码
	noVipNoEnoughPNoC_loc = (By.ID, "noVipNoEnoughPNoC")  # 资源>0,积分C币都为0定位框（测试账号cpongo4）
	do_openV_loc = (By.CLASS_NAME, "openV")  #开通VIP
	noVipNoEnoughPHasC_loc = (By.ID, "noVipNoEnoughPHasC")  # 积分不足有剩余C币定位框(测试账号cpongo8)
	dl_down_btn_loc = (By.XPATH, "//*[@id='noVipNoEnoughPHasC']/div[5]/a")  # 弹框中的确认下载按钮
	my_resource_loc = (By.LINK_TEXT, u"我的资源")  #二级导航-我的资源
	uresource_loc = (By.XPATH, "//*[@class='item uresource']/ul/li[1]/div/div[2]/h3/a") #上传资源列表第一个资源
	my_download_loc = (By.LINK_TEXT, u"已下载")  # 二级导航-已下载
	down_uresource_loc = (By.XPATH, "//*[@class='item uresource']/ul/li[1]/div/div[2]/h3/a") #第一个下载资源

	def zx_list(self):
		self.find_element(*self.zx_list_loc).click()

	def detail_list(self):
		self.find_element(*self.detail_list_loc).click()

	# 页面立即下载按钮
	def ym_direct_download(self):
		self.find_element(*self.ym_direct_download_loc).click()

	# 资源/积分/C币 == 0
	def noVipZeroP(self):
		self.find_element(*self.noVipZeroP_loc)

	# 双0用户，点击任务获取下载码
	def task(self):
		self.find_element(*self.task_loc).click()

	#资源>0,积分/C币 == 0
	def noVipNoEnoughPNoC(self):
		self.find_element(*self.noVipNoEnoughPNoC_loc)

	# 资源>0,积分/C币 == 0, 开通VIP按钮
	def do_openV(self):
		self.find_element(*self.do_openV_loc).click()

	# 积分不足有C币	
	def noVipNoEnoughPHasC(self):
		self.find_element(*self.noVipNoEnoughPHasC_loc)

	# 积分不足有剩余C币定位框中的确认下载按钮
	def dl_down_btn(self):
		self.find_element(*self.dl_down_btn_loc).click()

	# 二级导航-我的资源
	def my_resource(self):
		self.find_element(*self.my_resource_loc).click()

	# 我上传的第一个资源
	def uresource(self):
		self.find_element(*self.uresource_loc).click()

	# 二级导航-已下载
	def my_download(self):
		self.find_element(*self.my_download_loc).click()

	# 第一个下载资源
	def down_uresource(self):
		self.find_element(*self.down_uresource_loc).click()


	def downloadHasC_page(self):
		''' 积分不足有剩余C币 cpongo8'''
		LoginPage(self.driver).login_page(username="cpongo8",password="abc123")
		self.zx_list()
		sleep(3)
		self.detail_list()
		
		all_handle = self.driver.window_handles  # 获取所有的窗口
		now_handle = self.driver.current_window_handle  # 获取当前的窗口
		for handle in all_handle:
			if handle != now_handle:
				self.driver.close() #关闭前一个窗口
				self.driver.switch_to_window(handle)
				self.ym_direct_download()
				self.noVipNoEnoughPHasC()

				JF = self.driver.find_element_by_xpath("//*[@id='noVipNoEnoughPHasC']/div[2]/table/tbody/tr[2]/td[2]/strong").text
				CB = self.driver.find_element_by_xpath("//*[@id='noVipNoEnoughPHasC']/div[2]/table/tbody/tr[2]/td[3]/strong").text
				if JF == "0" and CB != "0":
					self.driver.get_screenshot_as_file("./img/积分不足有C币.jpg")
					sleep(2)
					self.dl_down_btn()
					sleep(2)
				else:
					print(u"资源已经被下载过，不需要扣除积分！")
					self.driver.close()
					sleep(2)


	def downloadNoJC_page(self):
		''' 资源>0，积分和C币==0 cpongo4'''
		LoginPage(self.driver).login_page(username="cpongo4",password="abc123")
		self.zx_list()
		self.detail_list()
		sleep(3)

		all_handle = self.driver.window_handles  # 获取所有的窗口
		now_handle = self.driver.current_window_handle  # 获取当前的窗口
		for handle in all_handle:
			if handle != now_handle:
				self.driver.close() #关闭前一个窗口
				self.driver.switch_to_window(handle)
				self.ym_direct_download()
				self.noVipNoEnoughPNoC()
				sleep(3)
				noC = self.driver.find_element_by_xpath("//*[@id='noVipNoEnoughPNoC']/div[3]/span/a").text
				if noC == u"积分和C币不足，点我赚C币吧！":
					self.driver.get_screenshot_as_file("./img/积分C币等于0.jpg")
					self.do_openV()
					all_handle1 = self.driver.window_handles  # 获取所有的窗口
					now_handle1 = self.driver.current_window_handle  # 获取当前的窗口
					for handle1 in all_handle1:
						if handle1 == now_handle1:
							self.driver.switch_to_window(handle1)
							sleep(3)
				else:
					print(u"资源已经被下载过，不需要扣除积分！")
					self.driver.close()



	def download_my_page(self):
		''' 下载自己的资源 '''
		LoginPage(self.driver).login_page(username="cpongo4",password="abc123")
		self.my_resource()
		self.uresource()
		sleep(2)
		all_handle = self.driver.window_handles
		now_handle = self.driver.current_window_handle
		for handle in all_handle:
			if handle != now_handle:
				self.driver.close()
				self.driver.switch_to_window(handle)
				self.ym_direct_download()
				sleep(2)


	
	def download_JC_page(self):
		''' 资源=0，积分和C币都为0 '''
		LoginPage(self.driver).login_page(username="cpongo4", password="abc123")
		self.driver.get("https://download.csdn.net/download/u013682507/8894183")  #积分为0的资源
		sleep(4)
		self.ym_direct_download()
		self.noVipZeroP()

		JF = self.driver.find_element_by_xpath("//*[@id='noVipZeroP']/div[2]/table/tbody/tr[2]/td[2]/strong").text #积分
		CB = self.driver.find_element_by_xpath("//*[@id='noVipZeroP']/div[2]/table/tbody/tr[2]/td[3]/strong").text #C币
		if CB == "0" and JF =="0":
			sleep(5)
			self.driver.get_screenshot_as_file("./img/双0用户.jpg")
			self.task()
			all_handle = self.driver.window_handles
			now_handle = self.driver.current_window_handle
			for handle in all_handle:
				if handle == now_handle:
					self.driver.switch_to_window(handle)
		else:
			self.driver.get_screenshot_as_file("./img/不是双0账号.jpg")
			self.driver.close()


	commentbox_loc = (By.XPATH, "//*[@id='csdn_dl_commentbox']/li[2]/i[3]")  # 评价资源
	cc_body_loc = (By.ID, "cc_body") # 评论框
	btn_red_loc = (By.CLASS_NAME, "btn-red") # 提交评论按钮
	download_popup_loc = (By.ID, "download") #已经下载过该资源，不再扣除积分弹框
	download_popup_btn_loc =(By.XPATH, "//*[@id='download']/div[2]/a") #不再扣除积分弹框中下载按钮

	def commentbox(self):
		self.find_element(*self.commentbox_loc).click()

	def cc_body(self):
		self.find_element(*self.cc_body_loc).send_keys("测试人员测试，看到后删除！")

	def btn_red(self):
		self.find_element(*self.btn_red_loc).click()

	def download_popup(self):
		self.find_element(*self.download_popup_loc)

	def download_popup_btn(self):
		self.find_element(*self.download_popup_btn_loc).click()


	def download_repeat_page(self):
		''' 再次下载重复资源-未评论/评论 '''
		LoginPage(self.driver).login_page(username="cpongo8", password="abc123")
		self.my_download()
		self.down_uresource()

		all_handle = self.driver.window_handles
		now_handle = self.driver.current_window_handle
		for handle in all_handle:
			if handle != now_handle:
				self.driver.close()
				self.driver.switch_to_window(handle)
				#comment_com = self.driver.find_element_by_xpath("//*[@id='comment']/div[2]/div/p/em").text  #已发表过评论
				tip_com = self.driver.find_element_by_xpath("//*[@id='comment']/div[2]/form/div/div[3]/span").text #未评论
				if tip_com == u"评论内容不能少于5个字":
					self.commentbox()
					self.cc_body()
					self.btn_red()
					sleep(2)
					self.ym_direct_download()
					self.download_popup()
					self.download_popup_btn()
					sleep(3)
				else:
					self.ym_direct_download()
					self.download_popup()
					#self.driver.close()
