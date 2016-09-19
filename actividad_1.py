# LPIII_2016
# Autor: HAROLD HERNANDEZ (UNEFA)
#ver en: https://repl.it/DdBN/1
# CLASE NODO

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
			
	# Metodo para mostrar la posicion actual 
	"""def	mostrar_actual (self):
		nodo = self.__primero
		for i in range (self.__n):
			print nodo.info
			nodo="""
			
	# Metodo Mostrar donde se movio el actual				
	def mostrar_actual (self, pos):

		nodo  = self.__primero
		aux = 0
		while (nodo != None) :
			
			if (aux == pos):
				self.__actual=nodo
				self.__p=aux
				print self.__actual.info
			
			nodo = nodo.sig
			aux=aux+1
		return
		

	# Metodo para buscar un elemento determinado 
	def buscar_elem (self,valor):
		nodo = self.__primero
		while(nodo!=None):
			if(nodo.info==valor):
				return True
			nodo=nodo.sig
		return False		


	# Metodo para eliminar el primero de la lista
	def eliminar_primero(self):
		if (self.__primero==None):
			return
		nodo=self.__primero
		self.__primero=nodo.sig
		self.__n=self.__n-1
		self.__pos=self.__pos-1
		del nodo
		if (self.__n==0):
			self.__ultimo=None
			self.__actual=None

			
# PRINCIPAL 

# Crea la lista de elementos
l = Lista()

# Inserta elementos en la lista 
l.insertar_actual(5);
l.insertar_actual(10);
l.insertar_actual(15);
l.insertar_actual(20);
l.insertar_inicio(25);
l.insertar_actual(30);
l.insertar_ultimo(35);

# Muestra los elementos de la lista 
print "Metodo para mostrar los elementos de una lista"
print " "
l.mostrar()
print " "

# Muestra si la lista contiene un elemento con un valor determinado
print "Metodo para buscar un elemento determinado"
print "Buscar el elemento: 15"
print " "

if (l.buscar_elem(15) == True):
	print "El elemento se encontro"
else:
	print "El elemento no se encuentra en la lista"

print " "

# Muestra los elementos que se han borrado de la lista
print "Metodo para eliminar el primero de la lista"
print " "

l.eliminar_primero()
l.mostrar()
print " "

# Muestra la nueva posicion del actual
print "La nueva posicion del actual es:"
print " "
l.mostrar_actual(2)