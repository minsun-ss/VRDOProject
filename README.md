# VRD Scraping
A handful of scripts for pulling variable rate information from EMMA. 

## Usage
```python
VRDOIssue.py # given a CUSIP or EMMA identifier, pull deal data
VRDOLiquidityFacility.py # given a CUSIP or EMMA identifier, pulls current liquidity facility provider
VRDOResetRate.py # given a CUSIP or EMMA identifier, pulls first 100 reset rates
```

The scripts use command line prompts and will ask you for file 
location where your CUSIP list is where you'd like to output results. 

The script relies on Selenium and BeautifulSoup4 python packages. 

## Caveats

The input file must be a CUSIP or the equivalent EMMA identifier.

Copyright (c) 2019 stuffofminsun
