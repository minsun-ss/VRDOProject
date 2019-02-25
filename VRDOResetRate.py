from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
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
    soup = BeautifulSoup(singlereset, 'html.parser')
    singleresetlist = soup.find_all('td')

    #Reset Date is first in the td list
    ResetDate = singleresetlist[0].text

    #Interest Rate is second in the list
    InterestRate = singleresetlist[1].text

    #Reset Date is third
    soup2 = BeautifulSoup(str(singleresetlist[2]), 'html.parser')
    taglist = soup2.find_all('img')
    try:
        RateType = taglist[0]['help']
    except:
        RateType = ""

    #Rate effective date is fourth in the list
    RateEffectiveDate = singleresetlist[3].text

    # Bank Bonds are fifth in the list
    AggregateParAmountBankBonds = singleresetlist[4].text

    # Non bank bonds are last
    AggregateParAmountBankBondsInvestorsAndRemarketingAgent = singleresetlist[5].text

    # try to print only those valid lines
    if ResetDate != "":
        print(ResetDate+","+InterestRate+","+RateType+","+RateEffectiveDate+","+AggregateParAmountBankBonds+","+AggregateParAmountBankBondsInvestorsAndRemarketingAgent)


browser.close()