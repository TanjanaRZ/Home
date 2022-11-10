import calc
import telebot
import log

bot = telebot.TeleBot('5512819290:AAGN6VPNlTKmYHWukGXoP0LSZAwB4MmQxD8')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне формулу')
    
@bot.message_handler(content_types=["text"])
def handle_text(message):
    res = calc.clclt(message.text)
    bot.send_message(message.chat.id, 'Ответ: ' + res)
    log.writeLog(message.chat.first_name, message.text, res, message.date)
    
bot.polling(none_stop=True, interval=0)