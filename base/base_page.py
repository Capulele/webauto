import logging
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from common.dir_path import screenshot_path


class BasePage:
	options = webdriver.ChromeOptions()
	options.add_experimental_option("useAutomationExtension" , False)
	options.add_experimental_option("excludeSwitches" , ['enable-automation'])
	driver = webdriver.Chrome(options = options)

	def browser(self):
		self.driver.get('http://cfgjt.cn:8981/devt-web/#/login')
		self.driver.maximize_window()

	def ele_locator(self , loc):
		try:
			return self.driver.find_element(*loc)
		except NoSuchElementException:
			return '元素未找到'

	def save_page_screenshot(self):
		# 路径配置文件中引入图片保存路径  + 年月日-时分秒
		#  # 截图 - 命名。 页面名称_行为名称_当前的时间.png
		#  页面_功能_时间.png
		now = time.strftime("%Y-%m-%d %H_%M_%S")
		screenshotfile_path = screenshot_path + "/{}.png".format(now)
		self.driver.implicitly_wait(5)
		self.driver.save_screenshot(screenshotfile_path)
		logging.info('截图保存的位置在{}'.format(screenshotfile_path))


# if __name__ == '__main__':
# 	BasePage()
# 	bas.browser()
# 	bas.save_page_screenshot()
