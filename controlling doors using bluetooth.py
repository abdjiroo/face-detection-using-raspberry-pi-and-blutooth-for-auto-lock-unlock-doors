import bluetooth
import RPi.GPIO as GPIO #calling for header file which helps in using GPIOs of PI
LOCK=13

GPIO.setmode(GPIO.BCM) #programming the GPIO by BCM pin numbers. (like PIN40 as GPIO21)
GPIO.setwarnings(False)
GPIO.setup(LOCK,GPIO.OUT) #initialize GPIO21 (LOCK) as an output Pin
GPIO.output(LOCK,0)

server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_socket.bind(("",port))
server_socket.listen(1)

client_socket,address = server_socket.accept()
print "Accepted connection from ",address
while 1:

data = client_socket.recv(1024)   “ Variable has the received command from the app”
print "Received: %s" % data
if (data == "0"): #if '0' is sent from the Android App, turn OFF the LOCK
print ("GPIO 21 LOW, LOCK OFF")
GPIO.output(LOCK,0)
if (data == "1"): #if '1' is sent from the Android App, turn OFF the LOCK
print ("GPIO 21 HIGH, LOCK ON")
GPIO.output(LOCK,1)
if (data == "q"):
print ("Quit")
break
