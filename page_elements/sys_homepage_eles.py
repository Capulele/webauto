from selenium.webdriver.common.by import By


class HomePageEle:
    sys_homepage = (By.XPATH, '//*[@id="fullscreenId"]/app-root/app-index/div/nz-layout/nz-sider/div/div/span/span')
    projectname_box = (By.XPATH, '//*[@id="head_div"]/div/div[1]/div[2]/input')
    search_button = (By.XPATH, '//*[@id="head_div"]/div/div[2]/button[1]/span')
