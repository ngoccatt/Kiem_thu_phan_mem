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

filename = path = Path(__file__).parent / "equipClassData_full.json"

nameTest = []


def dataForTest():
    global nameTest
    commonData = {}
    dataTest = []
    with open(filename, "r") as f:
        data = json.load(f)
        for key, values in data.items():
            print(key)
            if "commonData" in key:
                commonData = values
            if "test" in key:
                url = values["url"]
                loginCredential = values["loginCredential"]
                eventName = values["eventName"]
                startTime = values["startTime"]

                expectedTime = values["expectedTime"]
                dataTest.append(
                    (commonData, url, loginCredential, eventName, startTime,
                     expectedTime)
                )
                nameTest.append(key)

    return dataTest


"""
get element value, assuming each element have "value" attribute
"""


def getElementValue(element):
    return element["value"].strip()


class TestEquiclass1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(3000)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()
        pass

    """
       Save effort when finding element, assuming all element object has "findMethod" and "findString" attribute.
       findMethod: By.??
       findString: a string to find element, depend on the findMethod.
       """

    def findElementShort(self, element):
        return self.driver.find_element(By.get_finder(element["findMethod"]), element["findString"])

    @pytest.mark.parametrize(
        "commonData, "
        "url, "
        "loginCredential, "  # (username, password)
        "eventName, "
        "startTime, "  # (day, month, year)
        "expectedTime, ",  # expected (day, month, year)
        dataForTest(),
        ids=nameTest
    )
    def test_equiclass1(self, commonData, url,
                        loginCredential, eventName, startTime, expectedTime):
        self.driver.get(url)
        self.driver.set_window_size(1274, 757)
        self.findElementShort(commonData["loginHomeButton"]).click()
        time.sleep(3)
        self.findElementShort(loginCredential["username"]).clear()
        self.findElementShort(loginCredential["password"]).clear()
        self.findElementShort(loginCredential["username"]).send_keys(getElementValue(loginCredential["username"]))
        self.findElementShort(loginCredential["password"]).send_keys(getElementValue(loginCredential["password"]))
        self.findElementShort(commonData["loginButton"]).click()
        time.sleep(3)
        self.findElementShort(commonData["dashboardButton"]).click()
        time.sleep(2)

        self.vars["month"] = self.driver.find_element(By.CSS_SELECTOR, ".current:nth-child(3)").text
        if self.driver.execute_script("return (arguments[0] != \"November 2024\")", self.vars["month"]):
            assert self.driver.find_element(By.CSS_SELECTOR, ".arrow_text:nth-child(2)").text == "November"
            self.driver.find_element(By.CSS_SELECTOR, ".arrow_text:nth-child(2)").click()

        self.findElementShort(commonData["newEventButton"]).click()
        time.sleep(1)
        self.findElementShort(eventName).send_keys(getElementValue(eventName))

        self.findElementShort(startTime["year"]).click()
        dropdown = self.findElementShort(startTime["year"])
        dropdown.find_element(By.XPATH,
                              f".//option[. = '{getElementValue(startTime["year"])}']").click()

        self.findElementShort(startTime["month"]).click()
        dropdown = self.findElementShort(startTime["month"])
        dropdown.find_element(By.XPATH,
                              f".//option[. = '{getElementValue(startTime["month"])}']").click()
        time.sleep(3)
        dropdown.find_element(By.XPATH,
                              f".//option[. = '{getElementValue(startTime["month"])}']").click()
        time.sleep(1)
        dropdown.find_element(By.XPATH,
                              f".//option[. = '{getElementValue(startTime["month"])}']").click()

        self.findElementShort(startTime["day"]).click()
        dropdown = self.findElementShort(startTime["day"])
        dropdown.find_element(By.XPATH,
                              f".//option[. = '{getElementValue(startTime["day"])}']").click()

        value = self.findElementShort(expectedTime["year"]).get_property("value")
        assert value == getElementValue(expectedTime["year"])
        value = self.findElementShort(expectedTime["month"]).get_property("value")
        assert value == getElementValue(expectedTime["month"])
        value = self.findElementShort(expectedTime["day"]).get_property("value")
        assert value == getElementValue(expectedTime["day"])
        # Create an ActionChains object
        actions = ActionChains(self.driver)
        # Send the ESC key
        actions.send_keys(Keys.ESCAPE).perform()
        actions.send_keys(Keys.ESCAPE).perform()
        # log out
        time.sleep(3)
        self.findElementShort(commonData["userToggleMenu"]).click()
        self.findElementShort(commonData["logOutButton"]).click()