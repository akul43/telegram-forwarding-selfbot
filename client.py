from telethon import TelegramClient, events
import os
import re
import time
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

try:
    # Retrieve and convert environment variables
    api_id = int(os.getenv('API_ID'))
    api_hash = os.getenv('API_HASH')
    channel_copy_message = int(os.getenv('CHANNEL_COPY_MESSAGE'))
    channel_send_message = int(os.getenv('CHANNEL_SEND_MESSAGE'))
except (TypeError, ValueError) as e:
    # Print error message and exit if environment variables are not set correctly
    print(f"Error loading environment variables: {e}")
    exit(1)

# Initialize the Telegram client
client = TelegramClient('client', api_id, api_hash)

@client.on(events.NewMessage(chats=[channel_copy_message]))
async def unified_handler(event):
    # Print message details for debugging
    print(f"Message received in channel {channel_copy_message}")
    print(f"Forwarding to channel {channel_send_message}")
    print(f"Content: {event.raw_text}")
    print(f"Timestamp: {event.date}")
    # Forward the message to the specified channel
    await send_message_to_channel(event.raw_text, channel_send_message)

async def send_message_to_channel(message, channel_send_message):
    # Get the entity of the target channel
    entity = await client.get_entity(channel_send_message)
    # Send the message to the target channel
    await client.send_message(entity=entity, message=message)

def main():
    # Start the Telegram client
    client.start()
    print("‧₊˚✧ TELEGRAM CLIENT STARTED ✧˚₊‧\n\n")
    # Run the client until it is disconnected
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
