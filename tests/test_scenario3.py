import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from pages.courses import CoursesPage
from pages.locators import CoursesLocators, FocusAreasLocators, SkillLevelsLocators
from selenium.webdriver.common.by import By


def test_filter_course_search_results():
    ff_driver = webdriver.Firefox()
    ff_driver.get("https://www.sans.org/cyber-security-courses/?per-page=10")
    ff_driver.maximize_window()
    courses_page = CoursesPage(ff_driver)
    assert CoursesLocators.page_title == ff_driver.title

    courses_page.apply_filter(FocusAreasLocators.open_source_intelligence_filter) # applying filter for Open Source Intelligence
    assert courses_page.filter_is_checked(FocusAreasLocators.open_source_intelligence_filter) # asserting the filter has been applied
    courses_page.apply_filter(SkillLevelsLocators.essentials_filter)
    assert courses_page.filter_is_checked(SkillLevelsLocators.essentials_filter)

    filtered_results = courses_page.aggregate_search_results() 
    assert courses_page.substring_in_list(filtered_results, "SEC497: Practical Open-Source Intelligence (OSINT)") # asserting course title is in the results
    assert courses_page.substring_in_list(filtered_results, "Certification: GIAC Open Source Intelligence (GOSI)") # asserting course has relevant certification

    # for future tests I would consider the following scenarios
    # 1. Add filters that would return no results and assert there are no courses shown
    # 2. Check a filter and uncheck it and assert it is not enabled
    # 3. Check a filter and uncheck it and assert the page state remains the same before the filter check
    # 4. Search for a keyword or course number then filter the results and assert the filter applied to the relevant search
    # 5. Search for a keyword or course number then apply a filter that would return no results and assert there are no courses shown
