import telebot
import subprocess
import os

bot = telebot.TeleBot('6850734062:AAG9Agmf6UbljQDCn3_XTn0WExZRu65-mAc')

admin_user_id = 6270618135

@bot.message_handler(commands=['save_file'])
def save_file(message):
    if message.from_user.id == admin_user_id:
        bot.send_message(message.chat.id, "Send me a file to save.")
        bot.register_next_step_handler(message, process_file_save)
    else:
        bot.send_message(message.chat.id, "You are not authorized to use this command.")

def process_file_save(message):
    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path

    downloaded_file = bot.download_file(file_path)
    file_name = f"{file_path.split('/')[-1]}"
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.send_message(message.chat.id, f"File '{file_name}' has been saved.")

@bot.message_handler(commands=['run_file'])
def run_file(message):
    if message.from_user.id == admin_user_id:
        bot.send_message(message.chat.id, "Enter the name of the file to run:")
        bot.register_next_step_handler(message, process_run_file)
    else:
        bot.send_message(message.chat.id, "You are not authorized to use this command.")

def process_run_file(message):
    file_name = message.text
    if os.path.exists(file_name):
        try:
            subprocess.run(["python3", file_name], check=True)
            bot.send_message(message.chat.id, "File executed successfully.")
        except subprocess.CalledProcessError as e:
            bot.send_message(message.chat.id, f"Error executing file: {e}")
    else:
        bot.send_message(message.chat.id, "File not found.")

bot.infinity_polling()
