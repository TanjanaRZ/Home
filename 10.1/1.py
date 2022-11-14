import telebot
import calc

bot = telebot.TeleBot('  ')
f1 = ''
f2 = ''

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Отправте первый многочлен')
    
@bot.message_handler(content_types=["text"])
def one(message):
    global f1
    f1 = message.text
    bot.send_message(message.chat.id, 'Отправте второй многочлен')
    bot.register_next_step_handler(message, two);
        

    
def two(message):
    global f2
    f2 = message.text
    res = calc.calc(f1 ,f2)
    bot.send_message(message.chat.id, res)
    
bot.polling(none_stop=True, interval=0)