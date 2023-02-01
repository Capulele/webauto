import time
from page_elements.sys_homepage_eles import HomePageEle
from operator_object.login_page import UserLogin


class SysHomePage(UserLogin , HomePageEle):
	# 数据查询功能正常可以连接数据库获取数据判断结果及功能是否正常
	def search_projectsname(self , projectsname):
		self.userlogin('admin' , '11111111')
		self.ele_locator(self.sys_homepage).click()
		self.ele_locator(self.projectname_box).send_keys(projectsname)
		self.ele_locator(self.search_button).click()
		time.sleep(1)
