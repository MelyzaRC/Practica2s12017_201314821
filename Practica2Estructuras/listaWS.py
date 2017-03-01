__author__ = "Melyza Rodriguez"

from flask import Flask, request, Response
app = Flask("EDD Lista Simple")


class Nodo:
	def __init__(self, palabra):
		self.palabra=palabra
		self.siguiente=None

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

lis = listaSimple()

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


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')