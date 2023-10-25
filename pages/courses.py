from seleniumpagefactory.Pagefactory import PageFactory
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.locators import CoursesLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class CoursesPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    def search_for_course(self, course_number):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, CoursesLocators.course_search_bar)))
            search_bar = self.driver.find_element(By.XPATH, CoursesLocators.course_search_bar)
            search_bar.send_keys(course_number) # populate search bar with desired course search
            search_bar.send_keys(Keys.ENTER)
        except Exception as error:
            print(error)

    def get_results_tag(self): #this function keeps returning a nonetype and can't quite figure out why. going to assert on the web element text directly in the test for time being
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, CoursesLocators.search_result_tag)))
            results_tag = self.driver.find_element(By.XPATH, CoursesLocators.search_result_tag).text
            return results_tag
        except Exception as error:
            print(error)

    def apply_filter(self, filter_path):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, filter_path)))
            self.driver.find_element(By.XPATH, filter_path).click()
        except Exception as error:
            print(error)

    def filter_is_checked(self, filter_path):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, filter_path)))
            return self.driver.find_element(By.XPATH, filter_path).is_enabled()
        except Exception as error:
            print(error)
    
    def aggregate_search_results(self):
        clean_results = [] # creating a new list of clean results
        try:
            result_set = self.driver.find_element(By.XPATH, CoursesLocators.search_result_list) # creating an element of the ul
            raw_results = result_set.find_elements(By.TAG_NAME, "li") # creating a list of the web elements

            for i in range(len(raw_results)): # looping through the elements and creating a list of cleaned up text from the courses
                clean_results.append(raw_results[i].text.replace('\n',' ')) # removing newline characters to make it easier to assert on substrings
            
            return clean_results # returning the trimmed results
        
        except Exception as error:
            print(error)
        

    def substring_in_list(self, results_list, substring): # this works for asserting a particular string is in a list but not viable for asserting a string is in every list item
        try:
            for result in results_list:
                if substring.upper() in result.upper(): return True
            return False
        except Exception as error:
            print(error)

    def substring_in_all_list_items(self,results_list, substring): # assert that a string exists in all list items
        bool_list = []
        try:
            for result in results_list:
                if substring.upper() in result.upper(): bool_list.append(True)
                else: bool_list.append(False)
            return all(bool_list)
            
        except Exception as error:
            print(error)

    def clear_search_results_from_search_bar(self): # clear the search results to allow additional searching
        try:
            self.driver.find_element(By.XPATH, CoursesLocators.clear_results_from_search_bar).click()
        except Exception as error:
            print(error)
    