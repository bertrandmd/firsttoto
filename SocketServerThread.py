#!/usr/bin/env python
# coding: Latin-1

### multi-thread a travers un socket

# Load library functions we want
import SocketServer
import os,time
from threading import Thread
import datetime
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)



# Settings for the RemoteKeyBorg server
portListen = 9038   

SortieAnticipe = False


# Class used to handle UDP messages
class PicoBorgHandler(SocketServer.BaseRequestHandler):
	# Function called when a new message has been received
	def handle(self):
		print 'pico lance'
		#global isRunning
		request, socket = self.request          # Read who spoke to us and what they said
		request = request.upper()               # Convert command to upper case
		driveCommands = request.split(',')      # Separate the command into individual drives
		compteur_gyro = 1
		print 'requete : ' + request
		print 'longueur message : ' + str(len(driveCommands))
		if len(driveCommands) == 1:
			# Special commands
			print 'message recu'
			if request == 'ALLOFF':
				# Turn all drives off
				#MotorOff()
				print 'All drives off'
		
		#ecrire(request)
			elif request == 'GYRO':
				compteur_gyro = compteur_gyro + 1
				if (compteur_gyro % 2) == 0: 				
					global b
					b = "thread_" + str(10 + compteur_gyro)
					b = Gyrophares()
					b.start()
				else :
					b.stop()				
			elif request == 'EXIT':
				print 'exit'
 				# Exit the program
				#ecrire(request)
				#isRunning = False
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
			print SortieAnticipe
		if SortieAnticipe == False:
			print ("le temps est écoulé, appuyez sur echap")
		else :
			print ("le temps imparti n'a pas été dépassé")



class Stop(Thread):
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
			print "PIN......."
			print ".......PON"
			time.sleep(0.5)
			global SortieAnticipe
			print 'la fin...'
			SortieAnticipe = True
	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True


class Recepteur(Thread):
	"""Thread qui permet d'interagir pdt le thread principal"""	
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
			# Loop until terminated remotely
			#isRunning = True
			#while isRunning:
				
		print 'Reception Terminée'

	def stop(self):
		"""methode pour arreter proprement le thread"""
		self.Terminated = True

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
		print 'clavier s arrete'

def main():
	try:

		debutProg = time.time()
		print "touches : \n G: Gyro \n P: Phares \n K: Slider \n L: Light \n H: Son \n Fleches : Deplacement \n ESC: Fin du programme"
		# Création des threads
		thread_1 = Clavier()
		thread_4 = Timer()
		thread_3 = Stop()
		thread_5 = Recepteur()
		# Lancement des threads
		#thread_1.start()
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
		#thread_3.stop()
		#print 'stop terminé'		
	except KeyboardInterrupt:
		print 'Terminé de manière anticipée'
		finProg = time.time()
		print 'prog terminé en : ' + str(finProg-debutProg) + ' sec'
		seconds = finProg-debutProg
		m, s = divmod(seconds, 60)
		h, m = divmod(m, 60)
		print "soit : %d:%02d:%02d" % (h, m, s)



if __name__=='__main__':
	main()	


