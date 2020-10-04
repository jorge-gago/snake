
def colition(canvas, snake, vivo, tl = 0):
	if (tl):
		teleport( canvas, snake)
	else:
		col_borde( canvas, snake, vivo)
	col_partes(snake, vivo)


def col_partes(snake, vivo):
	tamano = snake.dimensione_cuerpo + snake.borde
	for i in snake.cuerpo[1:]:
		if ( ((snake.cuerpo[0][0] - i[0]) < tamano) and ((snake.cuerpo[0][0] - i[0]) > (tamano * (-1)))):
			if ( ((snake.cuerpo[0][1] - i[1]) < tamano) and ((snake.cuerpo[0][1] - i[1]) > (tamano * (-1)))):
				vivo[0] = False
				break


def col_borde( canvas, snake, vivo):
	if ((snake.cuerpo[0][0]) < ((snake.dimensione_cuerpo + snake.borde)) or 
	snake.cuerpo[0][0] > canva.winfo_widht() - ((snake.dimensione_cuerpo + snake.borde))):
		vivo[0] = False

	elif ((snake.cuerpo[0][1]) < ((snake.dimensione_cuerpo + snake.borde)) or 
	snake.cuerpo[0][1] > canva.winfo_height() - ((snake.dimensione_cuerpo + snake.borde))):
		vivo[0] = False

	else:
		pass	
		
def teleport( canvas, snake):
	if ((snake.cuerpo[0][0]) < ((snake.dimensione_cuerpo + snake.borde))):
		snake.cuerpo[0][0] = canvas.winfo_widht() - ((snake.dimensione_cuerpo + snake.borde))

	elif (snake.cuerpo[0][0] > canva.winfo_widht() - ((snake.dimensione_cuerpo + snake.borde))):
		snake.cuerpo[0][0] = ((snake.dimensione_cuerpo + snake.borde))

	elif ((snake.cuerpo[0][1]) < ((snake.dimensione_cuerpo + snake.borde))):
		snake.cuerpo[0][1] = canvas.winfo_height() - ((snake.dimensione_cuerpo + snake.borde))

	elif (snake.cuerpo[0][1] > canva.winfo_height() - ((snake.dimensione_cuerpo + snake.borde))):
		snake.cuerpo[0][1] =((snake.dimensione_cuerpo + snake.borde))
	else:
		pass
		
