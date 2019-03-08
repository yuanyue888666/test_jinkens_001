import time
import pytest

from base.base_driver import init_driver
from page.page import Page

class TestContact:
    def setup(self):
        self.driver=init_driver()
        self.page=Page(self.driver)
    def teardown(self):
        time.sleep(2)
        self.driver.quit()


    @pytest.mark.parametrize(('name',"phone"),[['hello','188888'],['zhangsan','12222222222']])
    def test_add_contact(self,name,phone):
        self.page.contact_list.click_add_contact()
        self.page.add_contact.input_name(name)
        self.page.add_contact.input_phone(phone)

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_contact1(selfself):
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_contact2(selfself):
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_contact3(selfself):
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_contact4(selfself):
        assert 1

