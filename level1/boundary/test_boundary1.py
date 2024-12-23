# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

filename = path = Path(__file__).parent / "boundaryData_full.txt"


def dataForTest():
    dataTest = []
    with open(filename, "r") as f:
        line = f.readline()
        while line:
            data = line.split(";")
            for i in range(0, len(data)):
                data[i] = str(data[i]).strip()
            loginCredential = (data[0].split(","))
            answer1 = data[1]
            answer2 = data[2]
            expectedTotal = data[3]
            dataTest.append(
                (loginCredential, answer1, answer2, expectedTotal)
            )
            line = f.readline()
    return dataTest


class TestBoundary1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(3000)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def exit_help_modal(self, driver):
        # Create an ActionChains object
        actions = ActionChains(driver)
        # Send the ESC key to exit the help modal
        actions.send_keys(Keys.ESCAPE).perform()
        actions.send_keys(Keys.ESCAPE).perform()

    @pytest.mark.parametrize(
        "loginCredential, "  # (username, password)
        "answer1, "
        "answer2, "
        "expectedTotal, ",
        dataForTest(),
    )
    def test_boundary1(self, loginCredential, answer1, answer2, expectedTotal):
        self.driver.get("https://sandbox404.moodledemo.net/")
        self.driver.set_window_size(1210, 1017)
        self.driver.find_element(By.CSS_SELECTOR, ".login > a").click()
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "username").send_keys(loginCredential[0])
        self.driver.find_element(By.ID, "password").send_keys(loginCredential[1])
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "My courses").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".multiline > span:nth-child(2)").click()
        time.sleep(3)
        self.exit_help_modal(self.driver)
        self.driver.find_element(By.CSS_SELECTOR, ".modtype_quiz .aalink").click()
        self.driver.find_element(By.XPATH,
                                 "//button[contains(.,\'Attempt quiz\') or contains(.,\'Re-attempt quiz\')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[contains(@id, \"1_answer\")]").clear()
        self.driver.find_element(By.XPATH, "//input[contains(@id,\'1_answer\')]").send_keys(answer1)
        self.driver.find_element(By.XPATH, "//input[contains(@id,\'2_answer\')]").clear()
        self.driver.find_element(By.XPATH, "//input[contains(@id,\'2_answer\')]").send_keys(answer2)
        self.driver.find_element(By.ID, "mod_quiz-next-nav").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,\'Submit all and finish\')]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".modal-footer > .btn-primary").click()
        time.sleep(2)
        assert self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) > .cell:nth-child(2)").text == expectedTotal
        actions = ActionChains(self.driver)
        # Scroll down till the end (Finish review button is INTERCEPTED BY THE STUPID "THIS PAGE WILL BE RESET" OF MOODLE")
        actions.scroll_by_amount(0, 1000).perform()
        self.driver.find_element(By.LINK_TEXT, "Finish review").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
