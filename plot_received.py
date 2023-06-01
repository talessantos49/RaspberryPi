#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib import animation
import RPi.GPIO as gpio
import serial
import numpy as np
import time

try:
	arduino = serial.Serial("/dev/ttyACM0", 9600)
except:
	print("Arduino não identificado")
	exit()

upline = []
downline = []
fig, ax = plt.subplots()
splited_value = []
contador = 0
eixo_x = 50

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
		if one == None:
			one = "0"
		if two == None:
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

while (True):
	splited_value = cleaner()
	print(type(splited_value[0]))
	print(type(splited_value[1]))

	upline.append(splited_value[0])
	downline.append(splited_value[1])

	ax.clear()
	ax.set_xlim([0, eixo_x])
	ax.set_ylim([-5, 5])

	ax.plot(upline, '--', color='blue')
	ax.plot([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
	ax.plot(downline, '--', color='red')
	plt.pause(0.05)
	#plt.pause(.000001)
	contador = contador + 1
	if (contador > eixo_x):
		upline.pop(0)
		downline.pop(0)

