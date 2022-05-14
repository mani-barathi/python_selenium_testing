import time
import unittest
from selenium import webdriver  
from selenium.webdriver.common.by import By

INVALID_NAME_MESSAGE = "Invalid Name: Name should be between 3 and 25 characters"
INVALID_AGE_MESSAGE = "Invalid Age: Age should be between 18 and 55"
SUCCESS_MESSAGE = "Success"
name = "mani"
age = 2
expected_value = SUCCESS_MESSAGE
URL = r"https://mani-barathi.github.io/python_selenium_testing/"


class TestWebPage(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)  
        self.driver.maximize_window()  
        self.driver.get(URL)
        print("Test Case started...")  
        
    def test_form(self):
        self.driver.find_element(By.ID,"name").send_keys(name)  
        time.sleep(1)  

        self.driver.find_element(By.ID,"age").send_keys(age)  
        time.sleep(1)  

        self.driver.find_element(By.ID ,"btn").click()
        time.sleep(1)  
        actual_value = self.driver.find_element(By.ID, "output").text

        assert actual_value == expected_value

    def tearDown(self):
        self.driver.close()  
        print("test case completed")  
        

if __name__ == "__main__":
    unittest.main()