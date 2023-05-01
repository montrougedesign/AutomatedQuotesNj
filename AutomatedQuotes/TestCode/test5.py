import finnhub
import pprint
import datetime
import nltk
from bs4 import BeautifulSoup
from finvizfinance.quote import finvizfinance
"""


from operator import index
import re
from sys import api_version

from cv2 import detail_ExposureCompensator


wl = ['k','WL1','WL2','WL3','WL4','WL5','WL6','WL7']


test = 'WL1'

test_list = ['h','WL1','ABR']

tickers = [
        [],
        ['T','VZ','KBWD'],
        ['ADBE','ALGN','ISGR'],
        ['NKE','LULU','ETSY'],
        ['V','AXP','PYPL'],
        ['MMP','EPD','WPC'],
        ['TROW','IVZ','SCHW'],
        ['HRB','WBA','FDX'],
        ['CRM','SQ','JPM']]

ans = []

def switch(wl):
        my_dict ={
            '':0,
            'WL1':1,
            'WL2':2,
            'Wl3':3,
            'Wl4':4,
            'Wl5':5,
            'WL6':6,
            'WL7':7,
            'WL8':8,
            'WL9':9,
            'WL10':10,
            'WL11':11,
            'WL12':12,
            'WL13':13,
            'WL14':14,
            'WL15':15,
            'WL16':16,
            'WL17':17,
            'WL18':18,
        }
        return my_dict.get(wl)



for a in test_list:
    if str(type(switch(a))) == "<class 'int'>":
        dex = test_list.index(a)
        list_name_index = switch(a)
        list_of_tickers = tickers[list_name_index]
        for item in list_of_tickers:
            print(item + "\n")
        print(a)
        print(dex)
        print('hello')
        
    elif str(type(switch(a))) == "<class 'NoneType'>":
        dex = test_list.index(a)
        print(a)
        print(dex)
        print('nohello')
"""
"""today = datetime.date.today() 

finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")


rawData = finnhub_client.company_news('F', _from=today, to=today)

#pprint.pprint(rawData)

for i in rawData:
    #print(i["source"])
    print(i["headline"])
    #print(i["summary"])"""

"""
stock = finvizfinance('tsla')


#print(stock.ticker_fundament())    
print(finvizfinance('rh').ticker_inside_trader())"""

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
    def __init__(self, ticker, action):
        self.ticker = ticker
        self.action = action    
    def GetAll(self):
        result =""
        file = open("AutomatedQuotes\AutomatedQuotesNj\AutomatedQuotes\TestCode\data.txt", "r").read().split(",")
        headers = open("AutomatedQuotes\AutomatedQuotesNj\AutomatedQuotes\TestCode\dataHeaders.txt", "r").read().split(",")
        for index, item in enumerate(file) :
            item.strip('\"')
            header = headers[index].strip('\"')
            result += f"{header}: {finvizfinance(self.ticker).ticker_fundament()[item]}\n"   
        return result
    def GetOne(self):
        result = ""
        file = open("AutomatedQuotes\AutomatedQuotesNj\AutomatedQuotes\TestCode\data.txt", "r").read().split(",")
        headers = open("AutomatedQuotes\AutomatedQuotesNj\AutomatedQuotes\TestCode\dataHeaders.txt", "r").read().split(",")
        for index, head in enumerate(headers) :
            head = head.strip('\"')
            if self.action == head:
                file = file[index].strip('\"')
                result += f"{head}: {finvizfinance(self.ticker).ticker_fundament()[file]}"      
                break
        return result        
s = Stock('t', "ROE")   
#pprint.pprint()
print(s.GetOne())



"""print(r)
for i in r:
    i = i.strip('\"')
    i.strip('\n')
    print(i)
    print(finvizfinance('t').ticker_fundament()[i])"""
    
    