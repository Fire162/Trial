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
    file_name = message.document.file_name  # Use the user-provided file name
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
@bot.message_handler(func=lambda message: message.from_user.id == admin_user_id and message.text.startswith('/run '))
def run_command(message):
    command = message.text[5:]  # Extract the command after '/run '

    try:
        output = subprocess.check_output(command, shell=True, text=True)
        bot.reply_to(message, f"Output:\n{output}")
    except subprocess.CalledProcessError as e:
        bot.reply_to(message, f"Error executing command: {e}")
        
# Clear the chat screen
@bot.message_handler(commands=['clear'])
def clear_screen(message):
    if message.from_user.id == admin_user_id:
        bot.send_message(message.chat.id, "\x1b[H\x1b[J")  # ANSI escape code for clearing the screen
    else:
        bot.send_message(message.chat.id, "You are not authorized to use this command.")
@bot.message_handler(commands=['stop_process'])
def stop_process(message):
    if message.from_user.id == admin_user_id:
        command_parts = message.text.split(" ")
        
        if len(command_parts) == 2:
            process_name = command_parts[1].strip()
            
            try:
                # Use pgrep to find the PID of the running process
                pid = subprocess.check_output(f"pgrep -f {process_name}", shell=True, text=True).strip()
                
                if pid:
                    # Use kill to stop the process
                    subprocess.run(f"kill {pid}", shell=True)
                    bot.send_message(message.chat.id, f"Process '{process_name}' stopped successfully.")
                else:
                    bot.send_message(message.chat.id, f"No running process with the name '{process_name}'.")
            except subprocess.CalledProcessError as e:
                bot.send_message(message.chat.id, f"Error stopping process: {e}")
        else:
            bot.send_message(message.chat.id, "Usage: /stop_process <process_name>")
    else:
        bot.send_message(message.chat.id, "You are not authorized to use this command.")
@bot.message_handler(commands=['get_file'])
def get_file(message):
    if message.from_user.id == admin_user_id:
        bot.send_message(message.chat.id, "Enter the name of the file to send:")
        bot.register_next_step_handler(message, process_get_file)
    else:
        bot.send_message(message.chat.id, "You are not authorized to use this command.")

def process_get_file(message):
    file_name = message.text
    if os.path.exists(file_name):
        try:
            with open(file_name, 'rb') as file:
                bot.send_document(message.chat.id, file)
        except Exception as e:
            bot.send_message(message.chat.id, f"Error sending file: {e}")
    else:
        bot.send_message(message.chat.id, "File not found.")
        
bot.infinity_polling()
