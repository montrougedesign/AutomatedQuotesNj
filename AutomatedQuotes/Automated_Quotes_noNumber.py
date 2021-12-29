from email import message
from typing import Counter
from bs4.element import DEFAULT_OUTPUT_ENCODING
from requests.models import Response
import schedule
import smtplib
import requests
import finnhub
import time
import email
import imaplib
from bs4 import BeautifulSoup 

def automatedquotes():
    user = 'automatedquotesnj@gmail.com'
    password = 'Wassermans350'
    receiveserver = 'imap.gmail.com'
    sendserver = smtplib.SMTP('smtp.gmail.com', 587)
    sendserver.starttls()


    mail = imaplib.IMAP4_SSL(receiveserver)
    mail.login(user, password)

    sendserver.login(user , password)

    mail.select('Inbox')

    result, data = mail.uid('search', None, "ALL")

    status, delete_data = mail.search(None, 'All')

    new_item_list = data[0].split()

    new_item_list_delete = delete_data[0].split()

    list_length = len(new_item_list)

    
    
    

    def get_type():

        # extract the data
        for x in new_item_list:
            result2, email_data = mail.uid('fetch', x, '(RFC822)')
            raw_email = email_data[0][1].decode("utf-8")
            global email_message
            email_message = email.message_from_string(raw_email)
            counter = 1
            for part in email_message.walk():
                if part.get_content_maintype() == "multipart":
                    continue
                filename = part.get_filename()
                if not filename:
                    ext = '.html'
                    filename = 'mes-part-%08d%s' %( counter,ext)
                    counter += 1
            
            global msg_
            msg_ = part.get_payload()
            global content_type
            content_type = part.get_content_type()
            
            
            #format the data

            #for att----------
            if content_type == 'text/html':
                soup = BeautifulSoup(msg_, "html.parser")
                receivedticker = soup.td.get_text(strip=True)
                global receivedticker_up
                receivedticker_up = receivedticker.upper()
            #for vz-----------    
            elif content_type == 'text/plain':
                msg_ticker =msg_.strip()
                receivedticker_up = msg_ticker.upper()
            else:
                print("not a content type")       


    if list_length >= 1:

        get_type()              
                
        From_ = email_message['from']
        finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
                

                        
        price = str(finnhub_client.quote(receivedticker_up)['c'])
        percent_change = str(finnhub_client.quote(receivedticker_up)['dp'])
        Previous_close = str(finnhub_client.quote(receivedticker_up)['pc'])
        change = str(finnhub_client.quote(receivedticker_up)['d']) 


        end = receivedticker_up + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%" "\n" + "Previous Close  " + "$"+ Previous_close


        print(time.asctime() + '\n' +From_)
        sendserver.sendmail('automatedquotesnj@gmail.com', From_ ,end)

        print(end)          
            
    else:
        print(time.asctime() + '\n' +'nothing to show')

    for num in new_item_list_delete:
        mail.store(num,'+FLAGS','\\Deleted')


        mail.expunge()        
        
schedule.every(60).seconds.do(automatedquotes)

while 1:
    schedule.run_pending()
    time.sleep(1)


