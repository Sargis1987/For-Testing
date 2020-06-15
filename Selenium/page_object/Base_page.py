from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver=driver

    def _open_url(self, url):
        self.driver.get(url)

    def _find(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def _select(self,locator):
        self._find(locator).click()

    def _input(self,locator, typetext):
        self._find(locator).send_keys(typetext)

    def _presence(self,locator):
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

