from pages.base_page import BasePage
from selenium.webdriver.common.by import By


telegram = (By.CSS_SELECTOR, 'a[class="fa-brands fa-telegram"]')
vk = (By.CSS_SELECTOR, 'a[class="fa-brands fa-vk"]')
gmail = (By.CSS_SELECTOR, 'a[class="fa-brands fa-google"]')
phone = (By.CSS_SELECTOR, 'a[class="fa-solid fa-phone-flip"]')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://zemapapenko33.github.io/internship/')

    def telega(self):
        assert 'https://t.me/ZakharPapenko' in self.find_element(telegram).get_attribute('href')

    def vk(self):
        assert 'https://vk.com/zahapapenko' in self.find_element(telegram).get_attribute('href')

    def email(self):
        assert 'mailto:zakharpapenko@gmail.com' in self.find_element(telegram).get_attribute('href')

    def phone(self):
        assert 'tel:+375296403715' in self.find_element(telegram).get_attribute('href')