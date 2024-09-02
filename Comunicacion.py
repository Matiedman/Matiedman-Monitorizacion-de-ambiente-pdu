""" Configura el envio de mail y mensajes alertando 
    sobre el traspaso de limites establecidos de temperatura y humedad. 
    
    Además, tiene funciones/metodos que diferencian si enviar mensajes
    debido a la humedadd y/o temperatura . 
    
    returns de las funciones:
        0 -> Indica que no se produjeron errores.  
        Si ha ocurrido un error se imprime un mensaje del mismo y el programa termina.
"""
import smtplib, os , ssl #, pickle, requests                                 # Import smtplib for sending function
import sys
from dotenv import load_dotenv
from email.message import EmailMessage                                       # Import the email modules we'll need
#from google.oauth2.credentials import Credentials               
#from google_auth_oauthlib.flow import InstalledAppFlow
#from googleapiclient.discovery import build
from json import dumps
from httplib2 import Http

email_sender, email_reciever, password = "", "", ""

def emailConfig():
    
    """Configuración del email para enviar mensajes y correos"""
    try:        
        load_dotenv() # Se carga el archivo .env o se lo llama para que sea usado. 
        global email_sender, email_reciever, password

        # Se guardan el mail con remitente, destinatario. 
        email_sender = "alertas.iaas@psi.unc.edu.ar"
        password = os.getenv('PASSWORD')                           # Se accede al .env y se busca el valor de "PASSWORD".
        if password == None:
            raise NameError('Contraseña vacía, verificar que en el archivo .env esté escrita la misma o bien exista el archivo dentro del directorio. ')
        
        email_reciever = "psi.iaas@unc.edu.ar"                     # Luego de hacerle las pruebas al programa, reemplazar este campo con "psi.iaas@unc.edu.ar"
    except NameError as exception:                                 # manejo de la excepcion 'NameError'.
        print(f"Se produjo el siguiente error: {exception} El programa terminará. ")
        sys.exit(0)                                             
    except Exception as generalExcept:                             # manejo general de otras excepciones.  
        print(f"Ocurrió un error inesperado: {generalExcept}. El programa terminará. ")
        sys.exit(0)                      
    else:
        return 0                                                      

# Se envian mails alertando sobre un evento ambiental ocurrido. Puede ser haber pasado los limites de humedad o temperatura.
def sendEmailsToAlertForHumi(humiData, sector):

    """ Envio de emails para alertar sobre algun envento de humedad.
    
    Funcion que crea el asunto, cuerpo del email a enviar para alertar sobre eventos ocurridos con la humedad. 
    Segun el limite traspasadao, notifica si fue menor o mayor el valor registrado. 
    """
    sendMsgsAlert("humi", sector)

    subject  = "ALERTA! La humedad pasó los limites establecidos."
    
    # Lo que sigue es la construccion del cuerpo del msj a enviar. Se puede hacer en HTML. Tambien se pueden añadir imágenes. 
    if humiData < 25:
        if sector == "sectorA":
            body = "La humedad esta a menos del 25% en el sector A. Al momento de este email marcó " + str(humiData) + "%. Realizar las acciones pertinentes. "
        if sector == "sectorB":
            body = "La humedad esta a menos del 25% en el sector B. Al momento de este email marcó " + str(humiData) + "%. Realizar las acciones pertinentes. "     
    
    else:
        if sector == "sectorA":
            body = "La humedad esta a más del 90% en el sector A. Al momento de este email marcó " + str(humiData) + "%. Realizar las acciones pertinentes. "
        if sector == "sectorB":
            body = "La humedad esta a más del 90% en el sector B. Al momento de este email marcó " + str(humiData) + "%. Realizar las acciones pertinentes. "
    
    try:
        # Se crea el mail  asunto, y cuerpo del mensaje.
        theEmail = EmailMessage()                                         # Se inicializa el objeto email para luego cargar los parametros.
        theEmail["From"] = email_sender
        theEmail["To"] = email_reciever
        theEmail["Subject"] = subject
        theEmail.set_content(body)
        contexto = ssl.create_default_context()                           # Se crea un contexto o canal seguro para la comunicacion por defecto.

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = contexto) as smtp:   # Se accede al servidor, en este caso al de gmail.
            smtp.login(email_sender, password)                                      # Se loguea para enviar el email.
            smtp.sendmail(email_sender, email_reciever, theEmail.as_string())       # Se envía el mail        
    except ssl.SSLError as exception:                              # manejo de la excepcion 'NameError'.
        print(f"Se produjo el siguiente error: {exception}. El programa terminará. ")
        sys.exit(0)                                                   
    except Exception as generalExcept:                             # manejo general de otras excepciones.
        print(f"Ocurrió un error inesperado: {generalExcept}. El programa terminará. ")
        sys.exit(0)
    else:
        return 0                                                                                                 

def sendEmailsToAlertForTemp(tempData, sector):

    """ Envio de emails para alertar sobre algun envento de temperatura.
    
    Funcion que crea el asunto, cuerpo del email a enviar para alertar sobre eventos ocurridos con la temperatura. 
    Segun el limite traspasadao, notifica si fue menor o mayor el valor registrado y su valor.
    
    Es mas especifica que la funcion sendMsgsAlert(msg), que es general. 
    """
    
    sendMsgsAlert("temp", sector)

    subject  = "ALERTA! La temperatura pasó los limites establecidos"
    # Lo que sigue es la construccion del cuerpo del msj a enviar. Se puede hacer en HTML. Tambien se pueden añadir imágenes. 
    if tempData < 12:
        if sector == "sectorA":
            body = "La temperatura esta a menos de 12ºC en el sector A. Al momento de este email marcó " + str(tempData) + "ºC. Realizar las acciones pertinentes. "
        if sector == "sectorB":
            body = "La temperatura esta a menos de 12ºC en el sector B. Al momento de este email marcó " + str(tempData) + "ºC. Realizar las acciones pertinentes. "
    else:
        if sector == "sectorA":
            body = "La temperatura esta a mas de 20ºC en el sector A. Al momento de este email marcó " + str(tempData) + "ºC. Realizar las acciones pertinentes. "
        if sector == "sectorB":
            body = "La temperatura esta a mas de 20ºC en el sector B. Al momento de este email marcó " + str(tempData) + "ºC. Realizar las acciones pertinentes. "
    
    try:  
        theEmail = EmailMessage()                                         # Se inicializa el objeto email para luego cargar los parametros.
        theEmail["From"] = email_sender
        theEmail["To"] = email_reciever
        theEmail["Subject"] = subject
        theEmail.set_content(body)
        contexto = ssl.create_default_context()                           # Se crea un contexto o canal seguro para la comunicacion por defecto.

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = contexto) as smtp:   # Se accede al servidor, en este caso al de gmail.
            smtp.login(email_sender, password)                                      # Se loguea para enviar el email.
            smtp.sendmail(email_sender, email_reciever, theEmail.as_string())       # Se envía el mail        
    except ssl.SSLError as exception:                              # manejo de la excepcion 'NameError'.
        print(f"Se produjo el siguiente error: {exception}. El programa terminará. ") # El programa seguirá funcionando pero no podrá comunicar inconvenientes vía email y chat. ")
        sys.exit(0)                                                   
    except Exception as generalExcept:                             # manejo general de otras excepciones.
        print(f"Ocurrió un error inesperado: {generalExcept}. El programa terminará. ") # El programa seguirá funcionando pero no podrá comunicar inconvenientes vía email y chat. ")
        sys.exit(0) 
    else:     
        return 0
    
# Se envian las alertas por medio del chat de Google. 
def sendMsgsAlert(msg, sector):
    
    """ Metodo que envia alertas por mensajes mediante webhooks al espacio de Infraestructura en Google. 
    
    Se envian mensajes al espacio de Infraestrucutra alertando sobre cambios limites segun sea por temperatura o humedad. 
    Es un mensaje gral. que solo alerta mas no indica el dato ambiental. 
    
    Este método es mas general que aquellos que envian mails de temperatura y humedad donde se especifica el valor que disparó la alerta. 
    """

    # """Google Chat incoming webhook."""

    # Se crea el contexto. 
    url = os.getenv('PASSWORDCHAT')                           # Se accede al .env y se busca el valor de "PASSWORDCHAT"
    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    http_obj = Http()
    
    if msg == "humi":
        if sector == "sectorA":
            app_message = {"text": "¡¡¡ATENCIÓN!!!. Se ha pasado el limite establecido de humedad en el sector A del DC Campus Virtual. Realizar acciones necesarias. "}
            
        if sector == "sectorB":
            app_message = {"text": "¡¡¡ATENCIÓN!!!. Se ha pasado el limite establecido de humedad en el sector B del DC Campus Virtual. Realizar acciones necesarias. "}
    
    if msg == "temp":
        if sector == "sectorA":
            app_message = {"text": "¡¡¡ATENCIÓN!!!. Se ha pasado el limite establecido de temperatura en el sector A del DC Campus Virtual. Realizar acciones necesarias. "}

        if sector == "sectorB":
            app_message = {"text": "¡¡¡ATENCIÓN!!!. Se ha pasado el limite establecido de temperatura en el sector B del DC Campus Virtual. Realizar acciones necesarias. "}
           
    http_obj.request(uri=url, method="POST", headers=message_headers, body=dumps(app_message), )
    return 0
    
    
    #Mensaje por defecto:    
    # app_message = {"text": "¡¡¡ATENCIÓN!!!. Se le ha enviado un email alertando sobre el traspaso de los limites establecidos de temperatura y/o humedad."}
    # http_obj.request(uri=url, method="POST", headers=message_headers, body=dumps(app_message), )
    # return 0