# Arbol Binario
# Autor Codigo Fuente: Javier Rivera
# Autores de los Metodos: Gepsy, Harold, Nestor
# https://repl.it/DonC/4

class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.hizq = None
		self.hder = None

class Arbolb:
	def __init__(self):
		self.__raiz = None
	
	def insertar(self, valor, raiz = None):
	
		if (raiz == None):
			if (self.__raiz == None):
				self.__raiz = Nodo(valor)
				return
			raiz = self.__raiz
				
		if (valor < raiz.info):
			if(raiz.hizq == None):
				raiz.hizq = Nodo(valor)
			else:
				self.insertar (valor, raiz.hizq)
		else:
			if (raiz.hder == None):
				raiz.hder = Nodo(valor)
			else:
				self.insertar (valor, raiz.hder)
	# Retorna el hermano de un elemento del arbol, indica cual hermano es
	def hermano (self, valor, raiz=None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz
		
		if(valor < raiz.info):
			if (raiz.hizq.info== valor):
				if(raiz.hder!=None):
					return raiz.hder.info
			else:	
				self.hermano(valor, raiz.hizq)	
	
		if(valor > raiz.info):
			if (raiz.hder.info== valor):
				if(raiz.hizq!=None):
					return raiz.hizq.info
			else: 
				self.hermano(valor, raiz.hder)	
		
	
	# Retorna el numero de hojas de un arbol
	def hojas(self,raiz=None):
		if (raiz == None):
			if (self.__raiz==None):
				return
			raiz= self.__raiz

		if (raiz.hizq==None) and (raiz.hder==None):
			return 1
		h=0
		if(raiz.hizq!=None):
			h+=self.hojas(raiz.hizq)
		if(raiz.hder!=None):
			h+=self.hojas(raiz.hder)
		return h
	
	# Retorna si los datos de un arbol son consecutivos (paso 1) recorrido inorden
	def elem_consecutivos (self):
		pass
	
	# Retorna el tipo del nodo de un elemento
	# Raiz, Rama Derecha, Rama Izquierda, Hijo Derecho, Hijo Izquiedo, 
	def tipo_nodo (self, valor, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz
			if (raiz.info == valor):
				return "Es la raiz"

		if(valor < raiz.info):
			if ((raiz.hizq != None) and (raiz.hizq.info == valor)):
				if((raiz.hizq.hizq == None) and (raiz.hizq.hder == None)):
					return "Es hoja izquierda"
				return "Es rama izquierda"
			return self.tipo_nodo(valor, raiz.hizq)

		if(valor > raiz.info):
			if((raiz.hder != None) and ( raiz.hder.info == valor)):
				if((raiz.hder.hizq == None) and (raiz.hizq.hder == None)):
					return "Es hoja derecha"
				return "Es rama derecha"
			return self.tipo_nodo(valor, raiz.hder)

	def preorden (self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz
		
		print raiz.info,
		if (raiz.hizq != None):
			self.preorden (raiz.hizq)
		if (raiz.hder != None):
			self.preorden (raiz.hder)
			
	def postorden (self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz

		if (raiz.hizq != None):
			self.postorden (raiz.hizq)
		if (raiz.hder != None):
			self.postorden (raiz.hder)
		print raiz.info,	

	def inorden (self, raiz = None):
		if (raiz == None):
			if (self.__raiz == None):
				return
			raiz = self.__raiz

		if (raiz.hizq != None):
			self.inorden (raiz.hizq)
			
		print raiz.info,
		if (raiz.hder != None):
			self.inorden (raiz.hder)
			

# PRINCIPAL

a = Arbolb()
a.insertar(5)
a.insertar(2)
a.insertar(7)
a.insertar(9)
a.insertar(8)
a.insertar(4)
a.insertar(3)
a.insertar(6)

print 
print " El hermano es: ", a.hermano(2)
print 


print 
print " El numero de Hojas del Arbol es: ", a.hojas()
print 

print 
print " El tipo de nodo es: ", a.tipo_nodo(9)
print 

