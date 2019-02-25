from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time


filename = input("What is the filename with the cusips?")
outputname = input("Where do you want the results?")
filename = filename+".txt"


f = open(filename, "r")
f2 = open(outputname, "a+")

for x in f:
    x = x.rstrip("\n\r")
    url = "http://emma.msrb.org/Security/Details/" + x
    print("Working on: " + x)

    opts = Options()
    opts.headless = True
    browser = webdriver.Firefox(options=opts)
    browser.get(url)

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

        # Reset Date is first in the td list
        ResetDate = singleresetlist[0].text

        # Interest Rate is second in the list
        InterestRate = singleresetlist[1].text

        # Reset Date is third
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
            f2.write(x+","+ResetDate+","+InterestRate+","+RateType+","+RateEffectiveDate+","+AggregateParAmountBankBonds+","+AggregateParAmountBankBondsInvestorsAndRemarketingAgent+"\n")

    browser.close()
print("Done")