#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Author：hms5232
Repo：https://github.com/hms5232/deploy-python-telegram-bot-on-heroku
"""


from configparser import ConfigParser

from telegram.ext import Updater, CommandHandler


# 設定一些個人的環境變數
TOKEN = os.environ["TOKEN"]
PORT = int(os.environ.get('PORT', '8443'))


updater = Updater(token=TOKEN)  # 呼叫 bot 用


def welcome(bot, update):
	""" Show user welcome message. """
	
	chat_id = update.message.from_user.id
	
	about_bot = ''
	about_bot = about_bot + 'Hello! 感謝您的使用\n'
	about_bot = about_bot + '本機器人由 [hms5232](https://medium.com/@hms5232) 開發\n'
	about_bot = about_bot + '用於將機器人部署在 Heroku 上的教學文的範例\n'
	about_bot = about_bot + '可於 [Github](https://github.com/hms5232) 上找到我\n'
	about_bot = about_bot + '文章原文可在[repo簡介](https://github.com/hms5232/deploy-python-telegram-bot-on-heroku)上找到\n'
	
	bot.send_message(chat_id, about_bot, parse_mode='Markdown')


def hello(bot, update):
	""" Hello World! """
	
	update.message.reply_text('Hello world!')


updater.dispatcher.add_handler(CommandHandler('start', welcome))  # 歡迎訊息
updater.dispatcher.add_handler(CommandHandler('hi', hello))  # Hello World!


# 執行機器人必須要的，讓機器人運作聽命
#updater.start_polling()
# 改用 webhook 的方式
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://{你的 heroku 專案名稱}.herokuapp.com/" + TOKEN)
updater.idle()
