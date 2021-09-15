import pandas as pd
import numpy as np
import re

from bs4 import BeautifulSoup
from scrape_cat import PROXY_LIST
import requests
import time






for tt in PROXY_LIST:     
    try:
        r = requests.get('https://tamkeenstores.com.sa/product/mk-zj2700ktz/', proxies={'http': tt, 'https': tt}, timeout=10 )
        if r.status_code == 200:
            print(r.status_code)
            break
    except:
        pass
soup  = BeautifulSoup(r.text, 'html.parser')
sku = soup.find('span', {'class': 'sku'}).text.strip()
print('sku', sku)