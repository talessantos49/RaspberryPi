#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation
import RPi.GPIO as gpio
import serial
import numpy as np
import pandas as pd

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

def animate(i):
#	x = contador
#	y1 = splited_value[0]
#	y2 = splited_value[1]
	data = pd.read_csv('data.csv')
	x = data['x_value']
	upline = data['total_1']
	downline = data['total_2']
	
	plt.cla()
	
	plt.plot(x, upline, '--', color='blue')
	plt.plot([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
	plt.plot(x, downline, '--', color='red')
	plt.tight_layout()
	

		
#while (True):


	#ax.clear()
	#ax.set_xlim([0, eixo_x])
	#ax.set_ylim([-5, 5])

	#ax.plot(upline, '--', color='blue')
	#ax.plot([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
	#ax.plot(downline, '--', color='red')
	#plt.pause(0.05)
	#plt.pause(.000001)
#contador = contador + 1
#if (contador > eixo_x):
#	upline.pop(0)
#	downline.pop(0)
ani = FuncAnimation(plt.gcf(), animate, interval=500)
plt.tight_layout()
plt.show()
