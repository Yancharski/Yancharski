from pages.home_page import HomePage
import allure
import pytest


@allure.feature('Telegram opened')
def test_telegram(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.telega()


@allure.feature('Vk opened')
def test_telegram(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.vk()


@allure.feature('Email opened')
def test_telegram(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.email()


@allure.feature('Phone number opened')
def test_phone(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.phone()
