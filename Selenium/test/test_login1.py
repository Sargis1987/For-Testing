from page_object.Base_page import BasePage
from page_object.Login_page import LoginPage
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import HtmlTestRunner
class test_page(unittest.TestCase, BasePage):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(r'C:\Users\ssarg\Desktop\project\Selenium\vendor\chromedriver.exe')
        cls.OpenUrl("http://the-internet.herokuapp.com/login")

    def test_invalid_credentials(self, login):
        login._with("tomsmith", "bad password")
        self.assert_(login.success_message_present() == False)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test is completed")

if __name__ == "__main__" :
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner('..\\reports'))