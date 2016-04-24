from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains

#gets the different year options for the particular dataset/survey/quarter selection
def getYears():
    print('years') #cuz debugging is hard
    try:
        time.sleep(5)
        years = driver.find_element_by_xpath('//span[text()="Year(s)"]/..')
        yearsOptions = years.find_elements_by_tag_name('input')
        return [years, yearsOptions, True]
    except:
        return [0, 0, False]

#gets the different ship options for the particular dataset/survey/quarter/year selections
def getShips():
    print('ships')
    try:
        time.sleep(3)
        ships = driver.find_element_by_xpath('//span[text()="Ship(s)"]/../..')
        allShips = ships.find_elements_by_tag_name('input')[0]
        #sometimes we grab the options too quickly and they haven't updated
        if (allShips.get_attribute('checked') != None):
            raise Exception('lol too quick')
        return [ships, allShips, True]
    except:
        return [0, 0, False]

#gets the different gears options for the particular dataset/survey/quarter/year selections
def getGears():
    print('gears')
    try:
        time.sleep(1)
        gears = driver.find_element_by_xpath('//span[text()="Gear(s)"]/..')
        allGears = ships.find_elements_by_tag_name('input')[0]
        #sometimes we grab the options too quickly and they haven't updated
        if (allGears.get_attribute('checked') != None):
            raise Exception('lol too quick')
        return [gears, allGears, True]
    except:
        return [0, 0, False]

#gets the different area options for the particular dataset/survey/quarter/year selections
def getAreas():
    print('areas')
    try:
        time.sleep(1)
        areas = driver.find_element_by_xpath('//span[text()="Area(s)"]/..')
        allAreas = ships.find_elements_by_tag_name('input')[0]
        #sometimes we grab the options too quickly and they haven't updated
        if (allAreas.get_attribute('checked') != None):
            raise Exception('lol too quick')
        return [areas, allAreas, True]
    except:
        return [0, 0, False]

#gets the different area options for the particular dataset/survey/quarter/year selections
def getSpecies():
    try:
        time.sleep(1)
        species = driver.find_element_by_xpath('//span[text()="Species"]/../..')
        allSpecies = ships.find_elements_by_tag_name('input')[0]
        #sometimes we grab the options too quickly and they haven't updated
        if (allSpecies.get_attribute('checked') != None):
            raise Exception('lol too quick')
        return [species, allSpecies, True]
    except:
        return [0, 0, False]

#go to page
driver = webdriver.Firefox()
#start a selenium browser
driver.get('https://datras.ices.dk/Data_products/Download/Download_Data_public.aspx')

#get all data products options
dataProducts = driver.find_element_by_xpath('//span[text()="Data products"]/..')
productOptions = dataProducts.find_elements_by_tag_name("option")
#get all different datasets for a particular product
for i in range(0,len(productOptions)):
    #have to reset selections every time the page changes, otherwise they're disconnected from the DOM
    dataProducts = driver.find_element_by_xpath('//span[text()="Data products"]/..')
    productOptions = dataProducts.find_elements_by_tag_name("option")
    productOptions[i].click()

    time.sleep(5)
    #get all of the survey options.
    survey = driver.find_element_by_xpath('//span[text()="Survey"]/..')
    surveyOptions = survey.find_elements_by_tag_name("option")

    #get all datasets for all different surveys
    for j in range(0,len(surveyOptions)):
        survey = driver.find_element_by_xpath('//span[text()="Survey"]/..')
        surveyOptions = survey.find_elements_by_tag_name("option")
        surveyOptions[j].click()

        quarters = driver.find_element_by_xpath('//span[text()="Quarter(s)"]/..')
        allQuarters = quarters.find_elements_by_tag_name('input')[0]
        if allQuarters.get_attribute('checked') == None:
            allQuarters.click()


        #since the page changes everytime something is clicked, and the speed of the updates
        #is variable, need to keep trying until it's updated despite a bunch of exceptions
        worked = False
        while(worked == False):
            data = getYears()
            years = data[0]
            yearsOptions = data[1]
            worked = data[2]

        #Need to get all the data for all the years, but sometimes it's too large to download directly, so download year
        #by year
        for k in range(0,len(yearsOptions) + len(yearsOptions)%5,5):
            worked = False
            while(worked == False):
                data = getYears()
                years = data[0]
                yearsOptions = data[1]
                worked = data[2]

            for l in range(k,k+5):
                if (len(yearsOptions) > l and yearsOptions[l].get_attribute('id') != 'ContentPlaceHolder1_cblist_years_0'):
                    yearsOptions[l].click()

            #This info doesn't always exist
            if (len(driver.find_elements_by_xpath('//span[text()="Ship(s)"]/..')) != 0):
                worked = False
                count = 0;
                while(worked == False and count < 3):
                    data = getShips()
                    ships = data[0]
                    allShips = data[1]
                    worked = data[2]
                    count += 1

                if (worked):
                    allShips.click();
            #gear info doesn't always exist, so you need to check if the section exists, then download
            #the data if it does
            if (len(driver.find_elements_by_xpath('//span[text()="Gear(s)"]/..')) != 0):
                worked = False
                count = 0
                while(worked == False and count < 3):
                    data = getGears()
                    gears = data[0]
                    allGears = data[1]
                    worked = data[2]
                    count += 1

                if (worked):
                    allGears.click();

            #area info doesn't always exist, so you need to check if the section exists, then download
            #the data if it does
            if (len(driver.find_elements_by_xpath('//span[text()="Area(s)"]/..')) != 0):
                worked = False
                count = 0
                while(worked == False and count < 3):
                    data = getAreas()
                    areas = data[0]
                    allAreas = data[1]
                    worked = data[2]
                    count += 1

                if (worked):
                    allAreas.click();

            #species info doesn't always exist, so you need to check if the section exists, then download
            #the data if it does
            if (len(driver.find_elements_by_xpath('//span[text()="Species"]/../..')) != 0):
                worked = False
                count = 0
                while(worked == False and count < 3):
                    data = getSpecies()
                    species = data[0]
                    allSpecies = data[1]
                    worked = data[2]
                    count += 1

                if (worked):
                    allSpecies.click();

            #have to submit the form, then accept the terms of use to download the info
            time.sleep(2)
            driver.find_elements_by_xpath('//input[@name="ctl00$ContentPlaceHolder1$btn_submit"]')[0].click()
            time.sleep(2)
            driver.find_element_by_xpath('//input[@name="ctl00$ContentPlaceHolder1$cbk_accept"]').click()
            time.sleep(1)

            #uncheck all of the year selections and do it all over again
            worked = False
            while(worked == False):
                data = getYears()
                years = data[0]
                yearsOptions = data[1]
                worked = data[2]

            for l in range(k,k+5):
                if (len(yearsOptions) > l and yearsOptions[l].get_attribute('id') != 'ContentPlaceHolder1_cblist_years_0'):
                    yearsOptions[l].click()


driver.close()


