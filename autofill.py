import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

inputName = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
inputEmailID = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
inputPhone = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
Submit = '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div'


def sleep():
    time.sleep(3)

form_link = input("Enter the link for the google form")
browser_name = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe")
browser_name.get(form_link)

name=  []
email = []
phone = []

with open("input.csv", "r") as f_input:
    csv_input = csv.DictReader(f_input)
    for row in csv_input:
        name.append(row['name'])
        email.append(row['email'])
        phone.append(row['phone_number'])

i = 0

while i < len(name):
    browser_name.find_element_by_xpath(inputName).send_keys(name[i])
    browser_name.find_element_by_xpath(inputEmailID).send_keys(email[i])
    browser_name.find_element_by_xpath(inputPhone).send_keys(phone[i])
    sleep()
    browser_name.find_element_by_xpath(Submit).click()
    i += 1
    sleep()
    browser_name.back()
    sleep()

browser_name.quit()