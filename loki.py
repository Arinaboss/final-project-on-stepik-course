from selenium.webdriver.common.by import By


class shopLokators():
    SHOP = (By.CSS_SELECTOR, "#menu-item-661")
    SEARCH = (By.CSS_SELECTOR, "[type='search']")
    BUTTON = (By.CSS_SELECTOR, "[class='button-search']")
    PRODUCT = (By.CSS_SELECTOR, ".product-grid .name ")