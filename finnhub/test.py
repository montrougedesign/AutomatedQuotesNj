from email import message
from typing import Counter
from requests.models import Response
import schedule
import smtplib
import requests
import finnhub
import time
import email
import imaplib
from bs4 import BeautifulSoup 
def moshe_automated():
    user = 'automatedquotesnj@gmail.com'
    password = 'Wassermans350'
    receiveserver = 'imap.gmail.com'
    sendserver = smtplib.SMTP('smtp.gmail.com', 587)
    sendserver.starttls()


    mail = imaplib.IMAP4_SSL(receiveserver)
    mail.login(user, password)

    sendserver.login(user , password)




    mail.select('moshe')


    result, data = mail.uid('search', None , "ALL")

    status, delete_data = mail.search(None, 'All')



    new_item_list = data[0].split()

    new_item_list_delete = delete_data[0].split()


    list_length_delete = len(new_item_list_delete)


    if list_length_delete >= 1:

        most_recent_email = new_item_list[-1]

        result2, email_data = mail.uid('fetch', most_recent_email, '(RFC822)')

        raw_email = email_data[0][1].decode("utf-8")

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
            


        content_type = part.get_content_type()

        html_ = part.get_payload()
        soup = BeautifulSoup(html_, "html.parser")
        receivedticker = soup.td.get_text(strip=True)
        receivedticker_up = receivedticker.upper()


        finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")

        price = str(finnhub_client.quote(receivedticker_up)['c'])
        percent_change = str(finnhub_client.quote(receivedticker_up)['dp'])
        Previous_close = str(finnhub_client.quote(receivedticker_up)['pc'])
        change = str(finnhub_client.quote(receivedticker_up)['d'])



        end = receivedticker_up + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%" "\n" + "Previos close  " + "$"+ Previous_close



        sendserver.sendmail('automatedquotesnj@gmail.com','8482262840@mms.att.net',end)

        print(end)
        
        for num in new_item_list_delete:
                mail.store(num,'+FLAGS','\\Deleted')


        mail.expunge()

        
    else: 
        print('nothing to show moshe')


def marcus_automated():
    user = 'automatedquotesnj@gmail.com'
    password = 'Wassermans350'
    receiveserver = 'imap.gmail.com'
    sendserver = smtplib.SMTP('smtp.gmail.com', 587)
    sendserver.starttls()


    mail = imaplib.IMAP4_SSL(receiveserver)
    mail.login(user, password)

    sendserver.login(user , password)




    mail.select('marcus')


    result, data = mail.uid('search', None , "ALL")

    status, delete_data = mail.search(None, 'All')



    new_item_list = data[0].split()

    new_item_list_delete = delete_data[0].split()


    list_length_delete = len(new_item_list_delete)


    if list_length_delete >= 1:

        most_recent_email = new_item_list[-1]

        result2, email_data = mail.uid('fetch', most_recent_email, '(RFC822)')

        raw_email = email_data[0][1].decode("utf-8")

        email_message = email.message_from_string(raw_email)

        for part in email_message.walk():
            part.get_content_maintype() == "multipart"
            msg = part.get_payload()
            msg_ticker =msg.strip()
            receivedticker_up = msg_ticker.upper()


        finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")

        price = str(finnhub_client.quote(receivedticker_up)['c'])
        percent_change = str(finnhub_client.quote(receivedticker_up)['dp'])
        Previous_close = str(finnhub_client.quote(receivedticker_up)['pc'])
        change = str(finnhub_client.quote(receivedticker_up)['d'])



        end = receivedticker_up + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%" "\n" + "Previos close  " + "$"+ Previous_close



        sendserver.sendmail('automatedquotesnj@gmail.com','8482262840@mms.att.net',end)

        print(end)
        
        for num in new_item_list_delete:
                mail.store(num,'+FLAGS','\\Deleted')


        mail.expunge()

        
    else: 
        print('nothing to show marcus')

def schorr_automated():
    user = 'automatedquotesnj@gmail.com'
    password = 'Wassermans350'
    receiveserver = 'imap.gmail.com'
    sendserver = smtplib.SMTP('smtp.gmail.com', 587)
    sendserver.starttls()


    mail = imaplib.IMAP4_SSL(receiveserver)
    mail.login(user, password)

    sendserver.login(user , password)




    mail.select('schorr')


    result, data = mail.uid('search', None , "ALL")

    status, delete_data = mail.search(None, 'All')



    new_item_list = data[0].split()

    new_item_list_delete = delete_data[0].split()


    list_length_delete = len(new_item_list_delete)


    if list_length_delete >= 1:

        most_recent_email = new_item_list[-1]

        result2, email_data = mail.uid('fetch', most_recent_email, '(RFC822)')

        raw_email = email_data[0][1].decode("utf-8")

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
            


        content_type = part.get_content_type()

        html_ = part.get_payload()
        soup = BeautifulSoup(html_, "html.parser")
        receivedticker = soup.td.get_text(strip=True)
        receivedticker_up = receivedticker.upper()


        finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")

        price = str(finnhub_client.quote(receivedticker_up)['c'])
        percent_change = str(finnhub_client.quote(receivedticker_up)['dp'])
        Previous_close = str(finnhub_client.quote(receivedticker_up)['pc'])
        change = str(finnhub_client.quote(receivedticker_up)['d'])



        end = receivedticker_up + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%" "\n" + "Previos close  " + "$"+ Previous_close



        sendserver.sendmail('automatedquotesnj@gmail.com','8482262840@mms.att.net',end)

        print(end)
        
        for num in new_item_list_delete:
                mail.store(num,'+FLAGS','\\Deleted')


        mail.expunge()

        
    else: 
        print('nothing to show schorr')





schedule.every(60).seconds.do(moshe_automated)
schedule.every(60).seconds.do(marcus_automated)
schedule.every(60).seconds.do(schorr_automated)

while 1:
    schedule.run_pending()
    time.sleep(1)

