import telebot
from telebot import types
token = '6967810496:AAH2FbRr6dOoYZn0Ea6eKArAkvdE5-TBT6A'
bot = telebot.TeleBot(token)
@bot.message_handler(func=lambda message: True)
def msg(message):
    bot.send_message(message.chat.id,message)
    bot.send_message(message.chat.id,message.from_user)
    mention = f"<a href='tg://user?id={message.chat.id}'>{message.from_user.id}</a>"
    bot.reply_to(message,mention,parse_mode='HTML')
bot.infinity_polling()
