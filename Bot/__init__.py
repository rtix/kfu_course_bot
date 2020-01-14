import configparser

import telebot

import Bot.config
import Bot.helper
import Models.Mail

sets = configparser.ConfigParser()
sets.read(Bot.config.ROOT_DIR + '/settings.cfg')

if not Models.Mail.check_valid(sets['mail']['email']):
    raise Models.Mail.WrongEMail("Неправильный email в файле настроек.")

bot = telebot.TeleBot(sets['bot']['token'])

if sets['optional']['proxy']:
    telebot.apihelper.proxy = {
        'https': sets['optional']['proxy']
    }

email = Models.Mail.Mail(sets['mail']['email'], sets['mail']['password'], sets['optional']['smtp_host'])

botHelper = Bot.helper.BotHelper(bot)
