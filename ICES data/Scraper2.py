from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains


def getYears():
    print('years')
    try:
        time.sleep(5)
        years = driver.find_element_by_xpath('//span[text()="Year(s)"]/..')
        yearsOptions = years.find_elements_by_tag_name('input')
        return [years, yearsOptions, True]
    except:
        return [0, 0, False]

def getShips():
    print('ships')
    try:
        time.sleep(3)
        ships = driver.find_element_by_xpath('//span[text()="Ship(s)"]/../..')
        allShips = ships.find_elements_by_tag_name('input')[0]
        if (allShips.get_attribute('checked') != None):
            raise Exception('lol too quick')
        return [ships, allShips, True]
    except:
        return [0, 0, False]

def getGears():
    print('gears')
    try:
        time.sleep(1)
        gears = driver.find_element_by_xpath('//span[text()="Gear(s)"]/..')
        allGears = ships.find_elements_by_tag_name('input')[0]
        if (allGears.get_attribute('checked') != None):
            raise Exception('lol too quick')
        return [gears, allGears, True]
    except:
        return [0, 0, False]

def getAreas():
    print('areas')
    try:
        time.sleep(1)
        areas = driver.find_element_by_xpath('//span[text()="Area(s)"]/..')
        allAreas = ships.find_elements_by_tag_name('input')[0]
        if (allAreas.get_attribute('checked') != None):
            raise Exception('lol too quick')
        return [areas, allAreas, True]
    except:
        return [0, 0, False]

def getSpecies():
    try:
        time.sleep(1)
        species = driver.find_element_by_xpath('//span[text()="Species"]/../..')
        allSpecies = ships.find_elements_by_tag_name('input')[0]
        if (allSpecies.get_attribute('checked') != None):
            raise Exception('lol too quick')
        return [species, allSpecies, True]
    except:
        return [0, 0, False]

#go to page
driver = webdriver.Firefox()
driver.get('https://datras.ices.dk/Data_products/Download/Download_Data_public.aspx')

#get all data products and survey options
dataProducts = driver.find_element_by_xpath('//span[text()="Data products"]/..')
productOptions = dataProducts.find_elements_by_tag_name("option")
for i in range(0,len(productOptions)):
    dataProducts = driver.find_element_by_xpath('//span[text()="Data products"]/..')
    productOptions = dataProducts.find_elements_by_tag_name("option")
    productOptions[i].click()

    time.sleep(5)
    survey = driver.find_element_by_xpath('//span[text()="Survey"]/..')
    surveyOptions = survey.find_elements_by_tag_name("option")

    for j in range(0,len(surveyOptions)):
        survey = driver.find_element_by_xpath('//span[text()="Survey"]/..')
        surveyOptions = survey.find_elements_by_tag_name("option")
        surveyOptions[j].click()

        quarters = driver.find_element_by_xpath('//span[text()="Quarter(s)"]/..')
        allQuarters = quarters.find_elements_by_tag_name('input')[0]
        if allQuarters.get_attribute('checked') == None:
            allQuarters.click()



        worked = False
        while(worked == False):
            data = getYears()
            years = data[0]
            yearsOptions = data[1]
            worked = data[2]


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


            time.sleep(2)
            driver.find_elements_by_xpath('//input[@name="ctl00$ContentPlaceHolder1$btn_submit"]')[0].click()
            time.sleep(2)
            driver.find_element_by_xpath('//input[@name="ctl00$ContentPlaceHolder1$cbk_accept"]').click()
            time.sleep(1)

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


