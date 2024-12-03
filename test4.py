import telebot
import pyscreenshot
import os

ADMINS=(8194881876,)

bot = telebot.TeleBot("7896520923:AAGrjCbORTrVnVihYLyRm8oqP8fPXlT2nL8")

@bot.message_handler(commands="cid")
def cmd_cid(m):
    bot.send_message(m.chat.id, str(m.chat.id))

@bot.message_handler(commands="1")
def cmd_captura_servidor(m):
    if es_admin(m.chat.id):
        print("Capturando la pantalla")
        captura=pyscreenshot.grab()
        print("Guardando la captura")
        captura.save("captura.jpg")
        print("Enviando la captura")
        bot.send_document(m.chat.id, open("captura.jpg", "rb"), caption="captura del servidor")
        print("Eliminando la captura")
        os.remove("captura.jpg")


def es_admin(cid, info=True):
    if cid in ADMINS:
        return True
    else:
        if info:
            print(f'{cid} no esta autorizado')
            bot.send_message(cid, "No estas autorizado", parse_mode="html")
        return False

if __name__=='__main__':
    print("Iniciando el bot...")
    bot.infinity_polling()