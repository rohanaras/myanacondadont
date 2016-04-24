import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# page 1

browser = webdriver.Firefox()
browser.get('http://oceanadapt.rutgers.edu/download/')
assert 'Ocean Adapt' in browser.title

elem_name = browser.find_element_by_name('my-name') #Find the search box
elem_name.send_keys('Rick Roll')

elem_email = browser.find_element_by_name('my-email')
elem_email.send_keys('RickRoll@Astley.com')

elem_institution = browser.find_element_by_name('my-institution')
elem_institution.send_keys('Astley')

elem_purpose = browser.find_elements_by_tag_name("textarea")
elem_purpose[0].send_keys("never gonna give you up...")

elem_button = browser.find_elements_by_tag_name("button")
elem_button[0].click()


# page 2

#select a region
#elem_region = browser.find_element_by_id("regionID")
#print elem_region
#for option in elem_region.find_element_by_tag_name('option'):
#    print option

# All Check Boxes

elem_alldata2 = browser.find_elements_by_css_selector('input[type="checkbox"]')
for elem in elem_alldata2:
    browser.execute_script("$(arguments[0]).click();", elem)


# lat, long, depth

# hit download


#elem.send_keys('seleniumhq' + Keys.RETURN)

#browser.quit()