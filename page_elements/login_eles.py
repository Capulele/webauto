from selenium.webdriver.common.by import By


class LoginEle:

    name_input = (By.XPATH, '//*[@id="fullscreenId"]/app-root/app-login/div/div[2]/div/nz-input-group[1]/input')
    pwd_input = (By.XPATH, '//*[@id="fullscreenId"]/app-root/app-login/div/div[2]/div/nz-input-group[2]/input')
    submit_button = (By.XPATH, '//*[@id="fullscreenId"]/app-root/app-login/div/div[2]/div/button')
    sys_homepage = (By.XPATH, '//*[@id="fullscreenId"]/app-root/app-index/div/nz-layout/nz-sider/div/div/span/span')
    logined_error = (By.XPATH, '//*[@id="cdk-overlay-5"]/nz-message-container/div/nz-message/div/div/div/span')
