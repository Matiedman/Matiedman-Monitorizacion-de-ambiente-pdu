#!/usr/bin/python3             

"""
    Este modoulo inicia el procesamiento de los datos ambientales del DC del campus virtual.
"""

import Configuraciones
from Configuraciones import *
from Operaciones import saPromedioTemp, saPromedioHumi, sbPromedioHumi, sbPromedioTemp, saLeftLimitTemp, saLeftLimitHumi,  sbLeftLimitTemp, sbLeftLimitHumi
from Comunicacion import sendEmailsToAlertForHumi, sendEmailsToAlertForTemp, emailConfig
from CreacionDato import *
# from easysnmp import Session, snmp_get, snmp_walk


promTempSa, promTempSb, promTempSc, promHumiSa, promHumiSb, promHumiSc = 0, 0, 0, 0, 0, 0
leftEndTempSa, rightEndTempSa, leftEndTempSb, rightEndTempSb, leftEndTempSc, rightEndTempSc = 0, 0, 0, 0, 0, 0 
leftEndHumiSa, rightEndHumiSa, leftEndHumiSb, rightEndHumiSb, leftEndHumiSc, rightEndHumiSc = 0, 0, 0, 0, 0, 0

 
def main():
    """
    Funcion principal que crea configuraciones para poder operar el programa,
    crea los datos te temperatura y humedad, se crean los direccionarios
    para manejar los datos anteriores mediante nomeclatura 'Llave: valor', 
    Se obtiene el promedio de temperatura y humedad asi como el promedio del 
    lateral izquierdo. 
    
    Seguidamente se imprime por pantalla los datos buscados que son:
    
    Promedio de temperatura y humedad del sector A y B.
    Promedio de temperatura y humedad del lateral izqquierdo del sector A y B
    
    Functions:  
                configCreate()
                tempHumiDataCreate()
                sxFxRxKey_value() 
                getProm()
                getEdgeData()
    """
    
    configCreate()                   # Se crean las configuraciones de los objetos para obtener los datos de temperatura y humedad. 
    tempHumiDataCreate()             # Creacion del dato. 
    sxFxRxKey_value()                # Se crean diccionarios para menejar los datos de la anterior funcion mediante el esquema "Llave: Valor". Esta funcion se repite para actualizar valores.
    getProm()                        # Obtencion de promedios
    getEdgeData()               

    # Se imprimen los datos. Esta forma de impresion es para que Grafana los pueda tomar y visualizarlos, ya que es su formato.
    print("PDUenvironmentSa,name=Temp Temp=" + str(promTempSa))
    print("PDUenvironmentSa,name=Humi Humi=" + str(promHumiSa))
    print("PDUenvironmentSa,name=Temp LeftTemp=" + str(leftEndTempSa))
    print("PDUenvironmentSa,name=Humi LeftHumi=" + str(leftEndHumiSa))
    print("PDUenvironmentSb,name=Temp Temp=" + str(promTempSb))
    print("PDUenvironmentSb,name=Humi Humi=" + str(promHumiSb))
    print("PDUenvironmentSb,name=Temp LeftTemp=" + str(leftEndTempSb))
    print("PDUenvironmentSb,name=Humi LeftHumi=" + str(leftEndHumiSb))

   
def configCreate():

    """
    Función que definie los pdu, configura los nombres de los dispositivos, se crean los datos de humedad y temeperatura,
    se crean diccionarios para emplear los datos anteriores como "llave: valor", se configura el email. 
    """
    pduDefinitions()
    deviceConfigName()
    emailConfig()

def getProm(): 

    """
    Se obtiene el promedio de temperatura y humedad los sectores A y B.
    Además verifica los valores y si sobrepasan los limites se enviaran alertas. 
    """
    global promTempSa, promTempSb, promTempSc, promHumiSa, promHumiSb, promHumiSc
   
    promTempSa = saPromedioTemp(Configuraciones.SaKeyValueTemp) 
    promHumiSa = saPromedioHumi(Configuraciones.SaKeyValueHumi) 
    saTempHumiCheck(promTempSa, promHumiSa)
    
    promTempSb = sbPromedioTemp(Configuraciones.SbF1KeyValueTemp, Configuraciones.SbF2KeyValueTemp) 
    promHumiSb = sbPromedioHumi(Configuraciones.SbF1KeyValueHumi, Configuraciones.SbF2KeyValueHumi) 
    sbTempHumiCheck(promTempSb, promHumiSb)
   
    # promTempSc = Operaciones.scPromedioTemp(Configuraciones.ScF1KeyValueTemp, Configuraciones.ScF2KeyValueTemp) -> Hay que crear el diccionario. 
    # promHumiSc = Operaciones.scPromedioHumi(Configuraciones.ScF1KeyValueHumi, Configuraciones.ScF2KeyValueHumi)
    
    # Se actualizan los archivos txt de los tres sectores con los datos obtenidos. Se comentan ya que no hace falta por el momento.
    # saUpdateFileTXT(promHumiSa, promTempSa)
    # sbUpdateFileTXT(promHumiSb, promTempSb)  
    # scUpdateFileTXT(promHumiSc, promTempSc) ->  Este aun no está implementado fisicamente. 
    

def getEdgeData():
    
    """
    Se obtienen los promedios de los laterales izquierdos de humedad y temperatura de ambos sectores. 
    Está como opcion generar un registro mediante .txt, no está implementada. 
    """

    global leftEndTempSa, rightEndTempSa, leftEndTempSb, rightEndTempSb, leftEndTempSc, rightEndTempSc
    global leftEndHumiSa, rightEndHumiSa, leftEndHumiSb, rightEndHumiSb, leftEndHumiSc, rightEndHumiSc
    
    # Hay que ver sus ubicaciones fisicas. Luego descomentar y probar. 
    leftEndTempSa = saLeftLimitTemp(Configuraciones.SaKeyValueTemp.get('saR1pduTemp', 'Error en conectar'), Configuraciones.SaKeyValueTemp.get('saR4pduTemp', 'Error en conectar'))
    # rightEndTempSa = Operaciones.saRightLimitTemp(Configuraciones.SaKeyValueHumi.get())
    leftEndHumiSa = saLeftLimitHumi(Configuraciones.SaKeyValueHumi.get('saR1pduHumi', 'Error en conectar'), Configuraciones.SaKeyValueHumi.get('saR4pduHumi', 'Error en conectar'))
    # rightEndHumiSa = Operaciones.saRightLimitHumi(Configuraciones.SaKeyValueHumi.get())
    
    leftEndTempSb = sbLeftLimitTemp(Configuraciones.SbF1KeyValueTemp.get('sbF1R1pduTemp', 'Error en conectar'), Configuraciones.SbF2KeyValueTemp.get('sbF2R1pduTemp', 'Error en conectar'))
    # rightEndTempSb = Operaciones.sbRightLimitTemp(Configuraciones.SbF1KeyValueTemp.get('sbF1R10pduTemp', 'Error en conectar'), Configuraciones.SbF2KeyValueTemp.get('sbF2R10pduTemp', 'Error en conectar')) -> Racks no disponibles
    leftEndHumiSb = sbLeftLimitHumi(Configuraciones.SbF1KeyValueHumi.get('sbF1R1pduHumi', 'Error en conectar'), Configuraciones.SbF2KeyValueHumi.get('sbF2R1pduHumi', 'Error en conectar'))
    # rightEndHumiSb = Operaciones.sbRightLimitHumi(Configuraciones.SbF1KeyValueHumi.get('sbF1R10pduHumi', 'Error en conectar'), Configuraciones.SbF2KeyValueHumi.get('sbF2R10pduHumi', 'Error en conectar')) -> Racks no disponibles

    # Hay que crear los diccionarios para el sector C. Luego descomentar y probar. 
    # leftEndTempSc = Operaciones.scLeftLimitTemp(Configuraciones.ScF1KeyValueTemp, Configuraciones.ScF2KeyValueTemp)
    # rightEndTempSc = Operaciones.scRightLimitTemp(Configuraciones.ScF1KeyValueTemp, Configuraciones.ScF2KeyValueTemp)
    # leftEndHumiSc = Operaciones.scLeftLimitHumi(Configuraciones.ScF1KeyValueTemp, Configuraciones.ScF2KeyValueTemp)
    # rightEndHumiSc = Operaciones.scRightLimitHumi(Configuraciones.ScF1KeyValueHumi, Configuraciones.ScF2KeyValueHumi)
    
    # Se actualizan los archivos txt de los tres sectores con los datos obtenidos de sus extremos.
    # Se comentan ya que es opcional y el sector C aun no esta implementado. 
    
    # saLeftUpdateFileTXT(leftEndHumiSa, leftEndTempSa)
    # saRightUpdateFileTXT(rightEndHumiSa, rightEndTempSa)
    
    # sbLeftUpdateFileTXT(leftEndHumiSb, leftEndTempSb)
    # sbRightUpdateFileTXT(rightEndHumiSb, rightEndTempSb)
    
    # scLeftUpdateFileTXT(leftEndHumiSc, leftEndTempSc)
    # scRightUpdateFileTXT(rightEndHumiSc, rightEndTempSc)

def saTempHumiCheck(promTempSa, promHumiSa): 
    
    """ Verifica que los valores promedios estén dentro de un rango para el sector A. Si no es asi, envia menjsaje de alerta. 
    
    Para humedad, comprueba si es menor a 25% y mayor que 85%. Si es verdad, envia una alerta.
    Caso contrario no. 
    De igual forma con la temperatura. Si es menor a 12ºC y mayor que 20ªC se enviarà una alarma, 
    caso contrario no. 
    
    El mensaje de alerta se envía mediante un email y al espacio de chat del equipo de Infraestructura. 
    Por practicidad se comentan las funciones que prueban los lados extremos. 
    

    Args:
        promTempSa (float): recibe promedio de temperatura del sector A
        promHumiSa (float): recibe promedio de humedad del sector A
    """
    
    if promTempSa < 12 or promTempSa > 20:
        if(promTempSa < 12):
            sendEmailsToAlertForTemp(promTempSa, "sectorA")
        else:
            sendEmailsToAlertForTemp(promTempSa, "sectorA")
    
    if promHumiSa < 25 or promHumiSa > 85:
        if(promHumiSa < 25):
            sendEmailsToAlertForHumi(promHumiSa, "sectorA")
        else:
            sendEmailsToAlertForHumi(promHumiSa, "sectorA")
    
    return 0
            
# def saTempHumiLeftCheck(leftEndTempSa, leftEndHumiSa):
    
#     if leftEndTempSa < 12 or leftEndTempSa > 20:
#         if(promTempSa < 12):
#             sendEmailsToAlertForTemp(leftEndTempSa)
#         else:
#             sendEmailsToAlertForTemp(leftEndTempSa)
    
#     if leftEndHumiSa < 25 or leftEndHumiSa > 85:
#         if(leftEndHumiSa < 25):
#             sendEmailsToAlertForHumi(leftEndHumiSa)
#         else:
#             sendEmailsToAlertForHumi(leftEndHumiSa)
               
def sbTempHumiCheck(promTempSb, promHumiSb):  
    
    """ Verifica que los valores promedios estén dentro de un rango para el sector B. Si no es asi, envia menjsaje de alerta. 
    
    Para humedad, comprueba si es menor a 25% y mayor que 85%. Si es verdad, envia una alerta.
    Caso contrario no. 
    De igual forma con la temperatura. Si es menor a 12ºC y mayor que 20ªC se enviarà una alarma, 
    caso contrario no. 
    
    El mensaje de alerta se envía mediante un email y al espacio de chat del equipo de Infraestructura. 
    Por practicidad se comentan las funciones que prueban los lados extremos. 
    

    Args:
        promTempSa (float): recibe promedio de temperatura del sector A
        promHumiSa (float): recibe promedio de humedad del sector A
    """
    
    if promTempSb < 12 or promTempSb > 20:
        if(promTempSb < 12):
            sendEmailsToAlertForTemp(promTempSb, "sectorB")
        else:
            sendEmailsToAlertForTemp(promTempSb, "sectorB")
    
    if promHumiSb < 25 or promHumiSb > 85:
        if(promHumiSb < 25):
            sendEmailsToAlertForHumi(promHumiSb, "sectorB")
        else:
            sendEmailsToAlertForHumi(promHumiSb, "sectorB")
            
    return 0

# def sbTempHumiLeftCheck(leftEndTempSb, leftEndHumiSb):
    
#     if leftEndTempSb < 12 or leftEndTempSb > 20:
#         if(promTempSb < 12):
#             sendEmailsToAlertForTemp(leftEndTempSb)
#         else:
#             sendEmailsToAlertForTemp(leftEndTempSb)
    
#     if leftEndHumiSb < 25 or leftEndHumiSb > 85:
#         if(leftEndHumiSb < 25):
#             sendEmailsToAlertForHumi(leftEndHumiSb)
#         else:
#             sendEmailsToAlertForHumi(leftEndHumiSb)
    

if __name__ == '__main__':
    main()