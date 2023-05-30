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
import pymongo
import certifi
import datetime
from finvizfinance.quote import finvizfinance
import requests

class TD():
    
    def __init__(self,ticker):
        self.tdaAPI_KEY = 'KGJRQK2GZHFIPSCIQSCFZ6JVK8G6GYYL'
        self.ticker = ticker
        self.fundamental = requests.get(f"https://api.tdameritrade.com/v1/instruments?apikey={self.tdaAPI_KEY}&symbol={self.ticker}&projection=fundamental").json()
    
    def Fundamental(self,ticker):
        
        response = requests.get(f"https://api.tdameritrade.com/v1/instruments?apikey={self.tdaAPI_KEY}&symbol={ticker}&projection=fundamental").json()
        
        return response
    
    
    def GetName(self):
        
        name = self.fundamental[self.ticker.upper()]['description']
        
        return name
    def GetPE(self):
        
        #pe = self.Fundamental(ticker)[ticker.upper()]['fundamental']['peRatio']
        pe = self.fundamental[self.ticker.upper()]['fundamental']['peRatio']
        
        if pe == 0:
            pe = '-'
            
        result = f'PE: {pe}'  
        
        return result
    def GetROE(self):
        
        #pe = self.Fundamental(ticker)[ticker.upper()]['fundamental']['returnOnEquity']
        respons = self.fundamental[self.ticker.upper()]['fundamental']['returnOnEquity']
        
        if  respons == 0:
            respons = '-'
            
        result = f'ROE: {respons}'  
        
        return result
    def GetROA(self):
        
        #pe = self.Fundamental(ticker)[ticker.upper()]['fundamental']['returnOnAssets']
        respons = self.fundamental[self.ticker.upper()]['fundamental']['returnOnAssets']
        
        if  respons == 0:
            respons = '-'
            
        result = f'ROA: {respons}'  
        
        return result
    def GetCR(self):
        
        #pe = self.Fundamental(ticker)[ticker.upper()]['fundamental']['currentRatio']
        respons = self.fundamental[self.ticker.upper()]['fundamental']['currentRatio']
        
        if  respons == 0:
            respons = '-'
            
        result = f'CR: {respons}'  
        
        return result
    def GetBVPS(self):
        
        #pe = self.Fundamental(ticker)[ticker.upper()]['fundamental']['bookValuePerShare']
        respons = self.fundamental[self.ticker.upper()]['fundamental']['bookValuePerShare']
        
        if  respons == 0:
            respons = '-'
            
        result = f'BVPS: {respons}'  
        
        return result
    def GetGM(self):
        
        #pe = self.Fundamental(ticker)[ticker.upper()]['fundamental']['grossMarginMRQ']
        respons = self.fundamental[self.ticker.upper()]['fundamental']['grossMarginMRQ']
        
        if  respons == 0:
            respons = '-'
            
        result = f'GM: {respons}'  
        
        return result
    def GetDE(self):
        
        #pe = self.Fundamental(ticker)[ticker.upper()]['fundamental']['totalDebtToEquity']
        respons = self.fundamental[self.ticker.upper()]['fundamental']['totalDebtToEquity']
        
        if  respons == 0:
            respons = '-'
            
        result = f'DE: {respons}'  
        
        return result
#td = TD('aapl')
"""print(td.GetName())    
print(td.GetPE())    
print(td.GetROE()) 
print(td.GetROA())
print(td.GetCR())"""
