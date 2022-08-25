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

def code():

    try:
        user = 'txtaquote@gmail.com'
        password = 'yumdkitwnqhmixzf'
        receiveserver ='imap.gmail.com'
        sendserver = smtplib.SMTP('smtp.gmail.com', 587)
        sendserver.starttls()
        mail = imaplib.IMAP4_SSL(receiveserver)
        mail.login(user, password)
        sendserver.login(user, password)

        mail.select('Inbox')
        #get the inbox
        result, data = mail.uid('search',None, 'UnSeen')
        #Make a list of the new items(list of emails in the Inbox)
        new_items = data[0].split()
        #get the length of the new item list (how many emails in the Inbox)
        list_length = len(new_items)




        item_data_list = []

        from_list = []





        def get_text():
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
                    soup = BeautifulSoup(msg_,'html.parser')
                    text = soup.td.get_text(strip=True).upper()
                    item_data_list.append(text)
                elif content_type == 'text/plain':
                    text = msg_.strip().upper()
                    item_data_list.append(text)
                else:
                    print('not a content type')
                from_list.append(email_message['From'])    




        tickers = [['T','VZ','KBWD'],
                ['ADBE','ALGN','ISRG'],
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
                ['FB','PINS','NFLX'],
                ['WFC','C','MA'],
                ['AAPL','GOOGL','AMZN']]



        def switch(wl):
                my_dict ={
                    '':0,
                    'WL1':1,
                    'WL2':2,
                    'WL3':3,
                    'WL4':4,
                    'WL5':5,
                    'WL6':6,
                    'WL7':7,
                    'WL8':8,
                    'WL9':9,
                    'WL10':10,
                    'WL11':11,
                    'WL12':12,
                    'WL13':13,
                    'WL14':14,
                    'WL15':15,
                    'WL16':16,
                    'WL17':17,
                    'WL18':18,
                }
                return my_dict.get(wl)

        finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")

        time_ = time.asctime()
        wl_result =[]
        counter = 0

        if list_length >= 1:
            get_text()
            for a in item_data_list:
                item_token = nltk.word_tokenize(a)
                if len(item_token) == 1:
                    if str(type(switch(a))) == "<class 'int'>":
                        
                        list_name_index = switch(a) - 1
                        list_of_tickers = tickers[list_name_index]
                        list_result = []
                        for item in list_of_tickers:
                            price = str(finnhub_client.quote(item)['c'])
                            percent_change = str(finnhub_client.quote(item)['dp'])
                            change = str(finnhub_client.quote(item)['d'])

                            end = "\n" + item + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"    

                            list_result.append(end)
                            list_result_str = "".join(map(str,list_result))
                        
                        sendserver.sendmail('textaword@gmail.com',from_list[counter],list_result_str)
                        print('\n'+ time_ + '\n' + from_list[counter] +'\n'+ list_result_str)
                        counter +=1
                        time.sleep(10)
                        
                    elif str(type(switch(a))) == "<class 'NoneType'>":
                        price = str(finnhub_client.quote(a)['c'])
                        percent_change = str(finnhub_client.quote(a)['dp'])
                        Previous_close = str(finnhub_client.quote(a)['pc'])
                        change = str(finnhub_client.quote(a)['d'])
                        dex = item_data_list.index(a)

                        end = "\n" + a + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%" "\n" + "Previous Close  " + "$"+ Previous_close


                        print("\n" + time.asctime() + '\n' + from_list[counter] + end)
                        sendserver.sendmail('textaword@gmail.com', from_list[counter] ,end)
                        time.sleep(10)
                        counter += 1
                elif len(item_token) == 2:

                    if item_token[1] == 'ALL':
                        raw = finnhub_client.company_basic_financials(item_token[0],"all")

                        price = 'Price: ' + '$'+str(finnhub_client.quote(item_token[0])['c'])

                        pe = 'P/E: ' + str(raw['metric']['peBasicExclExtraTTM'])

                        roe = 'ROE: ' + str(raw['metric']['roeRfy'])
                        
                        roa = 'ROA: ' + str(raw['metric']['roaRfy'])
                        
                        cr = 'CR: ' + str(raw['metric']['currentRatioAnnual'])

                        bvps = 'BVPS: ' + str(raw['metric']['bookValuePerShareAnnual'])

                        gm = 'GM: ' + str(raw['metric']['grossMarginAnnual'])

                        de = 'D/E: ' + str(raw['metric']['totalDebt/totalEquityAnnual'])

                        ps = 'P/S: ' + str(raw['metric']['psAnnual'])

                        div = 'DIV: ' + str(raw['metric']['dividendYieldIndicatedAnnual']) + '%'

                        pfcf = 'PFCF: '+ str(raw['metric']['pfcfShareAnnual'])

                        mc = 'MC: ' + str(raw['metric']['marketCapitalization'])



                        all = item_token[0] + '\n' +price +'\n'+ pe + '\n' + roe + '\n' +roa + '\n' +cr + '\n' + bvps + '\n' + gm + '\n' +de + '\n' + ps + '\n' + div + '\n' + pfcf + '\n' + mc

                        print('\n' + time_ + "\n " + from_list[counter]+'\n'+ all)

                        sendserver.sendmail('textaword@gmail.com', from_list[counter] , all)
                        time.sleep(10)
                        counter += 1

                        # Price per earnings ratio
                    elif item_token[1] == "PE":

                            price = str(finnhub_client.quote(item_token[0])['c'])

                            raw = finnhub_client.company_basic_financials(item_token[0],"all")

                            pe = str(raw['metric']['peBasicExclExtraTTM'])

                            last = item_token[0] +"\n"+'Price: '+ price +'\n'+'P/E: ' + pe

                            time_ = time.asctime()

                            print('\n'+ time_ + '\n' + from_list[counter] + last)

                            sendserver.sendmail('textaword@gmail.com', from_list[counter] , last)

                            time.sleep(10)
                            counter += 1

                        # Return on equity
                    elif item_token[1] == "ROE":

                        price = str(finnhub_client.quote(item_token[0])['c'])

                        raw = finnhub_client.company_basic_financials(item_token[0],"all")

                        roe = str(raw['metric']['roeRfy'])

                        last = item_token[0] +"\n"+'Price: '+ price +'\n'+'ROE: ' + roe

                        print('\n'+ time_ + '\n' + from_list[counter] +'\n'+ last)

                        sendserver.sendmail('textaword@gmail.com', from_list[counter] , last)

                        time.sleep(10)
                        counter += 1

                        # Return on assets
                    elif item_token[1] == "ROA":

                        price = str(finnhub_client.quote(item_token[0])['c'])

                        raw = finnhub_client.company_basic_financials(item_token[0],"all")

                        roa = str(raw['metric']['roaRfy'])

                        last = item_token[0] +"\n"+'Price: '+ price +'\n'+'ROA: ' + roa

                        print('\n'+ time_ + '\n' + from_list[counter] +'\n'+ last)

                        sendserver.sendmail('textaword@gmail.com', from_list[counter] , last)

                        time.sleep(10)
                        counter += 1

                        # Current Ratio
                    elif item_token[1] == "CR":

                        price = str(finnhub_client.quote(item_token[0])['c'])

                        raw = finnhub_client.company_basic_financials(item_token[0],"all")

                        cr = str(raw['metric']['currentRatioAnnual'])

                        last = item_token[0] +"\n"+'Price: '+ price +'\n'+'CR: ' + cr

                        print('\n'+ time_ + '\n' + from_list[counter] +'\n'+ last)

                        sendserver.sendmail('textaword@gmail.com', from_list[counter] , last)

                        time.sleep(10)
                        counter += 1
                        
                        # Book Value Per Share
                    elif item_token[1] == "BVPS":

                        price = str(finnhub_client.quote(item_token[0])['c'])

                        raw = finnhub_client.company_basic_financials(item_token[0],"all")

                        bvps = str(raw['metric']['bookValuePerShareAnnual'])

                        last = item_token[0] +"\n"+'Price: '+ price +'\n'+'BV/PS: ' + bvps

                        print('\n'+ time_ + '\n' + from_list[counter] +'\n'+ last)

                        sendserver.sendmail('textaword@gmail.com', from_list[counter] , last)

                        time.sleep(10)
                        counter += 1
                        
                        # Gross margin
                    elif item_token[1] == "GM":

                        price = str(finnhub_client.quote(item_token[0])['c'])

                        raw = finnhub_client.company_basic_financials(item_token[0],"all")

                        gm = str(raw['metric']['grossMarginAnnual'])

                        last = item_token[0] +"\n"+'Price: '+ price +'\n'+'GM: ' + gm

                        print('\n'+ time_ + '\n' + from_list[counter] +'\n'+ last)

                        sendserver.sendmail('textaword@gmail.com', from_list[counter] , last)

                        time.sleep(10)
                        counter += 1

                        # price to sales
                    elif item_token[1] == "PS":

                        price = str(finnhub_client.quote(item_token[0])['c'])

                        raw = finnhub_client.company_basic_financials(item_token[0],"all")

                        ps = str(raw['metric']['psAnnual'])

                        last = item_token[0] +"\n"+'Price: '+ price +'\n'+'P/S: ' + ps

                        print('\n'+ time_ + '\n' + from_list[counter] +'\n'+ last)

                        sendserver.sendmail('textaword@gmail.com', from_list[counter] , last)

                        time.sleep(10)
                        counter += 1

                        #Debt to equity
                    elif item_token[1] == "DE":

                        price = str(finnhub_client.quote(item_token[0])['c'])

                        raw = finnhub_client.company_basic_financials(item_token[0],"all")

                        de = str(raw['metric']['totalDebt/totalEquityAnnual'])

                        last = item_token[0] +"\n"+'Price: '+ price +'\n'+'D/E: ' + de

                        print('\n'+ time_ + '\n' + from_list[counter] +'\n'+ last)

                        sendserver.sendmail('textaword@gmail.com', from_list[counter] , last)

                        time.sleep(10)
                        counter += 1

                    elif item_token[1] == "DIV":

                        price = str(finnhub_client.quote(item_token[0])['c'])

                        raw = finnhub_client.company_basic_financials(item_token[0],"all")

                        div = str(raw['metric']['dividendYieldIndicatedAnnual']) + '%'

                        last = item_token[0] +"\n"+'Price: '+ price +'\n'+'DIV: ' + div

                        print('\n'+ time_ + '\n' + from_list[counter] +'\n'+ last)

                        sendserver.sendmail('textaword@gmail.com', from_list[counter] , last)

                        time.sleep(10)
                        counter += 1

                    elif item_token[1] == "PFCF":

                        price = str(finnhub_client.quote(item_token[0])['c'])

                        raw = finnhub_client.company_basic_financials(item_token[0],"all")

                        pfcf = str(raw['metric']['pfcfShareAnnual'])

                        last = item_token[0] +"\n"+'Price: '+ price +'\n'+'PFCF: ' + pfcf

                        print('\n'+ time_ + '\n' + from_list[counter] +'\n'+ last)

                        sendserver.sendmail('textaword@gmail.com', from_list[counter] , last)  

                        time.sleep(10)
                        counter += 1

                    elif item_token[1] == "MC":

                        price = str(finnhub_client.quote(item_token[0])['c'])

                        raw = finnhub_client.company_basic_financials(item_token[0],"all")

                        pfcf = str(raw['metric']['marketCapitalization'])

                        last = item_token[0] +"\n"+'Price: '+ price +'\n'+'PFCF: ' + pfcf

                        print('\n'+ time_ + '\n' + from_list[counter] +'\n'+ last)

                        sendserver.sendmail('textaword@gmail.com', from_list[counter] , last)    
                        
                        time.sleep(10)
                        counter += 1

                    else:
                        
                        sendserver.sendmail('textaword@gmail.com', from_list[counter] , "Sorry Not a valid input.")
                        print('\n'+ time_ + '\n' + from_list[counter] +'\n'+ "Sorry not a valid input.")
                else:

                    sendserver.sendmail('textaword@gmail.com', from_list[counter] , "Sorry not a valid input!")
                    print('\n'+ time_ + '\n' + from_list[counter] +'\n'+ "Sorry not a valid input!")
        else:
            print('\n'+ 'stocks' +'\n'+ time_ +'\n'+ "Nothing to show")
    except:
        print("it passed")
        pass

schedule.every(20).seconds.do(code)

while 1:
    schedule.run_pending()
    time.sleep(1)