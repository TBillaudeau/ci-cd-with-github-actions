import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestAppE2E(unittest.TestCase):
    def setUp(self):
        # Launch your flask app first
        chrome_options = Options()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://localhost:5000')

    def test_add_and_delete_item(self):
        # you can use the driver to find elements in the page
        # example:
        """input_field = self.driver.find_element_by_name('item')"""
        # this refers to the 'name="item"' attribute of the html element
        # checkout the rest of the methods in the documentation:
        # https://selenium-python.readthedocs.io/locating-elements.html
        
        # after you select your element, you can send it a key press:
        """input_field.send_keys('New E2E Item')"""
        """input_field.send_keys(Keys.RETURN)"""
        
        # and you can use the rest of the assetion methods as well:
        """self.assertIn('New E2E Item', self.driver.page_source)"""

        # Test adding an item
        # self.driver.get("http://127.0.0.1:5000/")
        # self.driver.find_element(By.NAME, "item").click()
        # self.driver.find_element(By.NAME, "item").send_keys("New Item")
        # self.driver.find_element(By.CSS_SELECTOR, "button").click()
        # self.driver.find_element(By.LINK_TEXT, "Delete").click()

        time.sleep(1)
        self.driver.find_element(By.NAME, "item").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "item").send_keys("Test Item")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "new_item").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "new_item").send_keys("Modified Item")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "li button").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "item").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "item").send_keys("A new Item")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".container > form > button").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Delete").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Delete").click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()