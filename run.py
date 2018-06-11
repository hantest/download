# coding=utf-8

from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import unittest, time, os
from test_case.login1_case import Login
from test_case.logout_case import Logout
from test_case.collect_case import Collect
from test_case.nocollect_case import Nocollect
from test_case.report_case import Report
from test_case.downloadvip_case import DownloadVip
from test_case.download_case import Download
from test_case.follow_case import Follow
from test_case.comment_case import Comment
from test_case.album_case import Album
from test_case.search_case import Search
from test_case.jp_album_case import Jpalbum
from test_case.rank_case import Rank                                               



# 多线程
if __name__ == '__main__':

	# 指定测试用例为当前文件夹下的page_obj目录
	#test_dir = './test_case'
	#discover = unittest.defaultTestLoader.discover(test_dir, pattern='login.py')
	
	#构建测试集
	suite = unittest.TestSuite()

	#suite.addTest(unittest.makeSuite(Login,"test_login"))  #登陆
	#suite.addTest(unittest.makeSuite(Login,"test_login5"))
	#suite.addTest(unittest.makeSuite(Logout,"test_logout")) #退出
	#suite.addTest(unittest.makeSuite(Search,"test_search"))  #首页搜索
	#suite.addTest(unittest.makeSuite(Collect,"test_collect")) #收藏
	#suite.addTest(unittest.makeSuite(Nocollect,"test_nocollect")) #取消收藏
	#suite.addTest(unittest.makeSuite(Report,"test_report"))  #举报
	#suite.addTest(unittest.makeSuite(DownloadVip,"test_download")) #VIP下载
	#suite.addTest(unittest.makeSuite(DownloadVip,"test_downloady_vip")) #VIP页面下载
	#suite.addTest(unittest.makeSuite(DownloadVip,"test_downloadg_vip")) #VIP跟随菜单下载
	#suite.addTest(unittest.makeSuite(DownloadVip,"test_downloadx_vip"))  #VIP相关推荐下载
	suite.addTest(unittest.makeSuite(Download,"test_download"))  #普通用户下载-积分不足有剩余C币


	#suite.addTest(unittest.makeSuite(Follow,"test_follow"))  #关注
	#suite.addTest(unittest.makeSuite(Follow,"test_not_follow")) #取消关注
	#suite.addTest(unittest.makeSuite(Comment,"test_comment"))  #评论
	#suite.addTest(unittest.makeSuite(Comment,"test_notdownload_comment")) #资源未下载点击评论
	#suite.addTest(unittest.makeSuite(Comment,"test_download_comment")) #下载资源后评论
	
	#suite.addTest(unittest.makeSuite(Rank,"test_rank"))  #排行榜
	#suite.addTest(unittest.makeSuite(Album,"test_album"))  #专辑管理
	#suite.addTest(unittest.makeSuite(Jpalbum,"test_jp_album"))  #精品专辑-顶部图片切换
	#suite.addTest(unittest.makeSuite(Jpalbum,"test_album_gx"))  #精品专辑-专辑贡献榜
	#suite.addTest(unittest.makeSuite(Jpalbum,"test_album_list"))  #精品专辑列表-点击用户头像/用户名跳转

	# 获取当前时间
	now = time.strftime("%Y-%m-%d %H_%M_%S")

	#定义报告存放路径
	filename = './report/' + now + 'result.html'
	fp = open(filename,'wb')

	#定义测试报告
	runner = HTMLTestRunner(stream=fp, title='下载测试报告', description='用例执行情况：')
	runner.run(suite) # 运行测试用例
	fp.close() # 关闭报告文件