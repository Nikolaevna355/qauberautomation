'''
Automation test to verify BidQA logo links to homepage
Natasha 7/10/2015

'''

from selenium import webdriver
import unittest

class BidQALogo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://bidqa.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bid_q_a_logo(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("logo").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
