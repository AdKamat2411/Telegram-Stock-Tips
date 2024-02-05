import openpyxl
import datetime
import re
import telethon.sync
import asyncio
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterDocument
import csv

# Replace with your own values
api_id = 
api_hash = ''
phone = ''
client = TelegramClient(phone, api_id, api_hash)

# Replace with the names of the Telegram groups you want to monitor
group_names = ['intraday_tradex', 'tradephoenix_stocks', 'ShareMarket_Intraday']

# Replace with the names of the Indian people you want to look for
indian_names = ['BANKNIFTY']

# Replace with the path and name of the Excel file you want to create
excel_file = 'messages.xlsx'

# Set the time range to search for messages
start_time = datetime.time(7, 0, 0)
end_time = datetime.time(9, 0, 0)

# Create a regular expression pattern to match Indian names
indian_pattern = re.compile('|'.join(indian_names), re.IGNORECASE)

with client:
    # Create an empty list to store the matching messages
    messages = []
    # Iterate over the group names
    for group_name in group_names:
        # Find the corresponding group ID
        group = client.get_entity(group_name)
        # Create a filter to search for messages within the time range
        # Iterate over the messages in the group
        for message in client.iter_messages(group, offset_date=datetime.date.today(), reverse=True):
            # Check if the message contains an Indian name
            if indian_pattern.search(message.message):
                # Add the matching message to the list
                messages.append({
                    'group': group_name,
                    'sender': message.sender.username,
                    'text': message.message,
                    'date': message.date.strftime('%Y-%m-%d %H:%M:%S')
                })




