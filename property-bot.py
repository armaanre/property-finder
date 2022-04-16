from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os



driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")

driver.get('https://www.domain.com.au')