# python_login_bot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def startbot(username,password,url):
    path=r"C:\Users\Ryan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    services=Service(path)
    chrome_options=Options()
    chrome_options.add_argument("--start-maximized")
    driver=webdriver.Chrome(service=services,options=chrome_options)
    driver.get(url)
    username_field=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"username")))
    username_field.send_keys(username)
    password_field=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"password")))
    password_field.send_keys(password)
    click_login=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"submit")))
    click_login.click()
    # driver.find_element(By.NAME,"username").send_keys(username)
    # driver.find_element(By.NAME,"password").send_keys(password)
    # driver.find_element(By.CSS_SELECTOR,"login_button_css_selector").click()
username="username"
password="password"
url="https://www.instagram.com/"    
    
startbot(username,password,url)
