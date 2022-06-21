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
    user = 'txtaquote@gmail.com'
    password = '@Wassermans350'
    receiveserver = 'imap.gmail.com'
    sendserver = smtplib.SMTP4_SSL('smtp.gmail.com', 587)
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
                msg_ticker = msg_.strip()
                receivedticker_up = msg_ticker.upper()
            else:
                print("not a content type")       


    if list_length >= 1:

        get_type()

        if receivedticker_up == "WL1":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl1 = ['T','VZ','KBWD']
            wl1_result =[]

            for x in wl1:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl1_result.append(end)

            wl1_result_str ="".join(map(str,wl1_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl1_result_str)

            print(wl1_result_str)
            
        elif receivedticker_up == "WL2":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl2 = ['ADBE','ALGN','ISRG']
            wl2_result =[]

            for x in wl2:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl2_result.append(end)

            wl2_result_str ="".join(map(str,wl2_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl2_result_str)

            print(wl2_result_str)

        elif receivedticker_up == "WL3":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl3 = ['NKE','LULU','ETSY']
            wl3_result =[]

            for x in wl3:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl3_result.append(end)

            wl3_result_str ="".join(map(str,wl3_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl3_result_str)

            print(wl3_result_str)

        elif receivedticker_up == "WL4":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl4 = ['V','AXP','PYPL']
            wl4_result =[]

            for x in wl4:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl4_result.append(end)

            wl4_result_str ="".join(map(str,wl4_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl4_result_str)

            print(wl4_result_str)
        
        elif receivedticker_up == "WL5":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl5 = ['MMP','EPD','WPC']
            wl5_result =[]

            for x in wl5:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl5_result.append(end)

            wl5_result_str ="".join(map(str,wl5_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl5_result_str)

            print(wl5_result_str)
        
        elif receivedticker_up == "WL6":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl6 = ['TROW','IVZ','SCHW']
            wl6_result =[]

            for x in wl6:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl6_result.append(end)

            wl6_result_str ="".join(map(str,wl6_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl6_result_str)

            print(wl6_result_str)

        elif receivedticker_up == "WL7":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl7 = ['HRB','WBA','FDX']
            wl7_result =[]

            for x in wl7:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl7_result.append(end)

            wl7_result_str ="".join(map(str,wl7_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl7_result_str)

            print(wl7_result_str)

        elif receivedticker_up == "WL8":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl8 = ['CRM','SQ','JPM']
            wl8_result =[]

            for x in wl8:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl8_result.append(end)

            wl8_result_str ="".join(map(str,wl8_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl8_result_str)

            print(wl8_result_str)

        elif receivedticker_up == "WL9":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl9 = ['AMT','SBUX','DVA']
            wl9_result =[]

            for x in wl9:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl9_result.append(end)

            wl9_result_str ="".join(map(str,wl9_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl9_result_str)

            print(wl9_result_str)

        elif receivedticker_up == "WL10":
                From_ = email_message['from']
                finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
                wl10 = ['QQQ','VTI','SPY']
                wl10_result =[]

                for x in wl10:
                    #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                    price = str(finnhub_client.quote(x)['c'])
                    percent_change = str(finnhub_client.quote(x)['dp'])
                    #Previous_close = str(finnhub_client.quote(x)['pc'])
                    change = str(finnhub_client.quote(x)['d']) 


                    end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                    wl10_result.append(end)

                wl10_result_str ="".join(map(str,wl10_result))
                print("\n"+time.asctime() + '\n' +From_)
                sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl10_result_str)

                print(wl10_result_str)

        elif receivedticker_up == "WL11":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl11 = ['LUV','ALK','DAL']
            wl11_result =[]

            for x in wl11:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl11_result.append(end)

            wl11_result_str ="".join(map(str,wl11_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl11_result_str)

            print(wl11_result_str)

        elif receivedticker_up == "WL12":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl12 = ['IPAY','QQQJ','JETS']
            wl12_result =[]

            for x in wl12:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl12_result.append(end)

            wl12_result_str ="".join(map(str,wl12_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl12_result_str)

            print(wl12_result_str)  

        elif receivedticker_up == "WL13":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl13 = ['XLK','XLF','VTV']
            wl13_result =[]

            for x in wl13:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl13_result.append(end)

            wl13_result_str ="".join(map(str,wl13_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl13_result_str)

            print(wl13_result_str)

        elif receivedticker_up == "WL14":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl14 = ['NLOK','BIG','OLED']
            wl14_result =[]

            for x in wl14:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl14_result.append(end)

            wl14_result_str ="".join(map(str,wl14_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl14_result_str)

            print(wl14_result_str) 

        elif receivedticker_up == "WL15":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl15 = ['PM','MO','STOR']
            wl15_result =[]

            for x in wl15:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl15_result.append(end)

            wl15_result_str ="".join(map(str,wl15_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl15_result_str)

            print(wl15_result_str)

        elif receivedticker_up == "WL16":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl16 = ['FB','PINS','NFLX']
            wl16_result =[]

            for x in wl16:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl16_result.append(end)

            wl16_result_str ="".join(map(str,wl16_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl16_result_str)

            print(wl16_result_str)

        elif receivedticker_up == "WL17":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl17 = ['WFC','C','MA']
            wl17_result =[]

            for x in wl17:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl17_result.append(end)

            wl17_result_str ="".join(map(str,wl17_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl17_result_str)

            print(wl17_result_str)

        elif receivedticker_up == "WL18":
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
            wl18 = ['AAPL','GOOGL','AMZN']
            wl18_result =[]

            for x in wl18:
                #name = str(finnhub_client.company_profile2(symbol = x)['name']) 
                price = str(finnhub_client.quote(x)['c'])
                percent_change = str(finnhub_client.quote(x)['dp'])
                #Previous_close = str(finnhub_client.quote(x)['pc'])
                change = str(finnhub_client.quote(x)['d']) 


                end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                wl18_result.append(end)

            wl18_result_str ="".join(map(str,wl18_result))
            print("\n"+time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ , wl18_result_str)

            print(wl18_result_str)             

        else:             
                
            From_ = email_message['from']
            finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
                    

            #name = str(finnhub_client.company_profile2(symbol = receivedticker_up)['name'])               
            price = str(finnhub_client.quote(receivedticker_up)['c'])
            percent_change = str(finnhub_client.quote(receivedticker_up)['dp'])
            Previous_close = str(finnhub_client.quote(receivedticker_up)['pc'])
            change = str(finnhub_client.quote(receivedticker_up)['d']) 


            end = "\n" + receivedticker_up + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%" "\n" + "Previous Close  " + "$"+ Previous_close


            print("\n" + time.asctime() + '\n' +From_)
            sendserver.sendmail('automatedquotesnj@gmail.com', From_ ,end)

            print(end)          
            
    else:
        print("\n" + time.asctime() + '\n' +'nothing to show')

    for num in new_item_list_delete:
        mail.store(num,'+FLAGS','\\Deleted')


        mail.expunge()        
        




def wifi():
    url = "https://google.com"
    timeout_five = 10

    while True:
        try:
            request = requests.get(url , timeout = timeout_five)
            print("\n ------- \n" + "Connected")
            automatedquotes()
            
        except:
            print("\n ------- \n" + "Not Connected")
        

schedule.every(10).seconds.do(wifi)

while 1:
    schedule.run_pending()
    time.sleep(1)    