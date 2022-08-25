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


wl = [
    'WL1',
    'WL2',
    'WL3',
    'WL4',
    'WL5',
    'WL6',
    'WL7',
    'WL8',
    'WL9',
    'WL10',
    'WL11',
    'WL12',
    'WL13',
    'WL14',
    'WL15',
    'WL16',
    'WL17',
    'WL18']

tickers = [['T','VZ','KBWD'],
        ['ADBE','ALGN','ISGR'],
        ['NKE','LULU','ETSY'],
        ['V','AXP','PYPL'],
        ['MMP','EPD','WPC'],
        ['TROW','IVZ','SCHW'],
        ['HRB','WBA','FDX'],
        ['CRM','SQ','JPM'],
        ['AMT','SBUX','DVA'],
        ['QQQ','VTI','SPY'],
        ['LUV','ALK','DAL'],
        ['IPAY','QQQJ','JETS'],
        ['XLK','XLF','VTV'],
        ['NLOK','BIG','OLED'],
        ['PM','MO','STOR'],
        ['META','PINS','NFLX'],
        ['WFC','C','MA'],
        ['AAPL','GOOGL','AMZN']]

'''stock = [
    ['WL18','J'],
    ['WL5']
    ]'''
morelist = []
main_list =[]
all_from = []

index = 0

number = 0

wl_result = []

user = 'textaword@gmail.com'
password = 'mxbqirbsmlwkyesy'
receiveserver ='imap.gmail.com'
sendserver = smtplib.SMTP('smtp.gmail.com', 587)
sendserver.starttls()
mail = imaplib.IMAP4_SSL(receiveserver)
mail.login(user, password)
sendserver.login(user, password)


#select imbox
mail.select('Inbox')
#get the inbox
result, data = mail.uid('search',None, 'ALL')
#Make a list of the new items(list of emails in the Inbox)
new_items = data[0].split()
#get the length of the new item list (how many emails in the Inbox)
list_length = len(new_items)

counter = 0
if list_length >=1:
    for x in new_items:
        #get the email
        result2, email_data = mail.uid('fetch', new_items[counter] , '(RFC822)')
        #decode the email 
        raw_email = email_data[0][1].decode("utf-8")
        #not sure what this does will write it when i figure it out
        email_message = email.message_from_string(raw_email)
        #gets the email sender
        #from_ = email_message['From']
        all_from.append(email_message['From'])
        status, delete_data = mail.search(None, 'All')

        new_item_delete = delete_data[0].split()

        for part in email_message.walk():
            content_type = part.get_content_type()
            msg_ = part.get_payload()

            continue

        if content_type =='text/html':
            soup = BeautifulSoup(msg_,'html.parser')
            text = soup.td.get_text(strip=True).upper()
            morelist.append(text)
            counter += 1
        elif content_type == 'text/plain':
            text = msg_.strip().upper()
            morelist.append(text)
            counter +=1
        else:
            print('not a content type')
        
        print(counter)
print(all_from[number])
for w in morelist:
    morelist_new = nltk.word_tokenize(w)
    main_list.append(morelist_new)

    
    for x in wl:  
        for w in main_list:  
            
                if (x == w[0]):
                    print(w[0])
                    index = wl.index(w[0])
                    tictosend = tickers[index]
                    for x in tictosend:
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d'])
                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl_result.append(end)
                        #print(all_from[number])
                        number +=1


        wl_result_str ="".join(map(str,wl_result))


    print(wl_result_str)
