# MonitorizacionPDU-DCCampusVirtual

## Descripción General
Los  conceptos de Internet de las cosas (IoT) se aplicarán para sostener de forma constante el monitoreo de los datos ambientales del Data Center del Campus Virtual de la UNC. Estos son de temperatura y humedad que sirven para mantener en estado estable y buen funcionamiento los equipos físicos del Data Center para que pueda entregar los servicios de software a la comunidad universitaria. Además, dichos datos serán obtenidos mediante sensores que vienen incorporados en las ePDU (Eaton Power Distribution Unit) que son como “zapatillas” que tienen tomacorrientes que garantizan la distribución de la energía y protección de circuitos para los equipos conectados a ellos. Estos están instalados de forma perpendicular al piso en un rack y el sensor está en la parte superior del mismo.

Se creó un software que trata los datos y se los muestra mediante Grafana en un monitor para su visaulización y asi llevar un control de los mismos en tiempo real. Seguidamente, se creó la funcionalidad de enviar mensajes y correos en caso que se pasen límites establecidos de temperatura y humedad al equipo de Infraestructura para que tomen acciones necesarias y no permitan el incorrecto funcionamiento del Data Center.

Puede encontrar la documentación del proyecto con mas detalles en [Bookstack](https://bookstack.psi.unc.edu.ar/books/ups-pdu/page/monitorizacion-de-pdus). Se recomienda leerlo. 

## Requisitos

Dirijase a [bookstack](https://bookstack.psi.unc.edu.ar/books/ups-pdu/page/monitorizacion-de-pdus) para ver los requisitos de instalación de tal forma de poder continuar con los apartados siguientes. 

## Instalación

Para bajar el proyecto a su repositorio local clonelo con el siguiente comando:

~$ git clone https://gitlab.unc.edu.ar/psi.iaas/udp_temp.git

Seguidamente cree un archivo .env donde guardará las contraseñas de acceso al email y al chat. Este archivo debe estar junto a los modulos en la misma ubicación. Puede crear dicho documento mediante: 

~$ touch .env

Acceder al mismo mediante vim y escribir las contraseñas. Estas las podrá encontrar en bookstack en la seccion de Infraestructura. Puede preguntar a su lider o compañero para ubicarse. 

Luego, compruebe que las conexiones de su maquina virtual o el lugar desde donde se ejecute el programa tenga acceso a las PDUs del Data Center del Campus Virtual. Es necesario comprobarlo con la ayuda del equipo de Redes o chequear si ya se hizo verificando el lugar donde se lo haya documentando. 

Aun asi puede hacerlo mediante la ejecución del comando ping + ip de la pdu o host + nombre del host de la PDU. Ejemplo,

~$ ping 172.16.46.51

~$ host sbf1r1pdu.psi.unc.edu.ar

Antes de ejecutar el programa, hay que darle permisos de ejecución al modulo denominado "Inicio.py". Luego ejecujarlo con ~$ ./Inicio.py 

Con estos pasos debería poder ver una secuencia de datos como sigue, 

PDUenvironmentSa,name=Temp Temp=13.1 

PDUenvironmentSa,name=Humi Humi=43.8 

PDUenvironmentSa,name=Temp LeftTemp=13.6 

PDUenvironmentSa,name=Humi LeftHumi=42.4 

PDUenvironmentSb,name=Temp Temp=13.8 

PDUenvironmentSb,name=Humi Humi=42.4 

PDUenvironmentSb,name=Temp LeftTemp=13.3 

PDUenvironmentSb,name=Humi LeftHumi=42.5


## Uso del Software

Vease su descripción en bookstack, biblioteca de infraestructura en el capitulo de UPS-PDU.

## Contribuciones

Al proyecto se lo puede contribuir mediante la mejora y optimización de su código asi como de su mantenimiento. Corroborar en dejarlo en correcto funcionamiento.

## Contacto

Puedes consultarme, ante algun inconveniente, enviandome un mail a mati.mangin@unc.edu.ar o a mati.edman@gmail.com


## Estado del proyecto

Proyecto en fase terminada. Solo hay que hacerle los mantenimientos correspondientes a las actualizaciones del lenguaje de programacion Python y del sistema operativo. Es decir, actualizar el entorno para que el proyecto funcione adecuadamente. 

## Créditos

Proyecto desarrollado por Mangin Matias Eduardo, estudiante de Ingenería Electrónica y pasante en la Prosecreataría de Informatica cuyo rol es Analista de Infraestructura. 

Colaboraciones en la construcción del proyecto: 

    Área de Infraestructura Guillermo Getar, Mauro Alejandro Pereira y Alejandro Miguel Diaz Crivelli. 
    Área de Servicios Martin R. Disandro y Marcelo E. Rocha Vargas.
    Área de Redes y Telecomunicaciones. 

