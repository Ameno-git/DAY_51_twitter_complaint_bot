from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISSED_UP = 10
PROMISSED_DOWN = 100
LOGIN = "+LOGIN"
PASSWORD = "PASSWORD q"
CHROME_DRIVER_PATH = "D:\pythonProject\othersoft\chromedriver.exe"


class InternetSpeedTwitterBot:

    def __init__(self, driver_pass):
        self.driver = webdriver.Chrome(driver_pass)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        """
        Testing ur internet connection speed
        """
        self.driver.get("https://www.speedtest.net/")
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        time.sleep(60)
        self.down = float(self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
            '2]/div/div[2]/span').text)
        self.up = float(self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
            '3]/div/div[2]/span').text)
        print(self.up, self.down)

        time.sleep(2)

    def twit_at_provider(self):
        """
        Log in twitter and post angry twit
        """
        if self.down < PROMISSED_DOWN:
            # login
            self.driver.get("https://twitter.com/login/")
            time.sleep(2)
            login = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
            login.send_keys(LOGIN)
            password = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
            password.send_keys(PASSWORD)
            password.send_keys(Keys.ENTER)
            time.sleep(2)

            # tweet
            tweet = f"Hey #ICN #Odessa why my connection speed is {self.up}(up)/{self.down}(down) whet" \
                    f" I pay for {PROMISSED_UP}(up)/{PROMISSED_DOWN}(down)"
            twee_text_field = self.driver.find_element_by_css_selector("br[data-text='true']")
            twee_text_field.send_keys(tweet)
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div['
                '1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()
            time.sleep(2)
            self.driver.quit()

        else:
            print("Speed is ok")


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.twit_at_provider()
