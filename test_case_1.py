import pytest
from selenium import webdriver

from sait import Page

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    return driver


def test_can_search_product(browser):
    link = "https://chumakov.by/"
    page = Page(browser, link)
    page.open()
    page.open_shop()
    page.shop_page()
    page.product()

