# -*-coding:Latin-1 -*

import time
import sys
from threading import Thread
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((64, 48))
pygame.display.set_caption('KeyB Caption')
pygame.mouse.set_visible(0)


SortieAnticipe = False
a = ""	
		

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
		while not done:
			#global thread_5
			global SortieAnticipe
			for event in pygame.event.get():
				if (event.type == KEYUP):
					if (event.type == KEYUP and event.key == K_UP):
						print("pi n'avance plus !")
					if (event.type == KEYUP and event.key == K_DOWN):
						print("pi ne recule plus !")
					if (event.type == KEYUP and event.key == K_RIGHT):
						print("pi se réaxe !")
					if (event.type == KEYUP and event.key == K_LEFT):
						print("pi se réaxe !")
				if (event.type == KEYDOWN):
					if (event.type == KEYDOWN and event.key == K_ESCAPE):
						done = True
						SortieAnticipe = True		
						print("SORTIE")	
					if (event.type == KEYDOWN and event.key == K_UP):
						print("pi avance !")
					if (event.type == KEYDOWN and event.key == K_RIGHT):
						print("tourne a droite")	
					if (event.type == KEYDOWN and event.key == K_LEFT):
						print("tourne a gauche")	
					if (event.type == KEYDOWN and event.key == K_DOWN):
						print("marche arriere")

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
			print "PIN......."
			print ".......PON"
			time.sleep(0.5)
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
			pass
		print "Les PHARES SONT ETEINTS !"
	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True
	#def allumerPhares(self)
	#	print "LES PHARES SONT ALLUMES !"
	#def eteindrePhares(self)
	#	print "LES PHARES SONT ETEINTS !"

def main():
	debutProg = time.time()
	# Création des threads
	#thread_5 = Hymne()
	#thread_1 = Enumerateur(text)
	#thread_2 = Enumerateur(text2)
	thread_3 = Clavier()
	#thread_3 = Clavier(thread_5)
	thread_4 = Timer()
	#thread_5 = Hymne()

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
	print 'prog terminé en : ' + str(finProg-debutProg) + ' sec'
	seconds = finProg-debutProg
	m, s = divmod(seconds, 60)
	h, m = divmod(m, 60)
	print "soit : %d:%02d:%02d" % (h, m, s)

if __name__=='__main__':
    main()


