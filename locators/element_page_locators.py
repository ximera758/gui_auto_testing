from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR,"button[title ='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR,"span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR,"svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")

class RadioButtonPageLocators:
    YES_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    IMPRESSIVE_RADIO_BUTTON= (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    NO_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTablePageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR,"button[id='addNewRecordButton']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='First Name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='name@example.com']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[placeholder='Salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[placeholder='Department']")
    SUBMIT = (By.CSS_SELECTOR,"button[id='submit']")


    #tabel
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR,"div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR,'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR,'span[title=Delete]')
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"