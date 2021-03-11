from selenium import webdriver
from .loki import shopLokators
from .chumakov_jopa import BasePage


class Page(BasePage):
    def open_shop(self):
        shop = self.browser.find_element(*shopLokators.SHOP)
        shop.click()

    def shop_page(self):
        search = self.browser.find_element(*shopLokators.SEARCH)
        search.send_keys("NITTAKU Violoncello")
        button = self.browser.find_element(*shopLokators.BUTTON)
        button.click()

    def product(self):
        racket = "NITTAKU Violoncello"
        page_probuct = self.browser.find_element(*shopLokators.PRODUCT)
        assert racket == page_probuct.text, f"except {racket} got {page_probuct.text}"