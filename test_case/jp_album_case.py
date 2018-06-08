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
	 	self.assertEqual(self.driver.title, "我的CSDN")

	 def test_album_gx(self):
	 	''' 专辑贡献榜 '''
	 	JpalbumPage(self.driver).album_gx_page()

	 def test_album_list(self):
	 	''' 专辑列表-点击用户头像或用户名跳转到个人中心 '''
	 	JpalbumPage(self.driver).album_my_page()
	 	

	 def dearDown(self):
	 	self.driver.quit()

if __name__ == "__main__":
	unittest.main()