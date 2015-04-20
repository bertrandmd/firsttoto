#!/usr/bin/env python
# -*-coding:Latin-1 -*

import time
import sys
from threading import Thread
import pygame
from pygame.locals import *
import RPi.GPIO as GPIO # bibliothèque pour utiliser les GPIO


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

#23off = GPIO.output(23,GPIO.LOW)
#25off = GPIO.output(25,GPIO.LOW)
#22off = GPIO.output(22,GPIO.LOW)
#24off = GPIO.output(24,GPIO.LOW)

#1off = GPIO.output(4,GPIO.LOW)
#2off = GPIO.output(17,GPIO.LOW)
#3off = GPIO.output(18,GPIO.LOW)
#4off = GPIO.output(7,GPIO.LOW)
#5off = GPIO.output(27,GPIO.LOW)

#23on = GPIO.output(23,GPIO.HIGH)
#25on = GPIO.output(25,GPIO.HIGH)
#22on = GPIO.output(22,GPIO.HIGH)
#24on = GPIO.output(24,GPIO.HIGH)

#1on = GPIO.output(4,GPIO.HIGH)
#2on = GPIO.output(17,GPIO.HIGH)
#3on = GPIO.output(18,GPIO.HIGH)
#4on = GPIO.output(7,GPIO.HIGH)
#5on = GPIO.output(27,GPIO.HIGH)


#22off
#23off
#24off
#25off




pygame.init()
screen = pygame.display.set_mode((64, 48))
pygame.display.set_caption('KeyB Caption')
pygame.mouse.set_visible(0)

pygame.mixer.init(48000, -16, 1, 1024)
#soundA = pygame.mixer.Sound("darth.mp3")
soundA = pygame.mixer.Sound("r2d2.wav")

soundChannelA = pygame.mixer.Channel(1)


SortieAnticipe = False
a = ""	

def avancer():
	print "GAZZZZZZZZZZZZZZZ"
	GPIO.output(25,GPIO.HIGH) # sortie au niveau logique haut (3.3 V)
def droite():
	print "GAZZZZZZZZZZZZZZZ"
	GPIO.output(23,GPIO.HIGH) # sortie au niveau logique haut (3.3 V)
def gauche():
	print "GAZZZZZZZZZZZZZZZ"
	GPIO.output(22,GPIO.HIGH) # sortie au niveau logique haut (3.3 V)
def arriere():
	print "GAZZZZZZZZZZZZZZZ"
	GPIO.output(24,GPIO.HIGH) # sortie au niveau logique haut (3.3 V)

def stop():
        print "ARRRRREEEEEET !!!!"
        GPIO.output(25,GPIO.LOW) # sortie au niveau logique bas (0 V)
	GPIO.output(24,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(24,GPIO.LOW)	

def stopDroite():
        print "ARRRRREEEEEET !!!!"
        GPIO.output(23,GPIO.LOW) # sortie au niveau logique bas (0 V)
def stopGauche():
        print "ARRRRREEEEEET !!!!"
        GPIO.output(22,GPIO.LOW) # sortie au niveau logique bas (0 V)
def stopArriere():
        print "ARRRRREEEEEET !!!!"
        GPIO.output(24,GPIO.LOW) # sortie au niveau logique bas (0 V)


def gyro():
	GPIO.output(23,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(23,GPIO.LOW)
	time.sleep(0.2)
	GPIO.output(24,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(24,GPIO.LOW)

def phares():
	GPIO.output(25,GPIO.HIGH)
def pharesEteints():
	GPIO.output(25,GPIO.LOW)
	

def lumieres():
	for i in range(0,4) :
		GPIO.output(4,GPIO.HIGH)
		GPIO.output(17,GPIO.HIGH)
		GPIO.output(18,GPIO.HIGH)
		GPIO.output(7,GPIO.HIGH)
		GPIO.output(27,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(4,GPIO.LOW)
		GPIO.output(17,GPIO.LOW)
		GPIO.output(18,GPIO.LOW)
		GPIO.output(7,GPIO.LOW)
		GPIO.output(27,GPIO.LOW)
		i = i+1



class Clavier(Thread):
	"""Thread qui permet d'interagir dans le main() au clavier"""
		
	def __init__(self): #(self, thread5):
		Thread.__init__(self)
		#self.thread5 = thread5

	def run(self):
		"""code Ã  executer pdt le thread"""
		done = False
		compteur_hymne = 1
		compteur_gyro = 1
		compteur_phares = 1
		compteur_lumieres = 1
		while not done:
			#global thread_5
			global SortieAnticipe
			for event in pygame.event.get():
				if (event.type == KEYUP):
					if (event.type == KEYUP and event.key == K_UP):
						print("pi n'avance plus !")
						stop()
					if (event.type == KEYUP and event.key == K_DOWN):
						print("pi ne recule plus !")
						stopArriere()
					if (event.type == KEYUP and event.key == K_RIGHT):
						print("pi se rÃ©axe !")
						stopDroite()
					if (event.type == KEYUP and event.key == K_LEFT):
						print("pi se rÃ©axe !")
						stopGauche()
				if (event.type == KEYDOWN):
					if (event.type == KEYDOWN and event.key == K_ESCAPE):
						done = True
						SortieAnticipe = True		
						print("SORTIE")	
					if (event.type == KEYDOWN and event.key == K_UP):
						print("pi avance !")
						avancer()
					if (event.type == KEYDOWN and event.key == K_RIGHT):
						print("tourne a droite")
						droite()	
					if (event.type == KEYDOWN and event.key == K_LEFT):
						print("tourne a gauche")
						gauche()	
					if (event.type == KEYDOWN and event.key == K_DOWN):
						print("marche arriere")
						arriere()
					if (event.type == KEYDOWN and event.key == K_h):
						compteur_hymne = compteur_hymne + 1
						if (compteur_hymne % 2) == 0: 
							global a
							a = "thread_" + str(10 + compteur_hymne)
							a = Hymne()
							a.start()
						else :
							a.stop()

					if (event.type == KEYDOWN and event.key == K_g):
						compteur_gyro = compteur_gyro + 1
						if (compteur_gyro % 2) == 0: 
							global b
							b = "thread_" + str(10 + compteur_gyro)
							b = Gyrophares()
							b.start()
						else :
							b.stop()

					if (event.type == KEYDOWN and event.key == K_p):
						compteur_phares = compteur_phares + 1
						if (compteur_phares % 2) == 0: 
							global c
							c = "thread_" + str(10 + compteur_phares)
							c = Phares()
							c.start()
						else :
							c.stop()

					if (event.type == KEYDOWN and event.key == K_l):
						compteur_lumieres = compteur_lumieres + 1
						if (compteur_lumieres % 2) == 0: 
							global d
							d = "thread_" + str(10 + compteur_lumieres)
							d = Lumiere()
							d.start()
						else :
							d.stop()


class Timer(Thread):
	"""Thread qui permet d'interagir dans le main() au clavier"""
		
	def __init__(self):
		Thread.__init__(self)


	def run(self):
		"""code Ã  executer pdt le thread"""
		t_end = time.time() + 80
		i = 0
		global SortieAnticipe
		while (time.time() < t_end) and SortieAnticipe == False:
			i += 1
			time.sleep(5)
			print str(i*5) + " secondes..."
			print SortieAnticipe
		if SortieAnticipe == False:
			print ("le temps est Ã©coulÃ©, appuyez sur echappe")
		else :
			print ("le temps imparti n'a pas Ã©tÃ© dÃ©passÃ©")
			

class Hymne(Thread):
	"""Thread qui permet """	
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
			time.sleep(2)
	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True

class Gyrophares(Thread):
	"""Thread qui permet """	
	def __init__(self):
		Thread.__init__(self)
		self.Terminated = False
	def run(self):
		"""code Ã  executer pdt le thread"""
		global SortieAnticipe
		print "Gyrophares allumÃ©s !"
		while  SortieAnticipe == False and self.Terminated == False:
			gyro()
			#print "PIN......."
			#print ".......PON"
			#time.sleep(0.5)
	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True

class Phares(Thread):
	"""Thread qui permet """	
	def __init__(self):
		Thread.__init__(self)
		self.Terminated = False
	def run(self):
		"""code Ã  executer pdt le thread"""
		global SortieAnticipe
		print "LES PHARES SONT ALLUMES !"
		phares()
		while  SortieAnticipe == False and self.Terminated == False:
			pass
		print "Les PHARES SONT ETEINTS !"
		pharesEteints()
	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True
	#def allumerPhares(self)
	#	print "LES PHARES SONT ALLUMES !"
	#def eteindrePhares(self)
	#	print "LES PHARES SONT ETEINTS !"


class Lumiere(Thread):
	"""Thread qui permet """	
	def __init__(self):
		Thread.__init__(self)
		self.Terminated = False
	def run(self):
		"""code Ã  executer pdt le thread"""
		global SortieAnticipe
		while 