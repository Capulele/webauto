from selenium.common import NoSuchElementException


def ele_locator(self , loc):
	try:
		self.driver.implicitly_wait(10)
		return self.driver.find_element(*loc)

	except NoSuchElementException:
		return '元素未找到'
