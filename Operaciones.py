""" Mediante operaciones matematicas se obtienen los promedios de temperatura 
y humedad para cada sector. Ademas, se obtienen las temperaturas y humedad de ambos 
extremos de los mismos. 
"""

# Descomentar y probar una vez que el funcionamiento fisico de cada dispositivo, segun sector, este correcto. 
  
def saPromedioTemp(SaKeyValueTemp):
    
    """Obtención del promedio de los valores de temperatura de cada pdu del sector A. Se toma con un decimal.

    Args:
        SaKeyValueTemp (dict): Llave - valor de la temperatura del sector A. 
        
    Returns:
        float: Promedio de la temperatura del sector A.
    """
    
    dataAuxTempSa = 0
    if len(SaKeyValueTemp) == 0:
        print(ZeroDivisionError + ". Division por cero. Esto puede deberse a problema de conexion u otro, investigar. ")
        # NOTIFICAR POR EMAIL Y CHAT
        return 1
    
    dicSizeSa = len(SaKeyValueTemp)
    
    
    for RxTempValue in SaKeyValueTemp.values():
        dataAuxTempSa += RxTempValue
    
    auxTempPromSa = dataAuxTempSa/dicSizeSa
    saTempProm = round(auxTempPromSa, 1)
    
    return saTempProm

def saPromedioHumi(SaKeyValueHumi):
    
    """Obtención del promedio de los valores de humedad de cada pdu del sector A. Se toma con un decimal.

    Args:
        SaKeyValueHumi (dict): Llave - valor de la humedad del sector A. 
        
    Returns:
        float: Promedio de la hummedad del sector A.
    """
    
    dataAuxHumiSa = 0
    if len(SaKeyValueHumi) == 0:
        print(ZeroDivisionError + ". Division por cero. Esto puede deberse a problema de conexion u otro, investigar. ")
        # NOTIFICAR POR EMAIL Y CHAT
        return 1
    
    dicSizeSa = len(SaKeyValueHumi)
    
    for RxHumiValue in SaKeyValueHumi.values():
        dataAuxHumiSa += RxHumiValue
        
    auxHumiPromSa = dataAuxHumiSa/dicSizeSa
    saHumiProm = round(auxHumiPromSa, 1)
    
    return saHumiProm

def sbPromedioTemp(SbF1KeyValueTemp, SbF2KeyValueTemp):

    """Obtención del promedio de los valores de temperatura de cada pdu del sector B. 
    Se tienen dos parametros de entrada que corresponen a las filas 1 y 2 de dicho sector. 
    Se toma con un decimal.

    Args:
        SbF1KeyValueTemp (dict): Llave - valor de la temperatura de la fila 1 del sector B. 
        SbF2KeyValueTemp (dict): Llave - valor de la temperatura de la fila 2 del sector B. 
        
    Returns:
        float: Promedio de la temperatura del sector B.
    """

    dataAuxTempF1, dataAuxTempF2 = 0, 0
    if len(SbF1KeyValueTemp) == 0 or len(SbF2KeyValueTemp) == 0:
        print(ZeroDivisionError + ". Division por cero. Esto puede deberse a problema de conexion u otro, investigar. ")
        # NOTIFICAR POR EMAIL Y CHAT
        return 1
    
    dicSizeSbF1 = len(SbF1KeyValueTemp)
    dicSizeSbF2 = len(SbF2KeyValueTemp)

    for F1RxTempValue in SbF1KeyValueTemp.values():
        dataAuxTempF1 += F1RxTempValue

    for F2RxTempValue in SbF2KeyValueTemp.values():
         dataAuxTempF2 += F2RxTempValue

    auxTempPromF1 = dataAuxTempF1/dicSizeSbF1
    auxTempPromF2 = dataAuxTempF2/dicSizeSbF2
    sbTempProm = round((auxTempPromF1 + auxTempPromF2)/2, 1)

    return sbTempProm



def sbPromedioHumi(SbF1KeyValueHumi, SbF2KeyValueHumi):
    
    """Obtención del promedio de los valores de humedad de cada pdu del sector B. 
    Se tienen dos parametros de entrada que corresponen a las filas 1 y 2 de dicho sector. 
    Se toma con un decimal.

    Args:
        SbF1KeyValueTemp (dict): Llave - valor de la humedad de la fila 1 del sector B. 
        SbF2KeyValueTemp (dict): Llave - valor de la humedad de la fila 2 del sector B. 
        
    Returns:
        float: Promedio de la humedad del sector B.
    """

    dataAuxHumiF1, dataAuxHumiF2 = 0, 0
    if len(SbF1KeyValueHumi) == 0 or len(SbF2KeyValueHumi) == 0:
        print(ZeroDivisionError + ". Division por cero. Esto puede deberse a problema de conexion u otro, investigar. ")
        # NOTIFICAR POR EMAIL Y CHAT
        return 1
    
    dicSizeSbF1 = len(SbF1KeyValueHumi)
    dicSizeSbF2 = len(SbF2KeyValueHumi)

    for F1RxHumiValue in SbF1KeyValueHumi.values():
        dataAuxHumiF1 += F1RxHumiValue

    for F2RxHumiValue in SbF2KeyValueHumi.values():
        dataAuxHumiF2 += F2RxHumiValue

    auxHumiPromF1 = dataAuxHumiF1/dicSizeSbF1
    auxHumiPromF2 = dataAuxHumiF2/dicSizeSbF2

    sbHumiProm = round((auxHumiPromF1 + auxHumiPromF2)/2, 1)

    return sbHumiProm


# def scPromedioTemp(ScF1KeyValueTemp, ScF2KeyValueTemp):
#     return
# def scPromedioHumi(ScF1KeyValueHumi, ScF2KeyValueHumi):
#     return

# Obtencion de los valores extremos izquierdo de los pdu por sector de temperatura y humedad.   
def saLeftLimitTemp(saR1pduTemp, saR4pduTemp):
    
    """Obtención del promedio de los valores de temperatura de los pdu que están en el extremo izquierdo del sector A. 
    Se tienen dos parametros de entrada que corresponen al Rack 1 y 4 de dicho sector. 
    Se toma con un decimal.

    Args:
        saR1pduTemp (float): valor de la temperatura del Rack 1 del sector A. 
        saR4pduTemp (float): valor de la temperatura del Rack 4 del sector A. 
        
    Returns:
        float: Promedio de la temperatura del lado izquierdo del sector A.
    """
    
    leftAverageTemp = round((saR1pduTemp + saR4pduTemp)/2, 1)
    return leftAverageTemp

def saLeftLimitHumi(saR1pduHumi, saR4pduHumi):
    
    """Obtención del promedio de los valores de humedad de los pdu que están en el extremo izquierdo del sector A. 
    Se tienen dos parametros de entrada que corresponen al Rack 1 y 4 de dicho sector. 
    Se toma con un decimal.

    Args:
        saR1pduHumi (float): valor de la humedad del Rack 1 del sector A. 
        saR4pduHumi (float): valor de la humedad del Rack 4 del sector A. 
        
    Returns:
        float: Promedio de la humedad del lado izquierdo del sector A.
    """
    
    leftAverageHumi = round((saR1pduHumi + saR4pduHumi)/2, 1)
    
    return leftAverageHumi

def sbLeftLimitTemp(sbF1R1pduTemp, sbF2R1pduTemp):
    
    """Obtención del promedio de los valores de temperatura de los pdu que están en el extremo izquierdo del sector B. 
    Se tienen dos parametros de entrada que corresponen a la fila 1 y 2 de dicho sector. 
    Se toma con un decimal.

    Args:
        sbF1R1pduTemp (float): valor de la temperatura de la fila 1 del sector B. 
        sbF2R1pduTemp (float): valor de la temperatura de la fila 2 del sector B. 
        
    Returns:
        float: Promedio de la temperatura del lado izquierdo del sector B.
    """

    leftAverageTemp = round((sbF1R1pduTemp + sbF2R1pduTemp)/2, 1)
    return leftAverageTemp

def sbLeftLimitHumi(sbF1R1pduHumi, sbF2R1pduHumi):

    """Obtención del promedio de los valores de humedad de los pdu que están en el extremo izquierdo del sector B. 
    Se tienen dos parametros de entrada que corresponen a la fila 1 y 2 de dicho sector. 
    Se toma con un decimal.

    Args:
        sbF1R1pduHumi (float): valor de la temperatura de la fila 1 del sector B. 
        sbF1R1pduHumi (float): valor de la temperatura de la fila 2 del sector B. 
        
    Returns:
        float: Promedio de la temperatura del lado izquierdo del sector B.
    """

    leftAverageHumi = round((sbF1R1pduHumi + sbF2R1pduHumi)/2, 1)
    return leftAverageHumi



# def scLeftLimitTemp():
#     return

# def scLeftLimitHumi():
#     return

# # Obtencion de los valores extremos derecho de los pdu por sector de temperatura y humedad. 
# def saRightLimitTemp():
#     return

# def saRightLimitHumi():
#     return

# def sbRightLimitTemp():
#     return

# def sbRightLimitHumi():
#     return

# def scRightLimitTemp():
#     return

# def scRightLimitHumi():
#     return
