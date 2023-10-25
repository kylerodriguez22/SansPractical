class HomeLocators:
    base_url = "https://www.sans.org/"
    page_title = "Cyber Security Training, Degrees & Resources | SANS Institute"
    train_and_certify_link = "//a[contains(@href, '/cyber-security-training-overview/?msc=main-nav') and contains(text(),'Train and Certify')]" # "/html/body/div[1]/div/div/header/div/div/div/div/nav[1]/ul/li[1]/a"
    courses_link = "//a[contains(@href, '/cyber-security-courses/?msc=main-nav') and contains(text(),'Courses')]" # "/html/body/div[1]/div/div/header/div/div/div/div/nav[1]/ul/li[1]/div/ul/li[2]/a"
    full_course_list_link = "//a[contains(@href, '/cyber-security-courses/?msc=main-nav') and contains(text(),'Full Course List')]" # "/html/body/div[1]/div/div/header/div/div/div/div/nav[1]/ul/li[1]/div/ul/li[2]/ul/li[2]/a"

    # Initially considered using the full xpath but to better future proof in case of additional menu items I used more conditional contains xpaths.
    # Preferably I would add custom ID tags to reference for my elements     


class CoursesLocators:
    base_url = "https://www.sans.org/cyber-security-courses/?msc=main-nav"
    page_title = "Cyber Security Courses | SANS Institute"
    page_header = "//*[@class='title-search__heading' and contains(text(),'Cybersecurity Courses & Certifications')]"
    page_header_text = "Cybersecurity Courses & Certifications"
    course_search_bar = "//input[contains(@id, 'search-query') and contains(@placeholder,'Enter a course name or other keyword')]"
    search_result_tag = "//h3[contains(text(),'Results for')]"
    clear_results_from_search_bar = "//a[@class='title-search__input__clear title-search__input__clear--active']"
    search_result_list = "//ul[@class='article-listing' and @datalayercontext='Course Listing']"

class FocusAreasLocators:
    cloud_security_filter = "//div[label[text()='Cloud Security']]"
    cyber_defense_filter = "//label[text()='Cyber Defense']"
    cyber_security_and_IT_essentials_filter = "//label[text()='Cybersecurity and IT Essentials']"
    digital_forensics_filter = "//label[text()='Digital Forensics, Incident Response & Threat Hunting']"
    industrial_control_systems_filter = "//label[text()='Industrial Control Systems Security']"
    offensive_operations_filter = "//label[text()='Offensive Operations']"
    open_source_intelligence_filter = "//label[text()='Open-Source Intelligence (OSINT)']"
    security_management_filter = "//label[text()='Security Management, Legal, and Audit']"

class SkillLevelsLocators:
    new_to_cyber_filter = "//label[text()='New to Cyber (200-399)']"
    essentials_filter = "//label[text()='Essentials (400-499)']"
    advanced_filter = "//label[text()='Advanced (500-699)']"
    expert_filter = "//label[text()='Expert (700+)']"