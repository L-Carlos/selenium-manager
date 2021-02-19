from time import sleep

from .selenium_manager import SeleniumManager


def main():
    url = "https://github.com/"

    search_bar = ".form-control.input-sm.header-search-input.jump-to-field.js-jump-to-field.js-site-search-focus"
    search_term = "Test"

    sm = SeleniumManager()
    sm.browser.get(url)
    sm.wait_element_click(sm.wait_css, search_bar)
    sm.wait_element_send_keys(sm.wait_css, search_term, search_bar)

    sleep(5)

    sm.browser.quit()
