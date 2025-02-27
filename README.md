# Telegram Forwarding Selfbot

A simple Telegram self-bot to forward messages from one channel to another using Telethon.

If you like the project and it helps, give it a STAR

## Prerequisites

- Python 3.6+
- Telethon
- python-dotenv

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/telegram-forwarding-selfbot.git
    cd telegram-forwarding-selfbot
    ```

2. **Install the required packages**:

    ```sh
    pip install telethon python-dotenv
    ```

3. **Create a Telegram application**:

    - Go to [my.telegram.org](https://my.telegram.org).
    - Log in with your phone number.
    - Click on "API Development Tools".
    - Create a new application and note down the `API_ID` and `API_HASH`.

4. **Create a [.env](http://_vscodecontentref_/0) file**:

    In the root directory of the project, create a [.env](http://_vscodecontentref_/1) file and add your environment variables:

    ```properties
    API_ID=your_api_id
    API_HASH=your_api_hash
    CHANNEL_COPY_MESSAGE=your_channel_copy_message_id
    CHANNEL_SEND_MESSAGE=your_channel_send_message_link
    ```

    - Replace `your_api_id` with the API ID you obtained from Telegram.
    - Replace `your_api_hash` with the API hash you obtained from Telegram.
    - Replace `your_channel_copy_message_id` with the ID of the channel from which you want to copy messages. This should be a negative number (e.g., `-1001234567890`).
    - Replace `your_channel_send_message_link` with the link of the channel to which you want to send messages (e.g., `https://t.me/your_channel_name`).

## Usage

1. **Run the selfbot**:

    ```sh
    python client.py
    ```

2. The bot will start and listen for new messages in the specified channel. When a new message is received, it will be forwarded to the target channel.

## Environment Variables

- `API_ID`: Your Telegram API ID.
- `API_HASH`: Your Telegram API hash.
- `CHANNEL_COPY_MESSAGE`: The ID of the channel to copy messages from.
- `CHANNEL_SEND_MESSAGE`: The link of the channel to send messages to.