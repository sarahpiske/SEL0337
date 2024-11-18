from gpiozero import LED #Importa a biblioteca gpiozero
import RPi.GPIO as gpio #Importa a biblioteca RPi.GPIO

pin = LED(14) #Define o LED no GPIO 14

pin.off() #Desliga o LED
gpio.cleanup() #Limpa o GPIO
