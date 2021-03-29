from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'http://ec2-54-208-152-154.compute-1.amazonaws.com'


class WebControl():
    """contains methods to interact with web browser"""

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)

    def fill_bowl(self, lst: list, side: str):
        """
        Appends coins to the different bowl sides
        :param: side: str right or left
        """
        for i in range(len(lst)):
            elem = self.driver.find_element(By.ID, f"{side}_{i}")
            elem.send_keys(lst[i])

    def click_weigh(self):
        self.driver.find_element(By.XPATH, "//button[text()='Weigh']").click()

    def click_reset(self):
        self.driver.find_element(By.XPATH, "//button[text()='Reset']").click()

    def get_result(self):
        elem = self.driver.find_element(
            By.XPATH, "//div/button[@id='reset']").text
        return elem

    def get_weighing(self):
        elems = self.driver.find_elements_by_tag_name("li")
        weighs = [elem.text for elem in elems]
        print("weighing list: \n", weighs)
        return weighs

    def check_alert(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        print(f"Alert Message: {text}")
        alert.accept()
        return text

    def click_fakebar(self, index: int):
        self.driver.find_element_by_id(f"coin_{index}").click()
        alert = self.check_alert()
        return alert

    def close_driver(self):
        self.driver.close()
