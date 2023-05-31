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

class DB():
    ca = certifi.where()
    client = pymongo.MongoClient("mongodb+srv://MYCoding:QV9BcLxtJqrInZB4@mycoding.pzucnk1.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)
    def NewUse(self,userID,tickerID):
        db = self.client["Stocks"]
        collection = db["Users"]
        post = {"User": userID, "Ticker": tickerID}
        collection.insert_one(post)
    def PostLots(self,Function,API_Field):
        db = db = self.client["Stocks"]
        collection = db["Alpha_Vantage"]
        for i, f in enumerate(Function):
            post = {"Function":f, "API_Field":API_Field[i]}
            collection.insert_one(post)
    def PostOne(self,Function,API_Field):
        db = db = self.client["Stocks"]
        collection = db["Alpha_Vantage"]
        post = {"Function":Function, "API_Field":API_Field}
        collection.insert_one(post)       
    def GetAllFundemetals(self):
        db = db = self.client["Stocks"]
        collection = db["Alpha_Vantage"]
        return collection.find()

