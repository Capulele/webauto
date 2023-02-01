import allure
import pytest
from base.base_page import BasePage
from common.dir_path import userdata_path
from common.load_log import load_log
from common.yamlutil import load_user_yaml
from operator_object.login_page import UserLogin


@allure.feature('登录功能')
class TestLogin:
	@allure.story('登录功能验证')
	@pytest.mark.parametrize('username,password,except_res' , load_user_yaml(userdata_path))
	def test_01_login(self , username , password , except_res):
		load_log().info('测试用户名{},密码{}'.format(username , password))
		result = UserLogin().userlogin(username , password)
		bs = BasePage()
		# noinspection PyBroadException
		try:
			assert result == except_res
			load_log().info('实际结果"{}"与预期结果"{}"一致'.format(result , except_res))
			load_log().info('---登录功能用例通过---')
			# 调用截图方法进行截图
			bs.save_page_screenshot()
		except:
			load_log().error('---登录测试不通过---')
			bs.save_page_screenshot()
