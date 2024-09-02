""" Configura el envio de mail y mensajes alertando 
    sobre el traspaso de limites establecidos de temperatura y humedad. 
    
    Además, tiene funciones/metodos que diferencian si enviar mensajes
    debido a la humedadd y/o temperatura . 
    
    returns de las funciones:
        1 -> Indica error.
        0 -> Indica que no se produjeron errores.  
"""
import smtplib, os , ssl #, pickle, requests                                 # Import smtplib for sending function
from dotenv import load_dotenv
from email.message import EmailMessage                                       # Import the email modules we'll need
#from google.oauth2.credentials import Credentials               
#from google_auth_oauthlib.flow import InstalledAppFlow
#from googleapiclient.discovery import build
from json import dumps
from httplib2 import Http

email_sender, email_reciever, password = "", "", ""