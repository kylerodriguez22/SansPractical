from seleniumpagefactory.Pagefactory import PageFactory
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import HomeLocators

class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    # This function when called on in hover over menu item kept getting a name is not defined error so for sake of time I added the logic to
    # the function directly. Ideally wouldn't duplicate code here but with the hover I didn't want to have flakey tests without the WebDriverWait
    # def wait_for_and_create_element(self, menu_xpath):
    #     try:
    #         WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, menu_xpath)))
    #         return self.driver.find_element(By.XPATH, menu_xpath)
    #     except Exception as error:
    #         print(error)
    
    def hover_over_menu_item(self, menu_xpath): 
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, menu_xpath)))
            menu_link = self.driver.find_element(By.XPATH, menu_xpath)
            menu_link.hover()
        except Exception as error:
            print(error)
    
    def click_menu_link(self, menu_xpath):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, menu_xpath)))
            menu_link = self.driver.find_element(By.XPATH, menu_xpath)
            menu_link.click()
        except Exception as error:
            print(error)


