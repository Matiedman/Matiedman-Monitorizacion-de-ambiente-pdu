"""Se obtienen los datos en crudo de cada pdu y luego se crean los datos de temeperatura y humedad.
Además, se crean archivos txt donde se registrarán los valores para que puedan ser mostrado en Grafana. 
Esto es opcioanl y desde otros modulos está comentado por lo que no se lo está utilizando."""

import os
import sys
from easysnmp import EasySNMPTimeoutError
# from easysnmp import snmp_get, snmp_walk

dataTemp = {}
dataHumi = {}
actualRoute = os.getcwd()
sBFilePathName = "Datos historicos del sector B.txt"
sBFilePathNameLeftSide = "Datos historicos del lado izquierdo del sector B.txt"
sBFilePath = os.path.join(actualRoute, sBFilePathName)
sBLeftSideFilePath = os.path.join(actualRoute, sBFilePathNameLeftSide)

# A esta funcion aplicar try catch para manejo de erorres. Un error es el siguiente "easysnmp.exceptions.EasySNMPTimeoutError: timed out while connecting to remote host"
def getTemperature(sxFxRxpdu):

    """Función que obtiene la temperatura según la sesión del pdu.
    Args:
        sxFxRxpdu (Object): Objeto que es la sesión de los diferentes ePDUs. 
                            Esto trae varias caracteristicas para obtener los datos mediante métodos. 
    
    Returns:
        float : Devuelve el valor de la temperatura según sxFxRxpdu con un decimal. 
        Si ha ocurrido un error se imprime un mensaje del mismo y el programa termina. """
        
    try:
        # Se almacena el objeto, su tipo, que es OBJECT-TYPE -> Integer. Su acceso es de solo lectura.
        getInterfaceTempStauts = sxFxRxpdu.get('1.3.6.1.4.1.534.6.6.7.7.1.1.4.0.1')
        # temperatureOID = getInterfaceTempStauts.oid                  # Se almacena el OID de la temperatura.
        # dataTypeTempOID = getInterfaceTempStauts.snmp_type           # Se almacena el tipo de dato que devuelve el OID.         
        tempValue = getInterfaceTempStauts.value                       # Se almacena el dato de la temperatura obtenido del OID
        # objectType = type(getInterfaceTempStauts)                    # Guarda el tipo de dato que almacena la variable
        temp = (int(tempValue))/10                                     # Se conviernte el tipo de dato a entero y luego lo divide por 10. 
    except EasySNMPTimeoutError as error:
        # easysnmp.exceptions.EasySNMPTimeoutError: timed out while connecting to remote host   
        print(f"Ocurrió un error inesperado: {error}. El programa terminará. ")
        sys.exit(0)
    except Exception as error2:
        print(f"Ocurrió un error inesperado: {error2}. El programa terminará. ")
        sys.exit(0)
    else:
        return temp

def getHumidity(sxFxRxpdu):
    
    """Función que obtiene la humedad según la sesión del pdu.
    Args:
        sxFxRxpdu (Object): Objeto que es la sesión de los diferentes ePDUs. 
                            Esto trae varias caracteristicas para obtener los datos mediante métodos. 
    
    Returns:
        float : Devuelve el valor de la humedad según sxFxRxpdu con un decimal.
        Si ha ocurrido un error se imprime un mensaje del mismo y el programa termina. """
        
    try:
        
        # Se almacena el objeto, su tipo, que es OBJECT-TYPE -> Integer. Su acceso es de solo lectura.
        getInterfaceHumStauts = sxFxRxpdu.get('1.3.6.1.4.1.534.6.6.7.7.2.1.4.0.1')     
        # humidityOID = getInterfaceHumStauts.oid                       # Se almacena el OID de la humedad.
        # dataTypeHumOID = getInterfaceHumStauts.snmp_type              # Se almacena el tipo de dato que devuelve el OID.         
        humiValue = getInterfaceHumStauts.value                         # Se almacena el dato de la humedad obtenido del OID
        # objectType = type(getInterfaceHumStauts)                      # Guarda el tipo de dato que almacena la variable
        humi = (int(humiValue))/10                                      # Se conviernte el dato a entero y luego lo divide por 10. 
    except EasySNMPTimeoutError as error:
        # easysnmp.exceptions.EasySNMPTimeoutError: timed out while connecting to remote host   
        print(f"Ocurrió un error inesperado: {error}. El programa terminará. ")
        sys.exit(0)
    except Exception as error2:
        print(f"Ocurrió un error inesperado: {error2}. El programa terminará.  ")
        sys.exit(0)
    else:
        return humi

# Las siguientes tres funciones actualizan la informacion en un archivo TXT para que desde ahi pueda ser mostrada desde Grafana. 
# Se comentan las actualizaciones del sector A y C ya que no está implementado. 

# def saUpdateFileTXT(humi, temp):

#    """Actualiza la información ambiental en un archivo TXT para que desde ahi pueda ser mostrada desde Grafana."""
    
#     global dataTemp, dataHumi,

#     filePlace = "/home/matias/Proyectos_en_el_NOC_como_PASANTE/Proyecto_de_Becas_de_Tecnologias_de_la_Informacion/Monitorizacion_del_ambiente_del_DC/Datos historicos del sector A.txt"
#     dataTemp['SAtemp'] = temp
#     dataHumi['SAhumi'] = humi

#     # Leer contenido actual y lo guarda. 
#     with open(filePlace, 'r') as file:
#         originalContent = file.read()

#     # Se abre el archivo txt "datos historicos" para ir almacenando los datos y su tiempo de registro. 
#     with open(filePlace,"w") as file:
#         file.write("Sector A: Temperatura = " + str(dataTemp.get('SAtemp')) + "ºC; Humedad = " + str(dataHumi.get('SAhumi')) + "% | " + actualTime.strftime('A las %Hhs %Mmin %Sseg; tomado el %d %b del %Y') + " \n") # Se escribe nueva informacion. 
#         file.write(originalContent) # Se escribe el contenido original luego de la nueva informacion. 
        
#     return 0

# def sbUpdateFileTXT(humi, temp):
    
#     """Actualiza la información ambiental en un archivo TXT para que desde ahi pueda ser mostrada desde Grafana."""

#     global dataTemp, dataHumi, sBFilePath
    
#     dataTemp['SBtemp'] = temp
#     dataHumi['SBhumi'] = humi

#     # Leer contenido actual y lo guarda. En esta funcion se dejan estas lineas comentadas ya que corresponde a que almacenen los datos hitoricos en un txt indefinidamente.
#     # with open(sBFilePath, 'r') as file:
#     #     originalContent = file.read()

#     # Se abre el archivo txt "datos historicos" para ir escribiendo los datos registrados. Cada vez que se ejecuta esta funcion se pisan los datos viejos. 
#     with open(sBFilePath,"w") as file:
#         # Estas lineas comentadas tienen que ver con las anteriores ya que funcuionan con ellas. Se las deja planteadas por ese motivo. 
#         # file.write("Sector B: Temperatura = " + str(dataTemp.get('SBtemp')) + "ºC; Humedad = " + str(dataHumi.get('SBhumi')) + "% | " + actualTime.strftime('A las %Hhs %Mmin %Sseg; tomado el %d %b del %Y') + " \n") # Se escribe nueva informacion. 
#         # file.write(originalContent) # Se escribe el contenido original luego de la nueva informacion. 
        
#         file.write("PDUenvironment,name=Temp Temp= " + str(dataTemp.get('SBtemp')) + "\n")
#         file.write("PDUenvironment,name=Humi Humi= " + str(dataHumi.get('SBhumi')))
 
#     return 0 

# Modificar siguiente funcion segun los parametros correspondientes al sector C. 
# def scUpdateFileTXT(humi, temp):

#   """Actualiza la información ambiental en un archivo TXT para que desde ahi pueda ser mostrada desde Grafana."""
    
#     global dataTemp, dataHumi, filePlace, actualTime

#     filePlace = "/home/matias/Proyectos_en_el_NOC_como_PASANTE/Proyecto_de_Becas_de_Tecnologias_de_la_Informacion/Monitorizacion_del_ambiente_del_DC/Datos historicos del sector C.txt"
#     dataTemp['SCtemp'] = temp
#     dataHumi['SChumi'] = humi

#     # Leer contenido actual y lo guarda. 
#     with open(filePlace, 'r') as file:
#         originalContent = file.read()

#     # Se abre el archivo txt "datos historicos" para ir almacenando los datos y su tiempo de registro. 
#     with open(filePlace,"w") as file:
#         file.write("Sector C: Temperatura = " + str(dataTemp.get('SCtemp')) + "ºC; Humedad = " + str(dataHumi.get('SChumi')) + "% | " + actualTime.strftime('A las %Hhs %Mmin %Sseg; tomado el %d %b del %Y') + " \n") # Se escribe nueva informacion. 
#         file.write(originalContent) # Se escribe el contenido original luego de la nueva informacion. 
        
#     return 0

# Lados extremos del sector A. Se comentan ya que, ademas de no estar implementado, no es necesario o es opcional por el momento. 
# def saLeftUpdateFileTXT(leftHumi, leftTemp):
    
#     return 0

# def saRightUpdateFileTXT(rihtHumi, rightTemp):
    
#     return 0

# Lados extremos del sector B.
# def sbLeftUpdateFileTXT(leftHumi, leftTemp):
    
#     """Actualiza la información ambiental del lado izquierdo en un archivo TXT para que desde ahi pueda ser mostrada desde Grafana."""
    
#     global dataTemp, dataHumi, sBLeftSideFilePath
    
#     dataTemp['leftSBtemp'] = leftTemp
#     dataHumi['leftSBhumi'] = leftHumi

#     # Se abre el archivo txt "datos historicos" para ir escribiendo los datos registrados. Cada vez que se ejecuta esta funcion se pisan los datos viejos.
#     with open(sBLeftSideFilePath,"w") as file:
#         file.write("PDUenvironment,name=Temp Temp= "+ str(dataTemp.get('leftSBtemp')) + "\n")  
#         file.write("PDUenvironment,name=Humi Humi= "+ str(dataHumi.get('leftSBhumi')))
        
#     return 0

# Se comentan ya que, ademas de no estar implementado, no es necesario o es opcional por el momento.
# def sbRightUpdateFileTXT(rightHumi, rightTemp):
    
#     return 0

# # Extremos del sector C. 
# def scLeftUpdateFileTXT(leftHumi, leftTemp):
    
#     return 0

# def scRightUpdateFileTXT(rightHumi, rightTemp):
    
#     return 0