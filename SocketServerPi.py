#!/usr/bin/env python
# coding: Latin-1
 
# Load library functions we want
import SocketServer
import os,time
import datetime
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
 
# Set which GPIO pins the drive outputs are connected to
DRIVE_1 = 4
DRIVE_2 = 18
DRIVE_3 = 8
DRIVE_4 = 7
 
# Set all of the drive pins as output pins
#GPIO.setup(DRIVE_1, GPIO.OUT)
#GPIO.setup(DRIVE_2, GPIO.OUT)
#GPIO.setup(DRIVE_3, GPIO.OUT)
#GPIO.setup(DRIVE_4, GPIO.OUT)
 
# Map of drives to pins
lDrives = [DRIVE_1, DRIVE_2, DRIVE_3, DRIVE_4]
 
# Function to set all drives off
#def MotorOff():
#    GPIO.output(DRIVE_1, GPIO.LOW)
#    GPIO.output(DRIVE_2, GPIO.LOW)
#    GPIO.output(DRIVE_3, GPIO.LOW)
#    GPIO.output(DRIVE_4, GPIO.LOW)
 
# Settings for the RemoteKeyBorg server
portListen = 9038                       # What messages to listen for (LEDB on an LCD)
 

fichier_log = open("log_socket.txt", "a")

def ecrire(param):
    heure = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    fichier_log.write(heure + ' : ' + param + '\n')



# Class used to handle UDP messages
class PicoBorgHandler(SocketServer.BaseRequestHandler):
    # Function called when a new message has been received
    def handle(self):
        global isRunning
 
        request, socket = self.request          # Read who spoke to us and what they said
        request = request.upper()               # Convert command to upper case
        driveCommands = request.split(',')      # Separate the command into individual drives
        if len(driveCommands) == 1:
            # Special commands
            if request == 'ALLOFF':
                # Turn all drives off
                #MotorOff()
                print 'All drives off'
                ecrire(request)
            elif request == 'EXIT':
                # Exit the program
                ecrire(request)
                isRunning = False
            else:
                # Unknown command
                print 'Special command "%s" not recognised' % (request)
        elif len(driveCommands) == len(lDrives):
            print 'reception'
            # For each drive we check the command
            for driveNo in range(len(driveCommands)):
                command = driveCommands[driveNo]
                if command == 'ON':
                    # Set drive on
                    print 'ON'
                    ecrire(request)
                    #GPIO.output(lDrives[driveNo], GPIO.HIGH)
                elif command == 'OFF':
                    # Set drive off
                    print 'off'
                    ecrire(request)
                    #GPIO.output(lDrives[driveNo], GPIO.LOW)
                elif command == 'X':
                    # No command for this drive
                    pass
                else:
                    # Unknown command
                    print 'Drive %d command "%s" not recognised!' % (driveNo, command)
        else:
            # Did not get the right number of drive commands
            print 'Command "%s" did not have %d parts!' % (request, len(lDrives))
 
try:
    global isRunning
 
    # Start by turning all drives off
    #MotorOff()
    raw_input('You can now turn on the power, press ENTER to continue')
    debutProg = time.time()
    # Setup the UDP listener
    remoteKeyBorgServer = SocketServer.UDPServer(('', portListen), PicoBorgHandler)
    # Loop until terminated remotely
    isRunning = True
    while isRunning:
        remoteKeyBorgServer.handle_request()
    # Turn off the drives and release the GPIO pins
    print 'Finished'
    #MotorOff()
    raw_input('Turn the power off now, press ENTER to continue')
    #GPIO.cleanup()
    fichier_log.close()
    finProg = time.time()
    print 'prog terminé en : ' + str(finProg-debutProg) + ' sec'
    seconds = finProg-debutProg
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    print "soit : %d:%02d:%02d" % (h, m, s)
except KeyboardInterrupt:
    # CTRL+C exit, turn off the drives and release the GPIO pins
    print 'Terminated'
    #MotorOff()
    raw_input('Turn the power off now, press ENTER to continue')
    #GPIO.cleanup()
    fichier_log.close()
    finProg = time.time()
    print 'prog terminé en : ' + str(finProg-debutProg) + ' sec'
    seconds = finProg-debutProg
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    print "soit : %d:%02d:%02d" % (h, m, s)
