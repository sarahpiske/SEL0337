from gpiozero import LED #Importa a biblioteca gpiozero para o funcionamento do LED
from time import sleep #Importa a biblioteca time para pausas no código

pin = LED(14) #Define o LED no GPIO 14

while 1: #Inicializa o loop
	pin.on() #Liga o LED
	sleep(1) #Espera 1 segundo
	pin.off() #Desliga o LED
	sleep(1) #Espera mais um segundo para recomeçar o loop
