class TinyIntError(Exception):
	def __init__(self):
		self.message = 'El número no cuenta con las caracteristicas de un número tiny_int' #Mensaje default..
		
	def __str__(self):
		return self.message