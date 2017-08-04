import telepot
from ChatBot import Chatbot

telegram = telepot.Bot("378676352:AAEcnOA2-NTH1qFryL80sSTJRHqXEhFtXYc")

bot = Chatbot()

def recebendoMsg(msg):
    frase = bot.escuta(frase=msg['text'])
    print(frase)
    bot.pensa(frase)
    resp = bot.fala()
    #chatID = msg['chat']['id']
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID, resp)

telegram.message_loop(recebendoMsg)

while True:
    pass
