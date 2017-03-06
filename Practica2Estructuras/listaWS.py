__author__ = "Melyza Rodriguez"

from flask import Flask, request, Response
app = Flask("EDD Lista Simple")
import subprocess
from graphviz import Digraph

#Nodo para lista pila cola
class Nodo:
	def __init__(self, palabra):
		self.palabra=palabra
		self.siguiente=None
		self.anterior =None

##ListaSimple
class listaSimple:
	def __init__(self):
		self.primero =None
		self.ultimo = None

	def vacia(self):
		if self.primero == None:
			return True
		else:
			return False

	def agregar(self, dato):
   	 if self.vacia() == True:
   	 	self.primero = self.ultimo = Nodo(dato)
   	 else:
   	 	temp = Nodo(dato)
   	 	self.ultimo.siguiente = temp
   	 	self.ultimo = temp

	def recorrer(self):
		auxt = self.primero
		if self.vacia() == True:
			return "La lista esta vacia"
		else:
			s = ""
			while auxt != None:
				s = s + "Elemento: " + auxt.palabra + "\n"
				auxt = auxt.siguiente
			return s

	def eliminar(self, numero):
		if self.vacia() == True:
			return "La lista está vacía no se puede eliminar"
		else:
			if int(numero) == 0:
				u1 = self.primero.siguiente
				self.primero = None
				self.primero = u1
				return "Eliminacion exitosa"
			else:
				ho = self.primero
				c10 = -1
				while ho != None:
					c10 = c10 + 1
					ho = ho.siguiente
				if c10 < int(numero):
					return "No se puede eliminar, fuera de rango."
				else:
					hi = self.primero
					c1 = 0
					while hi != None:
						c1 = c1 +1
						hi = hi.siguiente
					if c1 == int(numero):
						self.ultimo = None
						return "Eliminacion exitosa"
					else:
						a1 = self.primero
						contador = 0
						while a1 != None:
							if contador == int(numero)-1:
								a2 = a1.siguiente
								a3 = a2.siguiente
								a2 = None
								a1.siguiente = a3
							a1 = a1.siguiente
							contador = contador +1
						return "Eliminacion exitosa"

	def graficarListaSimple(self):
		dot = Digraph(comment = 'GraficaLista')
		dot
		aux10 = self.primero
		if aux10== None:
			return "lista vacia"
		else:
			if aux10 == self.primero == self.ultimo:
				dot.node(aux10.palabra)
				dot.render('test-output/ListaSimple.dot', view=False)
			else:
				while aux10.siguiente != None:
					dot.node(aux10.palabra)
					dot.node(aux10.siguiente.palabra)
					dot.edge(str(aux10.palabra),str(aux10.siguiente.palabra))
					aux10 = aux10.siguiente
					dot.render('test-output/ListaSimple.dot', view=False)
			return "Graficado"

	def buscar(self, criterio):
		b1 = self.primero
		cb1 = 0
		bb1 = False

		while b1 != None:
			if b1.palabra == str(criterio):
				bb1=True
				break
			else:
				cb1 = cb1+1
				bb1 = False
			b1 = b1.siguiente

		if bb1 == False:
			return "No se ha encontrado el elemento"
		else:
			return "Elemento encontrado en la posicion: " + str(cb1) 		

##Cola
class Cola:
	def __init__(self):
		self.primero =None
		self.ultimo = None

	def vacia(self):
		if self.primero == None:
			return True
		else:
			return False

	def graficarCola(self):
		dot = Digraph(comment = 'GraficaCola')
		dot
		aux10 = self.primero
		if aux10== None:
			return "lista vacia"
		else:
			if aux10 == self.primero == self.ultimo:
				dot.node(aux10.palabra)
				dot.render('test-output/Cola.dot', view=False)
			else:
				while aux10.siguiente != None:
					dot.node(aux10.palabra)
					dot.node(aux10.siguiente.palabra)
					dot.edge(str(aux10.palabra),str(aux10.siguiente.palabra))
					aux10 = aux10.siguiente
					dot.render('test-output/Cola.dot', view=False)
			return "Graficado"

	def agregar(self, dato):
   	 if self.vacia() == True:
   	 	self.primero = self.ultimo = Nodo(dato)
   	 	return "Agregado: " + str(dato)
   	 else:
   	 	temp = Nodo(dato)
   	 	self.ultimo.siguiente = temp
   	 	self.ultimo = temp
   	 	return "Agregado: " + str(dato)

	def recorrer(self):
		ai1 = self.primero
		if self.vacia() == True:
			return "La cola esta vacia"
		else:
			s = ""
			while ai1 != None:
				s = s + "Elemento: " + ai1.palabra + "\n"
				ai1 = ai1.siguiente
		return s

	def sacar(self):
		if self.vacia() == True:
			return "La cola está vacía"
		else:
			tm = self.primero
			ai2 = self.primero.siguiente 
			self.primero =None
			self.primero = ai2
			return "Elemento saliente: " + tm.palabra

##Pila
class Pila:
	def __init__(self):
		self.primero =None
		self.ultimo = None

	def vacia(self):
		if self.ultimo == None:
			return True
		else:
			return False

	def graficarPila(self):
		dot = Digraph(comment = 'GraficaPila')
		dot
		aux10 = self.ultimo
		if aux10== None:
			return "pila vacia"
		else:
			if aux10 == self.primero == self.ultimo:
				dot.node(aux10.palabra)
				dot.render('test-output/Pila.dot', view=False)
			else:
				while aux10.anterior != None:
					dot.node(aux10.palabra)
					dot.node(aux10.anterior.palabra)
					dot.edge(str(aux10.palabra),str(aux10.anterior.palabra))
					aux10 = aux10.anterior
					dot.render('test-output/Pila.dot', view=False)
			return "Graficado"

	def agregar(self, dato):
   		if self.vacia() == True:
   			self.primero = self.ultimo = Nodo(dato)
   			return "Agregado: " + str(dato)
   		else:
   			temp = Nodo(dato)
   			temp.anterior = self.ultimo
   			self.ultimo = temp
   			return "Agregado: " + str(dato)

	def recorrer(self):
		ai1 = self.ultimo
		if self.vacia() == True:
			return "La pila esta vacia"
		else:
			s = ""
			while ai1 != None:
				s = s + "Elemento: " + ai1.palabra + "\n"
				ai1 = ai1.anterior
			return s

	def sacar(self):
		if self.vacia() == True:
			return "La pila está vacía"
		else:
			tm = self.ultimo
			ai2 = self.ultimo.anterior 
			self.ultimo =None
			self.ultimo = ai2
			return "Elemento saliente: " + tm.palabra

#Nodo para la matriz
class NodoMatriz:
	def __init__(self, contenido, pContenido, uContenido, numeroLetra):
		self.contenido = contenido
		self.pContenido = pContenido
		self.uContenido = uContenido
		self.numeroLetra = numeroLetra
		self.siguiente=None
		self.anterior =None
		self.arriba = None
		self.abajo = None
		self.adelante = None
		self.atras = None

class matrizDispersa:
	def __init__(self):
		self.primerDominio =None
		self.ultimoDominio = None
		self.primeraLetra = None
		self.ultimaLetra = None

	def vacia(self): 
		if self.primerDominio == None:
			return True
		else:
			return False


	def graficarMatrizDispersa(self):
		dot = Digraph(comment = 'GraficaMatrixDispersa')
		dot

		tempDominio = self.primerDominio
		tempLetra = self.primeraLetra

		if tempDominio == None:
			return "La matriz está vacía"
		else:
			if tempDominio == self.primerDominio == self.ultimoDominio:
				dot.node(tempDominio.contenido)
			else:
				##Dominios
				while tempDominio.siguiente != None:
					dot.node(tempDominio.contenido)
					dot.node(tempDominio.siguiente.contenido)
					dot.edge(str(tempDominio.contenido),str(tempDominio.siguiente.contenido))
					tempDominio = tempDominio.siguiente
				tempDominio2 = self.ultimoDominio
				while tempDominio2.anterior != None:
					dot.node(tempDominio.contenido)
					dot.node(tempDominio2.anterior.contenido)
					dot.edge(str(tempDominio2.contenido),str(tempDominio2.anterior.contenido))
					tempDominio2 = tempDominio2.anterior
				##Dominios y abajo y arriba
				Dom12 = self.primerDominio
				while Dom12 != None:
					tempDominio = Dom12.pContenido
					dot.node(Dom12.contenido)
					dot.node(tempDominio.contenido)
					dot.edge(str(Dom12.contenido),str(tempDominio.contenido))
					dot.edge(str(tempDominio.contenido),str(Dom12.contenido))
					while tempDominio.abajo != None:
						dot.node(tempDominio.contenido)
						dot.node(tempDominio.abajo.contenido)
						dot.edge(str(tempDominio.contenido),str(tempDominio.abajo.contenido))
						dot.edge(str(tempDominio.abajo.contenido),str(tempDominio.contenido))
						tempDominio = tempDominio.abajo
					Dom12 = Dom12.siguiente
				
				if tempLetra == self.primeraLetra == self.ultimaLetra: 
					dot.node(tempDominio.contenido)
				else:
					tempLetra = self.primeraLetra
					while tempLetra.abajo != None:
						dot.node(tempLetra.contenido)
						dot.node(tempLetra.abajo.contenido)
						dot.edge(str(tempLetra.abajo.contenido),str(tempLetra.contenido))
						dot.edge(str(tempLetra.contenido),str(tempLetra.abajo.contenido))
						tempLetra = tempLetra.abajo
				Le12 = self.primeraLetra
				while Le12 != None:
					tempLetra = Le12.pContenido
					dot.node(Le12.contenido)
					dot.node(tempLetra.contenido)
					dot.edge(str(Le12.contenido),str(tempLetra.contenido))
					dot.edge(str(tempLetra.contenido),str(Le12.contenido))
					while tempLetra.siguiente != None:
						dot.node(tempLetra.contenido)
						dot.node(tempLetra.siguiente.contenido)
						dot.edge(str(tempLetra.contenido),str(tempLetra.siguiente.contenido))
						dot.edge(str(tempLetra.siguiente.contenido),str(tempLetra.contenido))
						tempLetra = tempLetra.siguiente
					Le12 = Le12.abajo
				Le13 = self.primeraLetra
				while Le13 != None:
					Le13c = Le13.pContenido
					while Le13c.atras != None:
						dot.node(Le13c.contenido)
						dot.node(Le13c.atras.contenido)
						dot.edge(str(Le13c.contenido),str(Le13c.atras.contenido))
						dot.edge(str(Le13c.atras.contenido),str(Le13c.contenido))
						Le13c = Le13c.atras
					Le13 = Le13.abajo

					dot.render('test-output/MatrizDispersa.dot', view=False)
			return "Graficado"


	def ingresarCorreo(self, correoR, dominioR, letraR, numeroR):
		s = ""
		if self.vacia() == True:
			nodoTemp = NodoMatriz(correoR, None, None, numeroR)
			self.primerDominio = self.ultimoDominio = NodoMatriz(dominioR, None, None, None)
			self.primeraLetra = self.ultimaLetra = NodoMatriz(letraR, None, None, numeroR)
			self.primerDominio.pContenido = self.primerDominio.uContenido = self.ultimoDominio.pContenido = self.ultimoDominio.uContenido = self.primeraLetra.pContenido = self.primeraLetra.uContenido = self.ultimaLetra.pContenido = self.ultimaLetra.uContenido = nodoTemp
			self.primerDominio.abajo = self.ultimoDominio.abajo  = self.primeraLetra.siguiente= self.ultimaLetra.siguiente = nodoTemp
			self.primerDominio.pContenido.arriba = self.primerDominio.uContenido.arriba = self.ultimoDominio.pContenido.arriba = self.ultimoDominio.uContenido.arriba = self.primerDominio
			self.primeraLetra.pContenido.anterior = self.primeraLetra.uContenido.anterior = self.ultimaLetra.pContenido.anterior = self.ultimaLetra.uContenido.anterior = self.primeraLetra
			self.primerDominio.siguiente = self.ultimoDominio.siguiente = None
			self.primeraLetra.abajo = self.ultimaLetra.abajo = None
			s ="Ingresado: " + nodoTemp.contenido + " Arriba: " + nodoTemp.arriba.contenido + " Anterior: " + nodoTemp.anterior.contenido
			return s
		else:
			##Valua el dominio cuando la lista ya no está vacia
			nuevoDom = NodoMatriz(dominioR, None, None, None)
			tempDom = self.primerDominio
			domEncontrado = False
			while tempDom != None:
				if nuevoDom.contenido == tempDom.contenido:
					domEncontrado = True
				tempDom = tempDom.siguiente
			
			if domEncontrado == True:
				domEncontrado = True
			else:
				nuevoDom.anterior = self.ultimoDominio
				self.ultimoDominio.siguiente = nuevoDom
				self.ultimoDominio = nuevoDom
				s =  "Agregado el nuevo dominio"
			#Termina de valuar el dominio
			#Valua la letra
			nuevaL = NodoMatriz(letraR, None, None, numeroR)
			tempL = self.primeraLetra
			leEncontrada = False
			while tempL != None:
				if int(tempL.numeroLetra) == int(nuevaL.numeroLetra):
					leEncontrada = True
				tempL = tempL.abajo
			if leEncontrada == True:
				s = s + " Letra encontrada"
			else:
				if int(numeroR) < int(self.primeraLetra.numeroLetra):
					tempa = self.primeraLetra
					self.primeraLetra = nuevaL
					self.primeraLetra.abajo = tempa
					tempa.arriba = self.primeraLetra
					s = s + "\nSe agrego la letra al inicio"
				elif int(numeroR) > int(self.ultimaLetra.numeroLetra):
					nuevaL.arriba = self.ultimaLetra
					self.ultimaLetra.abajo = nuevaL
					self.ultimaLetra = nuevaL
					s = s + "\nSe agrego la letra al final"
				else:
					tempL2 = self.primeraLetra
					while tempL2 != None:
						if int(numeroR) < int(tempL2.numeroLetra):
							nuevaL.arriba = tempL2.arriba
							tempL2.arriba.abajo = nuevaL
							nuevaL.abajo = tempL2
							tempL2.arriba = nuevaL
							leEncontrada = True
							s = s +  "\nLetra agregada"
							break
						tempL2 = tempL2.abajo

					if leEncontrada == True:
						s = s + "\n Se agregó antes la letra"
					else:
						tempL3 = self.ultimaLetra
						while tempL3 != None:
							if int(numeroR) > int(tempL3.numeroLetra):
								nuevaL.arriba = tempL3.arriba
								tempL3.arriba.abajo = nuevaL
								nuevaL.abajo = tempL3
								tempL3.arriba = nuevaL
								leEncontrada = True
								s = s +  "\nLetra agregada"
								break
							tempL3 = tempL3.abajo
			#Termina de valuar la letra

			#Sitúa el nodo actual 
			nuevoElemento = NodoMatriz(correoR, None, None, numeroR)

			tempRL = self.primeraLetra
			while tempRL != None:
				if str(tempRL.contenido) == str(letraR):
					tempDA = self.primerDominio
					while  tempDA != None:
						if str(tempDA.contenido) == str(dominioR):
							if tempRL.pContenido == None:
								if tempDA.pContenido ==None:
									#Letra y dominio estan vacíos 
									tempRL.pContenido = tempRL.uContenido = tempDA.pContenido = tempDA.uContenido = nuevoElemento
									tempRL.siguiente = tempDA.abajo = nuevoElemento
									nuevoElemento.arriba = tempDA
									nuevoElemento.anterior = tempRL
									s = "Ingresado : " + str(nuevoElemento.contenido) + "  Dominio: " + nuevoElemento.arriba.contenido + " Letra: " + nuevoElemento.anterior.contenido  
								else:
									#Letra vacia pero dominio no vacio
									if int(numeroR) < int(tempDA.pContenido.numeroLetra):
										tempRL.pContenido = tempRL.uContenido = nuevoElemento
										tempRL.siguiente = nuevoElemento
										nuevoElemento.anterior = tempRL
										tempDA.abajo = nuevoElemento
										tempDA.pContenido.arriba = nuevoElemento
										nuevoElemento.abajo = tempDA.pContenido
										nuevoElemento.arriba = tempDA 
										tempDA.pContenido = nuevoElemento
										s = "Ingresado : " + str(nuevoElemento.contenido) + "  Arriba: " + nuevoElemento.arriba.contenido + " Letra: " + nuevoElemento.anterior.contenido 
									elif int(numeroR) > int(tempDA.uContenido.numeroLetra):
										tempRL.pContenido = tempRL.uContenido = nuevoElemento
										tempRL.siguiente = nuevoElemento
										nuevoElemento.anterior = tempRL
										nuevoElemento.arriba = tempDA.uContenido
										tempDA.uContenido.abajo = nuevoElemento
										tempDA.uContenido = nuevoElemento
										s = "Ingresado : " + str(nuevoElemento.contenido) + "  Arriba: " + nuevoElemento.arriba.contenido + " Letra: " + nuevoElemento.anterior.contenido 
									else:
										tempED = tempDA.pContenido
										while tempED != None:
											if int(numeroR) <  int(tempED.numeroLetra):
												tempRL.pContenido = tempRL.uContenido = nuevoElemento
												tempRL.siguiente = nuevoElemento
												nuevoElemento.anterior = tempRL
												tempED.arriba.abajo = nuevoElemento
												nuevoElemento.arriba = tempED.arriba
												nuevoElemento.abajo = tempED
												tempED.arriba = nuevoElemento
												s = "Ingresado : " + str(nuevoElemento.contenido) + "  Arriba: " + nuevoElemento.arriba.contenido + " Letra: " + nuevoElemento.anterior.contenido 
											tempED = tempED.abajo
							else:
								if tempDA.pContenido ==None:
									#Letra no vacia y dominio vacio
									tempRL.uContenido.siguiente = tempDA.pContenido = tempDA.uContenido = nuevoElemento
									nuevoElemento.anterior = tempRL.uContenido
									tempRL.uContenido = nuevoElemento
									nuevoElemento.arriba = tempDA
									s = "Ingresado : " + str(nuevoElemento.contenido) + "  Dominio: " + nuevoElemento.arriba.contenido + " Anterior: " + nuevoElemento.anterior.contenido  
								else:
									ingC = False
									#Letra y dominio no vacios
									#Cuando ya hay una letra igual en el recorrido del dominio 
									tempDO = tempDA.pContenido
									while tempDO != None:
										if str(tempDO.numeroLetra) == str(numeroR):
											if tempDO.pContenido == None:
												tempDO.pContenido = tempDO.uContenido = nuevoElemento
												tempDO.atras = nuevoElemento
												nuevoElemento.adelante = tempDO
												ingC = True
												s = "Ingresado : " + str(nuevoElemento.contenido) + "  Adelante: " + nuevoElemento.adelante.contenido
											else:
												tempDO.uContenido.atras = nuevoElemento
												nuevoElemento.adelante = tempDO.uContenido
												tempDO.uContenido=nuevoElemento
												ingC = True
												s = "Ingresado : " + str(nuevoElemento.contenido) + "  Adelante: " + nuevoElemento.adelante.contenido
										tempDO = tempDO.abajo
									#Cuando no hay registro de esa letra en el dominio
									if ingC == False:
										#Primero debe crear el nodo en la posicion correcta alfabeticamente dentro del mismo dominio
										if int(numeroR) < int(tempDA.pContenido.numeroLetra):
											nuevoElemento.arriba = tempDA
											nuevoElemento.abajo = tempDA.pContenido
											tempDA.abajo = nuevoElemento
											tempDA.pContenido.arriba = nuevoElemento
											ingC = True
										elif int(numeroR) > int(tempDA.uContenido.numeroLetra):
											tempDA.uContenido.abajo = nuevoElemento
											nuevoElemento.arriba = tempDA.uContenido
											tempDA.uContenido = nuevoElemento
											ingC = True
										else:
											cc = tempDA.pContenido
											while cc != None:
												if int(numeroR) < int(cc.numeroLetra):
													cc.arriba.abajo = nuevoElemento
													nuevoElemento.arriba = cc.arriba
													nuevoElemento.abajo = cc
													cc.arriba = nuevoElemento
													ingC = True
													break
												cc = cc.abajo
									#Termino de crear el nodo actual y ahora le pongo sus siguientes y anteriores esto es por si el dominio y la letra no son vacio pero no esta la letra en el dominio
									##Valuar anterior si el dominio es la primera posicion
										if tempDA == self.primerDominio:
											encSig = False
											jj = tempDA.siguiente
											while jj != None:
												yy = jj.pContenido
												while yy != None:
													if str(yy.numeroLetra) == str(numeroR):
														encSig = True
														break
													yy = yy.abajo
												jj = jj.siguiente
											if encSig == True:
												buscando1 = True
												rr = tempDA.siguiente
												while rr != None:
													ss = rr.pContenido
													if buscando1 == True:
														while ss != None:
															if str(ss.numeroLetra) == str(numeroR):
																encSig = True
																buscando1 = False
																if ss == tempRL.pContenido:
																	ss.anterior.siguiente = nuevoElemento
																	nuevoElemento.anterior = ss.anterior
																	nuevoElemento.siguiente = ss
																	ss.anterior = nuevoElemento
																	tempRL.pContenido = nuevoElemento
																	s = "ingresado: " + nuevoElemento.contenido + " anterior: " + nuevoElemento.anterior.contenido + " siguiente: " + nuevoElemento.siguiente.contenido + " Arriba: " + nuevoElemento.arriba.contenido
																else:
																	ss.anterior.siguiente = nuevoElemento
																	nuevoElemento.anterior = ss.anterior
																	nuevoElemento.siguiente = ss
																	ss.anterior = nuevoElemento
																s = "ingresado: " + nuevoElemento.contenido + " anterior: " + nuevoElemento.anterior.contenido + " siguiente: " + nuevoElemento.siguiente.contenido + " Arriba: " + nuevoElemento.arriba.contenido
																break
															ss = ss.abajo
													rr = rr.siguiente											
											#Valuar en los siguientes dominios
										elif tempDA == self.ultimoDominio:
											encSig = False
											jj = tempDA.anterior
											while jj != None:
												yy = jj.pContenido
												while yy != None:
													if str(yy.numeroLetra) == str(numeroR):
														encSig = True
														break
													yy = yy.abajo
												jj = jj.anterior

											if encSig == True:
												buscando1 = True
												rr = tempDA.anterior
												while rr != None:
													ss = rr.pContenido
													if buscando1 == True:
														while ss != None:
															if str(ss.numeroLetra) == str(numeroR):
																encSig = True
																buscando1 = False
																if ss == tempRL.uContenido:
																	ss.siguiente = nuevoElemento
																	nuevoElemento.anterior = ss
																	tempRL.uContenido = nuevoElemento
																	s = "ingresado: " + nuevoElemento.contenido + " anterior: " + nuevoElemento.anterior.contenido + " siguiente: NO TIENE   Arriba: " + nuevoElemento.arriba.contenido
																break
															ss = ss.abajo
													rr = rr.anterior
										else:
											encAnt = False
											encSi = False

											jj = tempDA.anterior
											while jj != None:
												yy = jj.pContenido
												while yy != None:
													if str(yy.numeroLetra) == str(numeroR):
														encAnt = True
														break
													yy = yy.abajo
												jj = jj.anterior

											pp = tempDA.anterior
											while pp != None:
												ti = pp.pContenido
												while ti != None:
													if str(ti.numeroLetra) == str(numeroR):
														encSi = True
														break
													ti = ti.abajo
												pp = pp.siguiente

											buscando2 = True
											if encAnt == True:
												jj = tempDA.anterior
												while jj != None:
													if buscando2 == True:
														yy = jj.pContenido
														while yy != None:
															if str(yy.numeroLetra) == str(numeroR):
																encAnt = True
																buscando2=False
																nuevoElemento.anterior = yy
																nuevoElemento.siguiente = yy.siguiente 
																yy.siguiente.anterior = nuevoElemento
																yy.siguiente = nuevoElemento
																s = "Se ingresó: " + nuevoElemento.contenido + " Anterior: " + nuevoElemento.anterior.contenido
																break
															yy = yy.abajo
													jj = jj.anterior
											buscando2 = True
			
											if encSi == True:
												jj = tempDA.siguiente
												while jj != None:
													if buscando2 == True:
														yy = jj.pContenido
														while yy != None:
															if str(yy.numeroLetra) == str(numeroR):
																encSi = True
																buscando2=False
																
																nuevoElemento.anterior = yy.anterior
																yy.anterior.siguiente = nuevoElemento
																yy.anterior = nuevoElemento
																nuevoElemento.siguiente = yy
																s = s +" Siguiente: " + nuevoElemento.siguiente.contenido
																break
															yy = yy.abajo
													jj = jj.siguiente
											else:
												nuevoElemento.siguiente = None
												s = s + "NO tiene siguiente"




						tempDA = tempDA.siguiente
				tempRL = tempRL.abajo
		return s

	def buscarLetra(self, num):
		var = "Resultado de la búsqueda\n"
		if str(num) != "":
			temp1 = self.primerDominio
			while temp1 != None:
				temp2 = temp1.pContenido
				while temp2 != None:
					if str(temp2.numeroLetra) == str(num):
						var = var + str(temp2.contenido) + "\n"
						temp3 = temp2.pContenido
						while temp3 != None:
							var = var + str(temp3.contenido) + "\n"
							temp3 = temp3.atras
					temp2 = temp2.abajo
				temp1 = temp1.siguiente
		return var

	def buscarDominio(self, dominioBuscar):
		var = "Resultado de la búsqueda de: " + "@"+ str(dominioBuscar) + "\n"
		busq = str(dominioBuscar)
		if str(dominioBuscar) != "":
			temp1 = self.primerDominio
			while temp1 != None:
				if str(temp1.contenido) == busq:			 
					temp2 = temp1.pContenido
					while temp2 != None:
						var = var + temp2.contenido + "\n"
						temp2 = temp2.atras
				temp1 = temp1.siguiente
		return var

	def recorrerMatrizDispersa(self):
		s = ""
		temp1 = self.primerDominio 
		while temp1 != None:
			s = s + "Dominio: " + temp1.contenido + "\n"
			temp1 = temp1.siguiente
		temp2 = self.primeraLetra
		while  temp2 != None:
			s = s + "Letra: " + temp2.contenido + "\n"
			temp2 = temp2.abajo
		return s
			
	

lis = listaSimple()
co = Cola()
pi = Pila()
md = matrizDispersa()

@app.route('/buscarDominio',methods=['POST']) 
def buscarDom():
	ret = str(md.buscarDominio(str(request.form['dominio'])))
	return ret 

@app.route('/graficarMatriz',methods=['POST']) 
def graficarMatriz():
	ret = str(md.graficarMatrizDispersa())
	return ret 

@app.route('/buscarLetra',methods=['POST']) 
def buscarLetra():
	ret = str(md.buscarLetra(str(request.form['numeroLetra'])))
	return ret 

@app.route('/insertarMatrizDispersa',methods=['POST']) 
def insertarMatrizDispersa():
	correoTemp= str(request.form['correo'])
	dominioTemp = str(request.form['dominio'])
	letraTemp = str(request.form['letra'])
	numeroTemp = str(request.form['numeroLetra'])
	return md.ingresarCorreo(correoTemp, dominioTemp, letraTemp,numeroTemp)

@app.route('/recorrerMatrizDispersa',methods=['POST']) 
def recorrerMatrizDispersa():
	return md.recorrerMatrizDispersa()

@app.route('/insertarLista',methods=['POST']) 
def insertarLista():
	dato = str(request.form['palabra'])
	lis.agregar(str(dato))
	return "Ingresado: " + str(dato)

@app.route('/recorrerLista',methods=['POST'])
def recorrerLista():
	return  lis.recorrer()

@app.route('/eliminarLista', methods=['POST'])
def eliminarLista():
	return lis.eliminar(request.form['eliminacion'])

@app.route('/buscarLista', methods=['POST'])
def buscarLista():
	return lis.buscar(request.form['busqueda'])

@app.route('/graficarLista', methods=['POST'])
def graficarLista():
	v = lis.graficarListaSimple()
	return v

@app.route('/addCola', methods=['POST'])
def addCola():
	return co.agregar(request.form['valor'])
@app.route('/recorrerCola', methods=['POST'])
def recorrerCola():
	return co.recorrer()
@app.route('/sacarCola', methods=['POST'])
def sacarCola():
	return co.sacar()
@app.route('/graficarCola', methods=['POST'])
def graficarCola():
	v = co.graficarCola()
	return v



@app.route('/addPila', methods=['POST'])
def addPila():
	return pi.agregar(request.form['valor'])
@app.route('/recorrerPila', methods=['POST'])
def recorrerPila():
	return pi.recorrer()
@app.route('/sacarPila', methods=['POST'])
def sacarPila():
	return pi.sacar()

@app.route('/graficarPila', methods=['POST'])
def graficarPila():
	v = pi.graficarPila()
	return v


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')




  ##EEEEEror en insertar nuevos valores cuando el dominio y al letra ya existen