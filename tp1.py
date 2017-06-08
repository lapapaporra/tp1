import picamera
import time
from os import system
camera = picamera.PiCamera()

pregunta = raw_input("Hola Tomi, como estas? Somos Pedro Araoz, Agustin Carli\nIvan Dominguez de Alzaga, Martin Pimentel y Alejo Ramirez Gismondi.\n'a' para timelapse o 'b' para foto con efecto\n> ") 
if pregunta == "a":
        numb = raw_input("Cuantas fotos queres para tu timelapse?\n> ")
        nombre = raw_input("Insertar nombre de archivo\n> ")
        for i in range(0, int(numb)):
                i = i + 1
                camera.start_preview()
                camera.capture(nombre + str(i) + ".jpg")
                camera.stop_preview()        
        gif = raw_input("Queres hacer un gif?\n(y/n)\n> ")
        if gif == "y":
                system("convert   -delay 20   -loop 0   " + nombre+"*.jpg  " + nombre + ".gif")
                print "Se guardo el gif como: " + nombre + ".gif"
        elif gif == "n":
                print "Ok, bye! >:( programe todo esto y no lo usas..."
        else:
                print "Y or N, no es muy dificil!"
                
elif pregunta == "b":
        nombre = raw_input("Insertar nombre de archivo\n> ")
        camera.start_preview()
        time.sleep(2)
	camera.image_effect = 'negative'
	camera.capture(nombre + ".jpg")
	camera.stop_preview()
	camera.image_effect = 'none'
else:
	print "Oops, something went wrong, please try again"
