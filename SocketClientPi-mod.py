#!/usr/bin/env python
# coding: Latin-1
 
# Load library functions we want
import socket
import time
import pygame
 
# Settings for the RemoteKeyBorg client
broadcastIP = '172.16.18.146'           # IP address to send to, 255 in one or more positions is a broadcast / wild-card (IP address to send to (Raspberry Pi with the PicoBorg), may be a single machine (e.g. 192.168.1.5) or a broadcast (e.g. 192.168.1.255) where '255' is used to indicate that number is everybody)
broadcastPort = 9038                    # What message number to send with (LEDB on an LCD)
leftDrive = 1                           # Drive number for left motor
rightDrive = 4                          # Drive number for right motor
interval = 1 #0.1                          # Time between keyboard updates in seconds, smaller responds faster but uses more processor time
regularUpdate = False #True                    # If True we send a command at a regular interval, if False we only send commands when keys are pressed or released
 
# Setup the connection for sending on
sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)       # Create the socket
sender.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)                        # Enable broadcasting (sending to many IPs based on wild-cards)
sender.bind(('0.0.0.0', 0))                                                         # Set the IP and port number to use locally, IP 0.0.0.0 means all connections and port 0 means assign a number for us (do not care)
 
# Setup pygame and key states
global hadEvent
global avance
global arriere
global gauche
global droite
global moveQuit
global gyroOn
global phare
hadEvent = True
avance = False
arriere = False
gauche = False
droite = False
moveQuit = False
gyroOn = False
phare = False
pygame.init()
screen = pygame.display.set_mode([300,300])
pygame.display.set_caption("RemoteKeyBorg - Press [ESC] to quit")
 
# Function to handle pygame events
def PygameHandler(events):
    # Variables accessible outside this function
    global hadEvent
    global avance
    global arriere
    global droite
    global gauche
    global moveQuit
    global gyroOn
    global phare
    # Handle each event individually
    for event in events:
        if event.type == pygame.QUIT:
            # User exit
            hadEvent = True
            moveQuit = True
        elif event.type == pygame.KEYDOWN:
            # A key has been pressed, see if it is one we want
            #hadEvent = True
            if event.key == pygame.K_UP:
                sender.sendto('AVAN', (broadcastIP, broadcastPort))
                avance = True
                print "Up"
            elif event.key == pygame.K_DOWN:
                sender.sendto('ARRI', (broadcastIP, broadcastPort))
                arriere = True
                print "Down"
            elif event.key == pygame.K_LEFT:
                sender.sendto('GAUC', (broadcastIP, broadcastPort))
                gauche = True
                print "Left"
            elif event.key == pygame.K_RIGHT:
                sender.sendto('DROI', (broadcastIP, broadcastPort))
                droite = True
                print "Right"
            elif event.key == pygame.K_ESCAPE:
                sender.sendto('EXIT', (broadcastIP, broadcastPort))
                moveQuit = True
                hadEvent = True
                print "Quit"
            elif event.key == pygame.K_g:
                sender.sendto('GYRO', (broadcastIP, broadcastPort))
                gyroOn = True
                print "GYRO"
            elif event.key == pygame.K_p:
                sender.sendto('PHAR', (broadcastIP, broadcastPort))
                phare = True
                print "PHARES"
            elif event.key == pygame.K_h:
                sender.sendto('HYMNE', (broadcastIP, broadcastPort))
                #phare = True
                print "Hymnes"
            elif event.key == pygame.K_k:
                sender.sendto('K2000', (broadcastIP, broadcastPort))
                #phare = True
                print "k2000"
            elif event.key == pygame.K_j:
                sender.sendto('SLIDER2', (broadcastIP, broadcastPort))
                #phare = True
                print "SLIDER2"
            elif event.key == pygame.K_l:
                sender.sendto('LUMIERE', (broadcastIP, broadcastPort))
                #phare = True
                print "Lumieres"			
        elif event.type == pygame.KEYUP:
            # A key has been released, see if it is one we want
            #hadEvent = True
            if event.key == pygame.K_UP:
                avance = False
                sender.sendto('STOP', (broadcastIP, broadcastPort))
            elif event.key == pygame.K_DOWN:
                arriere = False
                sender.sendto('STOP_ARRI', (broadcastIP, broadcastPort))
            elif event.key == pygame.K_LEFT:
                gauche = False
                sender.sendto('STOP_GAUC', (broadcastIP, broadcastPort))
            elif event.key == pygame.K_RIGHT:
                droite = False
                sender.sendto('STOP_DROI', (broadcastIP, broadcastPort))
            elif event.key == pygame.K_ESCAPE:
                moveQuit = False
            elif event.key == pygame.K_g:
                gyroOn = False
            elif event.key == pygame.K_p:
                phare = False
				
try:
    print 'Press [ESC] to quit'
    # Loop indefinitely
    while True:
        # Get the currently pressed keys on the keyboard
        PygameHandler(pygame.event.get())
        if hadEvent or regularUpdate:
            # Keys have changed, generate the command list based on keys
            hadEvent = False
            driveCommands = ['X']
            if moveQuit:
                break
            elif gyroOn:
                driveCommands[leftDrive - 1] = 'GYRO'
            elif phare:
                driveCommands[leftDrive - 1] = 'PHARE'
            elif avance:
                driveCommands[leftDrive - 1] = 'AVAN'
            elif droite:
                driveCommands[leftDrive - 1] = 'DROI'
            elif gauche:
                driveCommands[leftDrive - 1] = 'GAUC'
            elif arriere:
                driveCommands[leftDrive - 1] = 'ARRI'
            else:
                print 'commande non reconnue'
            # Send the drive commands
            command = ''
            for driveCommand in driveCommands:
                command += driveCommand + ','
            command = command[:-1]                                  # Strip the trailing comma
            sender.sendto(command, (broadcastIP, broadcastPort))
            print command
        # Wait for the interval period
        time.sleep(interval)
    # Inform the server to stop
    sender.sendto('EXIT', (broadcastIP, broadcastPort))
except KeyboardInterrupt:
    # CTRL+C exit, inform the server to stop
    sender.sendto('EXIT', (broadcastIP, broadcastPort))


