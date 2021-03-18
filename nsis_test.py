import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def init_driver():
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 10)
    return driver


def logga(driver, user, password):
    driver.get("http://nsis.sanita.it")
    try:
        print("//html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input")
        box_user = driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input")
        #box_user = driver.find_element_by_name("Ecom_User_ID")
        #box_user = driver.wait.until(EC.presence_of_element_located(
        #    (By.NAME, "Ecom_User_ID")))
        box_pwd = driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/input")
        #box_pwd = driver.find_element_by_name("Ecom_Password")
        #box_pwd = driver.wait.until(EC.presence_of_element_located(
        #    (By.NAME, "Ecom_Password")))
        #button = driver.wait.until(EC.element_to_be_clickable(
        #    (By.NAME, "loginButton2")))
        ######box_user.send_keys(user)
        ######box_pwd.send_keys(password)
        #button.click()
    except TimeoutException:
        print("Box or Button not found in google.com")


if __name__ == "__main__":
    driver = init_driver()
    logga(driver, "mi141180", "wCsoL,yksghg59")
    time.sleep(25)
    ##driver.quit()
