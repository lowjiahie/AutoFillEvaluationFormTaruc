# -*- codeing = utf-8 -*-
# @Time : 6/10/2022 10:50 PM
# @Author : JASON LOW
# @File : autoEvaluation.py
# @Software : PyCharm
from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

print("This is auto filling evaluation form program")
studentID = input("Please enter your intranet student id : ")
password = input("Please enter your intranet password : ")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://web.tarc.edu.my/portal/login.jsp')

userNameInput = driver.find_element(By.ID,'username')
userNameInput.click()
userNameInput.send_keys(studentID)


passwordInput = driver.find_element(By.ID,'password')
passwordInput.click()
passwordInput.send_keys(password)

submitLoginBtn = driver.find_element(By.XPATH,'(//button[@type="button"])[1]')
submitLoginBtn.click()
time.sleep(1)

# find the survey dropdown
surveyDropdown = driver.find_element(By.CLASS_NAME, 'fa-pencil-square-o')
surveyDropdown.find_element(By.XPATH,'..').click()
time.sleep(1)

# find the evaluation a tag link which placed at 53
linkToEvaluate = driver.find_element(By.XPATH,'(//a)[53]')
linkToEvaluate.click()

# all the radio btn
allRadioBtn = driver.find_elements(By.XPATH,'(//input[@type="radio"])')

print(allRadioBtn)
print(len(allRadioBtn))

count = 1

while count <= len(allRadioBtn):
    radioBtn = driver.find_element(By.XPATH,'(//input[@type="radio"])[1]')
    radioBtn.click()
    submitBtn = driver.find_element(By.XPATH,'(//input[@type="submit"])[1]')
    submitBtn.click()
    time.sleep(1)
    allPointRadioButton = driver.find_elements(By.XPATH,'(//input[@value="10"])')
    for pointRadioButton in allPointRadioButton:
        pointRadioButton.click()
        time.sleep(1)

    time.sleep(1)
    lastSubmitBtn = driver.find_element(By.ID,'submitbtn')
    lastSubmitBtn.click()
    count+=1
