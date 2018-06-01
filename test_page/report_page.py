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
# 功能：资源举报
# 用例：1、未下载资源举报 2、举报自己的资源 3、下载后举报
# time:2018-6-1
# @HAN
#

class ReportPage(Page):

	download_report_loc = (By.ID, "download_report") #未下载点击举报弹出框
	myself_loc = (By.ID, "myself")  #举报自己的资源弹框
	dlReport_loc = (By.ID, "dlReport")  #下载后举报

	


