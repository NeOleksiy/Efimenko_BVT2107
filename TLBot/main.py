import telebot
from telebot import types
import psycopg2
import sys
import locale
from datetime import date
import datetime


d = date.today()
start = date(2021, 9, 1)
delta = str((d - start)//7)
list(delta)
delt=delta[0]+delta[1]



conn = psycopg2.connect(database="Timetable",
                        user= "postgres",
                        password="1234",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()

token = "2142853168:AAGnNDgD05XaJDxBQZtj7I4k_Dg0mhZNehw"
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("понедельник", "вторник",'среда','четверг','пятница','суббота\n', "расписание на текущую неделю",'расписание на следующую неделю')
    bot.send_message(message.chat.id,"Я бот с расписанием группы БВТ2107\nкоманды:\n/help\n/start\n/mtuci\n/week", reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help_messag(message):
    bot.send_message(message.chat.id, 'Я бот с расписанием группы БВТ2107\nкоманды:\n/help\n/start\n/mtuci\n/week')


@bot.message_handler(commands=['mtuci'])
def help_messa(message):
    bot.send_message(message.chat.id, 'https://mtuci.ru/')


@bot.message_handler(commands=['week'])
def help_mess(message):
    if int(delt)%2==0:
        bot.send_message(message.chat.id, 'верхняя')
    if int(delt) % 2 == 1:
        bot.send_message(message.chat.id, 'нижняя')


@bot.message_handler(content_types=['text'])
def week(message):
        if message.text.lower() == "понедельник" and int(delt)%2==1:
            sql_string = "SELECT * FROM cal.monday"
            cursor.execute(sql_string)
            bot.send_message(message.chat.id, 'чётная неделя\n')
            for records in cursor.fetchall():
                bot.send_message(message.chat.id, str(records).encode().decode('utf-8'))
        if message.text.lower() == "понедельник" and int(delt)%2==0:
            cursor.execute('SELECT * FROM cal.monday')
            for records in cursor.fetchall():
                bot.send_message(message.chat.id, 'нечётная неделя\n', str(records).encode().decode('utf-8'))

        if message.text.lower() == "вторник" and int(delt)%2==1:
            cursor.execute('SELECT * FROM cal.Tuesday_chot')
            bot.send_message(message.chat.id, 'чётная неделя\n')
            for records1 in cursor.fetchall():
                bot.send_message(message.chat.id, str(records1).encode().decode('utf-8'))
        if message.text.lower() == "вторник" and int(delt)%2==0:
            cursor.execute('SELECT * FROM cal.Tuesday_Nech')
            for records1 in cursor.fetchall():
                bot.send_message(message.chat.id, 'нечётная неделя\n', str(records1).encode().decode('utf-8'))

        if message.text.lower() == "среда" and int(delt)%2==1:
            cursor.execute('SELECT * FROM cal.Wednesday_chot')
            bot.send_message(message.chat.id, 'чётная неделя\n')
            for records2 in cursor.fetchall():
                bot.send_message(message.chat.id, str(records2).encode().decode('utf-8'))
        if message.text.lower() == "среда" and int(delt)%2==0:
            cursor.execute('SELECT * FROM cal.Wednesday_Nech')
            for records2 in cursor.fetchall():
                bot.send_message(message.chat.id, 'нечётная неделя\n', str(records2).encode().decode('utf-8'))

        if message.text.lower() == "четверг" and int(delt)%2==1:
            cursor.execute('SELECT * FROM cal.Thursday_chot')
            bot.send_message(message.chat.id, 'чётная неделя\n')
            for records3 in cursor.fetchall():
                bot.send_message(message.chat.id, str(records3).encode().decode('utf-8'))
        if message.text.lower() == "четверг" and int(delt)%2==0:
            cursor.execute('SELECT * FROM cal.Thursday_Nech')
            for records3 in cursor.fetchall():
                bot.send_message(message.chat.id, 'нечётная неделя\n', str(records3).encode().decode('utf-8'))

        if message.text.lower() == "пятница" and int(delt)%2==1:
            cursor.execute('SELECT * FROM cal.Friday_chot')
            bot.send_message(message.chat.id, 'чётная неделя\n')
            for records4 in cursor.fetchall():
                bot.send_message(message.chat.id, str(records4).encode().decode('utf-8'))
        if message.text.lower() == "пятница" and int(delt)%2==0:
            cursor.execute('SELECT * FROM cal.Friday_Nech')
            for records4 in cursor.fetchall():
                bot.send_message(message.chat.id, 'нечётная неделя\n', str(records4).encode().decode('utf-8'))

        if message.text.lower() == "суббота" and int(delt)%2==1:
            cursor.execute('SELECT * FROM cal.Saturday')
            bot.send_message(message.chat.id, 'чётная неделя\n')
            for records5 in cursor.fetchall():
                bot.send_message(message.chat.id, str(records5).encode().decode('utf-8'))
        if message.text.lower() == "суббота" and int(delt)%2==0:
            cursor.execute('SELECT * FROM cal.Saturday')
            for records5 in cursor.fetchall():
                bot.send_message(message.chat.id, 'нечётная неделя\n', str(records5).encode().decode('utf-8'))

        if message.text.lower() == "расписание на текущую неделю" and int(delt) % 2 == 0:
            bot.send_message(message.chat.id, 'нечётная неделя')
            bot.send_message(message.chat.id, 'понедельник')
            cursor.execute('SELECT * FROM cal.monday')
            for record in cursor.fetchall():
                bot.send_message(message.chat.id, str(record).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'вторник')
            cursor.execute('SELECT * FROM cal.Tuesday_Nech')
            for record1 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record1).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'среда')
            cursor.execute('SELECT * FROM cal.Wednesday_Nech')
            for record2 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record2).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'четверг')
            cursor.execute('SELECT * FROM cal.Thursday_Nech')
            for record3 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record3).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'пятница')
            cursor.execute('SELECT * FROM cal.Friday_Nech')
            for record4 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record4).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'суббота')
            cursor.execute('SELECT * FROM cal.Saturday')
            for record5 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record5).encode().decode('utf-8'))

        if message.text.lower() == "расписание на текущую неделю" and int(delt) % 2 == 1:
            bot.send_message(message.chat.id, 'чётная неделя')
            bot.send_message(message.chat.id, 'понедельник')
            cursor.execute('SELECT * FROM cal.monday')
            for record in cursor.fetchall():
                bot.send_message(message.chat.id, str(record).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'вторник')
            cursor.execute('SELECT * FROM cal.Tuesday_chot')
            for record1 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record1).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'среда')
            cursor.execute('SELECT * FROM cal.Wednesday_chot')
            for record2 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record2).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'четверг')
            cursor.execute('SELECT * FROM cal.Thursday_chot')
            for record3 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record3).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'пятница')
            cursor.execute('SELECT * FROM cal.Friday_chot')
            for record4 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record4).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'суббота')
            cursor.execute('SELECT * FROM cal.Saturday')
            for record5 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record5).encode().decode('utf-8'))

        if int(delt) % 2 == 0 and message.text.lower() == "расписание на следующую неделю":
            bot.send_message(message.chat.id, 'чётная неделя')
            bot.send_message(message.chat.id, 'понедельник')
            cursor.execute('SELECT * FROM cal.monday')
            for record in cursor.fetchall():
                bot.send_message(message.chat.id, str(record).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'вторник')
            cursor.execute('SELECT * FROM cal.Tuesday_chot')
            for record1 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record1).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'среда')
            cursor.execute('SELECT * FROM cal.Wednesday_chot')
            for record2 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record2).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'четверг')
            cursor.execute('SELECT * FROM cal.Thursday_chot')
            for record3 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record3).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'пятница')
            cursor.execute('SELECT * FROM cal.Friday_chot')
            for record4 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record4).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'суббота')
            cursor.execute('SELECT * FROM cal.Saturday')
            for record5 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record5).encode().decode('utf-8'))

        if int(delt) % 2 == 1 and message.text.lower() == "расписание на следующую неделю":
            bot.send_message(message.chat.id, 'нечётная неделя')
            bot.send_message(message.chat.id, 'понедельник')
            cursor.execute('SELECT * FROM cal.monday')
            for record in cursor.fetchall():
                bot.send_message(message.chat.id, str(record).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'вторник')
            cursor.execute('SELECT * FROM cal.Tuesday_Nech')
            for record1 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record1).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'среда')
            cursor.execute('SELECT * FROM cal.Wednesday_Nech')
            for record2 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record2).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'четверг')
            cursor.execute('SELECT * FROM cal.Thursday_Nech')
            for record3 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record3).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'пятница')
            cursor.execute('SELECT * FROM cal.Friday_Nech')
            for record4 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record4).encode().decode('utf-8'))
            bot.send_message(message.chat.id, 'суббота')
            cursor.execute('SELECT * FROM cal.Saturday')
            for record5 in cursor.fetchall():
                bot.send_message(message.chat.id, str(record5).encode().decode('utf-8'))
        else:
            bot.send_message(message.chat.id, 'якщо не розумію /help')


bot.polling(non_stop=True)
