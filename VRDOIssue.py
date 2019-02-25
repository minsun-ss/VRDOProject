from selenium import webdriver
from selenium.webdriver.firefox.options import Options

filename = input("What is the filename with the cusips?")
outputname = input("Where do you want the results?")
filename = filename+".txt"

f = open(filename, "r")
f2 = open(outputname, "a+")
for x in f:
    x = x.rstrip("\n\r")  # strip out trailing linebreaks
    url = "http://emma.msrb.org/Security/Details/"+x
    print("Working on: "+x)

    # open up emma, agree to terms of use, turn on headless mode so I don't have to see Firefox windows all day
    opts = Options()
    opts.headless = True
    browser = webdriver.Firefox(options=opts)
    browser.get(url)
    getin = browser.find_elements_by_class_name("yesButton")
    getin[0].click()

    # initialize variables
    #EmmaIssue1
    InterestRate = 0
    MaturityDate = ""
    DatedDate = ""
    PrincipalAmount = 0
    ResetPeriod = ""
    MaximumRate = ""
    MinimumRate = ""
    ClosingDate = ""
    MinimumDenomination = ""
    NotificationPeriod = ""
    InitialOffering = ""
    RemarketingAgent = ""

    showMore = browser.find_element_by_id("lnkMoreInfo")
    showMore.click()
    results = browser.page_source

    innerHTML = browser.execute_script("return document.body.innerHTML")
    getTitle = browser.find_elements_by_xpath("//span[@help='Click to view issue details']")
    EMMAIssue1 = str(getTitle[0].text)

    getValues = browser.find_elements_by_xpath("//div[@class='card-body']/ul/li/span")
    for i in range(len(getValues)):
        if getValues[i].text == "Interest Rate:":
            InterestRate = getValues[i+1].text
        elif getValues[i].text == "Maturity Date:":
            MaturityDate = getValues[i+1].text
        elif getValues[i].text == "Dated Date:":
            DatedDate = getValues[i+1].text
        elif getValues[i].text == "Principal Amount at Issuance:":
            PrincipalAmount = getValues[i+1].text
            ResetPeriod = getValues[i+2].text
            MaximumRate = getValues[i+3].text
            MinimumRate = getValues[i+4].text
        elif getValues[i].text == "Closing Date:":
            ClosingDate = getValues[i+1].text

    f2.write(x+","+EMMAIssue1+","+InterestRate+","+MaturityDate+","+DatedDate+","+PrincipalAmount+","+ResetPeriod+","+
             MaximumRate+","+MinimumRate+","+ClosingDate+"\n")
    browser.close()