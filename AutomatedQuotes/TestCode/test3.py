from cgitb import html
from email import message
from hashlib import new
import smtplib
import email
import imaplib
import pprint
from bs4 import BeautifulSoup
import nltk 
import finnhub
import time
import schedule

finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")


wl = ['WL1','WL2','WL3','WL4','WL5']

tickers = [['T','VZ','KBWD'],
        ['ADBE','ALGN','ISGR'],
        ['NKE','LULU','ETSY'],
        ['V','AXP','PYPL'],
        ['MMP','EPD','WPC'],
        ['TROW','IVZ','SCHW'],
        ['HRB','WBA','FDX'],
        ['CRM','SQ','JPM']]

stock = [['WL4','J'],['WL2'],['WL5']]

index = 0

wl_result = []

if len(stock) >1:

    for x in wl:
        for w in stock:

            if (x == w[0]):
                index = wl.index(w[0])
                tictosend = tickers[index]
                for x in tictosend:
                    price = str(finnhub_client.quote(x)['c'])
                    percent_change = str(finnhub_client.quote(x)['dp'])
                    change = str(finnhub_client.quote(x)['d'])
                    end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                    wl_result.append(end)

                wl_result_str ="".join(map(str,wl_result))



    print(wl_result_str)
