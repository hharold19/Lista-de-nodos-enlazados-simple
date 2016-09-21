
# LPIII_2016
# Autor: HAROLD HERNANDEZ Y MELEYCA CABRERA (UNEFA)
# Ver en : https://repl.it/DdBN/7
class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.sig = None
	
# CLASE LISTA
class Lista:
	
	# CONSTRUCTOR
	def __init__ (self):
		self.__primero = None
		self.__ultimo = None
		self.__actual = None
		self.__n = 0
		self.pos = 0

    # Metodo para insertar al inicio de la lista
	def insertar_inicio (self, valor):
		nodo = Nodo (valor)
		
		nodo.sig = self.__primero
		self.__primero = nodo
		self.__actual = nodo
		if (self.__ultimo == None):
			self.__ultimo = nodo
		
		self.__n = self.__n+1
		self.__pos = 0
		
	# Metodo para insertar al final de la lista
	def insertar_ultimo (self, valor):
		nodo = Nodo(valor)
		
		if (self.__ultimo == None):
			self.__primero = nodo
		else:
			self.__ultimo.sig = nodo

		self.__ultimo = nodo
		self.__actual = nodo
		self.__n = self.__n + 1
		self.__pos = self.__n - 1
		
	# Metodo para insertar adelante de la posicion actual de la lista
	def insertar_actual (self, valor):

		if(self.__n == 0):
			self.insertar_inicio (valor)
			return
			
		if(self.__actual == self.__ultimo):
			self.insertar_ultimo (valor)
			return
			
		nodo = Nodo(valor)
		nodo.sig = self.__actual.sig

		self.__actual.sig = nodo
		self.__actual = nodo
		
		self.__n = self.__n + 1
		self.__pos = self.__pos + 1
		
		
	# Metodo para mostrar los elementos de la lista 
	def mostrar (self):
		nodo = self.__primero
		for i in range (self.__n):
			print nodo.info
			nodo=nodo.sig
			
	

	#Metodo para buscar elemento REPETIDO en una lista 
	
	def buscar_repetido(self, valor):
		nodo = self.__primero
		aux = 0
		while(nodo!=None):
			if (nodo.info==valor):
					
				if (aux >= 2):
					return True
			nodo=nodo.sig
			aux = aux+1
		return False			
		

# PRINCIPAL 

# Crea la lista de elementos
l = Lista()

# Inserta elementos en la lista 
l.insertar_actual(10)
l.insertar_actual(35)
l.insertar_actual(85)
l.insertar_actual(55)
l.insertar_inicio(25)
l.insertar_actual(30)
l.insertar_ultimo(35)
l.insertar_ultimo(10)

# Muestra los elementos de la lista 
print "los elementos de la lista"
print " "
l.mostrar()
print " "

# Muestra si hay elementos repetidos en la lista
print "Muestra si hay elementos repetidos en la lista"
print " "
l.buscar_repetido(25)
print (l.buscar_repetido(25))