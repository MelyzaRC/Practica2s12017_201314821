__author__ = "Melyza Rodriguez"

from flask import Flask, request, Response
app = Flask("Practica 2 Estructuras")

class nodo():
	def __init__(self, palabra, busqueda, eliminacion):
		self.palabra = palabra
		self.busqueda = busqueda
		self.eliminacion = eliminacion
		
global lista
lista = [0]

@app.route("/addLista", methods=['POST'])
def addLista():
	palabra = str(request.form['palabra'])
	lista.append(palabra)
	return "Ingresado"

@app.route("/buscarLista", methods=['POST'])
def buscarLista():
	criterio = str(request.form['busqueda'])
	
	if criterio in lista:
		temp =  "EL DATO SE ENCUENTRA EN EL INDICE: " + str(lista.index(criterio))
		return temp
	else:
		return "NO SE ENCONTRÓ EL DATO"

@app.route("/eliminarLista", methods=['POST'])
def eliminarLista():
	eliminar = int(request.form['eliminacion'])
	del lista[eliminar]
	return "ELIMINACION EXITOSA"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')