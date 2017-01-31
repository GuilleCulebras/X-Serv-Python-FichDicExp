#!/usr/bin/python3

fd= open('/etc/passwd','r')

lineas= fd.readlines()

diccionario= {}

for linea in lineas:
	elementos= linea.split(':')
	login= elementos[0]
	shell= elementos[-1][:-1]

	diccionario[login]= shell

print(diccionario['root'])

try:
	print(diccionario['imaginario'])
except:
	print("login not found")	