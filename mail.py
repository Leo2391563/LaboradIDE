import serial
 
port = serial.Serial('COM10', 9600)
while True:
    if (input("> ")=="1"):
        port.write(b"1")
    else: port.write(b"2")