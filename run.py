# coding=utf-8

from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import unittest, time, os
from test_case.login_case import Login
from test_case.collect_case import Collect
from test_case.downloadvip_case import DownloadVip
from test_case.follow_case import Follow
from test_case.comment_case import Comment
                                                                                           



# 多线程
if __name__ == '__main__':

	# 指定测试用例为当前文件夹下的page_obj目录
	#test_dir = './test_case'
	#discover = unittest.defaultTestLoader.discover(test_dir, pattern='login.py')
	
	#构建测试集
	suite = unittest.TestSuite()
	#suite.addTest(login.Login("test_login"))  #登录
	
	#suite.addTest(unittest.makeSuite(Login,"test_login"))  #登陆
	#suite.addTest(unittest.makeSuite(Login,"test_logout")) #退出
	#suite.addTest(unittest.makeSuite(Login,"test_login"))  # 登陆、退出功能
	#suite.addTest(unittest.makeSuite(Collect,"test_collect")) #收藏
	#suite.addTest(unittest.makeSuite(Collect,"test_Nocollect")) #取消收藏
	#suite.addTest(unittest.makeSuite(DownloadVip,"test_download_vip")) #VIP用户下载
	#suite.addTest(unittest.makeSuite(Follow,"test_follow"))  #关注
	suite.addTest(unittest.makeSuite(Comment,"test_comment"))  #评论

	# 获取当前时间
	now = time.strftime("%Y-%m-%d %H_%M_%S")

	#定义报告存放路径
	filename = './report/' + now + 'result.html'
	fp = open(filename,'wb')

	#定义测试报告
	runner = HTMLTestRunner(stream=fp, title='下载测试报告', description='用例执行情况：')
	runner.run(suite) # 运行测试用例
	fp.close() # 关闭报告文件

	