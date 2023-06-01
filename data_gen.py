import time
import csv
import RPi.GPIO as gpio
import serial

x_value = 0
total_1 = 0
total_2 = 0

try:
	arduino = serial.Serial("/dev/ttyACM0", 9600)
except:
	print("Arduino não identificado")
	exit()
	
def cleaner():
	valor_recebido = arduino.readline()
	try:
		str_value = valor_recebido.decode("utf-8")
		if ((str_value.count("x")) < 1):
			splited_value[0] = 0.00
			splited_value[1] = 0.00
			return
		splited_value = valor_recebido.decode("utf-8").split("x")
		one = splited_value[0].strip(" ")
		two = splited_value[1].strip(" ")
		if type(one) == None:
			one = "0"
		if type(two) == None:
			two = "0"
		if len(one) > 4:
			one = one[0:4]
		one = float(one)
		if len(two) > 5:
			two = two[0:4]
		two = float(two)
		splited_value[0] = one
		splited_value[1] = two
		return (splited_value)
	except:
		print("Retorno nesse ponto")
		splited_value[0] = 0.00
		splited_value[1] = 0.00
		return (splited_value)


fieldnames = ["x_value", "total_1", "total_2"]

with open('data.csv', 'w') as csv_file:
	csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	csv_writer.writeheader()
	
while True:
	with open('data.csv', 'a') as csv_file:
		csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		info = {
			"x_value":x_value,
			"total_1":total_1,
			"total_2":total_2
		}
		csv_writer.writerow(info)
		print(x_value, total_1,total_2)
		x_value += 1
		splited_value = cleaner()
		total_1 = splited_value[0] 
		total_2 = splited_value[1]

	time.sleep(1)
