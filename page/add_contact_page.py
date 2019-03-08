import allure,os
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddContactPage(BaseAction):
    name_edit_text=By.XPATH,"//*[@text='姓名']"
    phone_edit_text=By.XPATH,"//*[@text='电话']"
    @allure.step(title='输入姓名')
    def input_name(self,text):
        allure.attach('描述','我是测试步骤姓名的描述')
        self.input(self.name_edit_text,text)
    @allure.step(title='输入电话')
    def input_phone(self,text):
        self.input(self.phone_edit_text, text)
        # self.driver.get_screenshot_as_file(os.getcwd()+os.sep+"screen"+os.sep+"xx.png")
        # with open('./screen','rb')as f:
        #     allure.attach('描述',f.read(),allure.attach_type.PNG)

            # os.getcwd() + os.sep + "screen" + os.sep + "xx.png"

        allure.attach('描述',self.driver.get_screenshot_as_png(),allure.attach_type.PNG)
