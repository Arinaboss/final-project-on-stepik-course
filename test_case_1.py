from 'test-case.sait' import Page


def test_can_search_product(browser):
    link = "https://chumakov.by/"
    page = Page(browser, link)
    page.open()
    page.open_shop()
    page.shop_page()
    page.product()

