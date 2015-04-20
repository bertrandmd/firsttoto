#!/usr/bin/env python 
import time,random

serie = [1,2,3,4,5]

#while 1:
def toto(x):
	for i in range (0,x):
		for i in serie:
			print i
			time.sleep(0.2)
		#serie.reverse()
		random.shuffle(serie)	
		i=i+1

def tata(x):
	if (len(serie) % 2) == 0: 
		for i in range (0,x):
			for i in range (0,len(serie)/2):
				#print str(serie[0]) + " " + str(serie[-1])
				print "%s %s" % (serie[0+i], serie[-1-i])			
				time.sleep(0.2)
				i=i+1
			i=len(serie)/2
			for i in range (len(serie)/2,0,-1):
				print "%s %s" % (serie[-1+i], serie[0-i])			
				time.sleep(0.2)
				i=i-1
	else:
		for i in range (0,x):
			for i in range (0,len(serie)/2):
				print "%s %s" % (serie[0+i], serie[-1-i])			
				time.sleep(0.2)
				i=i+1
			print serie[int(round(len(serie)/2,0))]
			print serie[int(round(len(serie)/2,0))]
			for i in range (len(serie)/2,0,-1):
				print "%s %s" % (serie[-1+i], serie[0-i])			
				time.sleep(0.2)
				i=i+1

def main():
	print "entrer un nbre de boucle :"
	x = input()
	#toto(x)
	tata(x)

if __name__=='__main__':
	main()
