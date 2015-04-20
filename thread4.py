#!/usr/bin/env python
# -*-coding:Latin-1 -*

import time
import sys
from threading import Thread
import pygame
from pygame.locals import *
import RPi.GPIO as GPIO # biblioth�que pour utiliser les GPIO


GPIO.setmode(GPIO.BCM) # mode de num�rotation des pins
GPIO.setup(25,GPIO.OUT) # la pin 25 r�gl�e en sortie (output)
GPIO.setup(23,GPIO.OUT) # la pin 23 r�gl�e en sortie (output)
GPIO.setup(22,GPIO.OUT) # la pin 22 r�gl�e en sortie (output)
GPIO.setup(24,GPIO.OUT) # la pin 24 r�gl�e en sortie (output)
GPIO.setup(4,GPIO.OUT) # la pin 25 r�gl�e en sortie (output)
GPIO.setup(17,GPIO.OUT) # la pin 23 r�gl�e en sortie (output)
GPIO.setup(18,GPIO.OUT) # la pin 22 r�gl�e en sortie (output)
GPIO.setup(7,GPIO.OUT) # la pin 24 r�gl�e en sortie (output)
GPIO.setup(27,GPIO.OUT) # la pin 24 r�gl�e en sortie (output)

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
	for i in range(0,1) :
		GPIO.output(4,GPIO.HIGH)
		GPIO.output(17,GPIO.HIGH)
		GPIO.output(18,GPIO.HIGH)
		GPIO.output(7,GPIO.HIGH)
		GPIO.output(27,GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(4,GPIO.LOW)
		GPIO.output(17,GPIO.LOW)
		GPIO.output(18,GPIO.LOW)
		GPIO.output(7,GPIO.LOW)
		GPIO.output(27,GPIO.LOW)
		time.sleep(0.5)
		#print i
		i = i+1


liste = (4,17,18,27,7)

def k2000():
	i=0
	x = 0
	#for i in range(0,3) :
	for i in liste:
		GPIO.output(i,GPIO.HIGH)	
		time.sleep(0.1)
		GPIO.output(i,GPIO.LOW)
	#liste.reverse()
	#for i in liste:
	#	GPIO.output(i,GPIO.HIGH)	
	#	time.sleep(0.1)
	#	GPIO.output(i,GPIO.LOW)	

serie = [17,18,27,7,4]

def toto(x):
	for i in range (0,x):
		for i in serie:
			GPIO.output(i,GPIO.HIGH)	
			time.sleep(0.1)
			GPIO.output(i,GPIO.LOW)
		serie.reverse()
		#random.shuffle(serie)	
		i=i+1
def toto2(x):
	for i in range (0,x):
		for i in serie:
			GPIO.output(i,GPIO.HIGH)	
			time.sleep(0.1)
			GPIO.output(i,GPIO.LOW)
		#serie.reverse()
		#random.shuffle(serie)	
		i=i+1


def tata(x):
	if (len(serie) % 2) == 0: 
		for i in range (0,x):
			for i in range (0,len(serie)/2):
				#print str(serie[0]) + " " + str(serie[-1])
				#print "%s %s" % (serie[0+i], serie[-1-i])
				GPIO.output(serie[0+i],GPIO.HIGH)
				GPIO.output(serie[-1-i],GPIO.HIGH)	
				time.sleep(0.2)
				GPIO.output(serie[0+i],GPIO.LOW)
				GPIO.output(serie[-1-i],GPIO.LOW)			
				time.sleep(0.2)
				i=i+1
			i=len(serie)/2
			for i in range (len(serie)/2,0,-1):
				#print "%s %s" % (serie[-1+i], serie[0-i])			
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
				#print "%s %s" % (serie[0+i], serie[-1-i])			
				time.sleep(0.2)
				GPIO.output(serie[0+i],GPIO.HIGH)
				GPIO.output(serie[-1-i],GPIO.HIGH)	
				time.sleep(0.2)
				GPIO.output(serie[0+i],GPIO.LOW)
				GPIO.output(serie[-1-i],GPIO.LOW)
				i=i+1
			time.sleep(0.2)
			#print serie[int(round(len(serie)/2,0))]
			GPIO.output(serie[int(round(len(serie)/2,0))],GPIO.HIGH)
			time.sleep(0.2)
			GPIO.output(serie[int(round(len(serie)/2,0))],GPIO.LOW)
			#time.sleep(0.2)
			#print serie[int(round(len(serie)/2,0))]
			#GPIO.output(serie[int(round(len(serie)/2,0))],GPIO.HIGH)
			#time.sleep(0.2)
			#GPIO.output(serie[int(round(len(serie)/2,0))],GPIO.LOW)
			for i in range (len(serie)/2,0,-1):
				#print "%s %s" % (serie[-1+i], serie[0-i])			
				time.sleep(0.2)
				GPIO.output(serie[-1+i],GPIO.HIGH)
				GPIO.output(serie[0-i],GPIO.HIGH)	
				time.sleep(0.2)
				GPIO.output(serie[-1+i],GPIO.LOW)
				GPIO.output(serie[0-i],GPIO.LOW)
				i=i+1



def finProgs():
	GPIO.output(23,GPIO.LOW)
	GPIO.output(25,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	GPIO.output(24,GPIO.LOW)
	GPIO.output(4,GPIO.LOW)
	GPIO.output(17,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)
	GPIO.output(7,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)

class Clavier(Thread):
	"""Thread qui permet d'interagir dans le main() au clavier"""
		
	def __init__(self): #(self, thread5):
		Thread.__init__(self)
		#self.thread5 = thread5

	def run(self):
		"""code à executer pdt le thread"""
		done = False
		compteur_hymne = 1
		compteur_gyro = 1
		compteur_phares = 1
		compteur_lumieres = 1
		compteur_slider = 1
		compteur_slider2 = 1
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
						print("pi se réaxe !")
						stopDroite()
					if (event.type == KEYUP and event.key == K_LEFT):
						print("pi se réaxe !")
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
							c.join()
						else :
							c.stop()

					if (event.type == KEYDOWN and event.key == K_l):
						compteur_lumieres = compteur_lumieres + 1
						if (compteur_lumieres % 2) == 0: 
							global d
							d = "thread_" + str(10 + compteur_lumieres)
							d = Lumiere()
							d.start()
							d.join()
						else :
							d.stop()

					if (event.type == KEYDOWN and event.key == K_k):
						compteur_slider = compteur_slider + 1
						if (compteur_slider % 2) == 0: 
							global e
							e = "thread_" + str(10 + compteur_slider)
							e = Slider()
							e.start()
							e.join()
						else :
							e.stop()

					if (event.type == KEYDOWN and event.key == K_s):
						compteur_slider2 = compteur_slider2 + 1
						if (compteur_slider2 % 2) == 0: 
							global f
							f = "thread_" + str(10 + compteur_slider2)
							f = Slider2()
							f.start()
							f.join()
						else :
							f.stop()


class Timer(Thread):
	"""Thread qui permet d'interagir dans le main() au clavier"""
		
	def __init__(self):
		Thread.__init__(self)


	def run(self):
		"""code à executer pdt le thread"""
		t_end = time.time() + 80
		i = 0
		global SortieAnticipe
		while (time.time() < t_end) and SortieAnticipe == False:
			i += 1
			time.sleep(5)
			print str(i*5) + " secondes..."
			print SortieAnticipe
		if SortieAnticipe == False:
			print ("le temps est écoulé, appuyez sur echappe")
		else :
			print ("le temps imparti n'a pas été dépassé")
			

class Hymne(Thread):
	"""Thread qui permet """	
	def __init__(self):
		Thread.__init__(self)
		self.Terminated = False
	def run(self):
		"""code à executer pdt le thread"""
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
		"""code à executer pdt le thread"""
		global SortieAnticipe
		print "Gyrophares allumés !"
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
		"""code � executer pdt le thread"""
		global SortieAnticipe
		print "LES PHARES SONT ALLUMES !"
		while  SortieAnticipe == False and self.Terminated == False:
			tata(1)
		print "Les PHARES SONT ETEINTS !"
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
		"""code à executer pdt le thread"""
		global SortieAnticipe
		print "Gyrophares allumés !"
		while  SortieAnticipe == False and self.Terminated == False:
			lumieres()
	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True


class Slider(Thread):
	"""Thread qui permet """	
	def __init__(self):
		Thread.__init__(self)
		self.Terminated = False
	def run(self):
		"""code à executer pdt le thread"""
		global SortieAnticipe
		print "Gyrophares allumés !"
		while  SortieAnticipe == False and self.Terminated == False:
			toto(1)
	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True

class Slider2(Thread):
	"""Thread qui permet """	
	def __init__(self):
		Thread.__init__(self)
		self.Terminated = False
	def run(self):
		"""code à executer pdt le thread"""
		global SortieAnticipe
		while  SortieAnticipe == False and self.Terminated == False:
			toto2(1)
	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True

def main():
	debutProg = time.time()
	print "touches : \n G: Gyro \n P: Phares \n K: Slider \n L: Light \n H: Son \n Fleches : Deplacement \n ESC: Fin du programme"
	# Cr�ation des threads
	#thread_5 = Hymne()
	#thread_1 = Enumerateur(text)
	#thread_2 = Enumerateur(text2)
	thread_3 = Clavier()
	#thread_3 = Clavier(thread_5)
	thread_4 = Timer()
	#thread_5 = Hymne()
	#thread_6 = Lumiere()
	#thread_7 = Slider()
	#thread_8 = Slider2()

	# Lancement des threads
	#thread_1.start()
	#thread_2.start()
	thread_3.start()
	thread_4.start()
	# Attend que les threads se terminent
	#thread_1.join()
	#thread_2.join()
	thread_3.join()
	thread_4.join()


	finProg = time.time()
	print 'prog termin� en : ' + str(finProg-debutProg) + ' sec'
	seconds = finProg-debutProg
	m, s = divmod(seconds, 60)
	h, m = divmod(m, 60)
	print "soit : %d:%02d:%02d" % (h, m, s)
	finProgs()
	GPIO.cleanup()

if __name__=='__main__':
    main()
