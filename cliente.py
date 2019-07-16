from temporizador import Temporizador
from time import sleep
 
t = Temporizador()

t.iniciar([0,0,15])

while True:
    tiempo = t.mostrar_tiempo()
    print tiempo
    sleep(0.5)
    if tiempo == "00 : 00 : 00":
        break
    t.retroceder()

while True:
    tiempo = t.mostrar_tiempo()
    print tiempo
    sleep(0.5)
    if tiempo == "00 : 00 : 15":
        break
    t.avanzar()


