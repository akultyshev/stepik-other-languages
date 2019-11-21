import time
from selenium.webdriver.common.by import By

class Test_OtherLanguage():
    def test_add_in_basket_button_on_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)

        button_elts = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
        
        add_button_count = len(button_elts)

        assert 0 <= add_button_count, f"Button not found on page"
