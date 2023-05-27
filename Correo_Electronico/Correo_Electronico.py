#Israel Cuellar Mendez - 2077688

#Importamos las librerias que se van a utilizar
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import ssl

#Definimos variables 
#El puerto que usaremos
port = 587
#Definimos el servidor
smtp_server = "smtp.gmail.com"
#Correo de quien lo envia
envia = ""
#Correron del que recibe
recibe = ""
#Contraseña
password = ""

#Creamos un objeto MIME para agregar texto e imagenes
mensaje = MIMEMultipart('related')
mensaje['Subject'] = "Prueba de envio (script Python) - 2077688"
mensaje['From'] = envia
mensaje['To'] = recibe
#Creamos el texto html para dar el formato pedido
html = """\
<html>
    <head>
    </head>
    <h1>Practica 12</h1>
    <p>
        Ejercicio de la practica 12 para el envio de correos <br>
        <b>Alumno:</b> Israel Cuéllar Méndez <br>
        <b>Matricula:</b> 2077688
    </p>
</html>
"""

parte1 = MIMEText(html, 'html')

#Creamos un objeto para la imagen
imagen = open('fcfm_cool.png', 'rb')
imgmen = MIMEImage(imagen.read())
imagen.close
parte2 = imgmen

#Agregamos el html y la imagen al mensaje
mensaje.attach(parte1)
mensaje.attach(parte2)

context = ssl.create_default_context()

#Hacemos la conexion con el servidor y enviamos el correo
try:
    server =  smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo
    server.login(envia, password)
    server.sendmail(envia, recibe, mensaje.as_string())
except Exception as e:
    print (e)
finally: 
    server.quit