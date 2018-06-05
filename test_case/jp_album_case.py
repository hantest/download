# conding=utf-8

from selenium import webdriver
import unittest, sys
sys.path.append("./modles")
sys.path.append("./test_page")
from models import myunit
from test_page.jp_album_page import JpalbumPage

#
# 用例：精品专辑
#

class Jpalbum(myunit.MyTest):
	 ''' 精品专辑 '''

	 def test_jp_album(self):
	 	''' 顶部图片切换，点击用户名跳转 '''
	 	JpalbumPage(self.driver).dl_album_page()

	 def dearDown(self):
	 	self.driver.quit()

if __name__ == "__main__":
	unittest.main()