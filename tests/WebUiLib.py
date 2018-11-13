from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class WebUiLib:

    def open_browser(self, url, browser):
        if browser.lower() == "chrome":
            self.driver = webdriver.Chrome("../source/chromedriver.exe")
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def get_tasks(self):
        import time
        elm = self.driver.find_element_by_name("task_id")
        elm.click()
        time.sleep(2)
        elm.clear()
        elm.send_keys(1)
        time.sleep(2)
        but_elm = self.driver.find_element_by_id("get_task")
        but_elm.click()
        time.sleep(2)

    def close_browser(self):
        self.driver.close()


