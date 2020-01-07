# Generated by Selenium IDE
# import pytest
import time
import json
import unittest
import HtmlTestRunner
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class test_signUp(unittest.TestCase):

  @classmethod
  def setup_method(self):
    self.driver = webdriver.Chrome('./chromedriver')

  def test_User_signUp(self):
    self.driver = webdriver.Chrome('./chromedriver')
    driver = self.driver
    driver.get("https://advisortodo.gntkwhqzn-test.advisortodo.com/#/auth/signin")
    driver.set_window_size(1366, 741)
    driver.find_element(By.LINK_TEXT, "Sign Up").click()
    driver.find_element(By.ID, "exampleInputFirstName").click()
    driver.find_element(By.ID, "exampleInputFirstName").send_keys("Nishit")
    driver.find_element(By.ID, "exampleInputLastName").send_keys("sheth")
    driver.find_element(By.ID, "organization").send_keys("TestingAdvisortodo")
    driver.find_element(By.ID, "exampleInputEmail1").click()
    driver.find_element(By.ID, "exampleInputEmail1").send_keys("Test@qa.com")
    driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test@123#")
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    print('Sign Up completed')

  def test_user_Forgot_Password(self):
    self.driver = webdriver.Chrome('./chromedriver')
    driver = self.driver
    driver.get("https://advisortodo.gntkwhqzn-test.advisortodo.com/#/auth/signin")
    driver.set_window_size(1366, 741)
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
    element = driver.find_element(By.CSS_SELECTOR, ".col-lg-4")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = driver.find_element(By.CSS_SELECTOR, ".col-lg-4")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, ".col-lg-4")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, ".col-lg-4").click()
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").send_keys("Test@qa.com")
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    driver.find_element(By.LINK_TEXT, "Forgot Password?").click()
    driver.find_element(By.CSS_SELECTOR, ".form-control").click()
    driver.find_element(By.CSS_SELECTOR, ".form-control").click()
    driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("Test@qa.com")
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    driver.find_element(By.LINK_TEXT, "Back to Sign In").click()
    print('Forgot Password completed')

  def test_User_SignIn(self):
    self.driver = webdriver.Chrome('./chromedriver')
    driver = self.driver
    driver.get("https://advisortodo.gntkwhqzn-test.advisortodo.com/#/auth/signin")
    driver.set_window_size(1366, 741)
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").send_keys("Test@qa.com")
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("Test@123#")
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    driver.implicitly_wait(15)
    element = driver.find_element(By.LINK_TEXT, "Categories")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.CSS_SELECTOR, "span:nth-child(1) > span").click()
    driver.find_element(By.CSS_SELECTOR, ".dropdown-item:nth-child(1)").click()
    element = driver.find_element(By.CSS_SELECTOR, "div > span:nth-child(1)")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.CSS_SELECTOR, "#profileDropdown div > span").click()
    driver.find_element(By.CSS_SELECTOR, ".dropdown-item:nth-child(3)").click()
    driver.implicitly_wait(5)
    print('Sign in Completed')



  @classmethod
  def teardown_method(self):

      self.driver.quit()
      self.driver.close()

if __name__ == '__main__':
   unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./Reports'))