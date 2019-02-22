from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://emma.msrb.org/Security/Details/A129CCBA06E6DF60CDAD51032BC0B3CF9")
getin = browser.find_elements_by_class_name("yesButton")
getin[0].click()

#initialize variables

#this opens up the "Get More Info" link on the EMMA VRDO page
showMore = browser.find_element_by_id("lnkMoreInfo")
showMore.click()
results = browser.page_source
#print(results)

#this gets the additional innerHTML... not sure if I am on the right track with that one.
#innerHTML = browser.execute_script("return document.body.innerHTML")
#print(innerHTML)


# not sure if I need these if I'm just stripping out the main parts of a deal - this might be better used when
# stripping data for liquidity facilities
getValues = browser.find_elements_by_xpath("//div[@id='divCollapsible']/ul/li/span")
# set up a chain
LiquidityFacility = []

print(len(getValues))
for j in range(len(getValues)):
    if getValues[j].text == "Liquidity Facility:":
        print("Yes")
        lf = getValues[j+1].text+","+getValues[j+3].text+","+getValues[j+5].text
        LiquidityFacility.append(lf)

print(LiquidityFacility)


browser.close()