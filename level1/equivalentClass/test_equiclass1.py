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

filename = path = Path(__file__).parent / "equipClassData_full.txt"

def dataForTest():
    dataTest = []
    with open(filename, "r") as f:
        line = f.readline()
        while line:
            data = line.split(";")
            for i in range(0, len(data)):
                data[i] = str(data[i]).strip()
            loginCredential = (data[0].split(","))
            eventName = data[1]
            startTime = (data[2].split(","))
            expectedTime = (data[3].split(","))
            dataTest.append(
                (loginCredential, eventName, startTime, expectedTime)
            )
            line = f.readline()
    return dataTest


class TestEquiclass1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(3000)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()
        pass

    @pytest.mark.parametrize(
        "loginCredential, "  # (username, password)
        "eventName, "
        "startTime, "  # (day, month, year)
        "expectedTime, ",  # expected (day, month, year)
        dataForTest(),
    )
    def test_equiclass1(self, loginCredential, eventName, startTime, expectedTime):
        self.driver.get("https://sandbox404.moodledemo.net/")
        self.driver.set_window_size(1274, 757)
        self.driver.find_element(By.CSS_SELECTOR, ".login > a").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "username").send_keys(loginCredential[0])
        self.driver.find_element(By.ID, "password").send_keys(loginCredential[1])
        self.driver.find_element(By.CSS_SELECTOR, ".login-container").click()
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
        time.sleep(2)
        self.vars["month"] = self.driver.find_element(By.CSS_SELECTOR, ".current:nth-child(3)").text
        if self.driver.execute_script("return (arguments[0] != \"November 2024\")", self.vars["month"]):
            assert self.driver.find_element(By.CSS_SELECTOR, ".arrow_text:nth-child(2)").text == "November"
            self.driver.find_element(By.CSS_SELECTOR, ".arrow_text:nth-child(2)").click()
        self.driver.find_element(By.XPATH, "//button[contains(.,\'New event\')]").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "id_name").send_keys("Testing")
        self.driver.find_element(By.ID, "id_timestart_year").click()
        dropdown = self.driver.find_element(By.ID, "id_timestart_year")
        dropdown.find_element(By.XPATH, f".//option[. = '{startTime[2]}']").click()
        self.driver.find_element(By.ID, "id_timestart_month").click()
        dropdown = self.driver.find_element(By.ID, "id_timestart_month")
        dropdown.find_element(By.XPATH, f".//option[. = '{startTime[1]}']").click()
        dropdown.find_element(By.XPATH, f".//option[. = '{startTime[1]}']").click()
        self.driver.find_element(By.ID, "id_timestart_day").click()
        dropdown = self.driver.find_element(By.ID, "id_timestart_day")
        dropdown.find_element(By.XPATH, f".//option[. = '{startTime[0]}']").click()
        value = self.driver.find_element(By.ID, "id_timestart_year").get_property("value")
        assert value == expectedTime[2]
        value = self.driver.find_element(By.ID, "id_timestart_month").get_property("value")
        assert value == expectedTime[1]
        value = self.driver.find_element(By.ID, "id_timestart_day").get_property("value")
        assert value == expectedTime[0]
        # Create an ActionChains object
        actions = ActionChains(self.driver)
        # Send the ESC key
        actions.send_keys(Keys.ESCAPE).perform()
        actions.send_keys(Keys.ESCAPE).perform()
        time.sleep(1)
        self.driver.find_element(By.ID, "user-menu-toggle").click()
        self.driver.find_element(By.XPATH, "//a[contains(.,\'Log out\')]").click()