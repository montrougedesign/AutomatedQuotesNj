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
            soup = BeautifulSoup(msg_,'html.parser')
            text = soup.td.get_text(strip=True).upper()
            item_data_list.append(text)
        elif content_type == 'text/plain':
            text = msg_.strip().upper()
            
            item_data_list.append(text)
        else:
            print('not a content type')
        
        from_list.append(email_message['From'])    
#item_data_list = []

#from_list = []


finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")


def token(Input):
    #makes any string to array
    Input = nltk.word_tokenize(Input)
    #converts that array to upper case
    new =[x.upper() for x in Input]   
    #returns the upper case Array
    return new



#UserInput should be a array of strings, and the sendName should be a string
def extraData(UserInput,sendNum):
    #get the Raw data so we dont have to call the api more then once
    rawData = finnhub_client.company_basic_financials(UserInput[0],"all")
    # list of all the options
    tickers = ["PE","ROE","ROA","CR","BVPS","GM","PS","DE","DIV","PFCF","MC","HIGH","LOW"]
    #list of this coresponding to what is in the othe list to put in the api 
    arrayPrint = [
        "peBasicExclExtraTTM",
        "roeRfy",
        "roaRfy",
        "currentRatioAnnual",
        "bookValuePerShareAnnual",
        "grossMarginAnnual",
        "totalDebt/totalEquityAnnual",
        "psAnnual",
        "dividendYieldIndicatedAnnual",
        "pfcfShareAnnual",
        "marketCapitalization",
        "52WeekHigh",
        "52WeekLow"]
    #printNameTag =['P/E| ','ROE| ','ROA| ','CR, ','BVPS, ','GM, ','D/E, ','P/S, ','DIV,','PFCF, ','MC, ','52 Week High, ','52 Week Low, ']
    
    
    if (UserInput[1] == "ALL"):
        price = 'Price| ' + str(finnhub_client.quote(UserInput[0])['c'])
        
        all = ""
        for index, each in enumerate(arrayPrint) :   
            all +=  str(tickers[index])+ ': ' +str(rawData['metric'][each])+"\n"
            
        all = str(all)
        sendserver.sendmail(user,sendNum,f"{UserInput[0]}\n{price}\n{all}")
        print(user)
        print (sendNum)
        print (all)
    else:
        for index, ticker in enumerate(tickers) :
            
            if UserInput[1] == ticker:   
                
                price = 'Price: ' + str(finnhub_client.quote(UserInput[0])['c'])
                metric = ticker + ': '  + str(rawData['metric'][arrayPrint[index]])
                sendserver.sendmail(user,sendNum,f"{UserInput[0]}\n{price}\n{metric}")
                print(user)
                print(sendNum)
                print(UserInput[0])
                print (price)
                print (metric)
        
def plainData(UserInput,sendNum):
    ListOfTickers = [['T','VZ','KBWD'],
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
                ['AAPL','GOOGL','AMZN'],
                ['GM','F','TSLA'],
                ['KBWB','BAC','C'],
                ['MU','AMD','NVDA'],
                ['PAW','CRWD','ZS'],
                ['SHOP','ABNB','SNOW']]
    WLNames =['WL1','WL2','WL3','WL4','WL5','WL6','WL7','WL8','WL9','WL10','WL11','WL12','W13','WL14','WL15','WL16','WL17','WL18','WL19','WL20','WL21','WL22','WL23' ] 
    

    
        
    for index, WLName in enumerate(WLNames):    
        if(UserInput[0] == WLName):
            resultArray = []
            for ticker in ListOfTickers[index]:
                rawData = finnhub_client.quote(ticker)
                price = 'Price: ' + str(rawData['c'])
                percent_change = 'Percent Change: ' +  str(rawData['dp'])+'%'
                change = 'Change: ' + '$' + str(rawData['d'])
                resultArray.append(ticker + '\n' + price + '\n' + change + '\n' + percent_change + '\n')
            result = "".join(map(str,resultArray))
            sendserver.sendmail(user,sendNum,result)
            print(user + '\n'+ sendNum + '\n' + result)
    if UserInput[0] not in WLNames:
        rawData = finnhub_client.quote(UserInput[0])
        try:  
            UserInput[0] = finnhub_client.company_profile2(symbol=UserInput[0])["name"]
        except:
            pass
        price = 'Price: $' + str(rawData['c'])
        change = 'Change: $' + str(rawData['d'])
        percent_change = 'Percent Change: ' + str(rawData['dp'])+'%'
        Previous_close = 'Previous Close: $' + str(rawData['pc'])
        result = UserInput[0] + '\n' + price + '\n' + change + '\n' + percent_change + '\n'+Previous_close
        sendserver.sendmail(user,sendNum,result)
        print(user + '\n' + sendNum + '\n' + result)
        
        #sendserver.sendmail(user,sendNum,f"{UserInput[0]}\n{price}\n{metric}")
def notGoodInput(user,sendNum):
    message = "Not a valid Input!"
    sendserver.sendmail(user,sendNum,message)
    print(user + '\n' +sendNum + '\n' + message)



def Main():

    
    time_ = time.asctime()
    emailserver()
    try:
        

        if list_length>0:
            get_text()
            for index, each in enumerate (item_data_list):
                if len(token(each)) == 2:
                    extraData(token(each),from_list[index])
                elif len(token(each)) == 1:
                    plainData(token(each),from_list[index])
                else:
                    notGoodInput()    
        else:
            print('\n'+ 'stocks' +'\n'+ time_ +'\n'+ "Nothing to show")            
    except:
        print("It Passed")
        pass    



schedule.every(20).seconds.do(Main)

while 1:
    schedule.run_pending()
    time.sleep(1)        
        
        