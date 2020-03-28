import datetime
from time import ctime
import ntplib
import os

t1 = datetime.datetime.now()
print ("t1: Fecha y hora = %s" % t1)
servidor_de_tiempo = "ntp2.recro.ae"
cliente_ntp = ntplib.NTPClient()
respuesta = cliente_ntp.request(servidor_de_tiempo)
t2 = datetime.datetime.now()
print ("t2: Fecha y hora = %s" % t2)
hora_actual = datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
print("Servidor de tiempo: " + str(hora_actual))
ajuste=(t2-t1)/2
print ("Ajuste: Fecha y hora = %s" % ajuste)
reloj=hora_actual+ajuste
print ("Reloj: Fecha y hora = %s" % reloj)

os.system(f"date --set '{reloj}'")