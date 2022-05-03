import datetime
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import warnings
from selenium.webdriver.common.by import By
import unittest
class Story(unittest.TestCase):
    driver = None
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    def test_1_login(self):
        driver = self.driver
        driver.get("https://dev-cms.wilsonlive.app/auth")
        driver.find_element(by=By.XPATH, value='//*[@name="phoneNumber"]').send_keys("+919173341234")
        time.sleep(2)
        driver.find_element(by=By.XPATH, value='//button[text()="Login"]').click()
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//*[@name="verificationCode"]').send_keys("6614")
        time.sleep(1)
        driver.find_element(by=By.XPATH, value='//button[text()="Send"]').click()
    def test_2_click_widgets(self):
        driver = self.driver
        driver.find_element(by=By.XPATH, value='(//a[text()="Widgets"])[2]').click()
        time.sleep(1)
        driver.find_element(by=By.XPATH, value='//button[text()="Create a Widget"]').click()
    def test_3_story_creation(self):
        driver = self.driver
        driver.find_element(by=By.ID, value='mui-component-select-type').click()
        time.sleep(1)
        driver.find_element(by=By.XPATH, value='//*[@data-value="STORY"]').click()
        #-----------------------------General Setting-----------------------------------------#
        driver.find_element(by=By.XPATH, value='//*[text()="General settings"]').click()
        driver.find_element(by=By.NAME, value='exclusive').click()
        x = datetime.datetime.now()
        random_number = x.strftime("%f")
        driver.find_element(by=By.NAME, value='title').send_keys('Story_'+random_number)
        driver.find_element(by=By.NAME, value='background').send_keys('#fcba03')
        driver.find_element(by=By.NAME, value='subtitle').send_keys('Webly_'+random_number)
        tags = ['Evolution','discount','Football','wilson']
        for x in tags:
            driver.find_element(by=By.ID, value='mui-13').send_keys(x)
            time.sleep(1)
            driver.find_element(by=By.XPATH, value='//*[@role="presentation"]').click()
            time.sleep(1)
        #---------------------------------Feed Assets------------------------------------#
        driver.find_element(by=By.XPATH,value='//*[text()="Feed assets"]').click()
        driver.find_element(by=By.XPATH, value='//*[@name="titleVisibility"]').click()
        driver.find_element(by=By.XPATH, value='//*[@name="buttonVisibility"]').click()
        driver.find_element(by=By.XPATH, value='//*[@name="shareIcon"]').click()
        driver.find_element(by=By.NAME, value='feedTitleColor').send_keys('#c1d9e0')
        driver.find_element(by=By.NAME, value='feedAssetsButtonText').send_keys('Click to Apply')
        driver.find_element(by=By.NAME, value='feedAssetsButtonColor').send_keys('#03c2fc')
        driver.find_element(by=By.NAME, value='feedAssetsButtonTextColor').send_keys('#f7f4f2')
        driver.find_element(by=By.XPATH, value='(//*[@type="file"])[1]').send_keys('D:/Wilson/ASSETS/1.jpg')
        #-----------------------------Story Assets----------------------------------#
        driver.find_element(by=By.XPATH,value='//*[text()="STORY ASSETS"]').click()
        driver.find_element(by=By.NAME, value='storyAuthorName').send_keys('WeblyQA')
        driver.find_element(by=By.NAME, value='storyButtonText').send_keys('Apply')
        driver.find_element(by=By.ID, value='avatar').send_keys('D:/Wilso/ASSETS/5.jpg')
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//button[text()="Add"]').click()
        check_url_photo = driver.find_element(by=By.XPATH, value="/html/body/div/div[1]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/input").get_attribute('id')
        print(check_url_photo)
        driver.find_element(by=By.ID, value=check_url_photo).send_keys('D:/Wilso/ASSETS/5.jpg')
        driver.find_element(by=By.NAME, value='name').send_keys('www.google.com')
        #-----------------------------------Right column-----------------------------------#
        driver.find_element(by=By.ID, value='mui-component-select-status').click()
        driver.find_element(by=By.XPATH, value='//*[@data-value="Live"]').click()
        x = datetime.datetime.now()
        driver.find_element(by=By.XPATH, value='(//input[@placeholder="mm/dd/yyyy"])[1]').send_keys(x.strftime("%m") + x.strftime("%d") + x.strftime("%Y"))
        driver.find_element(by=By.XPATH, value='(//input[@placeholder="hh:mm"])[1]').send_keys('0120')
        y = x.strftime("%m")
        z = int(y) + 2
        driver.find_element(by=By.XPATH, value='(//input[@placeholder="mm/dd/yyyy"])[2]').send_keys(str("0")+str(z) + x.strftime("%d") + x.strftime("%Y"))
        driver.find_element(by=By.XPATH, value='(//input[@placeholder="hh:mm"])[2]').send_keys('0120')
        for y in range(5, 9):
            driver.find_element(by=By.XPATH, value='(//input[@type="checkbox"])['+str(y)+']').click()
            time.sleep(1)
        driver.find_element(by=By.XPATH, value='//button[text()="Save"]').click()
    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Test completed")




















