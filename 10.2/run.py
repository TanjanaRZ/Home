import telebot
import fl
import re
import table

bot = telebot.TeleBot('  ')
users = []

@bot.message_handler(commands=["start"])
def start(message, res=False):
    hello = 'Здравствуйте. Вас приветствует программа "Список сотрудников"'
    bot.send_message(message.chat.id, hello)
    showMenu(message)
    
def showMenu(message):
    menu = '''Выбирете действие:
 /load - Загрузить список;
 /save - Сохранить список;
 /show - Показать список'''
    bot.send_message(message.chat.id, menu)
    bot.register_next_step_handler(message, mainmenu);

def mainmenu(message):
    global users
    if message.text.strip() == "/load":
        res = fl.load(users)
        bot.send_message(message.chat.id, res)
        showMenu(message)
    elif message.text.strip() == "/save":
        res = fl.save(users)
        bot.send_message(message.chat.id, res)
        showMenu(message)
    elif message.text.strip() == "/show":
        openMenu(message, users)
    else:
        bot.send_message(message.chat.id, 'Введите корректную команду')
        mainmenu(message)
    
def openMenu(message, users):
    if len(users) == 0:
        bot.send_message(message.chat.id, 'Нечего показывать')
    else:
        men = '''Как показать?
 число - Контакт под номером;
 /exit - назад'''
        bot.send_message(message.chat.id, men)
        bot.register_next_step_handler(message, qwst, users);

def qwst(message, users):
    ans = message.text.strip()
    if ans != '/exit':
        if ans.isdigit() and int(ans)>0 and int(ans)<len(users):
            showUser(message, users, int(ans))
        elif ans == '/add':
            addUser(message, users)
        else:
            bot.send_message(message.chat.id, 'Введите корректную команду')
            qwst(message, users)
    else:
        showMenu(message)
    
def showUser(message, users, num):
    res = table.crRow(users[num], num)
    bot.send_message(message.chat.id, res)
    menuUser(message ,users, num)
    
    
def menuUser(message ,users, num):
    men = '''Выбирете действие:
 /edit - Редактировать контакт;
 /del - Удалить контакт;
 /exit - назад'''
    bot.send_message(message.chat.id, men)
    bot.register_next_step_handler(message, chos, users, num);
    

def chos(message, users, num):
    ans = message.text.strip()
    if ans == '/edit':
        editUser(message, users, num)
    elif ans == '/del':
        users.pop(num)
        bot.send_message(message.chat.id, 'Контакт удалён')
        openMenu(message, users)
    elif ans == '/exit':
        openMenu(message, users)
    else:
        bot.send_message(message.chat.id, 'Введите корректную команду')
        chos(message, users, num)
    
def editUser(message, users, num):
    men = '''Что редактировать:
    /id - id;
    /firstname - Имя;
    /secondname - Фамилия;
    /date - Дата рождения;
    /department - Отдел;
    /firstphone - Личный номер;
    /secondphone - Рабочий номер; 
    /exit - выход'''
    bot.send_message(message.chat.id, men)
    bot.register_next_step_handler(message, eddt, users, num)
    

def eddt(message, users, num):
    secs = 'Изменено'
    ans = message.text.strip()
    if ans == '/id':
        bot.send_message(message.chat.id, 'id (5 цифр, /exit - выход)')
        bot.register_next_step_handler(message, setValue, '[0-9]{5}', users, num, 0)
        
    elif ans == '/firstname':
        bot.send_message(message.chat.id, 'Имя (/exit - выход)')
        bot.register_next_step_handler(message, setValue, '[а-яА-Я]{2,10}', users, num, 1)
        
    elif ans == '/secondname':
        bot.send_message(message.chat.id, 'Фамилия (/exit - выход)')
        bot.register_next_step_handler(message, setValue, '[а-яА-Я]{2,12}', users, num, 2)
        
    elif ans == '/date':
        bot.send_message(message.chat.id, 'Дата рождения (**.**.****, /exit - выход)')
        bot.register_next_step_handler(message, setValue, '[0-9]{1,2}.[0-9]{1,2}.[0-9]{4}', users, num, 3)
        
    elif ans == '/department':
        bot.send_message(message.chat.id, 'Отдел: (/exit - выход)')
        bot.register_next_step_handler(message, setValue, '[а-яА-Я]{2,12}', users, num, 4)
        
    elif ans == '/firstphone':
        bot.send_message(message.chat.id, 'Личный номер (+7 *** *** **-**, /exit - выход)')
        bot.register_next_step_handler(message, setValue, '\+7 [0-9]{3} [0-9]{3} [0-9]{2}-[0-9]{2}', users, num, 5)
        
    elif ans == '/secondphone':
        bot.send_message(message.chat.id, 'Рабочий номер (+7 *** *** **-** или пусто, /exit - выход)')
        bot.register_next_step_handler(message, setValue, '\+7 [0-9]{3} [0-9]{3} [0-9]{2}-[0-9]{2}|', users, num, 6)
        
    elif ans == '/exit':
        openMenu(message, users)
    else:
        bot.send_message(message.chat.id, 'Введите корректную команду')
        eddt(message, users, num)
    


def setValue(message, rex, users, num, clm):
    value = message.text.strip()
    if value == '/exit':
        editUser(message, users, num)
    elif re.fullmatch(rex, value) != None:
        users[num][clm] = value
        bot.send_message(message.chat.id, 'Изменено')
        editUser(message, users, num)
    else:
        bot.send_message(message.chat.id, 'Значение не подходит')









bot.polling(none_stop=True, interval=0)