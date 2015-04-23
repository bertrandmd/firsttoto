#!/usr/bin/env python
# coding: Latin-1

### multi-thread a travers un socket

# Load library functions we want
import SocketServer
import os,time
from threading import Thread
import datetime
import RPi.GPIO as GPIO

### pour le son
import pygame
from pygame.locals import *
#pygame.init()
#screen = pygame.display.set_mode((64, 48))
#pygame.display.set_caption('KeyB Caption')
#pygame.mouse.set_visible(0)
pygame.mixer.init(48000, -16, 1, 1024)
#soundA = pygame.mixer.Sound("darth.mp3")
soundA = pygame.mixer.Sound("r2d2.wav")

soundChannelA = pygame.mixer.Channel(1)



GPIO.setmode(GPIO.BCM) # mode de numérotation des pins
GPIO.setup(25,GPIO.OUT) # la pin 25 réglée en sortie (output)
GPIO.setup(23,GPIO.OUT) # la pin 23 réglée en sortie (output)
GPIO.setup(22,GPIO.OUT) # la pin 22 réglée en sortie (output)
GPIO.setup(24,GPIO.OUT) # la pin 24 réglée en sortie (output)
GPIO.setup(4,GPIO.OUT) # la pin 25 réglée en sortie (output)
GPIO.setup(17,GPIO.OUT) # la pin 23 réglée en sortie (output)
GPIO.setup(18,GPIO.OUT) # la pin 22 réglée en sortie (output)
GPIO.setup(7,GPIO.OUT) # la pin 24 réglée en sortie (output)
GPIO.setup(27,GPIO.OUT) # la pin 24 réglée en sortie (output)



# Settings for the RemoteKeyBorg server
portListen = 9038   

SortieAnticipe = False
global compteur_gyro
global compteur_hymne
global compteur_phares
global compteur_lumieres
global compteur_slider
global compteur_slider2	
compteur_gyro = 1
compteur_hymne = 1
compteur_phares = 1
compteur_lumieres = 1
compteur_slider = 1
compteur_slider2 = 1

### Fonctions moteur
def avancer():
	print "AVANCE"
	GPIO.output(25,GPIO.HIGH) # sortie au niveau logique haut (3.3 V)
def droite():
	print "Tourne Droite"
	GPIO.output(23,GPIO.HIGH) # sortie au niveau logique haut (3.3 V)
def gauche():
	print "Tourne Droite"
	GPIO.output(22,GPIO.HIGH) # sortie au niveau logique haut (3.3 V)
def arriere():
	print "RECULE"
	GPIO.output(24,GPIO.HIGH) # sortie au niveau logique haut (3.3 V)

def stop():
	print "Frein"
	GPIO.output(25,GPIO.LOW) # sortie au niveau logique bas (0 V)
	GPIO.output(24,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(24,GPIO.LOW)	

def stopDroite():
	GPIO.output(23,GPIO.LOW) # sortie au niveau logique bas (0 V)
def stopGauche():
	GPIO.output(22,GPIO.LOW) # sortie au niveau logique bas (0 V)
def stopArriere():
	GPIO.output(24,GPIO.LOW) # sortie au niveau logique bas (0 V)


def frein():
	print 'Arret Total'


### Fonctions Annexes
def gyro():
	'''Alterne 2 LED'''
	GPIO.output(23,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(23,GPIO.LOW)
	time.sleep(0.2)
	GPIO.output(24,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(24,GPIO.LOW)

def phares():
	'''Allume les LED à l'avant'''
	GPIO.output(25,GPIO.HIGH)
def pharesEteints():
	GPIO.output(25,GPIO.LOW)

def lumieres():
	'''fait clignoter le rail de LED'''
	liste_LED = (4,17,18,27,7)
	for i in range(0,1) :
		GPIO.output(liste_LED,GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(liste_LED,GPIO.LOW)
		time.sleep(0.5)
		i = i+1

serie = [17,18,27,7,4]

def toto(x):
	'''Fait slider les LED en A/R'''
	for i in range (0,x):
		for i in serie:
			GPIO.output(i,GPIO.HIGH)	
			time.sleep(0.1)
			GPIO.output(i,GPIO.LOW)
		serie.reverse()	
		i=i+1
def toto2(x):
	'''Fait slider les LED'''
	for i in range (0,x):
		for i in serie:
			GPIO.output(i,GPIO.HIGH)	
			time.sleep(0.1)
			GPIO.output(i,GPIO.LOW)
		i=i+1

def tata(x):
	'''Fait alterner les LED par paire'''
	if (len(serie) % 2) == 0: 
		for i in range (0,x):
			for i in range (0,len(serie)/2):
				GPIO.output(serie[0+i],GPIO.HIGH)
				GPIO.output(serie[-1-i],GPIO.HIGH)	
				time.sleep(0.2)
				GPIO.output(serie[0+i],GPIO.LOW)
				GPIO.output(serie[-1-i],GPIO.LOW)			
				time.sleep(0.2)
				i=i+1
			i=len(serie)/2
			for i in range (len(serie)/2,0,-1):			
				time.sleep(0.2)
				GPIO.output(serie[-1+i],GPIO.HIGH)
				GPIO.output(serie[0-i],GPIO.HIGH)	
				time.sleep(0.2)
				GPIO.output(serie[-1+i],GPIO.LOW)
				GPIO.output(serie[0-i],GPIO.LOW)
				i=i-1
	else:
		for i in range (0,x):
			for i in range (0,len(serie)/2):			
				time.sleep(0.2)
				GPIO.output(serie[0+i],GPIO.HIGH)
				GPIO.output(serie[-1-i],GPIO.HIGH)	
				time.sleep(0.2)
				GPIO.output(serie[0+i],GPIO.LOW)
				GPIO.output(serie[-1-i],GPIO.LOW)
				i=i+1
			time.sleep(0.2)
			GPIO.output(serie[int(round(len(serie)/2,0))],GPIO.HIGH)
			time.sleep(0.2)
			GPIO.output(serie[int(round(len(serie)/2,0))],GPIO.LOW)
			for i in range (len(serie)/2,0,-1):		
				time.sleep(0.2)
				GPIO.output(serie[-1+i],GPIO.HIGH)
				GPIO.output(serie[0-i],GPIO.HIGH)	
				time.sleep(0.2)
				GPIO.output(serie[-1+i],GPIO.LOW)
				GPIO.output(serie[0-i],GPIO.LOW)
				i=i+1



def finProgs():
	'''Remet tous les ports GPIO à LOW'''
	liste_LED = (22,23,24,25,4,7,17,18,27)
	GPIO.output(liste_LED,GPIO.LOW)




# Class used to handle UDP messages
class PicoBorgHandler(SocketServer.BaseRequestHandler):
	# Function called when a new message has been received
	def handle(self):
		request, socket = self.request          # Read who spoke to us and what they said
		#ecrire(request)
		if request == 'ALLOFF':
			# Turn all drives off
			#MotorOff()
			print 'All drives off'
		elif request == 'AVAN':
			avancer()
		elif request == 'STOP':
			stop()
		elif request == 'ARRI':
			arriere()
		elif request == 'GAUC':
			gauche()
		elif request == 'DROI':
			droite()
		elif request == 'STOP_ARRI':
			stopArriere()
		elif request == 'STOP_GAUC':
			stopGauche()
		elif request == 'STOP_DROI':
			stopDroite()
		elif request == 'GYRO':
			print 'gyro'
			global compteur_gyro
			compteur_gyro = compteur_gyro + 1
			if (compteur_gyro % 2) == 0: 				
				global b
				#b = "thread_" + str(10 + compteur_gyro)
				b = Gyrophares()
				#print compteur_gyro
				b.start()
			else :
				b.stop()
		elif request == 'PHAR':
			print 'phares'
			compteur_phares = compteur_phares + 1
			if (compteur_phares % 2) == 0: 
				global c
				#c = "thread_" + str(10 + compteur_phares)
				c = Phares()
				c.start()
			else :
				c.stop()
		elif request == 'HYMNE':
			print 'hymne'
			compteur_hymne = compteur_hymne + 1
			if (compteur_hymne % 2) == 0:
				global a
				#a = "thread_" + str(10 + compteur_hymne)
				a = Hymne()
				a.start()
			else :
				a.stop()
		elif request == 'K2000':
			print 'k2000'
			compteur_slider = compteur_slider + 1
			if (compteur_slider % 2) == 0: 
				global e
				#e = "thread_" + str(10 + compteur_slider)
				e = Slider()
				e.start()
			else :
				e.stop()
		elif request == 'SLIDER2':
			print 'slider2'
			compteur_slider2 = compteur_slider2 + 1
			if (compteur_slider2 % 2) == 0: 
				global f
				#f = "thread_" + str(10 + compteur_slider2)
				f = Slider2()
				f.start()
			else :
				f.stop()
		elif request == 'LUMIERE':
			print 'lumieres'
			compteur_lumieres = compteur_lumieres + 1
			if (compteur_lumieres % 2) == 0: 
				global d
				#d = "thread_" + str(10 + compteur_lumieres)
				d = Lumiere()
				d.start()
			else :
				d.stop()
		elif request == 'EXIT':
 			# Exit the program
			print 'exit'
			global SortieAnticipe
			SortieAnticipe = True
		else:
			# Unknown command
			print 'Special command "%s" not recognised' % (request)



class Timer(Thread):
	"""Thread qui permet de mesurer le temps du programme"""
		
	def __init__(self):
		Thread.__init__(self)


	def run(self):
		"""code à executer pdt le thread"""
		t_end = time.time() + 90
		i = 0
		global SortieAnticipe
		while (time.time() < t_end) and SortieAnticipe == False:
			i += 1
			time.sleep(5)
			print str(i*5) + " secondes..."
			#print SortieAnticipe
		if SortieAnticipe == False:
			print ("le temps est écoulé, appuyez sur echap")
		else :
			print ("le temps imparti n'a pas été dépassé")



class StopT(Thread):
	"""Thread qui permet de stopper le programme"""	
	def __init__(self):
		Thread.__init__(self)
		self.Terminated = False
	def run(self):
		"""code à  executer pdt le thread"""
		global SortieAnticipe
		while  SortieAnticipe == False and self.Terminated == False:
			raw_input('Presser Entrer pour terminer le programme\n')
			SortieAnticipe = True
		print "stop s'arrete"
	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True

class Gyrophares(Thread):
	"""Thread qui permet de faire autre chose pdt le thread principal"""	
	def __init__(self):
		Thread.__init__(self)
		self.Terminated = False
	def run(self):
		"""code à  executer pdt le thread"""
		global SortieAnticipe
		print "Gyrophares allumés !"
		while  SortieAnticipe == False and self.Terminated == False:
			gyro()
			print "PIN......."
			print ".......PON"
			time.sleep(0.5)
		print 'Gyro éteints'

	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True

class Phares(Thread):
	"""Thread qui permet """	
	def __init__(self):
		Thread.__init__(self)
		self.Terminated = False
	def run(self):
		"""code à executer pdt le thread"""
		global SortieAnticipe
		print "LES PHARES SONT ALLUMES !"
		while  SortieAnticipe == False and self.Terminated == False:
			tata(1)
		print "Les PHARES SONT ETEINTS !"
	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True


class Lumiere(Thread):
	"""Thread qui permet de faire clignoter le rail de LED"""	
	def __init__(self):
		Thread.__init__(self)
		self.Terminated = False
	def run(self):
		"""code Ã  executer pdt le thread"""
		global SortieAnticipe
		while  SortieAnticipe == False and self.Terminated == False:
			lumieres()
	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True


class Slider(Thread):
	"""Thread qui permet d'activer le Slider de LED en mode K2000"""	
	def __init__(self):
		Thread.__init__(self)
		self.Terminated = False
	def run(self):
		"""code Ã  executer pdt le thread"""
		global SortieAnticipe
		while  SortieAnticipe == False and self.Terminated == False:
			toto(1)
	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True

class Slider2(Thread):
	"""Thread qui permet d'activer le Slider de LED"""	
	def __init__(self):
		Thread.__init__(self)
		self.Terminated = False
	def run(self):
		"""code Ã  executer pdt le thread"""
		global SortieAnticipe
		while  SortieAnticipe == False and self.Terminated == False:
			toto2(1)
	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True

class Hymne(Thread):
	"""Thread qui permet de jouer des sons"""	
	def __init__(self):
		Thread.__init__(self)
		self.Terminated = False
	def run(self):
		"""code Ã  executer pdt le thread"""
		global SortieAnticipe
		while  SortieAnticipe == False and self.Terminated == False:
			soundChannelA.play(soundA)
			print "Allons enfants de la patrie !"
			print "lalalalalalallaaaaa...."
			#time.sleep(2)
	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True

class Recepteur(Thread):
	"""Thread qui recoit les commandes via socket"""	
	def __init__(self):
		Thread.__init__(self)
		self.Terminated = False

	def run(self):
		global SortieAnticipe
		#global isRunning
		remoteKeyBorgServer = SocketServer.UDPServer(('', portListen), PicoBorgHandler)
		print "reception en cours"
		while  SortieAnticipe == False and self.Terminated == False:
			remoteKeyBorgServer.handle_request()			
		print 'Reception Terminée'

	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True

def main():
	try:

		debutProg = time.time()
		#print "touches : \n G: Gyro \n P: Phares \n K: Slider \n L: Light \n H: Son \n Fleches : Deplacement \n ESC: Fin du programme"
		# Création des threads
		thread_4 = Timer()
		#thread_3 = StopT()
		thread_5 = Recepteur()
		# Lancement des threads
		#thread_3.start()
		thread_4.start()
		thread_5.start()
		# Attend que les threads se terminent
		#thread_3.join()
		#thread_1.join()
		thread_4.join()
		finProg = time.time()
		print 'prog terminé en : ' + str(finProg-debutProg) + ' sec'
		seconds = finProg-debutProg
		m, s = divmod(seconds, 60)
		h, m = divmod(m, 60)
		print "soit : %d:%02d:%02d" % (h, m, s)
		Recepteur().stop()
		print 'recepteur terminé'
		finProgs()
		GPIO.cleanup()	
	except KeyboardInterrupt:
		print 'Terminé de manière anticipée'
		finProg = time.time()
		print 'prog terminé en : ' + str(finProg-debutProg) + ' sec'
		seconds = finProg-debutProg
		m, s = divmod(seconds, 60)
		h, m = divmod(m, 60)
		print "soit : %d:%02d:%02d" % (h, m, s)
		finProgs()
		GPIO.cleanup()

if __name__=='__main__':
	main()	


