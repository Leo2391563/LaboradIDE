import serial
 
serialPort = serial.Serial('COM10', 9600)
while True:
    serialPort.write(b"1")
    print(serialPort.readlines())