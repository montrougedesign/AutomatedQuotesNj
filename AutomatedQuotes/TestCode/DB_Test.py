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


class DB():
    ca = certifi.where()
    client = pymongo.MongoClient("mongodb+srv://MYCoding:QV9BcLxtJqrInZB4@mycoding.pzucnk1.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)
    def NewUse(self,userID,tickerID):
        db = self.client["Stocks"]
        collection = db["Users"]
        post = {"User": userID, "Ticker": tickerID}
        collection.insert_one(post)
    def getNextSequence(self,name):
        db = self.client["Stocks"]
        ret = db.WL_Id_Counter.find_one_and_update(
                { '_id': name },
                { '$inc': { 'seq': 1 } },
                return_document= True
        )
        return ret['seq']
    def NewWL(self,user,tickers):    
        db = self.client["Stocks"]
        collection = db["WL"]
        post = {"User": user, "Tickers": tickers}
        collection.insert_one(post)
    def getWL(self,id):
        db = self.client["Stocks"]
        collection = db["WL"]    
        document = collection.find_one({'_id': id})
        return document
    def getWLByUser(self,user,wlNum):
        db = self.client["Stocks"]
        collection = db["WL"]
        document = collection.find({'User': user}).skip(wlNum).limit(1)[0]["Tickers"].split(',')
        return document
    def AddLotsWL(self,user,tickers):
        db = self.client["Stocks"]
        collection = db["WL"]
        for i in tickers:
            post = {"User": user, "Tickers": i}
            collection.insert_one(post)
#print(DB().getWL(1)['Tickers'])    
print(DB().getWLByUser("8482619494@mms.att.net",1))  
#DB().NewWL("8482262840@mms.att.net","T,M,GE")

