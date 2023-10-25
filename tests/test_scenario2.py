import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from pages.courses import CoursesPage
from pages.locators import HomeLocators, CoursesLocators
from selenium.webdriver.common.by import By

def test_search_for_courses():
    ff_driver = webdriver.Firefox()
    ff_driver.get("https://www.sans.org/cyber-security-courses/?per-page=10")
    ff_driver.maximize_window()
    courses_page = CoursesPage(ff_driver)
    assert CoursesLocators.page_title == ff_driver.title
    
    courses_page.search_for_course('SEC504')
    assert 'Results for "SEC504"' in courses_page.get_results_tag() # hardcoding the asserts for readability

    hacker_tools_course_list = courses_page.aggregate_search_results() # creating the cleaned up list of search results 
    assert courses_page.substring_in_list(hacker_tools_course_list, "SEC504: Hacker Tools, Techniques, and Incident Handling") # using the substring in list function I can assert the course titles are in the search results
    assert courses_page.substring_in_list(hacker_tools_course_list, "SEC504J: Hacker Tools, Techniques, Exploits, and Incident Handling - Japanese")

    courses_page.clear_search_results_from_search_bar()

    courses_page.search_for_course('auditing')
    assert 'auditing' in courses_page.get_results_tag()
    auditing_keyword_course_list = courses_page.aggregate_search_results() # list of courses that have the keyword auditing
    assert courses_page.substring_in_list(auditing_keyword_course_list, "Auditing") # capitalized substring to test out case sensitivity because one course doesn't have auditing in title

    # for future tests I would consider the following scenarios
    # 1. Search for a course number that does not exist and assert on no results shown
    # 2. Search for a keyword that does not exist and assert on no results shown
    # 3. Search with a non-alphanumeric character
    # 4. Search a course and assert on the certifications
    # 5. Search for a course with more than 10 results and assert there are additional page links
    # 6. Search for two different course numbers and assert the first course listed is returned
