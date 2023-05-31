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

Message = "We are excited to announce the release of version 3,\nwhich includes bug fixes and watch list updates.\nPlease reach out with any issues or suggestions 848.226.2840"

def emailserver():       
    global user 
    user = 'txtaquote@gmail.com'
    password = 'yumdkitwnqhmixzf'
    receiveserver ='imap.gmail.com'
    global sendserver
    sendserver = smtplib.SMTP('smtp.gmail.com', 587)
    sendserver.starttls()
    global mail
    mail = imaplib.IMAP4_SSL(receiveserver)
    mail.login(user, password)
    sendserver.login(user, password)
def sendEmails(msg):
    db = client["AMQ"]
    collection = db["Emails"]
    
    emails = collection.find({"email":{'$exists': True}})
    for email in emails:
        print(email['email'])    
        sendserver.sendmail(user,email['email'],msg)


def Main():
    emailserver()
    sendEmails(Message)

    print(Message)
Main()