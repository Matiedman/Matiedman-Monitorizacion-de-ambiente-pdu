""" Se definen los pdu de los sectores A y B del data center. Se establecen los nombres de los dispositivos.
Se obtienen los datos ambientales y se los guarda en diccionarios junto con su pdu correspondiente para su posterior uso.
Se crean diccionarios para manejar los valores segun dispositivos."""

from easysnmp import Session
#from CreacionDato import *
import CreacionDato 

SApduRxSession = [] # Array de elementos de las diferentes sesiones de los PDU en los Rx del sector A. 
SBpduF1Session = [] # Array de elementos de las diferentes sesiones de los PDU de la fila 1 del sector B. 
SBpduF2Session = [] # Array de elementos de las diferentes sesiones de los PDU de la fila 2 del sector B. 

SaKeyValueTemp = {}     # Contiene los elementos que almacenan datos "llave-valor" respecto a la temperatura de los diferentes dispositivos según área.
SbF1KeyValueTemp = {}
SbF2KeyValueTemp = {}
SaKeyValueHumi = {}     # Contiene los elementos que almacenan datos "llave-valor" respecto a la humedad de los diferentes dispositivos segun área.
SbF1KeyValueHumi = {}
SbF2KeyValueHumi = {}

saRxNameTemp = []        # Los siguientes elementos contienen los nombres de cada dispositivo según área para su temperatura y humedad.
sbF1RxpduNameTemp = []  
sbF2RxpduNameTemp = []

saRxNameHumi = []
sbF1RxpduNameHumi = []
sbF2RxpduNameHumi = []

saRxPduDatoTemp = []    # Los siguientes elementos contienen los datos de temperatura y humedad correspondiente a cada dispositivo según área. 
sbF1RxPduDatoTemp = []
sbF2RxPduDatoTemp = []

saRxPduDatoHumi = []
sbF1RXPduDatoHumi = []
sbF2RXPduDatoHumi = []

def pduDefinitions():
    
    """Función que carga las sesiones de cada pdu según rack, fila y sector del DC en distintas variables con nombre asociado  
       y luego en un array que los une por area y fila."""
    
    global SApduRxSession, SBpduF1Session, SBpduF2Session   # Esto indica que se hace referencia a la misma variable global antes declarada. 

    #-----------------------------------------------SECTOR A-------------------------------------------------------------#

    # En el sector A luego de debuggear ha salido para la sesion del R6 el siguiente error:
        # easysnmp.exceptions.EasySNMPTimeoutError: timed out while connecting to remote host
    

    saR1pduSession = Session(hostname='sar1pdu.psi.unc.edu.ar', community='publiceaton', version=1) 
    # saR2pduSession = Session(hostname='sar2pdu.psi.unc.edu.ar', community='publiceaton', version=1) # ---> r2 y r3 ESTAN DESCONECTADOS
    # saR3pduSession = Session(hostname='sar3pdu.psi.unc.edu.ar', community='publiceaton', version=1)
    saR4pduSession = Session(hostname='sar4pdu.psi.unc.edu.ar', community='publiceaton', version=1) 
    saR5pduSession = Session(hostname='sar5pdu.psi.unc.edu.ar', community='publiceaton', version=1) 
    saR6pduSession = Session(hostname='sar6pdu.psi.unc.edu.ar', community='publiceaton', version=1)
  
    SApduRxSession = [saR1pduSession, saR4pduSession, saR5pduSession, saR6pduSession] #[saR2pduSession, saR3pduSession, ]
    # Una vez reparado todos los erroes, descomentar las lineas y hacer el mismo procedimiento para probarlos. Debuggear.     

    #-----------------------------------------------SECTOR B-------------------------------------------------------------#
    sbF1R1pduSession = Session(hostname='sbf1r1pdu.psi.unc.edu.ar', community='publiceaton', version=1)
    sbF1R2pduSession = Session(hostname='sbf1r2pdu.psi.unc.edu.ar', community='publiceaton', version=1)
    sbF1R3pduSession = Session(hostname='sbf1r3pdu.psi.unc.edu.ar', community='publiceaton', version=1)
    sbF1R4pduSession = Session(hostname='sbf1r4pdu.psi.unc.edu.ar', community='publiceaton', version=1)
    sbF1R5pduSession = Session(hostname='sbf1r5pdu.psi.unc.edu.ar', community='publiceaton', version=1)

    sbF2R1pduSession = Session(hostname='sbf2r1pdu.psi.unc.edu.ar', community='publiceaton', version=1)
    sbF2R2pduSession = Session(hostname='sbf2r2pdu.psi.unc.edu.ar', community='publiceaton', version=1)
    sbF2R3pduSession = Session(hostname='sbf2r3pdu.psi.unc.edu.ar', community='publiceaton', version=1)
    sbF2R4pduSession = Session(hostname='sbf2r4pdu.psi.unc.edu.ar', community='publiceaton', version=1)
    sbF2R5pduSession = Session(hostname='sbf2r5pdu.psi.unc.edu.ar', community='publiceaton', version=1)

    SBpduF1Session = [sbF1R1pduSession, sbF1R2pduSession, sbF1R3pduSession, sbF1R4pduSession, sbF1R5pduSession]    
    SBpduF2Session = [sbF2R1pduSession, sbF2R2pduSession, sbF2R3pduSession, sbF2R4pduSession, sbF2R5pduSession]

    #-----------------------------------------------SECTOR C (en construccion)--------------------------------------------#
    #######################################################################################################################

def deviceConfigName():

    """Creación de diccionarios para almacenar los valores de temperatura y humedad como "Clave: Valor"."""

    global saRxNameTemp, sbF1RxpduNameTemp, sbF2RxpduNameTemp, saRxNameHumi, sbF1RxpduNameHumi, sbF2RxpduNameHumi

    # Lista de temperatura por area:
    saRxNameTemp = ["saR1pduTemp", "saR4pduTemp", "saR5pduTemp", "saR6pduTemp"] # ["saR2pduTemp", "saR3pduTemp"] Estas faltan conectar.  
    sbF1RxpduNameTemp = ["sbF1R1pduTemp", "sbF1R2pduTemp", "sbF1R3pduTemp", "sbF1R4pduTemp", "sbF1R5pduTemp"] # Falta continuar hasta el R10]  
    sbF2RxpduNameTemp = ["sbF2R1pduTemp", "sbF2R2pduTemp", "sbF2R3pduTemp", "sbF2R4pduTemp", "sbF2R5pduTemp"] # Falta continuar hasta el R10]

    # Lista de humedad por area:
    saRxNameHumi = ["saR1pduHumi", "saR4pduHumi", "saR5pduHumi", "saR6pduHumi"] # ["saR2pduHumi", "saR3pduHumi"]  Estas faltan conectar.
    sbF1RxpduNameHumi = ["sbF1R1pduHumi", "sbF1R2pduHumi", "sbF1R3pduHumi", "sbF1R4pduHumi", "sbF1R5pduHumi"] # Falta continuar hasta el R10]
    sbF2RxpduNameHumi = ["sbF2R1pduHumi", "sbF2R2pduHumi", "sbF2R3pduHumi", "sbF2R4pduHumi", "sbF2R5pduHumi"] # Falta continuar hasta el R10]
    
def tempHumiDataCreate():
    
    """Creación y obtención de los datos de temperatura y humedad."""
    
    # Creacion de los datos de temperatura:
    for SaRx in SApduRxSession:
        saRxPduDatoTemp.append(CreacionDato.getTemperature(SaRx))      # Con el metodo append() se van agregando elementos al final de la lista. 
    
    for SbF1Rx in SBpduF1Session:
        sbF1RxPduDatoTemp.append(CreacionDato.getTemperature(SbF1Rx))      
    
    for SbF2Rx in SBpduF2Session:
        sbF2RxPduDatoTemp.append(CreacionDato.getTemperature(SbF2Rx))     

    # Creacion de los datos de humedad:
    for SaRx in SApduRxSession:
        saRxPduDatoHumi.append(CreacionDato.getHumidity(SaRx))         
    
    for SbF1Rx in SBpduF1Session:
        sbF1RXPduDatoHumi.append(CreacionDato.getHumidity(SbF1Rx))      
    
    for SbF2Rx in SBpduF2Session:
        sbF2RXPduDatoHumi.append(CreacionDato.getHumidity(SbF2Rx))   
 
def sxFxRxKey_value():

    """A partir de las listas creadas, se harán diccionarios para manejar los valores segun el dispositivo (clave-valor)."""

    global SaKeyValueTemp, SbF1KeyValueTemp, SbF2KeyValueTemp, SaKeyValueHumi, SbF1KeyValueHumi, SbF2KeyValueHumi

    # Las siguientes lineas crean diccionarios a partir de dos listas (sxRxNameTemp y sxRxPduDatoTemp), donde las claves son los elementos de la primera lista 
    # y los valores son los elementos correspondientes de la segunda lista. 
    
    # Contiene los elementos que almacenan datos "llave-valor" respecto a la temperatura de los diferentes dispositivos según área.
    SaKeyValueTemp = {saRxNameTemp:saRxPduDatoTemp for (saRxNameTemp, saRxPduDatoTemp) in zip(saRxNameTemp, saRxPduDatoTemp)} 
    SbF1KeyValueTemp = {sbF1RxpduNameTemp:sbF1RxPduDatoTemp for (sbF1RxpduNameTemp, sbF1RxPduDatoTemp) in zip(sbF1RxpduNameTemp, sbF1RxPduDatoTemp)}
    SbF2KeyValueTemp = {sbF2RxpduNameTemp:sbF2RxPduDatoTemp for (sbF2RxpduNameTemp, sbF2RxPduDatoTemp) in zip(sbF2RxpduNameTemp, sbF2RxPduDatoTemp)}
    
    # Contiene los elementos que almacenan datos "llave-valor" respecto a la humedad de los diferentes dispositivos segun área.
    SaKeyValueHumi = {saRxNameHumi:saRxPduDatoHumi for (saRxNameHumi,saRxPduDatoHumi) in zip(saRxNameHumi, saRxPduDatoHumi)}    
    SbF1KeyValueHumi = {sbF1RxpduNameHumi:sbF1RXPduDatoHumi for (sbF1RxpduNameHumi, sbF1RXPduDatoHumi) in zip(sbF1RxpduNameHumi, sbF1RXPduDatoHumi)}
    SbF2KeyValueHumi = {sbF2RxpduNameHumi:sbF2RXPduDatoHumi for (sbF2RxpduNameHumi, sbF2RXPduDatoHumi) in zip(sbF2RxpduNameHumi, sbF2RXPduDatoHumi)}