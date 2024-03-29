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
import requests

class Emails():  
    def __init__(self , username , password):
        serverStart = 'imap.gmail.com'
        self.sendserver = smtplib.SMTP('smtp.gmail.com', 587)
        self.sendserver.starttls()
        self.mail = imaplib.IMAP4_SSL(serverStart)
        self.username = username
        self.password = password
        self.mail.login(self.username, self.password)
        self.sendserver.login(self.username, self.password)
    def GetMail(self):
        self.mail.select('Inbox')
        result, data = self.mail.uid('search',None, 'UnSeen')
        new_items = data[0].split()
        return new_items
    def GetLength(self):
        return len(self.GetMail())
    def Token(self, Input):
        #makes any string to array
        Input = nltk.word_tokenize(Input)
        #converts that array to upper case
        new =[x.upper() for x in Input]   
        #returns the upper case Array
        return new
    def GetDataAndFroms(self):
        froms =[]
        data = []
        if int(self.GetLength()) > 0:
            for x in self.GetMail():
                result2, email_data = self.mail.uid('fetch', x , '(RFC822)')
                raw_email = email_data[0][1].decode("utf-8")
                email_message = email.message_from_string(raw_email)
                froms.append(email_message['From'])
                #text =''
                for part in email_message.walk():
                    # get content type of each part of the email
                    content_type = part.get_content_type()
                    #if the part is 'text/html' or 'text/html' exctract the email content
                    #if(content_type == 'text/html'): 
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
                data.append(self.Token(text))  
            return froms, data
        else:
            print(f"\nstocks\n{time.asctime()}\nNo mail")  
            return froms, data    
class Stocks():
    finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
    # this function get the price of the stock from finnhub and the company name from finviz    
    def GetPrice(self,tick):
        rawData  = self.finnhub_client.quote(tick)
        fdata = requests.get(f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={tick}&apikey=NBNC70MNF0ALLX8A").json()
        
        result =f"{tick}\n"  
        result +=f"Price: {rawData['c']}\n"  
        result += f"Change: ${rawData['d']}\n"
        result += f"Percent Change: {rawData['dp']}%\n"
        result += f"Previous Close: ${rawData['pc']}\n"
        return result
    # this function get the all the data the we previde from finviz
    def GetAll(self,tick):
        tick = tick.upper()
        result = self.DayHighLow(tick)
        fdata = requests.get(f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={tick}&apikey=NBNC70MNF0ALLX8A").json()
        """"
        file = open("/root/Program/Data/data.txt", "r").read().split(",")
        headers = open("/root/Program/Data/dataHeaders.txt", "r").read().split(",")"""
        c = DB().GetAllFundemetals()
        for d in c:
            result += f"{d['Function']}:{fdata[d['API_Field']]}\n"
        return result
    #this function gets one data point that the user is askes for
    def GetOne(self,tick,headType):
        tick = tick.upper()
        result = self.GetPrice(tick)
        fdata = finvizfinance(tick).ticker_fundament()
        file = open("/root/Program/Data/data.txt", "r").read().split(",")
        headers = open("/root/Program/Data/dataHeaders.txt", "r").read().split(",")
        for index, head in enumerate(headers) :
            head = head.strip('\"')
            if(head == headType.upper()):
                dataType = file[index]
                result += f"{head}: {fdata[dataType]}\n"  
                break
        return result
    def WatchLists(self,wl,from_):
        wl = wl.upper()
        wl = int(wl.strip('WL'))
        ticks = DB().getWLByUser(from_,wl-1)
        result =''
        for i in ticks:
            DB().NewUse(from_,i)
            result += self.GetPrice(i)
        return result
    def DayHighLow(self,tick):
        raw = self.finnhub_client.quote(tick)
        result = self.GetPrice(tick)
        result += f"Day Low {raw['l']}\n"
        result += f"Day High {raw['h']}\n"
        return result
    def News(self,tick):
        today = datetime.date.today()
        rawNews = self.finnhub_client.company_news(tick, _from=today, to=today)
        result = self.GetPrice(tick)
        if len(rawNews) > 0:
            if len(rawNews) >5:       
                for i in range(0,5):
                    result += str(rawNews[i]["headline"])+"\n"  
                    result += "-"+"\n"
            else:
                for i in rawNews:
                    result += str(i["headline"])+"\n"  
                    result += "-"+"\n"        
        else: 
            result +='No News'       
        return result 
    def GetTickerFromName(self,name):
        ticks = f'-\n'
        uri = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={name}&apikey=NBNC70MNF0ALLX8A"
        rawTicks = requests.get(uri).json()["bestMatches"]
        for i, d in enumerate(rawTicks):
            if len(rawTicks[i]['1. symbol'])>4 and rawTicks[i]['1. symbol'][-4] == '.':
                continue
            if float(rawTicks[i]['9. matchScore']) >.3 and rawTicks[i]['8. currency'] == 'USD':
                ticks += f"Ticker: {rawTicks[i]['1. symbol']}\n"
                ticks += f"Name: {rawTicks[i]['2. name']}\n"
                ticks += f"-\n"
        return ticks  
class DB():
    ca = certifi.where()
    
    client = pymongo.MongoClient("mongodb+srv://MYCoding:QV9BcLxtJqrInZB4@mycoding.pzucnk1.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)
    #to collect user and usage information
    def NewUse(self,userID,tickerID):
        db = self.client["Stocks"]
        collection = db["Users"]
        post = {"User": userID, "Ticker": tickerID}
        collection.insert_one(post)
    #for the Alpha api    
    def PostLots(self,Function,API_Field):
        db = db = self.client["Stocks"]
        collection = db["Alpha_Vantage"]
        for i, f in enumerate(Function):
            post = {"Function":f, "API_Field":API_Field[i]}
            collection.insert_one(post)
    def PostOne(self,Function,API_Field):
        db = db = self.client["Stocks"]
        collection = db["Alpha_Vantage"]
        post = {"Function":Function, "API_Field":API_Field}
        collection.insert_one(post)  
    #fundamentals          
    def GetAllFundemetals(self):
        db = db = self.client["Stocks"]
        collection = db["Alpha_Vantage"]
        return collection.find()
    #wl stuff
    def NewWL(self,user,tickers):    
        db = self.client["Stocks"]
        collection = db["WL"]
        post = {"User": user, "Tickers": tickers}
        collection.insert_one(post)
    def getWLByUser(self,user,wlNum):
        db = self.client["Stocks"]
        collection = db["WL"]
        document = collection.find({'User': user}).skip(wlNum).limit(1)[0]["Tickers"].split(',')
        return document
    def AddLotsWL(self,user,tickers):
        db = self.client["Stocks"]
        collection = db["WL"]
        for i in tickers:
            post = {"User": user, "Tickers": i}
            collection.insert_one(post)
    def GetWlCount(self,user):
        db = self.client["Stocks"]
        collection = db["WL"]
        query = {'User': user}
        number = collection.count_documents(query)
        return str(number)
class Main():  
    def run(self):
        try:
            self.emailpro = Emails('paperstocksnj@gmail.com','oeurjrdemmeyrffb')
            self.froms, self.data = self.emailpro.GetDataAndFroms()
            if len(self.data) >0:
                for i, d in enumerate(self.data):
                    if len(d) > 1 and d[-1] == "SEARCH":
                        d.pop(-1)
                        name = ' '.join(d)
                        message = Stocks().GetTickerFromName(name)    
                        self.SendEmail(self.froms[i],message)   
                        print(name)
                    elif len(d) == 1:
                        if d[0] == 'COUNT':
                            WlNum = DB().GetWlCount(self.froms[i])
                            message = f'You have {WlNum} Watchlist'
                            self.SendEmail(self.froms[i],message)
                        elif len(d[0]) >= 3 and d[0][:2] =="WL":
                            message = Stocks().WatchLists(d[0],self.froms[i])
                            self.SendEmail(self.froms[i],message)
                        else:
                            try:
                                DB().NewUse(self.froms[i],d[0])
                                message = Stocks().GetPrice(d[0])
                                self.SendEmail(self.froms[i],message)
                            except Exception as e :
                                print(e)
                                message = "Not a Ticker"
                                self.SendEmail(self.froms[i],message)    
                    elif  len(d) == 2:
                        try:
                            DB().NewUse(self.froms[i],d[0])
                            if d[1] =="ALL":
                                message = Stocks().GetAll(d[0])
                                self.SendEmail(self.froms[i],message)
                            elif d[1] == "DHL":
                                message = Stocks().DayHighLow(d[0])
                                self.SendEmail(self.froms[i],message)
                            elif d[1] == "NEWS":
                                message = Stocks().News(d[0])    
                                self.SendEmail(self.froms[i],message)
                            elif d[1] == "SEARCH":
                                message = Stocks().GetTickerFromName(d[0])    
                                self.SendEmail(self.froms[i],message)  
                            elif d[1] == "ADD":
                                message = d[0].replace("/", ",")
                                DB().NewWL(self.froms[i], message)
                                self.SendEmail(self.froms[i], f"You added {message} to watchlist")
                            else:
                                message = Stocks().GetOne(d[0],d[1])
                                self.SendEmail(self.froms[i],message)
                        except Exception as e:
                            print(e)
                            message = "Not a Ticker"
                            self.SendEmail(self.froms[i],message)
                    elif len(d) == 3:
                        #wl add k/lulu/v      
                        if  d[1] == "ADD" and d[0] == "WL":
                            message = d[2].replace("/",",")
                            DB().NewWL(self.froms[i],message)
                            self.SendEmail(self.froms[i],f" you added {message} to watchlist")   
                        else:
                            message = "Not a input"
                            self.SendEmail(self.froms[i],message)        
        except Exception as e:
            print(e)                      
    def SendEmail(self,from_,message):
        self.emailpro.sendserver.sendmail(self.emailpro.username,from_,message)
        print(f"{time.asctime()}\n{from_}\n{message}")                    
        
schedule.every(10).seconds.do(Main().run)

while 1:
    schedule.run_pending()
    time.sleep(1)      
    
#print(Stocks().GetTickerFromName('tesla'))