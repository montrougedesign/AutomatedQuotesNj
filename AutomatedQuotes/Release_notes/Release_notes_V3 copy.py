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

Message = "Dueto technical difficulties txtaquote@gmail.com will not be working anymore. The new email address is textlivequotes@gmail.com "

def emailserver():       
    global user 
    user = 'textlivequotes@gmail.com'
    password = 'hvnhjfsnpsahjbhw'
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
