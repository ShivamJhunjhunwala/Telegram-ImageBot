import os
import random
import time
import telegram
from mega_utils import MegaUtils

class TelegramBot:
    def __init__(self, bot_token, chat_id, mega_utils):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.bot = telegram.Bot(token=bot_token)
        self.mega_utils = mega_utils

    def send_random_image(self, folder_name, local_path):
        file_links = self.mega_utils.get_file_links(folder_name)
        file_name = random.choice(file_links)
        self.mega_utils.download_file(file_name, local_path)
        file_list = os.listdir(local_path)
        for file in file_list:
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                file_path = os.path.join(local_path, file)
                self.bot.send_photo(chat_id=self.chat_id, photo=open(file_path, 'rb'))
        self.mega_utils.remove_file(local_path)

    def run_bot(self, folder_name, local_path):
        while True:
            self.send_random_image(folder_name, local_path)
            time.sleep(60)
