from config import *
import telebot
import threading
import time
import re
from telebot.types import ForceReply #Citar un mensaje
#Botones inline
from telebot.types import InlineKeyboardMarkup #Para crear la botonera
from telebot.types import InlineKeyboardButton #Para definir los botones
from conexion import connect_to_db

ADMINS=(8194881876, 7745691115)############################# USUARIOS CON PERMISO
#ADMINS=(8194881876, ) 

bot = telebot.TeleBot(TELEGRAM_TOKEN)

empresas = {} ################################### DATOS PARA UN NUEVO REGISTRO

usuarios = {}

@bot.message_handler(commands=["start"]) #Se definen los comandos, en este caso, los tres comandos harán exactamente lo mismo al estar en una sola lista
def cmd_start(message): #Asi es como definimos la acción que harán estos comandos
    #bot.reply_to(message, "Hola, ¿Cómo estas?") ##### Este es un ejemplo de como responder a mensajes especificos.
    texto = 'Hola, soy'    
    texto += '<b> Practicas ProBot</b>'
    texto += ', tu asistente para encontrar prácticas profesionales.'
    bot.send_chat_action(message.chat.id, "typing")
    msg = bot.send_message(message.chat.id, texto, parse_mode="html")
    time.sleep(1.5)
    bot.send_chat_action(message.chat.id, "typing")
    markup = ForceReply()
    texto = '¿Cómo te gustaría que te llamara?'
    msg = bot.send_message(message.chat.id, texto, reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_nombre)

def preguntar_nombre(message):
    if message.text.isdigit() or message.text.startswith("/"):
        bot.send_chat_action(message.chat.id, "typing")
        msg = bot.send_message(message.chat.id, "Lo siento, no entendí. Ingresa tu nombre, por favor.")
        bot.register_next_step_handler(msg, preguntar_nombre)
    else:
        usuarios[message.chat.id] = {"nombre": message.text.strip()}
        nombre = usuarios[message.chat.id]["nombre"]
        texto = f'Vamos a comenzar. ¿Qué te gustaría hacer {nombre}?\n'
        texto += '1. Consultar las ofertas de prácticas ---> /consultar\n'
        texto += '2. Ingresar una oferta de prácticas ---> /ingresar\n'
        bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=["ingresar"]) #Se definen los comandos, en este caso, los tres comandos harán exactamente lo mismo al estar en una sola lista
def cmd_ingresar(message):
    if es_admin(message.chat.id):
        texto = 'Es importante que sigas las instrucciones al pie de la letra para que tu información sea registrada con exito y que no existan inconvenientes.'
        bot.send_chat_action(message.chat.id, "typing")
        msg = bot.send_message(message.chat.id, texto)
        time.sleep(1.5)
        markup = ForceReply()
        bot.send_chat_action(message.chat.id, "typing")
        texto = '¿Cómo se llama la empresa?'
        msg = bot.send_message(message.chat.id, texto, reply_markup=markup)
        bot.register_next_step_handler(msg, nombre_empresa)

def nombre_empresa(message):
    #Muestra un mensaje con botones inline (Despues del contenido del mensaje)
    botones_carrera = InlineKeyboardMarkup(row_width=1) #Numero de botones por fila, por defecto son 3
    b1 = InlineKeyboardButton("Ingeniería Eléctrica", callback_data=1)
    b2 = InlineKeyboardButton("Ingeniería Electrónica", callback_data=3)
    b3 = InlineKeyboardButton("Ingeniería Sistemas Comp.", callback_data=5)
    b4 = InlineKeyboardButton("Ingeniería Mecánica", callback_data=7)
    b5 = InlineKeyboardButton("Ingeniería Mecatrónica", callback_data=9)
    bcerrar = InlineKeyboardButton("Cerrar", callback_data="cerrar")
    botones_carrera.add(b1,b2,b3,b4,b5, bcerrar)

    if message.text.isdigit() or message.text.startswith("/"): #Aqui estamos dando por sentado que el mensaje solo contiene texto, para condicionar que el mensaje realmente tenga texto agregamos: ' message.text and ... '
        bot.send_chat_action(message.chat.id, "typing")
        msg = bot.send_message(message.chat.id, "Lo siento, no entendí\nIngresa el nombre de la empresa por favor.") #Si el mensaje inicia con '/' y no está deifinido ese comando mandará este mensaje
        bot.register_next_step_handler(msg, nombre_empresa)
    else:
        empresas ["nombre_empresa"] = message.text
        print (empresas)
        time.sleep(1.5)
        bot.send_chat_action(message.chat.id, "typing")
        texto = f'Perfecto, ¿a qué carrera va dirigida esta oferta?.'
        msg = bot.send_message(message.chat.id, texto, reply_markup=botones_carrera)
    

def descripcion_puesto(message):
    if message.text.isdigit() or message.text.startswith("/"): #Aqui estamos dando por sentado que el mensaje solo contiene texto, para condicionar que el mensaje realmente tenga texto agregamos: ' message.text and ... '
        bot.send_chat_action(message.chat.id, "typing")
        msg = bot.send_message(message.chat.id, "Lo siento, no entendí \nIngresa un texto valido") #Si el mensaje inicia con '/' y no está deifinido ese comando mandará este mensaje
        bot.register_next_step_handler(msg, descripcion_puesto)
    else:
        empresas["descripcion"] = message.text
        time.sleep(1)
        bot.send_chat_action(message.chat.id, "typing")
        texto = 'Genial, suena muy interesante.'
        msg = bot.send_message(message.chat.id, texto)
        print(empresas)
        time.sleep(1)
        markup = ForceReply()
        bot.send_chat_action(message.chat.id, "typing")
        texto = 'Cuentame, ¿qué habilidades y caracteristicas debe tener el alumno?'
        texto += '<b>Ejemplo:</b> ' + '<u>(Ingresalos todos separados por comas)</u>' + '\n'
        texto += '<i>   Seguro facultativo, inglés avanzado, promedio minimo 8</i>'
        msg = bot.send_message(message.chat.id, texto, parse_mode="html", reply_markup=markup)
        bot.register_next_step_handler(msg,requisitos)


def requisitos(message):
    if message.text.isdigit() or message.text.startswith("/"): #Aqui estamos dando por sentado que el mensaje solo contiene texto, para condicionar que el mensaje realmente tenga texto agregamos: ' message.text and ... '
        bot.send_chat_action(message.chat.id, "typing")
        msg = bot.send_message(message.chat.id, "Lo siento, no entendí \nIngresa un texto valido") #Si el mensaje inicia con '/' y no está deifinido ese comando mandará este mensaje
        bot.register_next_step_handler(msg, requisitos)
    else:
        empresas["requisitos"] = message.text
        time.sleep(1)
        bot.send_chat_action(message.chat.id, "typing")
        texto = '¡Estupendo, en la UG tenemos gente preparada para todo!'
        msg = bot.send_message(message.chat.id, texto)
        print(empresas)
        time.sleep(1)
        markup = ForceReply()
        bot.send_chat_action(message.chat.id, "typing")
        texto = '¿Existe alguna fecha limite para aplicar?, en caso de que no, contesta "NA"'
        msg = bot.send_message(message.chat.id, texto, reply_markup=markup)
        bot.register_next_step_handler(msg,fecha_limit)
        

def fecha_limit(message):
    if message.text.startswith("/"): #Aqui estamos dando por sentado que el mensaje solo contiene texto, para condicionar que el mensaje realmente tenga texto agregamos: ' message.text and ... '
        bot.send_chat_action(message.chat.id, "typing")
        msg = bot.send_message(message.chat.id, "Lo siento, no entendí \nIngresa una fecha valida") #Si el mensaje inicia con '/' y no está deifinido ese comando mandará este mensaje
        bot.register_next_step_handler(msg, fecha_limit)
    else:
        empresas["fecha_limit"] = message.text
        print(empresas)
        time.sleep(1)
        markup = ForceReply()
        bot.send_chat_action(message.chat.id, "typing")
        texto = 'Entendido, ¿en qué ciudad se cúbica la empresa o área de trabajo?'
        msg = bot.send_message(message.chat.id, texto, reply_markup=markup)
        bot.register_next_step_handler(msg,ciudad)


def ciudad(message):
    if message.text.isdigit() or message.text.startswith("/"): #Aqui estamos dando por sentado que el mensaje solo contiene texto, para condicionar que el mensaje realmente tenga texto agregamos: ' message.text and ... '
        bot.send_chat_action(message.chat.id, "typing")
        msg = bot.send_message(message.chat.id, "Lo siento, no entendí \nIngresa una ciudad valida") #Si el mensaje inicia con '/' y no está deifinido ese comando mandará este mensaje
        bot.register_next_step_handler(msg, ciudad)
    else:
        empresas["ciudad"] = message.text
        print(empresas)
        time.sleep(1)
        bot.send_chat_action(message.chat.id, "typing")
        texto = 'Genial, estoy seguro que a los estudiantes les gustará'
        msg = bot.send_message(message.chat.id, texto)
        time.sleep(1)
        markup = ForceReply()
        bot.send_chat_action(message.chat.id, "typing")
        texto = '¿Me podrías proporcionar la dirección?'
        msg = bot.send_message(message.chat.id, texto, reply_markup=markup)
        bot.register_next_step_handler(msg,direccion)


def direccion(message):
    if message.text.isdigit() or message.text.startswith("/"): #Aqui estamos dando por sentado que el mensaje solo contiene texto, para condicionar que el mensaje realmente tenga texto agregamos: ' message.text and ... '
        bot.send_chat_action(message.chat.id, "typing")
        msg = bot.send_message(message.chat.id, "Lo siento, no entendí \nIngresa una direccion valida") #Si el mensaje inicia con '/' y no está deifinido ese comando mandará este mensaje
        bot.register_next_step_handler(msg, direccion)
    else:
        empresas["direccion"] = message.text
        print(empresas)
        time.sleep(1)
        markup = ForceReply()
        bot.send_chat_action(message.chat.id, "typing")
        texto = 'Registrado!\nFinalmente, ¿podrías proporcionar algun correo de contacto?'
        msg = bot.send_message(message.chat.id, texto, reply_markup=markup)
        bot.register_next_step_handler(msg,correo)


def correo(message):
    if message.text.isdigit() or message.text.startswith("/"): #Aqui estamos dando por sentado que el mensaje solo contiene texto, para condicionar que el mensaje realmente tenga texto agregamos: ' message.text and ... '
        bot.send_chat_action(message.chat.id, "typing")
        msg = bot.send_message(message.chat.id, "Lo siento, no entendí \nIngresa un correo valido") #Si el mensaje inicia con '/' y no está deifinido ese comando mandará este mensaje
        bot.register_next_step_handler(msg, correo)
    else:
        empresas["correo"] = message.text
        print(empresas)
        time.sleep(1)
        bot.send_chat_action(message.chat.id, "typing")
        texto = '<b><i>¡En hora buena!</i></b>' + '\n' + '\n'
        texto += '<b>Resumen de Datos a Introducir:</b>' + '\n'
        texto += f'<code>EMPRESA:</code> {empresas["nombre_empresa"]}\n'
        texto += f'<code>CARRERA DESTINADA:</code> {empresas["carrera"]}\n'
        texto += f'<code>DESCRIPCIÓN:</code> {empresas["descripcion"]}\n'
        texto += f'<code>REQUISITOS:</code> {empresas["requisitos"]}\n'
        texto += f'<code>FECHA LIMITE:</code> {empresas["fecha_limit"]}\n'
        texto += f'<code>CIUDAD:</code> {empresas["ciudad"]}\n'
        texto += f'<code>DIRECCIÓN:</code> {empresas["direccion"]}\n'
        texto += f'<code>CORREO:</code> {empresas["correo"]}\n'
        msg = bot.send_message(message.chat.id, texto, parse_mode="html")
        time.sleep(1)
        markup = ForceReply()
        bot.send_chat_action(message.chat.id, "typing")
        texto = '¿Toda la información es correcta?'
        msg = bot.send_message(message.chat.id, texto, reply_markup=markup)
        bot.register_next_step_handler(msg,respuesta_informacion_correcta)


def respuesta_informacion_correcta(message):
    respuesta2 = message.text.strip().lower() # Ag
    #if message.text != "Si" and message.text != "No": #Aqui estamos dando por sentado que el mensaje solo contiene texto, para condicionar que el mensaje realmente tenga texto agregamos: ' message.text and ... '
    #    bot.send_chat_action(message.chat.id, "typing")
    #    msg = bot.send_message(message.chat.id, 'Lo siento, no entendí \nPor favor responde "Si" o "No"') #Si el mensaje inicia con '/' y no está deifinido ese comando mandará este mensaje
    #    bot.register_next_step_handler(msg, respuesta_informacion_correcta)
    if re.match(r"^si\b|^sí\b|^sip\b|^claro\b|^por supuesto\b", respuesta2, re.IGNORECASE): # AG
    #elif message.text == "Si":
        guardar_en_db(empresas) # Funcion para Guardar
        time.sleep(1)
        bot.send_chat_action(message.chat.id, "typing")
        texto = '<b><i>INFORMACIÓN GUARDADA</i></b>'
        msg = bot.send_message(message.chat.id, texto, parse_mode="html")
        texto = (
            "¿Qué te gustaría hacer?\n"
            "1. Consultar las ofertas de prácticas ---> /consultar\n"
            "2. Ingresar una nueva oferta de prácticas ---> /ingresar\n"
        )
        bot.send_message(message.chat.id, texto)
        return
    elif re.match(r"^no\b|^nop\b", respuesta2, re.IGNORECASE): 
    #elif message.text == "No":
        time.sleep(1)
        markup = ForceReply()
        bot.send_chat_action(message.chat.id, "typing")
        texto = '¿Quieres volver a introducir la información?'
        msg = bot.send_message(message.chat.id, texto, reply_markup=markup)
        bot.register_next_step_handler(msg, corregir_info)
        return
        

def corregir_info(message):
    respuesta3 = message.text.strip().lower() # Ag
    #if  message.text != "Si" and message.text != "No": #Aqui estamos dando por sentado que el mensaje solo contiene texto, para condicionar que el mensaje realmente tenga texto agregamos: ' message.text and ... '
    #    bot.send_chat_action(message.chat.id, "typing")
    #    msg = bot.send_message(message.chat.id, 'Lo siento, no entendí \nPor favor responde "Si" o "No"') #Si el mensaje inicia con '/' y no está deifinido ese comando mandará este mensaje
    #    bot.register_next_step_handler(msg, corregir_info)
    if re.match(r"^si\b|^sí\b|^sip\b|^claro\b|^por supuesto\b", respuesta3, re.IGNORECASE):
    #if message.text == "Si":
        bot.send_chat_action(message.chat.id, "typing")
        texto = 'Introduce el comando: /ingresar'
        msg = bot.send_message(message.chat.id, texto)
    elif re.match(r"^no\b|^nop\b", respuesta3, re.IGNORECASE):
    # elif message.text == "No":
        ######################### AQUI VA LA FUNCION PARA GUARDAR #######################
        time.sleep(1)
        bot.send_chat_action(message.chat.id, "typing")
        texto = '<b><i>INFORMACIÓN GUARDADA</i></b>'
        msg = bot.send_message(message.chat.id, texto, parse_mode="html")
        return

def es_admin(cid, info=True):
    if cid in ADMINS:
        return True
    else:
        if info:
            print(f'{cid} no esta autorizado')
            bot.send_message(cid, "No estas autorizado", parse_mode="html")
        return False

@bot.message_handler(commands=["consultar"])
def cmd_consultar(message):
    nombre = usuarios.get(message.chat.id, {}).get("nombre", "usuario")
    texto = f'¡Vamos en busca del exito, {nombre}!'
    bot.send_message(message.chat.id, texto)
    preguntar_filtro(message.chat.id)

def preguntar_filtro(chat_id):
    #Muestra un mensaje con botones inline (Despues del contenido del mensaje)
    botones_carrera = InlineKeyboardMarkup(row_width=1) #Numero de botones por fila, por defecto son 3
    b1 = InlineKeyboardButton("Ingeniería Eléctrica", callback_data=2)
    b2 = InlineKeyboardButton("Ingeniería Electrónica", callback_data=4)
    b3 = InlineKeyboardButton("Ingeniería Sistemas Comp.", callback_data=6)
    b4 = InlineKeyboardButton("Ingeniería Mecánica", callback_data=8)
    b5 = InlineKeyboardButton("Ingeniería Mecatrónica", callback_data=10)
    bcerrar = InlineKeyboardButton("Cerrar", callback_data="cerrar")
    botones_carrera.add(b1,b2,b3,b4,b5, bcerrar)
    
    bot.send_chat_action(chat_id, "typing")
    texto = "Cuentame, ¿Para qué carrera te gustaría consultar \n las prácticas profesionales disponibles? Selecciona: "
    bot.send_message(chat_id, texto, reply_markup=botones_carrera)

######################################## RESPUESTAS BOTONES ########################################
@bot.callback_query_handler(func=lambda x: True)
def respuesta_botones_inline(call):
    #Gestiona las acciones a realizar al pulsar los botones
    cid = call.from_user.id
    mid = call.message.id
    print(call.data)
    if call.data == "cerrar":
        bot.delete_message(cid, mid)

    opciones1 = {
        2: "Genial, la ingeniería eléctrica tiene mucho potencial, ¿listo para energizar tu futuro?.",
        4: "Estupendo, esta ingeniería tiene un gran circuito de posibilidades, ¿listo para conectar con tu futuro?",
        6: "Excelente, con esta ingeniería será facil decir 'Hello, world!' al mundo profesional",
        8: "Fabuloso, la ingeniería mecánica es la base de muchas industrias, ¿listo para darle fuerza a tu futuro?",
        10: "Increible, la ingeniería mecatrónica es de las más sobresalientes, ¿listo para innovar tu futuro?"
    }
    opciones2 = {
        1: "Ingeniería Eléctrica",
        3: "Ingeniería Electrónica",
        5: "Ingeniería Sistemas Comp.",
        7: "Ingeniería Mecánica",
        9: "Ingeniería Mecatrónica"
    }
    
    if int(call.data) in opciones1 and int(call.data) - 1 in opciones2:
            bot.send_message(cid, opciones1[int(call.data)])
            carrera = opciones2[int(call.data) - 1]
            empresas["carrera"] = carrera
            time.sleep(1.5)
            texto = f'¿Deseas ver las ofertas disponibles actualmente para la carrera de {carrera}? (Puedes responder con "Si" o "No")'
            markup = ForceReply() 
            msg = bot.send_message(cid, texto, reply_markup=markup)
            bot.register_next_step_handler_by_chat_id(cid, procesar_respuesta_oferta)
    else:
            bot.send_message(cid, "Muy bien.")

    if int(call.data) % 2 != 0:
        if int(call.data) in opciones2:
            carrera = opciones2[int(call.data)]
            empresas["carrera"] = carrera
            texto = f'Perfecto, los alumnos de {carrera} estarán muy entusiasmados.'
            msg = bot.send_message(cid, texto)
            print(empresas)
            time.sleep(1)
            markup = ForceReply()
            bot.send_chat_action(cid, "typing")
            texto = '¿Cuál es el nombre del puesto o programa pertenecerá el alumno?\n'
            texto += '<b>Ejemplo:</b> ' + '<u>(Solo ingresa uno)</u>' + '\n'
            texto += '<i>   Practicante en manufactura\n</i>'
            texto += '<i>   Talento joven</i>'
            msg = bot.send_message(cid, texto, parse_mode="html", reply_markup=markup)
            bot.register_next_step_handler(msg,descripcion_puesto)
        else:
            bot.send_message(cid, "Lo siento, carrera no registrada.")
            return

def procesar_respuesta_oferta(message):
    cid = message.from_user.id
    respuesta = message.text.strip().lower()

    if re.match(r"^si\b|^sí\b|^sip\b|^claro\b|^por supuesto\b", respuesta, re.IGNORECASE):
        carrera = empresas.get("carrera", "desconocida")  # Obtener la carrera directamente del diccionario
        bot.send_message(cid, f"¡Muy bien! Ahora te muestro las ofertas actualmente disponibles para la carrera de {carrera}...")
        ### Se agrega la lógica para mostrar las ofertas de la carrera seleccionada
        conexion = connect_to_db()
        if not conexion:
            bot.send_message(cid, "Lo siento, no se pudo conectar a la base de datos. Inténtalo más tarde.")
            return

        try:
            cursor = conexion.cursor()
            query = "SELECT nombre_empresa, descripcion, requisitos, fecha_limit, ciudad, direccion, correo FROM ofertas WHERE carrera = ?"
            cursor.execute(query, (carrera,))
            resultados = cursor.fetchall()

            if resultados:
                for index, row in enumerate(resultados, start=1):
                    nombre_empresa, descripcion, requisitos, fecha_limit, ciudad, direccion, correo = row
                    mensaje = (
                        f" 🔵 <b>Oferta # {index}:</b>\n"
                        f" <code>Empresa:</code> {nombre_empresa}\n"
                        f" <code>Descripción:</code> {descripcion}\n"
                        f" <code>Requisitos:</code> {requisitos}\n"
                        f" <code>Fecha Límite:</code> {fecha_limit}\n"
                        f" <code>Ciudad:</code> {ciudad}\n"
                        f" <code>Dirección:</code>{direccion}\n"
                        f" <code>Correo:</code> {correo}\n\n"
                    )
                    bot.send_message(cid, mensaje, parse_mode="html")
            else:
                bot.send_message(cid, f"No se encontraron ofertas para {carrera} en este momento.")
        except Exception as e:
            bot.send_message(cid, f"Error al consultar las ofertas: {e}")
        finally:
            conexion.close()
        ### Termina logica
        bot.send_chat_action(cid, "typing")
        markup = ForceReply()
        texto = f"¿Te gustaría filtrar estas prácticas mostradas de {carrera} por alguna propiedad? (Puedes responder con 'Si' o 'No')"
        msg = bot.send_message(cid, texto, reply_markup=markup)
        bot.register_next_step_handler(msg, pregunto_propiedad)
    elif re.match(r"^no\b|^nop\b", respuesta, re.IGNORECASE):
        #bot.send_message(cid, "De acuerdo, no se mostrarán las ofertas en este momento.")
        texto = (
            "De acuerdo, no se mostrarán las ofertas en este momento.\n\n"
            "¿Qué te gustaría hacer?\n"
            "1. Consultar las ofertas para otra carrera ---> /consultar\n"
            "2. Ingresar una oferta de prácticas ---> /ingresar\n"
        )
        bot.send_message(cid, texto)
    else:
        bot.send_message(cid, 'Por favor responde con "Si" o "No".')
        bot.register_next_step_handler(message, procesar_respuesta_oferta)  # Esperar nuevamente la respuesta

### Inicia Filtrado por propiedad 
def pregunto_propiedad(message):
    cid = message.from_user.id
    respuesta = message.text.strip().lower()

    if re.match(r"^si\b|^sí\b|^sip\b|^claro\b|^por supuesto\b", respuesta, re.IGNORECASE):
        bot.send_chat_action(cid, "typing")
        markup = ForceReply()
        texto = "¿Por qué propiedad deseas filtrar? (Puedes usar: ciudad, nombre_empresa)"
        msg = bot.send_message(cid, texto, reply_markup=markup)
        bot.register_next_step_handler(msg, solicitar_valor_propiedad)
    elif re.match(r"^no\b|^nop\b", respuesta, re.IGNORECASE):
        texto = (
            "Entendido, no se aplicará ningún filtro adicional.\n\n"
            "¿Qué te gustaría hacer, ahora?\n"
            "1. Consultar las ofertas para otra carrera ---> /consultar\n"
            "2. Ingresar una oferta de prácticas ---> /ingresar\n"
        )
        bot.send_message(cid, texto)
    else:
        bot.send_message(cid, 'Por favor responde con "Si" o "No".')
        bot.register_next_step_handler(message, pregunto_propiedad)

def solicitar_valor_propiedad(message):
    cid = message.from_user.id
    propiedad = message.text.strip().lower()

    # Verificar si la propiedad es válida
    propiedades_validas = ["ciudad", "nombre_empresa",]
    if propiedad not in propiedades_validas:
        bot.send_message(cid, f"La propiedad '{propiedad}' no es válida. Por favor, selecciona una de estas: {', '.join(propiedades_validas)}.")
        bot.register_next_step_handler(message, solicitar_valor_propiedad)
        return

    # Guardar la propiedad seleccionada para usarla en el filtro
    empresas["propiedad_filtrar"] = propiedad
    bot.send_chat_action(cid, "typing")
    markup = ForceReply()
    texto = f"Perfecto, ahora ingresa el valor que deseas buscar para la propiedad '{propiedad}'."
    msg = bot.send_message(cid, texto, reply_markup=markup)
    bot.register_next_step_handler(msg, filtrar_por_propiedad)


def filtrar_por_propiedad(message):
    cid = message.from_user.id
    valor = message.text.strip()
    propiedad = empresas.get("propiedad_filtrar")

    if not propiedad:
        bot.send_message(cid, "Ocurrió un error al intentar filtrar. Por favor, inicia el proceso nuevamente.")
        return

    bot.send_chat_action(cid, "typing")
    bot.send_message(cid, f"Buscando prácticas donde '{propiedad}' sea '{valor}'...")
    conexion = connect_to_db()
    if not conexion:
        bot.send_message(cid, "Lo siento, no se pudo conectar a la base de datos. Inténtalo más tarde.")
        return

    try:
        cursor = conexion.cursor()
        query = f"""
        SELECT nombre_empresa, descripcion, requisitos, fecha_limit, ciudad, direccion, correo 
        FROM ofertas 
        WHERE carrera = ? AND {propiedad} LIKE ?
        """
        carrera = empresas.get("carrera", "desconocida")
        cursor.execute(query, (carrera, f"%{valor}%"))
        resultados = cursor.fetchall()

        if resultados:
            for index, row in enumerate(resultados, start=1):
                nombre_empresa, descripcion, requisitos, fecha_limit, ciudad, direccion, correo = row
                mensaje = (
                    f" 🔴 <b>Oferta Filtrada por {propiedad} # {index}:</b>\n"
                    f" <code>Empresa:</code> {nombre_empresa}\n"
                    f" <code>Descripción:</code> {descripcion}\n"
                    f" <code>Requisitos:</code> {requisitos}\n"
                    f" <code>Fecha Límite:</code> {fecha_limit}\n"
                    f" <code>Ciudad:</code> {ciudad}\n"
                    f" <code>Dirección:</code> {direccion}\n"
                    f" <code>Correo:</code> {correo}\n\n"
                )
                bot.send_message(cid, mensaje, parse_mode="html")
        else:
            bot.send_message(cid, f"No se encontraron prácticas donde '{propiedad}' sea '{valor}' para la carrera seleccionada.")
    except Exception as e:
        bot.send_message(cid, f"Error al filtrar las ofertas: {e}")
    finally:
        conexion.close()
    
    time.sleep(2)
    texto = (
        "Finalemente, ¿Qué te gustaría hacer?\n"
        "1. Consultar ofertas de prácticas profesionales para una nueva carrera ---> /consultar\n"
        "2. Ingresar una nueva oferta de prácticas ---> /ingresar\n"
    )
    bot.send_message(cid, texto)

###################################### FIN DEL CODIGO AGREGADO #############################################


def guardar_en_db(empresas):
    conn = connect_to_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO ofertas
    (nombre_empresa, carrera, descripcion, requisitos, fecha_Limit, ciudad, direccion, correo)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    # Extraemos los valores del diccionario empresas
    values = (
        empresas.get("nombre_empresa", ""),
        empresas.get("carrera", ""),
        empresas.get("descripcion", ""),
        empresas.get("requisitos", ""),
        empresas.get("fecha_limit", ""),
        empresas.get("ciudad", ""),
        empresas.get("direccion", ""),
        empresas.get("correo", "")
    )

    try:
        cursor.execute(query, values)
        conn.commit()  # Guardamos
        print("Información guardada en la base de datos.")
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")
    finally:
        cursor.close()
        conn.close()


############################ BUCLE QUE RECIBE MENSAJES ##################################
def recibir_mensajes():
    bot.infinity_polling()#Bucle infinito que comprueba si llegan mensajes

################################### M A I N ############################################
if __name__ == '__main__':
    #COMANDOS QUE ESTARÁN DISPONIBLES EN NUESTRO BOT
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Da la bienvenida"),
        telebot.types.BotCommand("/consultar", "Consultar las ofertas disponibles"),
        telebot.types.BotCommand("/ingresar", "Ingresar una nueva oferta (Empresas)")
    ])
    print('Iniciando el bot')
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    print('Bot iniciado')