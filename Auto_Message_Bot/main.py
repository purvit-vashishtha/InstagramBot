"""
Created on Wed Jul  7 13:30:00 2021

@author: purvit
"""

# importing libraries
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# driver for chrome where we will be logging in our instagram account.
driver = webdriver.Chrome(ChromeDriverManager().install())

# declaring list of users to whom we want to send message or text.
target = ['rohitsharma45','virat.kohli']
# text we want to send them all.
message = "Testing of a bot"

# create user_defined class for bot
class Auto_message_bot:
    
    # init variables using __init__()
    def __init__(self, username, password, user, message):
        # init. username
        self.username = username
        # init. password
        self.password = password
        # init. user/target
        self.user = user
        # init. message that user wants to send
        self.message = message
        # instagram homepage url
        self.base_url = 'https://www.instagram.com/'
        # init. driver for chrome
        self.bot = driver
        # call login function which is defined below
        self.login()
  
    #  login function
    def login(self):
        # get instagram url
        self.bot.get(self.base_url)
        
        # enter username
        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        
        # enter password
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        
        # click enter for login
        enter_password.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # overcome first pop-up
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".sqdOP.yWX7d.y3zKF     "))).click()
  
        # overcome 2nd pop-up
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()
  
        # click direct button
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".xWeGp"))).click()
        
        
        #self.bot.find_element_by_xpath(
        #    '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        #time.sleep(2)
  
        # click pencil icon
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".ZQScA"))).click()
        #self.bot.find_element_by_xpath(
         #   '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
        #time.sleep(2)
        
        # loop through user/target audience
        for i in target:
  
            # enter the username
            WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".TGYkm input"))).send_keys(i)
         
            # click on the username
            WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".dCJp8"))).click()
  
            # next button
            WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".sqdOP.yWX7d.y3zKF.cB_4K"))).click()
            
            # click on message area
            send = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".X3a-9 textarea")))
            
            # types message
            send.send_keys(self.message)
            time.sleep(1)
  
            # send message
            send.send_keys(Keys.RETURN)
            time.sleep(2)
            
            # back to inbox
            WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".xWeGp"))).click()
  
            # clicks on pencil icon
            WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".ZQScA"))).click()
        
# function to start or initialize bot
def init():
    # call the bot class which we created above to start
    Auto_message_bot('type your username here','type your password here',target, message)
    input("Done!!")

# start sending messages
init()
