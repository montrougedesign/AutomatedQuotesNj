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

#finnhub api key think
finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
#to find the right stl certificate for mongo db
ca = certifi.where()
#Mongo database API key think
client = pymongo.MongoClient("mongodb+srv://MYCoding:QV9BcLxtJqrInZB4@mycoding.pzucnk1.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)

#Message = "We are happy to announce that we fixed the ALL function\n and added a SEARCH function to be able to find a ticker for a company name"
#Message = "Please reach out to me with any issues or suggestions 848.226.2840"
#Message = " The way to use the SEARCH function is\ni.e 'tesla search'" 
#Message = "NEW FEATURE watch list. To add a WL you text ex. T/VZ/TMUS ADD. \nThis will create a WL. If this is your first WL the name will be WL1 the second WL2 etc."
#Message = "You can add as many tickers as you want but for best usage ONLY do 3 for each WL."
#Message = "To see how many WL you have, use function COUNT. If you have any questions or suggestions, feel free to contact me at \n848.226.2840"
Message = "Do to technical difficulties please use our new email address LakewoodnjQuotes@gmail.com Sorry for the inconvenience"
def emailserver():       
    global user 
    user = 'lakewoodnjQuotes@gmail.com'
    password = 'hlxnxrjvtgxeijky'
    receiveserver ='imap.gmail.com'
    global sendserver
    sendserver = smtplib.SMTP('smtp.gmail.com', 587)
    sendserver.starttls()
    global mail
    mail = imaplib.IMAP4_SSL(receiveserver)
    mail.login(user, password)
    sendserver.login(user, password)
def sendEmails(msg):
    db = client["Stocks"]
    collection = db["Users"]
    
    emails = collection.distinct("User")
    for email in emails:
        print(email)    
        sendserver.sendmail(user,email,msg)


def Main():
    emailserver()
    sendEmails(Message)

    print(Message)
Main()

