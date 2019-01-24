import time
import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\theda\\PycharmProjects\\UnitTestingUtest\\drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_loginFunctionality_1(self):
        self.driver.get("https://utest.com")
        #FindElement-> 1) Find and locate element
        #              2) Determine action
        #              3) Pass the parameter
        self.driver.find_element_by_link_text("Sign in").click()
        time.sleep(10)
        self.driver.find_element_by_id("username").send_keys("codingandtestingdaily@gmail.com")
        time.sleep(5)
        self.driver.find_element_by_name("password").send_keys("abcd1234")
        time.sleep(5)
        self.driver.find_element_by_id("kc-login").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Log in to uTest")

    def test_loginFunctionality_2(self):
        self.driver.get("https://utest.com")
        #FindElement-> 1) Find and locate element
        #              2) Determine action
        #              3) Pass the parameter
        self.driver.find_element_by_link_text("Sign in").click()
        time.sleep(10)
        self.driver.find_element_by_id("username").send_keys("codingandtestingdaily@gmail.com")
        time.sleep(5)
        self.driver.find_element_by_name("password").send_keys("abcd1234")
        time.sleep(5)
        self.driver.find_element_by_id("kc-login").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Log in to uTest")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("The Unit Test is 100% successfully COMPLETED!!!")

if __name__ == '__main__':
    unittest.main(verbosity=2)
