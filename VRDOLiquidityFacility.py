from selenium import webdriver
from selenium.webdriver.firefox.options import Options

filename = input("What is the filename with the cusips? ")
outputname = input("Where do you want the results? ")
filename = filename+".txt"

f = open(filename, "r")
f2 = open(outputname, "a+")
for x in f:
    x = x.rstrip("\n\r")  # strip out trailing linebreaks
    url = "http://emma.msrb.org/Security/Details/"+x
    print("Working on: "+x)

    # sets up headless mode to run in background
    opts = Options()
    opts.headless = True
    browser = webdriver.Firefox(options=opts)
    browser.get(url)
    getin = browser.find_elements_by_class_name("yesButton")
    getin[0].click()

    #agree to EMMA's terms of use
    showMore = browser.find_element_by_id("lnkMoreInfo")
    showMore.click()
    results = browser.page_source
    #print(results)


    getValues = browser.find_elements_by_xpath("//div[@id='divCollapsible']/ul/li/span")
    # set up a chain
    LiquidityFacility = []

    for j in range(len(getValues)):
        if getValues[j].text == "Liquidity Facility:":
            lf = getValues[j+1].text+","+getValues[j+3].text+","+getValues[j+5].text
            LiquidityFacility.append(lf)

    for i in range(len(LiquidityFacility)):
       f2.write(x+","+LiquidityFacility[i]+"\n")

    browser.close()
print("Done")