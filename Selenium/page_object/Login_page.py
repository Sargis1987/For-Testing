from Base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    login_form={"by": By.ID, "value": "login"}
    username_input={"by": By.ID, "value": "username"}
    password_input={"by": By.ID, "value": "password"}
    select_button={"by": By.CSS_SELECTOR, "value": "button"}
    success_message={"by": By.CSS_SELECTOR, "value": ".flash.success"}
    failure_message={"by": By.CSS_SELECTOR, "value": ".flash.error"}

    def __init__(self,driver):
        self.driver = driver
        assert self._presence(self.login_form)
        print("Login page POM instance is created")

    def _with(self, username, password):
        self._input(self.username_input, username)
        self._input(self.password_input, password)
        self._select( self.select_button)
        return LoginPage(self.driver)

    def success_message_present(self):
        return self._presence(self.success_message)

    def failure_message_present(self):
        return self._presence(self.failure_message)


