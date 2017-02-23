# Carrega as bibliotecas
#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import MySQLdb
import time
import sys

import Adafruit_GPIO.MCP230xx as MCP
import Adafruit_GPIO as GPIO


mcp = MCP.MCP23017()
mcp.setup(0, GPIO.OUT)


db = MySQLdb.connect(host="localhost", user="root", passwd="zabbix", db="Automacao")
cursor = db.cursor()

cursor.execute("SELECT * FROM Rele")

for row in cursor.fetchall() : 
 


	NumeroGPIO = int(row[3])
	Status     = str(row[2])
                        

	if Status == '1':

             mcp.output(NumeroGPIO, True)

	else:

		  mcp.output(NumeroGPIO, False)


cursor.close()


db.close ()

