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

def emailserver():       
    global user 
    user = 'marvinshteible@gmail.com'
    password = 'tgcspdaikdhkimko'
    receiveserver ='imap.gmail.com'
    global sendserver
    sendserver = smtplib.SMTP('smtp.gmail.com', 587)
    sendserver.starttls()
    global mail
    mail = imaplib.IMAP4_SSL(receiveserver)
    mail.login(user, password)
    sendserver.login(user, password)

    mail.select('Inbox')
    #get the inbox
    result, data = mail.uid('search',None, 'UnSeen')
    #Make a list of the new items(list of emails in the Inbox)
    global new_items
    new_items = data[0].split()
    #get the length of the new item list (how many emails in the Inbox)
    global list_length
    list_length = len(new_items)

def get_text():
    global from_list
    from_list =[]
    global item_data_list
    item_data_list = []
    for x in new_items:
        #get the email
        result2, email_data = mail.uid('fetch', x , '(RFC822)')
        #decode the email 
        raw_email = email_data[0][1].decode("utf-8")
        #not sure what this does will write it when i figure it out
        email_message = email.message_from_string(raw_email)
        #gets the email sender
        #from_list = email_message['From']

        status, delete_data = mail.search(None, 'All')

        new_item_delete = delete_data[0].split()

        for part in email_message.walk():
            content_type = part.get_content_type()
            msg_ = part.get_payload()

            continue

        if content_type =='text/html':
            try:
                soup = BeautifulSoup(msg_,'html.parser')
                text = soup.td.get_text(strip=True).upper()
                item_data_list.append(text)
            except:
                soup = BeautifulSoup(msg_,'html.parser')
                text = soup.div.get_text(strip=True).upper()
                item_data_list.append(text)    
        elif content_type == 'text/plain':
            text = msg_.strip().upper()
            
            item_data_list.append(text)
        else:
            print(content_type)
        
        from_list.append(email_message['From']) 
        
emailserver()
get_text()

print(item_data_list)