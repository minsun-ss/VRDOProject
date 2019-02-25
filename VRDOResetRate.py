from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import re
import time


browser = webdriver.Firefox()
browser.get("https://emma.msrb.org/Security/Details/A129CCBA06E6DF60CDAD51032BC0B3CF9")


getin = browser.find_elements_by_class_name("yesButton")
getin[0].click()
time.sleep(5)

#initialize variables
ResetDate = ""
InterestRate = ""
RateType = ""
RateEffectiveDate = ""
AggregateParAmountBankBonds = ""
AggregateParAmountBankBondsInvestorsAndRemarketingAgent = ""

#this opens up the "Get More Info" link on the EMMA VRDO page
showMore = browser.find_element_by_id("lnkMoreInfo")
showMore.click()

#find the Display and change from 10 to 100
select = Select(browser.find_element_by_name("vrdoRateHistory_length"))
select.select_by_visible_text("100")

results = browser.page_source
#print(results)

getValues = browser.find_elements_by_xpath("//tbody/tr[@role='row']")

for j in range(len(getValues)):
    singlereset = getValues[j].get_attribute('innerHTML')
    # print(singlereset)
    singleresetlist = singlereset.split("<td")
    #
    # skip first item, 2nd item is reset date

    #print(singleresetlist[1])
    singleresetlist[1] = singleresetlist[1].replace("</td>", "")
    singleresetlist[1] = singleresetlist[1][22:]
    ResetDate = singleresetlist[1]

    #print(singleresetlist[2])
    singleresetlist[2] = singleresetlist[2].replace("</td>", "")
    singleresetlist[2] = singleresetlist[2][13:]
    InterestRate = singleresetlist[2]

    #print(singleresetlist[3])
    a = singleresetlist[3].split
    soup = BeautifulSoup(singleresetlist[3], 'html.parser')
    taglist = soup.find_all(re.compile('img'))
    try:
        RateType = taglist[0]['help']
        print(RateType)
    except:
        print("nope, nothing")
        RateType = ""
    #print(a)



browser.close()