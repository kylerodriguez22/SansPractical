# Test Structure
### Pages
- Files for Home and Courses pages containing driver constructor and reusable methods for testing
- Locators file contains relevant xpaths to elements on pages in relevant classes

### Tests
- Test files for each scenario with a test function that is run using PyTest
- Test function name formatting must include test_* or *_test for PyTest to successfully run

### PyTest Installation
```
pip install pytest
```

# Running Tests
##### Example 1: Running scenario 3 test
```
pytest -s .\tests\test_scenario3.py
```
##### Example 2: Running scenario 3 test without Pytest in Path
```
python -m pytest -s .\tests\test_scenario3.py
```

# Lessons Learned
- Using xpath to identify elements in the webpage. Being a public page I was unable to add custom ID attributes which is preferred way of identifying elements
- Coming from a Cypress background Selenium as a whole was new to me and applying it to the Page Object Model (POM) was a bit of learning curve to begin
- Object Oriented Programming (OOP) with relation to Selenium and Python
- Selenium Framework in general and some of its best practices for example implicit/explicit waits
