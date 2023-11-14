"""Module Docstring
This script is used for scraping data from Telegram using the Telethon library.
It reads chat names from a file and scrapes relevant data.
"""

import datetime
import pandas as pd
import csv
from cleantext import clean
import re
import os
from telethon.sync import TelegramClient, events, types

def data():
    # Replace with your own values
    api_id = 'xxxxxxx'
    api_hash = 'xxxxxxxxxxxxxxx'
    phone = 'xxxxxxxxxxxxxx'
    client = TelegramClient(phone, api_id, api_hash)

    df=pd.DataFrame()

    f = open("Groups.txt","r")

    chats = f.readlines()

    # Set the offset date to the current date at 7:00:00 AM (Market opening time)
##    now = datetime.datetime.now()
##    offset_date = datetime.datetime(now.year, now.month, now.day, 0, 0, 0)

#Messages
    offset_date = datetime.datetime.now() - datetime.timedelta(minutes=5)


    # Set the max_id to retrieve messages until 9:00:00 AM on the current date
##    end_date = datetime.datetime(now.year, now.month, now.day, 5, 0, 0)
##    max_id = int((end_date - offset_date).total_seconds())

    stocks=['BANKNIFTY']
    '''
    stocks_lower=[kw.lower() for kw in stocks]
    message_filter = events.NewMessageSearchFilter(stocks_lower, case_sensitive=False)
    '''

    for chat in chats:
        with TelegramClient('test',api_id,api_hash) as client:
            messages=[]
            for message in client.iter_messages(chat,offset_date=offset_date,reverse=True):
    ##        for message in client.iter_messages(chat,offset_date=datetime.date.today(),reverse=True):
                if re.search(r'BANKNIFTY|BNF', message.text, re.IGNORECASE):
                    if re.search(r'VIP GROUP|JOIN|MONTHLY|\d+RS|\n\nFor more details|contact on telegram|LINK|DEMO', message.text, re.IGNORECASE):
                        continue
                    else:
##                        print(chat,message.text,message.date)
                        data = {"group": chat, "sender": message.sender_id, "text": clean(message.text,no_emoji=True), "date": message.date}
        
                        temp_df= pd.DataFrame(data, index=[1])
                        df = df.append(temp_df)
                    
    ##                message_det=[chat,message.sender_id,clean(message.text, no_emoji=True),message.date]
    ##                messages.append(message_det)

    print("Scraper: COMPLTED")
    try:
        df['date']=df['date'].dt.tz_localize(None)
        #Error occurs when no message in dataframe
        df.to_excel("D:\Telegram Stocks\messages_{}.xlsx".format(datetime.date.today()), index=False)
        print("Scraper: Messages found, appended to excel file")
    except:
        df.to_excel("D:\Telegram Stocks\messages_{}.xlsx".format(datetime.date.today()), index=False)
        print('Scraper: Empty, no messages found')

    ##with open("messages.csv","w",newline="") as f:
    ##    writer=csv.writer(f)
    ##    writer.writerows(messages)


#and int(str(message.date).split()[1][:2])<5

#testing
##data()
