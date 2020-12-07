import telebot
import config
import schedule_class

bot = telebot.TeleBot(config.token)
users = []

# @bot.message_handler()
# def print_hi(message):
#     bot.send_message(message.chat.id, 'Hi')

@bot.message_handler(commands=["start"])
def cmd_start(message):
    user = schedule_class.busy(message.chat.id)
    bot.send_message(message.chat.id, 'Теперь я тебя знаю и ты можешь добавлять свли задачи')

@bot.message_handler(commands=["help"])
def cmd_start(message):
    bot.send_message(message.chat.id,
        '''Команды:
        /today - все что запланировано на сегодня
        /yesterday - все что запланировано на завтра
        /week - все что запланировано на неделю
        /day - все что запланировано на заданный день
        /add - добавить событие, выбрав данные из ссылки
    ''')

@bot.message_handler(commands=["today"])
def cmd_start(message):
    bot.send_message(message.chat.id, users[message.chat.id].today())


bot.infinity_polling()
