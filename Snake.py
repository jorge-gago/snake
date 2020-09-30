class Snake ():

	cuerpo = []
	cant_cuerpo = 4
	dimensione_cuerpo = 5
	borde = 1


	
	def __init__(self, width = 800, height = 800):
		pos_x = width/2
		pos_y = height/2
		for i in range(self.cant_cuerpo):
			self.cuerpo.append([ pos_x, pos_y + (self.tamano() * i)])


		
	def tamano(self):
		tam = (self.borde * 2) + (self.dimensione_cuerpo * 2)

		return  tam

	def add_cuerpo(self):
		self.cuerpo.append([ 0, 0])


	def move(self, vels):	
		vel_x = vels[0]
		vel_y = vels[1]
	
		for i in range( -1, (len(self.cuerpo)*(-1)), -1):
			self.cuerpo[i] = self.cuerpo[i-1]
		
		#self.cuerpo[0][0] = (self.cuerpo[0][0]) + vel_x
		#self.cuerpo[0][1] = (self.cuerpo[0][1]) + vel_y
		self.cuerpo[0] = [ (self.cuerpo[0][0] + vel_x), (self.cuerpo[0][1] + vel_y)]






if __name__ == "__main__":
	snake = Snake()
	print( snake.cuerpo)

	snake.move([0, -12])
	print( snake.cuerpo)

	snake.add_cuerpo()
	snake.move([0, -12])
	print( snake.cuerpo)


