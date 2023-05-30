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
        result = f"{tick}\n" #f"{finvizfinance(tick).ticker_fundament()['Company']}\n"
        result +=f"Price: {rawData['c']}\n"  
        result += f"Change: ${rawData['d']}\n"
        result += f"Percent Change: {rawData['dp']}%\n"
        result += f"Previous Close: ${rawData['pc']}\n"
        return result
    # this function get the all the data the we previde from finviz
    def GetAll(self,tick):
        tick = tick.upper()
        result = self.GetPrice(tick)
        result += self.DayHighLow(tick)
        fdata = finvizfinance(tick).ticker_fundament()
        file = open("/root/Program/Data/data.txt", "r").read().split(",")
        headers = open("/root/Program/Data/dataHeaders.txt", "r").read().split(",")
        for index, head in enumerate(headers) :
            head = head.strip('\"')
            dataType = file[index]
            result += f"{head}: {fdata[dataType]}\n"
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
        WLFILE = open("/root/Program/Data/WL.txt", "r").read().split(",\n")
        wl = wl.upper()
        wl = int(wl.strip('WL'))
        if wl < len(WLFILE):
            ticks = WLFILE[wl-1].split(",")
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
class DB():
    ca = certifi.where()
    client = pymongo.MongoClient("mongodb+srv://MYCoding:QV9BcLxtJqrInZB4@mycoding.pzucnk1.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)
    def NewUse(self,userID,tickerID):
        db = self.client["Stocks"]
        collection = db["Users"]
        post = {"User": userID, "Ticker": tickerID}
        collection.insert_one(post)
        
        
class Main():  
    def run(self):
        try:
            self.emailpro = Emails('textlivequotes@gmail.com','hvnhjfsnpsahjbhw')
            self.froms, self.data = self.emailpro.GetDataAndFroms()
            if len(self.data) >0:
                for i, d in enumerate(self.data):
                    if len(d) == 1:
                        
                        if len(d[0]) >= 3 and d[0][:2] =="WL":
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
                            else:
                                message = Stocks().GetOne(d[0],d[1])
                                self.SendEmail(self.froms[i],message)
                        except:
                            message = "Not a Ticker"
                            self.SendEmail(self.froms[i],message)
                    elif len(d) == 3:      
                        if  d[1] == "ADD" and d[0] == "WL":
                            message = d[2].replace("/",",")
                            f = open("/root/Program/Data/WL.txt", "a")
                            f.write(f"{message},\n")
                            f.close()
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