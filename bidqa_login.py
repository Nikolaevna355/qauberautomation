from selenium import webdriver
import unittest

class Qauber(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://bidqa.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_qauber_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_class_name("login-awsome").click()
        driver.find_element_by_id("log").clear()
        driver.find_element_by_id("log").send_keys("antonina")
        driver.find_element_by_id("login_password").clear()
        driver.find_element_by_id("login_password").send_keys("12345")
        driver.find_element_by_id("submits").click()
        try: self.assertTrue(driver.title.find("My Account") != -1)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
