class Aresta():

		def __init__(self, origem: 'Vertice', destino: 'Vertice'):
				self.__origem = origem
				self.__destino = destino
	
		@property
		def origem(self) -> 'Vertice':
				return self.__origem
	

		@origem.setter
		def origem(self, novaOrigem: 'Vertice'):
				self.__origem = novaOrigem

		@property
		def destino(self) -> 'Vertice':
				return self.__destino
	

		@destino.setter
		def destino(self, novoDestino: 'Vertice'):
				self.__destino = novoDestino

		@property
		def peso(self)->int:
				return self.__peso
	
		@peso.setter
		def peso(self, peso: int):
				self.__peso = peso

		def __str__(self):
				return f'{self.__destino}'


class Vertice():

		def __init__(self, dado):
				self.__dado = dado
				self.__adj = list()
	
		def addAdj(self, edge: Aresta):
				self.__adj.append(edge)
	
		@property
		def dado(self):
				return self.__dado
	
		@dado.setter
		def dado(self, dado):
				self.__dado = dado
	
		@property
		def adj(self):
				return self.__adj


		def __str__(self):
				return self.__dado

		def printAdjs(self):
			for i in self.__adj:
				print (i)
