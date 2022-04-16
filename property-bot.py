from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



#warnings.filterwarnings("ignore", category=DeprecationWarning) 

search_type = 'rent'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)

driver.get('https://www.domain.com.au')
if search_type == 'rent':
    driver.find_element(By.XPATH,'//*[@id="domain-home-content"]/div/div/form/div[1]/div/button[2]').click()
    
    #click on filters
    driver.find_element(By.XPATH,'//*[@id="domain-home-content"]/div/div/form/div[2]/div/div/div[1]/div/section/div/div/div/div/div[2]/button/span').click()
    
    #click on exact values options
    driver.find_element(By.XPATH,'//*[@id="domain-home-content"]/div/div/div/div[2]/form/div[5]/div/div[2]/label/div[1]/input').click()
    driver.find_element(By.XPATH,'//*[@id="domain-home-content"]/div/div/div/div[2]/form/div[6]/div/div[2]/label/div[1]/input').click()
    #driver.find_element_by_xpath('//*[@id="domain-home-content"]/div/div/div/div[2]/form/div[7]/div/div[2]/label/div[1]/input').click()

    
    #click on 2 bedroom button
    driver.find_element(By.XPATH,'//*[@id="domain-home-content"]/div/div/div/div[2]/form/div[5]/div/div[1]/label[3]').click()
    
    #click on 2 bathrooms button
    driver.find_element(By.XPATH,'//*[@id="domain-home-content"]/div/div/div/div[2]/form/div[6]/div/div[1]/label[3]').click()
    
    #click on 1 parking spot
    driver.find_element(By.XPATH,'//*[@id="domain-home-content"]/div/div/div/div[2]/form/div[7]/div/div[1]/label[2]').click()



    search_areas = ['Waterloo,', 'Alexandria']
    
    
    for area in search_areas:
        driver.find_element(By.XPATH,'//*[@id="fe-pa-domain-home-typeahead-input"]').send_keys(area, Keys.RETURN)
    
    
    #search
    driver.find_element(By.XPATH,'//*[@id="domain-home-content"]/div/div/div/div[1]/div/div[3]/div[2]/button').click()
    
    
    resultSet = driver.find_element(By.XPATH,'//*[@id="skip-link-content"]/div[1]/div[2]/ul')
    options = resultSet.find_elements(By.TAG_NAME,"li")
    
    for option in options:
        print(option.text)
        print('**************NEW PROPERTY*******************')
        