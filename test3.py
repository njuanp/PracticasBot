from config import *
import telebot
#Botones inline
from telebot.types import InlineKeyboardMarkup #Para crear la botonera
from telebot.types import InlineKeyboardButton #Para definir los botones

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['botones'])
def cmd_botones(message):
    #Muestra un mensaje con botones inline (Despues del contenido del mensaje)
    markup = InlineKeyboardMarkup(row_width=2) #Numero de botones por fila, por defecto son 3
    b1 = InlineKeyboardButton("Amazon", url="https://www.amazon.com.mx/")
    b2 = InlineKeyboardButton("Mercado", url="https://www.mercadolibre.com.mx/")
    b3 = InlineKeyboardButton("YouTube", url="https://www.youtube.com/")
    b4 = InlineKeyboardButton("Facebook", url="https://www.facebook.com/")
    b5 = InlineKeyboardButton("Gmail", url="https://www.amazon.com.mx/")
    bcerrar = InlineKeyboardButton("Cerrar", callback_data="cerrar")
    markup.add(b1,b2,b3,b4,b5,b2, bcerrar)
    bot.send_message(message.chat.id, "Mis paginas favs:", reply_markup=markup)

@bot.callback_query_handler(func=lambda x: True)
def respuesta_botones_inline(call):
    #Gestiona las acciones a realizar al pulsar los botones
    cid = call.from_user.id
    mid = call.message.id
    if call.data == "cerrar":
        bot.delete_message(cid, mid)




if __name__ == '__main__':
    print("Iniciando bot")
    bot.infinity_polling()
