from selenium import webdriver
from selenium.webdriver.firefox.options import Options

filename = input("What is the filename with the cusips?")
outputname = input("Where do you want the results?")
filename = filename+".txt"

f = open(filename, "r")
f2 = open(outputname, "a+")
for x in f:
    url = "http://emma.msrb.org/Security/Details/"+x
    print("Working on: "+x)

    opts = Options()
    opts.headless = True
    browser = webdriver.Firefox(options=opts)
    browser.get(url)
    getin = browser.find_elements_by_class_name("yesButton")
    getin[0].click()

    #initialize variables

    #this opens up the "Get More Info" link on the EMMA VRDO page
    showMore = browser.find_element_by_id("lnkMoreInfo")
    showMore.click()
    results = browser.page_source
    #print(results)


    # not sure if I need these if I'm just stripping out the main parts of a deal - this might be better used when
    # stripping data for liquidity facilities
    getValues = browser.find_elements_by_xpath("//div[@id='divCollapsible']/ul/li/span")
    # set up a chain
    LiquidityFacility = []

    for j in range(len(getValues)):
        if getValues[j].text == "Liquidity Facility:":
            lf = getValues[j+1].text+","+getValues[j+3].text+","+getValues[j+5].text
            LiquidityFacility.append(lf)

    for i in range(len(LiquidityFacility)):
       f2.write(LiquidityFacility[i]+"\n")

    browser.close()