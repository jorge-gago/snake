vel_ini = 0
vel = 0

mov = [ 0, 0]

def vels(obj):
	global vel_ini
	global vel

	vel_ini = (obj.dimensione_cuerpo + obj.borde) * 2
	vel = (obj.dimensione_cuerpo + obj.borde) * 2

def actu_vel():
	global mov
	return mov

def colition(canvas, snake, fruta, vivo, puntos = 0, tl = 0):
	if (tl):
		teleport( canvas, snake)
	else:
		col_borde( canvas, snake, vivo)
	col_partes(snake, vivo)
	col_fruta(snake, fruta, puntos)

	#print(vivo)

def col_fruta(snake, fruta, puntos):
	cabeza = snake.cuerpo[0]
	frutas = fruta.cuerpo

	for i in frutas:
		if (abs(cabeza[0] - i[0]) < (snake.dimensione_cuerpo) * 2) and (abs(cabeza[1] - i[1]) < (snake.dimensione_cuerpo) * 2):
				print("fruta  ", i)

				fruta.cuerpo = []
				snake.add_cuerpo()
				fruta.cant_fru()


def col_partes(snake, vivo):
	tamano = snake.dimensione_cuerpo + snake.borde
	for i in snake.cuerpo[1:]:
		if ( ((snake.cuerpo[0][0] - i[0]) < tamano) and ((snake.cuerpo[0][0] - i[0]) > (tamano * (-1)))):
			if ( ((snake.cuerpo[0][1] - i[1]) < tamano) and ((snake.cuerpo[0][1] - i[1]) > (tamano * (-1)))):
				vivo[0] = False

				print("cuerpo")

				break


def col_borde( canvas, snake, vivo):

 	
	canvas.update_idletasks()

	#print(snake.cuerpo[0])
	#print(snake.dimensione_cuerpo + snake.borde)
	#print(canvas.winfo_width() - ((snake.dimensione_cuerpo + snake.borde)))


	if ((snake.cuerpo[0][0]) < ((snake.dimensione_cuerpo + snake.borde)) or 
	snake.cuerpo[0][0] > canvas.winfo_width() - ((snake.dimensione_cuerpo + snake.borde))):
		vivo[0] = False

		print("x")

	elif ((snake.cuerpo[0][1]) < ((snake.dimensione_cuerpo + snake.borde)) or 
	snake.cuerpo[0][1] > canvas.winfo_height() - ((snake.dimensione_cuerpo + snake.borde))):
		vivo[0] = False

		print("y")

	else:
		pass	
		
def teleport( canvas, snake):
	if ((snake.cuerpo[0][0]) < ((snake.dimensione_cuerpo + snake.borde))):
		snake.cuerpo[0][0] = canvas.winfo_width() - ((snake.dimensione_cuerpo + snake.borde))

	elif (snake.cuerpo[0][0] > canva.winfo_width() - ((snake.dimensione_cuerpo + snake.borde))):
		snake.cuerpo[0][0] = ((snake.dimensione_cuerpo + snake.borde))

	elif ((snake.cuerpo[0][1]) < ((snake.dimensione_cuerpo + snake.borde))):
		snake.cuerpo[0][1] = canvas.winfo_height() - ((snake.dimensione_cuerpo + snake.borde))

	elif (snake.cuerpo[0][1] > canva.winfo_height() - ((snake.dimensione_cuerpo + snake.borde))):
		snake.cuerpo[0][1] =((snake.dimensione_cuerpo + snake.borde))
	else:
		pass
		
def moves(move):
	#print(move)
	#print(type(move))

	global mov 

	if (move == "a" and mov != [ vel, 0]):
		mov = [ vel * (-1), 0]
	elif (move == "d" and mov != [ vel * (-1), 0]):
		mov = [ vel, 0]
	elif (move == "w" and mov != [ 0, vel]):
		mov = [ 0, vel * (-1)]
	elif (move == "s" and mov != [ 0, vel * (-1)]):
		mov = [ 0, vel ]

	#print(mov)