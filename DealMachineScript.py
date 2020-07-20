
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


def runEntry(loginUsername, loginPassword, propertyTag, filepath):
    # Starts WebDriver for chrome
    driver = webdriver.Chrome("C:\/chromedriver.exe")
    driver.get("https://dealmachine.com/login")
    time.sleep(2)

    loginUsername = "lvhomesolutionss@gmail.com"
    loginPassword = "l011178l"
    propertyTag = "Absentee"

    # finds email textbox and inputs given email
    emailInput = driver.find_element_by_xpath('//input[@name = "email"]')
    emailInput.clear()
    emailInput.send_keys(loginUsername)

    # finds password textbox and inputs given password
    passwordInput = driver.find_element_by_xpath('//input[@name = "password"]')
    passwordInput.clear()
    passwordInput.send_keys(loginPassword)

    # finds login button and clicks
    loginButton = driver.find_element_by_class_name("deal-primary-button")
    loginButton.click()
    time.sleep(2)

    driver.get("https://dealmachine.com/app/map")

    time.sleep(2)

    # From here

    address = "2485 Huff Rd, Imperial"
    homeOwner = "Mervat Kelada"
    propertyAddedBool = False
    propertyNewlyAddedBool = False

    searchButton = driver.find_element_by_xpath('//input[@name = "search"]')
    searchButton.click()

    searchButton.send_keys(address)
    searchButton.send_keys(Keys.ENTER)

    time.sleep(2)

    propertyButton = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/a[1]')
    propertyButton.click()

    time.sleep(1)

    homeOwnerSiteElement = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div/div[4]/div[1]/div/div[2]/div[2]/div')

    time.sleep(1)

    # Checks if property has already been added previously ----- make function that checks for previously added
    # propertyCheck = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div/div[2]/div[2]/div')
    # if (propertyCheck.text == "Pending Approval\nkeyboard_arrow_down") :
    #    propertyAddedBool = True

    # ------------------------------------------------------

    if (homeOwner == homeOwnerSiteElement.text) and (propertyAddedBool == False):
        addProperty = driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[1]/a/div/div/div[2]/div[3]/div/a')
        addProperty.click()
        propertyNewlyAddedBool = True

    time.sleep(2)

    if (propertyNewlyAddedBool == True):
        editTagsButton = driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div/div[1]/a/div/div/div[2]/div[2]/div[2]/div/a/div/div')
        editTagsButton.click()
        time.sleep(2)

        if (propertyTag == "Absentee"):
            absenteeTag = driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div[1]/form/div[1]/div[3]/div/div[2]/a/div/div[2]')
            absenteeTag.click()

        if (propertyTag == "Distressed"):
            distressedTag = driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div[1]/form/div[1]/div[3]/div/div[1]/a/div/div[2]')
            distressedTag.click()

        time.sleep(1)
        updateButton = driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div[1]/form/div[2]/button/div/div/div/span')
        updateButton.click()