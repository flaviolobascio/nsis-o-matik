# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class HSP11(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_h_s_p11(self):
        driver = self.driver
        driver.get("https://nsis.sanita.it/")
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath("//td").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath("//td").click()
        driver.find_element_by_name("Ecom_User_ID").click()
        driver.find_element_by_name("Ecom_User_ID").clear()
        driver.find_element_by_name("Ecom_User_ID").send_keys("mi141180")
        driver.find_element_by_name("Ecom_Password").click()
        driver.find_element_by_name("Ecom_Password").clear()
        driver.find_element_by_name("Ecom_Password").send_keys("Palmito.35")
        driver.find_element_by_name("loginButton2").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_link_text("Flussi Informativi").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_xpath("//tr[6]/td/table/tbody/tr/td").click()
        driver.find_element_by_xpath("//img[@onclick=\"window.open('https://nsis.sanita.it/BOMDS/BOCustomBridge/bo-bridge-logon.jsp?user=FLR_150000')\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_2 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=2 | ]]
        driver.find_element_by_id("MyDocs_treeView_treeNode7_name").click()
        driver.find_element_by_id("MyDocs_treeView_treeNode4_name").click()
        driver.find_element_by_id("MyDocs_treeView_treeNode8_name").click()
        driver.find_element_by_id("ListingURE_detailView_listColumn_1_0_1").click()
        driver.find_element_by_id("ListingURE_detailView_listColumn_1_0_1").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=ListingURE_detailView_listColumn_1_0_1 | ]]
        driver.find_element_by_id("ListingURE_detailView_listColumn_0_0_1").click()
        driver.find_element_by_id("ListingURE_detailView_listColumn_0_0_1").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=ListingURE_detailView_listColumn_0_0_1 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=5 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("IconImg__dhtmlLib_298").click()
        driver.find_element_by_id("fileTypeList").click()
        Select(driver.find_element_by_id("fileTypeList")).select_by_visible_text("Excel (.xlsx)")
        driver.find_element_by_id("fileTypeList").click()
        driver.find_element_by_id("BtnCImg_csvopOKButton").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_id("logoffLink-button").click()
        driver.close()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        driver.close()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath("//b").click()
        driver.close()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
