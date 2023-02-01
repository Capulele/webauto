from base.base_page import BasePage
from page_elements.login_eles import LoginEle


class UserLogin(BasePage , LoginEle):

	# noinspection PyBroadException
	def userlogin(self , username , password):
		# noinspection PyBroadException
		self.browser()
		try:
			self.driver.implicitly_wait(5)
			self.ele_locator(self.name_input).clear()
			self.ele_locator(self.name_input).send_keys(username)
			self.ele_locator(self.pwd_input).clear()
			self.ele_locator(self.pwd_input).send_keys(password)
			self.ele_locator(self.submit_button).click()
			res = self.ele_locator(self.sys_homepage).get_attribute('textContent')
			if res == '系统首页':
				return '登录成功'
			self.driver.quit()
		except:
			return '登录失败'

# if __name__ == '__main__':
#     UserLogin().userlogin('admin', '11111111')
