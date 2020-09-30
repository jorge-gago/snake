import random

class Frutas():

	bx = 0
	by = 0
	fruta = []
	color = [ "light green", "red", "blue"]  # lista de colores
	puntos = [ 10, 50, 5]

	def __init__( self, widht, height):
		self.bx = widht
		self.by = height
		self.fruta = [ (self.bx / 4), (self.by - (self.by / 4)),  "light green"]


	def crear_fruta( self, color, ptn):
		x = random.uniform( 0, self.bx)
		y = random.uniform( 0, self.by)
		fru = [ x, y, color, ptn]

		return fru

	def cant_fru( self, cant = 1):
		self.fruta.clear()
		for i in range(cant):
			self.fruta.append(self.crear_fruta( self.color[i], self.puntos[i]))


if __name__ == "__main__":
	
	fruta = Frutas( 800, 800)
	print(fruta.fruta)

	fruta.cant_fru(3)
	print(fruta.fruta)

	fruta.cant_fru(1)
	print(fruta.fruta)


