# import chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# from tkinter import *
bot = ChatBot(
    'Acrobot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
    ],
    database_uri='sqlite:///database.sqlite3'
)

training_data=open('trainingdata/ques_ans.txt',encoding="utf8").read().splitlines()
trainer = ListTrainer(bot)

trainer.train(training_data)
def chat(user):
     bot_response = bot.get_response(user)
       # print("Acrobot:", bot_response)
     return bot_response
