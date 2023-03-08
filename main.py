from mega_utils import MegaUtils
from telegram_bot import TelegramBot

# set up Mega account
email = "your_email"
password = "your_password"
mega_utils = MegaUtils(email, password)

# set up Telegram bot
bot_token = "your_bot_token"
chat_id = "your_chat_id"
telegram_bot = TelegramBot(bot_token, chat_id, mega_utils)

# run the bot
folder_name = "your_folder_name"
local_path = "/path/to/your/local/directory"
telegram_bot.run_bot(folder_name, local_path)
