import finnhub
import pprint
import datetime
import nltk
import smtpd
import email
import imaplib
import smtplib
from bs4 import BeautifulSoup
from finvizfinance.quote import finvizfinance


class Emails():
    serverStart = 'imap.gmail.com'
    sendserver = smtplib.SMTP('smtp.gmail.com', 587)
    sendserver.starttls()
    mail = imaplib.IMAP4_SSL(serverStart)
    def __init__(self , username , password):
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
                data.append(self.Token(text))  
            return froms, data
        else:
            print("No mail")  
            return froms, data      

class Stock:
    finnhub_client = finnhub.Client(api_key="c6s0ql2ad3ifcngb8qvg")
    def __init__(self, ticker, action):
        self.ticker = ticker.upper()
        self.action = action.upper()
    def GetPrice(self):
        result = f"{finvizfinance(self.ticker).ticker_fundament()['Company']}\n"
        result +=f"Price: {self.finnhub_client.quote(self.ticker)['c']}\n" 
        return result
    def GetDayHighLow(self,HighOrLow):
        if HighOrLow == "DHIGH":
            return f"Day High: {self.finnhub_client.quote(self.ticker)['h']}\n" 
        elif HighOrLow == "DLOW":
            return f"Day Low: {self.finnhub_client.quote(self.ticker)['l']}\n"
    def GetAll(self):
        result =self.GetPrice()
        file = open("AutomatedQuotes\AutomatedQuotesNj\AutomatedQuotes\TestCode\data.txt", "r").read().split(",")
        headers = open("AutomatedQuotes\AutomatedQuotesNj\AutomatedQuotes\TestCode\dataHeaders.txt", "r").read().split(",")
        for index, item in enumerate(file) :
            item.strip('\"')
            header = headers[index].strip('\"')
            result += f"{header}: {finvizfinance(self.ticker).ticker_fundament()[item]}\n"   
        return result
    def GetOne(self):
        result = self.GetPrice()
        file = open("AutomatedQuotes\AutomatedQuotesNj\AutomatedQuotes\TestCode\data.txt", "r").read().split(",")
        headers = open("AutomatedQuotes\AutomatedQuotesNj\AutomatedQuotes\TestCode\dataHeaders.txt", "r").read().split(",")
        for index, head in enumerate(headers) :
            head = head.strip('\"')
            if self.action == head:
                file = file[index].strip('\"')
                result += f"{head}: {finvizfinance(self.ticker).ticker_fundament()[file]}"      
                break
        return result    
class DoIt():
    def __init__(self, froms , data):
        self.data = data
        self.froms = froms
    def Run(self):
        for index, d  in enumerate(self.data):
            s = Stock(d[0],"n/a")
            if len(d) == 1:
                message = s.GetPrice()
                print(message)
                Emails.sendserver.sendmail("paperstocksnj@gmail.com",froms[index],message)

            else:
                if(d[1] == "ALL"):
                    message = s.GetAll()
                    print(message)
                    Emails.sendserver.sendmail("paperstocksnj@gmail.com",froms[index],message)
                else:
                    message = s.GetOne()
                    isHighLow = s.GetDayHighLow(d[1])
                    if isHighLow!= None: 
                        message += isHighLow
                    print(message)  
                    Emails.sendserver.sendmail("paperstocksnj@gmail.com",froms[index],message)

froms , data = Emails('paperstocksnj@gmail.com','oeurjrdemmeyrffb').GetDataAndFroms()
one = DoIt(froms, data)
one.Run()

