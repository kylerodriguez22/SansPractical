import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from pages.homepage import HomePage
from pages.locators import HomeLocators, CoursesLocators
from selenium.webdriver.common.by import By


def test_navigate_to_full_course_list():
    ff_driver = webdriver.Firefox()
    ff_driver.get("https://www.sans.org/")
    ff_driver.maximize_window()
    homepage = HomePage(ff_driver)
    assert HomeLocators.page_title == ff_driver.title

    homepage.hover_over_menu_item(HomeLocators.train_and_certify_link) 
    homepage.hover_over_menu_item(HomeLocators.courses_link)
    homepage.click_menu_link(HomeLocators.full_course_list_link)
    assert ff_driver.current_url == CoursesLocators.base_url # assert the URL is accurate following the menu click
    assert ff_driver.find_element(By.XPATH, CoursesLocators.page_header).text == CoursesLocators.page_header_text # assert the page header text is accurate