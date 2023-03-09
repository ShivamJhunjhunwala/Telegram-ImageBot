# Telegram-ImageBot

The Telegram-ImageBot is a Telegram bot that allows users to upload and share images from a remote Mega database. The bot is written in Python and uses the `python-telegram-bot` and `mega.py` libraries to interact with the Telegram API and Mega database, respectively.

## Features

- Allows users to upload images to a remote Mega database using a unique link provided by the bot.
- Sends a new image to the chat every minute from the Mega database.
- Allows users to retrieve a list of available images in the Mega database.
- Allows users to delete images from the Mega database.

## Installation

To run this bot, you need to follow these steps:

1. Clone or download this repository to your local machine.
2. Install the required dependencies by running the command `pip install -r requirements.txt`.
3. Create a new bot using the [BotFather](https://core.telegram.org/bots#6-botfather) and obtain your bot's token.
4. Obtain your Mega email and password, and log in to your Mega account using the `mega_login.py` script provided in the repository. This will generate a session ID that you will need to copy to the `config.ini` file.
5. Rename `config.example.ini` to `config.ini` and fill in the required information:
   * `BOT_TOKEN`: Your Telegram bot token.
   * `MEGA_EMAIL`: Your Mega email address.
   * `MEGA_PASSWORD`: Your Mega password.
   * `MEGA_SESSION_ID`: The path to the file containing your Mega session ID.
   * `MEGA_DB_FOLDER`: The name of the folder in the Mega database where you want to store your images.
6. Run the bot using the command `python bot.py`.

## Usage

Once the bot is running, users can interact with it by sending the following commands:

- `/start`: Displays a welcome message.
- `/help`: Displays a help message.
- `/upload`: Sends the user a unique link for uploading an image to the Mega database.
- `/list`: Displays a list of available images in the Mega database.
- `/delete`: Allows the user to delete an image from the Mega database. The user must specify the filename of the image to be deleted.

The bot also sends a new image to the chat every minute, as specified in the `bot.py` file.

## Conclusion

The Telegram-ImageBot is a useful tool for users who want to share images in a Telegram chat without having to upload them directly to the chat. By storing images in a remote Mega database, users can access and share their images from anywhere, without having to worry about storage limitations. The bot is easy to install and use, and can be customized to suit the needs of individual users.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Contributing

Contributions are welcome! Please read the `CONTRIBUTING.md` file for more information on how to contribute.

## Acknowledgments

- The `python-telegram-bot` and `mega.py` libraries were used to build this bot.
- This project was inspired by [this tutorial](https://www.twilio.com/blog/how-to-build-a-telegram-bot-in-30-minutes).
