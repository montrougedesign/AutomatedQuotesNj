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
import datetime
from finvizfinance.quote import finvizfinance
#nltk.download('punkt')
#finnhub api key think
finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
#to find the right stl certificate for mongo db
ca = certifi.where()
#Mongo database API key think
client = pymongo.MongoClient("mongodb+srv://MYCoding:QV9BcLxtJqrInZB4@mycoding.pzucnk1.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)

def emailserver():       
    global user 
    #for testing purposes
    """user = 'paperstocksnj@gmail.com'
    password = 'oeurjrdemmeyrffb'"""
    
    
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
        #add the email sender to the from_list
        from_list.append(email_message['From'])
        #walk trought all the parts of the email
        for part in email_message.walk():
            # get content type of each part of the email
            content_type = part.get_content_type()
            #if the part is 'text/html' or 'text/html' exctract the email content
            if(content_type == 'text/html'):
                
                msg_ = part.get_payload()
                if content_type =='text/html':
                    soup = BeautifulSoup(msg_,'html.parser')
                    try:
                        #ATT
                        text = soup.td.get_text(strip=True).upper() 
                    except:
                        #Emails
                        text = soup.div.get_text(strip=True).upper()
                elif content_type == 'text/plain':
                    #VZ
                    text = msg_.strip().upper() 
                else:
                    print('not a content type')
        #Append the parsed message to the list    
        item_data_list.append(text)    

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
    rawData2 = finnhub_client.quote(UserInput[0]) 
    message = UserInput[0]+"\n"
    # list of all the options
    DataPoints = ["ROE","ROA","CR","BVPS","GM","PS","DE","DIV","PFCF","MC","HIGH","LOW"]
    #list of this coresponding to what is in the othe list to put in the api 
    arrayPrint = [
        #"peBasicExclExtraTTM",
        #"peNormalizedAnnual",
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
    if (UserInput[1] == "ALL"):
        all = f"Price| {str(rawData2['c'])}\n"
        for index, each in enumerate(arrayPrint) :   
            try:
                all +=  str(DataPoints[index])+ ': ' +str(rawData['metric'][each])+"\n"
            except:
                continue
        all += f"Day High:  {str(rawData2['h'])} \n"
        all += f"Day Low: {str(rawData2['l'])}\n"
        sendserver.sendmail(user,sendNum,f"{UserInput[0]}\n{all}\n")
        print(user)
        print (sendNum)
        print (all)
    elif UserInput[1] == "DLOW":
        
        message += "Price "  + str(rawData2['c'])+"\n"
        message += "Day Low "  + str(rawData2['l'])+"\n"
        sendserver.sendmail(user,sendNum,message)  
        print(f"{user}\n{sendNum}\n{message}\n") 
    elif UserInput[1] == "DHIGH":
        message += "Price " + str(rawData2['c'])+"\n"
        message += "Day High " +str(rawData2['h'])+"\n"    
        sendserver.sendmail(user,sendNum,message) 
        print(f"{user}\n{sendNum}\n{message}\n") 
    elif UserInput[1] == "NEWS":
        today = datetime.date.today()
        rawNews = finnhub_client.company_news(UserInput[0], _from=today, to=today)
        if len(rawNews) > 0:        
            for i in rawNews:
                message += str(i["headline"])+"\n"  
                message += "-"+"\n"
            sendserver.sendmail(user,sendNum,message) 
            print(f"{user}\n{sendNum}\n{message}\n")    
        else:
            message += "No News"
            sendserver.sendmail(user,sendNum,message)
            print(f"{user}\n{sendNum}\n{message}\n")

    else:    
        for index, ticker in enumerate(DataPoints):
            if UserInput[1] == ticker:   
                price = 'Price: ' + str(rawData2['c'])
                metric = ticker + ': '  + str(rawData['metric'][arrayPrint[index]])
                sendserver.sendmail(user,sendNum,f"{UserInput[0]}\n{price}\n{metric}")
                print(user)
                print(sendNum)
                print(UserInput[0])
                print (price)
                print (metric)
        
def plainData(UserInput,sendNum):
    ListOfTickers = [
                #1
                ['T','VZ','KBWD'],
                #2
                ['ADBE','ALGN','ISRG'],
                #3
                ['NKE','LULU','ETSY'],
                #4
                ['V','AXP','PYPL'],
                #5
                ['MMP','EPD','WPC'],
                #6
                ['TROW','IVZ','SCHW'],
                #7
                ['HRB','WBA','FDX'],
                #8
                ['CRM','SQ','JPM'],
                #9
                ['AMT','SBUX','DVA'],
                #10
                ['QQQ','VTI','SPY'],
                #11
                ['LUV','ALK','DAL'],
                #12
                ['IPAY','QQQJ','JETS'],
                #13
                ['XLK','XLF','VTV'],
                #14
                ['GEN','BIG','OLED'],
                #15
                ['PM','MO','HDV'],
                #16
                ['META','PINS','NFLX'],
                #17
                ['WFC','C','MA'],
                #18
                ['AAPL','GOOGL','AMZN'],
                #19
                ['GM','F','TSLA'],
                #20
                ['KBWB','BAC','C'],
                #21
                ['MU','AMD','NVDA'],
                #22
                ['PANW','CRWD','ZS'],
                #23
                ['SHOP','ABNB','SNOW'],
                #24
                ['XHB','DHI','LEN'],
                #25
                ['WMT','TGT','COST'],
                #26
                ['XLRE','SPG','SLG'],
                #27
                ['BRK.B','RH','ULTA'],
                #28
                ['JWN','TJX','M'],
                #29
                ['XLF','NYCB','BK'],
                #30
                ['BLK','BX','JEF'],
                #31
                ['SCHG','XLY','IDRV'],
                #32
                ['HAS','HBI','MAT'],
                #33
                ['MAR','H','WYNN'],
                #34
                ['LOW','HD','SHW'],
                #35
                ['MRK','AMGN','ABT'],
                #36
                ['SBRA','GMRE','RITM'],
                #37
                ['ABR','DOUG','MORT'],
                #38
                ['CVX','OXY','DVN'],
                #39
                ['NEE','TAN','SEDG'],          
                #40
                ['NU','ALLY','COF'],  
                #41
                ['SCHD','XLP','VTV'],                    
                ]
    WLNames =['WL1','WL2','WL3','WL4','WL5','WL6','WL7','WL8','WL9','WL10','WL11','WL12','W13','WL14','WL15','WL16','WL17','WL18','WL19','WL20','WL21','WL22','WL23','WL24','WL25','WL26','WL27','WL28','WL29','WL30','WL31','WL32','WL33','WL34','WL35','WL36','WL37','WL38','WL39','WL40','WL41']     

    
        
    for index, WLName in enumerate(WLNames):    
        if(UserInput[0] == WLName):
            resultArray = []
            for ticker in ListOfTickers[index]:
                #TickersDB(ticker)
                rawData = finnhub_client.quote(ticker)
                price = 'Price: ' + str(rawData['c'])
                percent_change = 'Percent Change: ' +  str(rawData['dp'])+'%'
                change = 'Change: ' + '$' + str(rawData['d'])
                resultArray.append(ticker + '\n' + price + '\n' + change + '\n' + percent_change + '\n')
            result = "".join(map(str,resultArray))
            sendserver.sendmail(user,sendNum,result)
            print(user + '\n'+ sendNum + '\n' + result)
    if UserInput[0] not in WLNames:
        #TickersDB(UserInput[0])
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
        
def notGoodInput(user,sendNum):
    message = "Not a valid Input!"
    sendserver.sendmail(user,sendNum,message)
    print(user + '\n' +sendNum + '\n' + message)

"""def emailDB(fromlist):
    db = client["AMQ"]
    collection = db["Emails"]
    
    for email in from_list:
        emailcounter = 0
        results = collection.find({"email":email})
        for result in results:
            
            emailcounter = emailcounter + 1
        if emailcounter == 0:
            id_cursor = collection.find().sort('_id',-1).limit(1)
            id = id_cursor[0]['_id']+1
            post = {"_id": id,"email": email, "Times": 1}  
            collection.insert_one(post)  
        else:
            collection.update_one({"email":email}, {'$inc':{"Times": 1}})        
def sendEmails():
    db = client["AMQ"]
    collection = db["Emails"]
    
    emails = collection.find({"email":{'$exists': True}})
    for email in emails:
        print(email['email'])

def TickersDB(ticker):
    #ticker = ticker.upper()
    db = client["AMQ"]
    collection = db["Tickers"]
    results = collection.find({"Tick":ticker})
    resultCounter = 0
    for result in results:
        resultCounter += 1
    if resultCounter == 0:
        id_cursor = collection.find().sort('_id',-1).limit(1)
        id = id_cursor[0]['_id'] + 1
        collection.insert_one({"_id": id,"Tick": ticker,"Times":1}) 
    else:
        #stuff = collection.find()
        collection.update_one({"Tick":ticker}, {'$inc':{"Times": 1}})
        #collection.update_one"""

def Main():
    try:
        time_ = time.asctime()
        emailserver()
        
        if list_length>0:
            get_text()
            #emailDB(from_list)
            for index, each in enumerate (item_data_list):
                if len(token(each)) == 2:
                    extraData(token(each),from_list[index])
                elif len(token(each)) == 1:
                    plainData(token(each),from_list[index])
                else:
                    notGoodInput()    
        else:
            print('\n'+ 'stocks' +'\n'+ time_ +'\n'+ "Nothing to show")            
    except Exception as e:
        print(e)
        pass    



schedule.every(10).seconds.do(Main)

while 1:
    schedule.run_pending()
    time.sleep(1)      
        