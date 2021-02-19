import json
import os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumManager:
    def __init__(self, json_path=None):
        self.configs = self.config_from_json(json_path)
        self.options = webdriver.ChromeOptions()
        self.preferences = self.configs.get("prefs")
        self.arguments = self.configs.get("args")
        self.options.add_experimental_option("prefs", self.preferences)

        for a in self.arguments:
            self.options.add_argument(a)

        self.browser = webdriver.Chrome(
            executable_path=ChromeDriverManager().install()
        )

    def wait_css(self, css: str, timeout=20):
        try:
            element = WebDriverWait(self.browser, timeout=timeout).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, css)
                )
            )
            return element

        except TimeoutException:
            return False

    def wait_xpath(self, xpath: str, timeout=20):
        try:
            element = WebDriverWait(self.browser, timeout=timeout).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, xpath)
                )
            )
            return element

        except TimeoutException:
            return False

    def config_from_json(self, json_path=None):
        if json_path is None:
            base_dir = os.path.abspath(
                os.path.dirname(os.path.dirname(__file__))
            )
            json_path = os.path.join(base_dir, "configs.json")
        with open(json_path, "r") as json_file:
            return json.loads(json_file.read())

    def wait_element_click(self, func, *args, **kwargs):
        el = func(*args, **kwargs)
        if el:
            el.click()
        else:
            print("WARNING - element:", *args, "not found")

    def wait_element_send_keys(self, func, keys: str, *args, **kwargs):
        el = func(*args, **kwargs)
        if el:
            el.send_keys(keys)
        else:
            print("WARNING - element:", *args, "not found")
