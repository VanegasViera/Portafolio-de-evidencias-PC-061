import smtplib, ssl
import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = input("Ingrese su correo: ")
password = getpass.getpass("Ingrese su password: ")

destinatario = input("Ingrese el destinatario: ")
asunto = input("Ingrese el asunto: ")

mensaje = MIMEMultipart("alternative")
mensaje["Subject"] = asunto
mensaje["From"] = username
mensaje["To"] = destinatario

html = f"""
<html>
<body>
    <p>Angel Ivan Celaya Garcia y Jose Fidencio Vanegas Viera<br>
</body>
<html>
"""

parte_html = MIMEText(html, "html")
mensaje.attach(parte_html)

archivo = "y.jpg"

with open(archivo, "rb") as adjunto:
    contenido_adjunto = MIMEBase("application", "octet-stream")
    contenido_adjunto.set_payload(adjunto.read())

encoders.encode_base64(contenido_adjunto)

contenido_adjunto.add_header(
    "Content-Disposition",
    f"attachment; filename= {archivo}",
    )

mensaje.attach(contenido_adjunto)
text = mensaje.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(username, password)
    server.sendmail(username, destinatario, text)

