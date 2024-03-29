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

#nltk.download('punkt')

def test():
    #------ email ------
    try:
        #email login 
        user = 'txtaquote@gmail.com'
        password = 'yumdkitwnqhmixzf'
        receiveserver ='imap.gmail.com'
        sendserver = smtplib.SMTP('smtp.gmail.com', 587)
        sendserver.starttls()
        mail = imaplib.IMAP4_SSL(receiveserver)
        mail.login(user, password)
        sendserver.login(user, password)


        #select inbox
        mail.select('Inbox')
        #get the inbox
        result, data = mail.uid('search',None, 'ALL')
        #Make a list of the new items(list of emails in the Inbox)
        new_items = data[0].split()
        #get the length of the new item list (how many emails in the Inbox)
        list_length = len(new_items)



        time_ = time.asctime()


        #------ finnhub -----

        finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")

        #---------------------

        if list_length >= 1:

            #get the email
            result2, email_data = mail.uid('fetch', new_items[-1] , '(RFC822)')
            #decode the email 
            raw_email = email_data[0][1].decode("utf-8")
            #not sure what this does will write it when i figure it out
            email_message = email.message_from_string(raw_email)
            #gets the email sender
            from_ = email_message['From']

            status, delete_data = mail.search(None, 'All')

            new_item_delete = delete_data[0].split()

            for part in email_message.walk():
                content_type = part.get_content_type()
                msg_ = part.get_payload()

                continue

            if content_type =='text/html':
                soup = BeautifulSoup(msg_,'html.parser')
                text = soup.td.get_text(strip=True).upper()
            elif content_type == 'text/plain':
                text = msg_.strip().upper()
            else:
                print('not a content type')  
            

            # text in a list
            text_list = nltk.word_tokenize(text)

            text_list_length = len(text_list)

            if text_list_length == 1:
                if text_list[0] == "WL1":
                    wl1 = ['T','VZ','KBWD']
                    wl1_result =[]

                    for x in wl1: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl1_result.append(end)

                    wl1_result_str ="".join(map(str,wl1_result))
                    print("\n"+time_ + '\n' +from_)
                    print(wl1_result_str)
                    
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl1_result_str)
                    ##tweetapi.update_status(time_ + wl1_result_str + "\n" + "#stockquotes" )

                    
                    
                elif text_list[0] == "WL2":
                    wl2 = ['ADBE','ALGN','ISRG']
                    wl2_result =[]

                    for x in wl2: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl2_result.append(end)

                    wl2_result_str ="".join(map(str,wl2_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl2_result_str)
                    ##tweetapi.update_status(time_ + wl2_result_str + "\n" + "#stockquotes" )

                    print(wl2_result_str)

                elif text_list[0] == "WL3":
                    wl3 = ['NKE','LULU','ETSY']
                    wl3_result =[]

                    for x in wl3: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl3_result.append(end)

                    wl3_result_str ="".join(map(str,wl3_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl3_result_str)
                    ##tweetapi.update_status(time_ + wl3_result_str + "\n" + "#stockquotes" )

                    print(wl3_result_str)

                elif text_list[0] == "WL4":
                    wl4 = ['V','AXP','PYPL']
                    wl4_result =[]

                    for x in wl4: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl4_result.append(end)

                    wl4_result_str ="".join(map(str,wl4_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl4_result_str)
                    ##tweetapi.update_status(time_ + wl4_result_str + "\n" + "#stockquotes" )

                    print(wl4_result_str)

                elif text_list[0] == "WL5":
                    wl5 = ['MMP','EPD','WPC']
                    wl5_result =[]

                    for x in wl5: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl5_result.append(end)

                    wl5_result_str ="".join(map(str,wl5_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl5_result_str)
                    ##tweetapi.update_status(time_ + wl5_result_str + "\n" + "#stockquotes" )

                    print(wl5_result_str)

                elif text_list[0] == "WL6":
                    wl6 = ['TROW','IVZ','SCHW']
                    wl6_result =[]

                    for x in wl6: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl6_result.append(end)

                    wl6_result_str ="".join(map(str,wl6_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl6_result_str)
                    ##tweetapi.update_status(time_ + wl6_result_str + "\n" + "#stockquotes" )

                    print(wl6_result_str)

                elif text_list[0] == "WL7":
                    wl7 = ['HRB','WBA','FDX']
                    wl7_result =[]

                    for x in wl7: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl7_result.append(end)

                    wl7_result_str ="".join(map(str,wl7_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl7_result_str)
                    ##tweetapi.update_status(time_ + wl7_result_str + "\n" + "#stockquotes" )

                    print(wl7_result_str)

                elif text_list[0] == "WL8":
                    wl8 = ['CRM','SQ','JPM']
                    wl8_result =[]

                    for x in wl8: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl8_result.append(end)

                    wl8_result_str ="".join(map(str,wl8_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl8_result_str)
                    #tweetapi.update_status(time_ + wl8_result_str + "\n" + "#stockquotes" )

                    print(wl8_result_str)

                elif text_list[0] == "WL9":
                    wl9 = ['AMT','SBUX','DVA']
                    wl9_result =[]

                    for x in wl9: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl9_result.append(end)

                    wl9_result_str ="".join(map(str,wl9_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl9_result_str)
                    #tweetapi.update_status(time_ + wl9_result_str + "\n" + "#stockquotes" )

                    print(wl9_result_str)

                elif text_list[0] == "WL10":
                        from_ = email_message['from']
                        finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
                        wl10 = ['QQQ','VTI','SPY']
                        wl10_result =[]

                        for x in wl10:
                
                            price = str(finnhub_client.quote(x)['c'])
                            percent_change = str(finnhub_client.quote(x)['dp'])

                            change = str(finnhub_client.quote(x)['d']) 


                            end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                            wl10_result.append(end)

                        wl10_result_str ="".join(map(str,wl10_result))
                        print("\n"+time_ + '\n' +from_)
                        sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl10_result_str)
                        #tweetapi.update_status(time_ + wl10_result_str + "\n" + "#stockquotes" )

                        print(wl10_result_str)

                elif text_list[0] == "WL11":
                    wl11 = ['LUV','ALK','DAL']
                    wl11_result =[]

                    for x in wl11: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl11_result.append(end)

                    wl11_result_str ="".join(map(str,wl11_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl11_result_str)
                    #tweetapi.update_status(time_ + wl11_result_str + "\n" + "#stockquotes" )

                    print(wl11_result_str)

                elif text_list[0] == "WL12":
                    wl12 = ['IPAY','QQQJ','JETS']
                    wl12_result =[]

                    for x in wl12: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl12_result.append(end)

                    wl12_result_str ="".join(map(str,wl12_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl12_result_str)
                    #tweetapi.update_status(time_ + wl12_result_str + "\n" + "#stockquotes" )

                    print(wl12_result_str)  

                elif text_list[0] == "WL13":
                    wl13 = ['XLK','XLF','VTV']
                    wl13_result =[]

                    for x in wl13: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl13_result.append(end)

                    wl13_result_str ="".join(map(str,wl13_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl13_result_str)
                    #tweetapi.update_status(time_ + wl13_result_str + "\n" + "#stockquotes" )

                    print(wl13_result_str)

                elif text_list[0] == "WL14":
                    wl14 = ['NLOK','BIG','OLED']
                    wl14_result =[]

                    for x in wl14: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl14_result.append(end)

                    wl14_result_str ="".join(map(str,wl14_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl14_result_str)
                    #tweetapi.update_status(time_ + wl14_result_str + "\n" + "#stockquotes" )

                    print(wl14_result_str) 

                elif text_list[0] == "WL15":
                    wl15 = ['PM','MO','STOR']
                    wl15_result =[]

                    for x in wl15: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl15_result.append(end)

                    wl15_result_str ="".join(map(str,wl15_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl15_result_str)
                    #tweetapi.update_status(time_ + wl15_result_str + "\n" + "#stockquotes" )

                    print(wl15_result_str)

                elif text_list[0] == "WL16":
                    wl16 = ['FB','PINS','NFLX']
                    wl16_result =[]

                    for x in wl16: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl16_result.append(end)

                    wl16_result_str ="".join(map(str,wl16_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl16_result_str)
                    #tweetapi.update_status(time_ + wl16_result_str + "\n" + "#stockquotes" )

                    print(wl16_result_str)

                elif text_list[0] == "WL17":
                    wl17 = ['WFC','C','MA']
                    wl17_result =[]

                    for x in wl17: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl17_result.append(end)

                    wl17_result_str ="".join(map(str,wl17_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl17_result_str)
                    #tweetapi.update_status(time_ + wl17_result_str + "\n" + "#stockquotes" )

                    print(wl17_result_str)

                elif text_list[0] == "WL18":
                    wl18 = ['AAPL','GOOGL','AMZN']
                    wl18_result =[]

                    for x in wl18: 
                        price = str(finnhub_client.quote(x)['c'])
                        percent_change = str(finnhub_client.quote(x)['dp'])
                        change = str(finnhub_client.quote(x)['d']) 


                        end = "\n" + x + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%"
                        wl18_result.append(end)

                    wl18_result_str ="".join(map(str,wl18_result))
                    print("\n"+time_ + '\n' +from_)
                    sendserver.sendmail('automatedquotesnj@gmail.com', from_ , wl18_result_str)
                    #tweetapi.update_status(time_ + wl18_result_str + "\n" + "#stockquotes" )


                    print(wl18_result_str)             
                else:
                    price = str(finnhub_client.quote(text)['c'])
                    percent_change = str(finnhub_client.quote(text)['dp'])
                    Previous_close = str(finnhub_client.quote(text)['pc'])
                    change = str(finnhub_client.quote(text)['d'])
                    
                    end = "\n" + text + "\n" + "Price  " + "$" + price + "\n" + "Change  " + "$" +change + "\n" + "Percent Change  " + percent_change + "%" "\n" + "Previous Close  " + "$"+ Previous_close


                    print("\n" + time.asctime() + '\n' + from_ + end)
                    sendserver.sendmail('txtaquote@gmail.com', from_ ,end)
            elif text_list_length == 2:
                if text_list[1] == "ALL":

                    raw = finnhub_client.company_basic_financials(text_list[0],"all")

                    price = 'Price: ' + '$'+str(finnhub_client.quote(text_list[0])['c'])

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



                    all = text_list[0] + '\n' +price +'\n'+ pe + '\n' + roe + '\n' +roa + '\n' +cr + '\n' + bvps + '\n' + gm + '\n' +de + '\n' + ps + '\n' + div + '\n' + pfcf + '\n' + mc

                    print('\n' + time_ + "\n " + from_ +'\n'+ all)

                    sendserver.sendmail('txtaquote@gmail.com', from_ , all)

                    # Price per earnings ratio
                elif text_list[1] == "PE":

                    price = str(finnhub_client.quote(text_list[0])['c'])

                    raw = finnhub_client.company_basic_financials(text_list[0],"all")

                    pe = str(raw['metric']['peBasicExclExtraTTM'])

                    last = text_list[0] +"\n"+'Price: '+ price +'\n'+'P/E: ' + pe

                    time_ = time.asctime()

                    print('\n'+ time_ + '\n' + from_ + last)

                    sendserver.sendmail('txtaquote@gmail.com', from_ , last)
                    
                    # Return on equity
                elif text_list[1] == "ROE":

                    price = str(finnhub_client.quote(text_list[0])['c'])

                    raw = finnhub_client.company_basic_financials(text_list[0],"all")

                    roe = str(raw['metric']['roeRfy'])

                    last = text_list[0] +"\n"+'Price: '+ price +'\n'+'ROE: ' + roe

                    print('\n'+ time_ + '\n' + from_ +'\n'+ last)

                    sendserver.sendmail('txtaquote@gmail.com', from_ , last)

                    # Return on assets
                elif text_list[1] == "ROA":

                    price = str(finnhub_client.quote(text_list[0])['c'])

                    raw = finnhub_client.company_basic_financials(text_list[0],"all")

                    roa = str(raw['metric']['roaRfy'])

                    last = text_list[0] +"\n"+'Price: '+ price +'\n'+'ROA: ' + roa

                    print('\n'+ time_ + '\n' + from_ +'\n'+ last)

                    sendserver.sendmail('txtaquote@gmail.com', from_ , last)

                    # Current Ratio
                elif text_list[1] == "CR":

                    price = str(finnhub_client.quote(text_list[0])['c'])

                    raw = finnhub_client.company_basic_financials(text_list[0],"all")

                    cr = str(raw['metric']['currentRatioAnnual'])

                    last = text_list[0] +"\n"+'Price: '+ price +'\n'+'CR: ' + cr

                    print('\n'+ time_ + '\n' + from_ +'\n'+ last)

                    sendserver.sendmail('txtaquote@gmail.com', from_ , last)

                    # Book Value Per Share
                elif text_list[1] == "BVPS":

                    price = str(finnhub_client.quote(text_list[0])['c'])

                    raw = finnhub_client.company_basic_financials(text_list[0],"all")

                    bvps = str(raw['metric']['bookValuePerShareAnnual'])

                    last = text_list[0] +"\n"+'Price: '+ price +'\n'+'BV/PS: ' + bvps

                    print('\n'+ time_ + '\n' + from_ +'\n'+ last)

                    sendserver.sendmail('txtaquote@gmail.com', from_ , last)

                    # Gross margin
                elif text_list[1] == "GM":

                    price = str(finnhub_client.quote(text_list[0])['c'])

                    raw = finnhub_client.company_basic_financials(text_list[0],"all")

                    gm = str(raw['metric']['grossMarginAnnual'])

                    last = text_list[0] +"\n"+'Price: '+ price +'\n'+'GM: ' + gm

                    print('\n'+ time_ + '\n' + from_ +'\n'+ last)

                    sendserver.sendmail('txtaquote@gmail.com', from_ , last)

                    # price to sales
                elif text_list[1] == "PS":

                    price = str(finnhub_client.quote(text_list[0])['c'])

                    raw = finnhub_client.company_basic_financials(text_list[0],"all")

                    ps = str(raw['metric']['psAnnual'])

                    last = text_list[0] +"\n"+'Price: '+ price +'\n'+'P/S: ' + ps

                    print('\n'+ time_ + '\n' + from_ +'\n'+ last)

                    sendserver.sendmail('txtaquote@gmail.com', from_ , last)

                elif text_list[1] == "DE":

                    price = str(finnhub_client.quote(text_list[0])['c'])

                    raw = finnhub_client.company_basic_financials(text_list[0],"all")

                    de = str(raw['metric']['totalDebt/totalEquityAnnual'])

                    last = text_list[0] +"\n"+'Price: '+ price +'\n'+'D/E: ' + de

                    print('\n'+ time_ + '\n' + from_ +'\n'+ last)

                    sendserver.sendmail('txtaquote@gmail.com', from_ , last)

                elif text_list[1] == "DIV":

                    price = str(finnhub_client.quote(text_list[0])['c'])

                    raw = finnhub_client.company_basic_financials(text_list[0],"all")

                    div = str(raw['metric']['dividendYieldIndicatedAnnual']) + '%'

                    last = text_list[0] +"\n"+'Price: '+ price +'\n'+'DIV: ' + div

                    print('\n'+ time_ + '\n' + from_ +'\n'+ last)

                    sendserver.sendmail('txtaquote@gmail.com', from_ , last)

                elif text_list[1] == "PFCF":

                    price = str(finnhub_client.quote(text_list[0])['c'])

                    raw = finnhub_client.company_basic_financials(text_list[0],"all")

                    pfcf = str(raw['metric']['pfcfShareAnnual'])

                    last = text_list[0] +"\n"+'Price: '+ price +'\n'+'PFCF: ' + pfcf

                    print('\n'+ time_ + '\n' + from_ +'\n'+ last)

                    sendserver.sendmail('txtaquote@gmail.com', from_ , last)  
                elif text_list[1] == "MC":

                    price = str(finnhub_client.quote(text_list[0])['c'])

                    raw = finnhub_client.company_basic_financials(text_list[0],"all")

                    pfcf = str(raw['metric']['marketCapitalization'])

                    last = text_list[0] +"\n"+'Price: '+ price +'\n'+'PFCF: ' + pfcf

                    print('\n'+ time_ + '\n' + from_ +'\n'+ last)

                    sendserver.sendmail('txtaquote@gmail.com', from_ , last)      

                else:
                    
                    sendserver.sendmail('txtaquote@gmail.com', from_ , "Sorry we don't have that.")
                    print('\n'+ time_ + '\n' + from_ +'\n'+ "Sorry we don't have that.")

            for num in new_item_delete:
                    mail.store(num,'+FLAGS','\\Deleted')         
        else:
            print('\n'+ 'stocks'+ '\n' + time_ + '\n' + "Nothing to show")
    except:
        print("it passed")
        pass

schedule.every(20).seconds.do(test)

while 1:
    schedule.run_pending()
    time.sleep(1)

