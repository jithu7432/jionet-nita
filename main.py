#!/usr/bin/env python3
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

import warnings
warnings.filterwarnings('ignore')

USERNAME = "username"
PASSWORD = "password"


class XPATH:
    checkbox = "/html/body/div[4]/div[2]/div/div/div[1]/form/div[1]/section/div[4]/div[2]/label/span[1]/span"
    continue_btn = "/html/body/div[4]/div[2]/div/div/div[1]/form/div[1]/section/div[2]/div[2]/button/span"
    jio_id = """//*[@id="authSelectForm"]/section/div[2]/button"""
    login = "/html/body/div[4]/div[2]/div/div/div[1]/form/div[1]/section/div[5]/div[2]/button"
    logout = "/html/body/div[1]/div[2]/section[2]/div/div[2]/a/span"
    password = "/html/body/div[4]/div[2]/div/div/div[1]/form/div[1]/section/div[2]/div[2]/label/span/input"
    username = "/html/body/div[4]/div[2]/div/div/div[1]/form/div[1]/section/div[1]/div[2]/label/span/input"


class Browser:
    def __init__(self) -> None:
        self.home = "https://jionet2.jio.in:8443/"
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("detach", True)
        options.add_experimental_option("prefs", dict(credentials_enable_service=False, profile=dict(password_manager_enabled=False)))
        self.driver = WebDriver('/usr/bin/chromedriver', options=options)
        self.driver.get(self.home)

    def redirect_home(self) -> None:
        self.driver.get(self.home)

    def login(self) -> bool:
        jio_id = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, XPATH.jio_id)))
        jio_id.click()
        username = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, XPATH.username)))
        username.send_keys(USERNAME)
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, XPATH.password)))
        password.send_keys(PASSWORD)
        checkbox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, XPATH.checkbox)))
        checkbox.click()
        login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, XPATH.login)))
        login.click()
        contn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, XPATH.continue_btn)))
        contn.click()
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, XPATH.logout)))
        except NoSuchElementException:
            return False
        return True


def main() -> None:
    browser = Browser()
    if browser.login():
        # Router has some wierd behaviour
        raise SystemExit(browser.driver.quit())
    # else quit and repeat
    browser.driver.quit()
    main()


if __name__ == "__main__":
    main()
