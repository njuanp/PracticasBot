from config import *
import telebot
from telebot.types import ReplyKeyboardMarkup #Para crear botones
from telebot.types import ForceReply #Citar un mensaje
from telebot.types import ReplyKeyboardRemove

empresa = {}

bot = telebot.TeleBot(TELEGRAM_TOKEN)
usuarios = {}

@bot.message_handler(commands=['start', 'ayuda', 'help']) #Se definen los comandos, en este caso, los tres comandos harán exactamente lo mismo al estar en una sola lista
def cmd_start (message): #Asi es como definimos la acción que harán estos comandos
    markup = ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Usa el comando: /alta para introducir tus datos", reply_markup=markup)

@bot.message_handler(commands=['alta'])
def cmd_alta (message): 
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "¿Cómo te llamas?", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_edad)

def preguntar_edad (message):
    usuarios[message.chat.id] = {}
    usuarios[message.chat.id]["nombre"] = message.text
    empresa["nombre"] = message.text
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "¿Cuántos años tienes?", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_sexo)
    
def preguntar_sexo (message):
    if not message.text.isdigit():
        markup = ForceReply()
        msg = bot.send_message(message.chat.id, "ERROR: Debes indicar un numero. \n¿Cuántos años tienes?")
        bot.register_next_step_handler(msg, preguntar_sexo)
    else:
        usuarios[message.chat.id]["edad"] = int(message.text)
        empresa["edad"] = int(message.text)
        markup = ReplyKeyboardMarkup(
            one_time_keyboard=True, 
            input_field_placeholder="Pulsa un botón",
            resize_keyboard=True,
            row_width=1
            )
        #markup.add("Hombre", "Mujer")
        markup.row('Hombre')
        markup.row('Mujer')

        msg = bot.send_message(message.chat.id, "¿Cuál es tu sexo?", reply_markup=markup)
        bot.register_next_step_handler(msg, guardar_datos_usuarios)

def guardar_datos_usuarios (message):
    if message.text != "Hombre" and message.text != "Mujer":
        msg = bot.send_message(message.chat.id, 'ERROR: Sexo no válido. \nPulsa un botón')
        bot.register_next_step_handler(msg, guardar_datos_usuarios)
    else:
        usuarios[message.chat.id]["sexo"] = message.text
        empresa["sexo"] = message.text
        texto = 'Datos introducidos:\n'
        texto += f'<code>NOMBRE:</code> {usuarios[message.chat.id]["nombre"]}\n'
        texto += f'<code>EDAD:</code> {usuarios[message.chat.id]["edad"]}\n'
        texto += f'<code>SEXO:</code> {usuarios[message.chat.id]["sexo"]}\n'
        markup = ReplyKeyboardRemove()
        bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
        print(usuarios)
        del usuarios[message.chat.id]
        print(usuarios)
        print (empresa)



if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
