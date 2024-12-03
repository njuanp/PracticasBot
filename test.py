from config import *
import telebot
import time
import threading

bot = telebot.TeleBot(TELEGRAM_TOKEN)

#CONSIDERACIONES:
'''
1. En mensajes normales donde solo enviamos texto, podremos enviar hasta 4096 caracteres.
2. En mensajes con imagenes solo podremos enviar un maximo de 1024 caracteres en el caption.
3. Hay más metodos para enviar diferentes cosas ademas de solo mensajes de texto, no solo imagenes, videos y archivos.
'''

@bot.message_handler(commands=["start", "ayuda", "help"]) #Se definen los comandos, en este caso, los tres comandos harán exactamente lo mismo al estar en una sola lista
def cmd_start(message): #Asi es como definimos la acción que harán estos comandos
    bot.reply_to(message, "Hola, ¿Cómo estas?")
    print(message.chat.id)

#ESPECIFICACIÓN DEL MESNAJE ENVIADO POR EL USUARIO
@bot.message_handler(content_types=["text"]) #El mensaje solo contiene texto, si queremos agregar otro tipo de mesnaje agregamos a la lista el tipo de mensaje enviado: ' , "photo" '

def bot_mensajes_texto(message):
    #FORMATOS EN HTML
    texto_html = '<b> NEGRITA </b>' + '\n' #Negrita en HTML
    texto_html += '<i> CURSIVA </i>' + '\n' #Cursiva en HTML
    texto_html += '<u> SUBRAYADO </u>' + '\n' #Subrayar en HTML
    texto_html += '<s> TACHADO </s>' + '\n' #Tachado en HTML
    texto_html += '<code> MONOESPACIADO </code>' + '\n' #Monoespaciado en HTML
    texto_html += '<a href="https://www.youtube.com/"> ENLACE </a>' + '\n' #Enlace en HTML
    texto_html += '<b><u> Anidar </u> formatos </b>' + '\n' #Tambien podemos anidar formatos
    #FORMATOS MARKDOWNV2
    texto_markdown = '*NEGRITA*' + '\n'
    texto_markdown += '_CURSIVA_' + '\n'
    texto_markdown += '__SUBRAYADO__' + '\n'
    texto_markdown += '~TACHADO~' + '\n'
    texto_markdown += '```MONOESPACIADO```' + '\n'
    texto_markdown += '[ENLACE](https://www.youtube.com/)' + '\n'
    texto_markdown += '*__Anidar__ formatos *' + '\n'

    if message.text.startswith("/"): #Aqui estamos dando por sentado que el mensaje solo contiene texto, para condicionar que el mensaje realmente tenga texto agregamos: ' message.text and ... '
        bot.send_message(message.chat.id, "Lo siento, no entendí :(") #Si el mensaje inicia con '/' y no está deifinido ese comando mandará este mensaje
    else:
        #ENVIAR MENSAJES CON FORMATO
        '''
        bot.send_message(message.chat.id, texto_html, parse_mode="html") #Si queremos desabilitar la vista previa del enlace agregamos el parametro: ', disable_web_page_preview=True' 
        bot.send_message(message.chat.id, texto_markdown, parse_mode="MarkdownV2") #Si queremos desabilitar la vista previa del enlace agregamos el parametro: ', disable_web_page_preview=True'         
        '''
        #INFORMACIÓN DE LA ACCIÓN QUE ESTÁ REALIZANDO EL BOT
        '''
        'typing'#Escribiendo, 'upload_photo'#Cargando foto,
        'record_video'#Grabando video, 'upload_video'#Cargando video,
        'record_audio'#Grabando audio, 'upload_audio'#Cargando audio,
        'upload_document'#Cargando documento, 'find_location'#Buacando ubicacion,
        'record_video_note'#Grabando nota de video,
        'upload_video_note'#Cargando nota de video
        '''
        bot.send_chat_action(message.chat.id, "typing")#Así definimos que es lo que queremos poner y la linea siguiente será el mensaje que enviaremos
        

        #ENVIAR DOCUMENTOS MULTIMEDIA (PDF, IMAGENES, VIDEOS)
        '''
        foto = open("./media/pikachu.jpg", "rb") #Arimos la foto que queremos enviar
        bot.send_photo(message.chat.id, foto, "PIKA PIKA!!") #Enviamos la foto con un caption

        documento = open("Proyecto final.pdf", "rb") #Abrimos el archivo que queremos enviar
        bot.send_document(message.chat.id, documento, caption="¿De que se trata este bot?") #Enviamos el archivo con un caption
        
        video = open("./media/OSG Login 2024-06-01 20-14-35.mp4", "rb") #Arimos el video que queremos enviar
        bot.send_video(message.chat.id, video, caption="Otro de mis proyectos") #Enviamos el video con un caption
        '''
        
        #ASIGNAR EL VALOR DEL ID A UNA VARIABLE
        x = bot.send_message(message.chat.id, "Hi")

        #EDITAR, ELIMINAR MENSAJES Y TIMING PARA ACCIONES
        '''
        time.sleep(3) #Espera 3 seg para ejecutar la siguiente acción
        bot.edit_message_text("Hello", message.chat.id, x.message_id) #Editar mensajes con el ID del mensaje

        time.sleep(3) #Espera 3 seg para ejecutar la siguiente acción
        bot.delete_message(message.chat.id, x.message_id) #Eliminar mensajes con el ID del mensaje

        time.sleep(3) #Espera 3 seg para ejecutar la siguiente acción
        bot.delete_message(message.chat.id, message.message_id) #Eliminar mensajes enviados por el usuario con el ID del mensaje
        '''
#FUNCION QUE COMPRUEBA EL RECIBIMIENTO DE MENSAJES
def recibir_mensajes():
    bot.infinity_polling()#Bucle infinito que comprueba si llegan mensajes

##################### M A I N ##################################
if __name__ == '__main__':
    #COMANDOS QUE ESTARÁN DISPONIBLES EN NUESTRO BOT
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Da la bienvenida"),
        telebot.types.BotCommand("/boom", "Explotaremos!!")
    ])
    print('Iniciando el bot')
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    print('Bot iniciado')
    bot.send_message(CID_CANAL_PRUEBAS, "ola k ac")#Enviar mensaje desde el bot sin que el usuario haya enviado un mensaje

