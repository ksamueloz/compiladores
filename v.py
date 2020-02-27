# -*- coding: utf-8 -*-
import os
import sys
import threading
from time import time

class Potencia():
	def __init__(self, letterOrg):
		self.__letterOrg = letterOrg
		self.__letterVar = letterOrg
		self.__pow=1

	def powL(self):
		self.__pow+=1
		newList=[]

		for x in range(0,len(self.__letterOrg)):
			for y in range(0,len(self.__letterVar)):
				newList.append(self.__letterOrg[x]+self.__letterVar[y])

		self.__letterVar=newList

	def showL(self):
		print("Potencia {}".format(str(self.__pow)))
		print("{λ,",end="")

		for x in range(0,len(self.__letterVar)):
			if x==len(self.__letterVar)-1:
				print(self.__letterVar[x],end="")
			else:
				print(self.__letterVar[x]+",",end="")

		print("}\n")
	def getPow(self):
		return self.__pow


class Filtro():

	def __init__(self, conjunto):
		self.__conjunto = conjunto

	def filter(self):
		caracteres=[]

		if self.__conjunto[0]=="{" and self.__conjunto[len(self.__conjunto)-1]=="}":
				filtro=""
				for x in range(1,len(self.__conjunto)):
					if self.__conjunto[x]=="." or x==len(self.__conjunto)-1 and filtro!="":
						if filtro!="":
							caracteres.append(filtro)
							filtro=""

					elif self.__conjunto[x]!="λ" and self.__conjunto[x]!="ε":
						filtro+=self.__conjunto[x]

		return caracteres
		
		


if __name__ == '__main__':
	if len(sys.argv)>=3:
		conjunto= Filtro(sys.argv[1])

		try:
			potencia=int(sys.argv[2])
		except ValueError:
			print("Error de potencia")
		else:
			tiempo_inicial = time()
			if conjunto.filter() and potencia>0:

				lenguaje=Potencia(conjunto.filter())

				lenguaje.showL()

				nhilos=potencia-1
				
				for x in range(nhilos):
					hilo=threading.Thread(name='hilo%s' %nhilos,target=lenguaje.powL())
					hilo.start()

					hilo2=threading.Thread(name='hilo%s' %nhilos,target=lenguaje.showL())
					hilo2.start()

			else:
				print("{ λ }")

			tiempo_final = time()
			tiempo_ejecucion = tiempo_final - tiempo_inicial

			print("El tiempo de ejecucion fue de {}".format(tiempo_ejecucion))