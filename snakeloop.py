import Snake
import fruta
import reglas
import pantalla

vivo = [ True]
# loop del juego

def loop(event = ""):
	reglas.vels(snake)
	
	if (event != ""):
		pantalla.key(event)
		pantalla.update(canvas, snake, fruta)
		
	if (vivo[0]):
		canvas.delete("all")
		canvas.bind('<Key>', pantalla.key)
		pos = reglas.actu_vel()
		snake.move( pos)
		reglas.colition(canvas, snake, fruta, vivo)
		pantalla.update(canvas, snake, fruta)
		canvas.after( 60, loop)
	else:
		fail = pantalla.fail(canvas)
		reset()
		#canvas.after( 1000, reset(fail))
		#canvas.delete("all")
		#canvas.bind("<Key>", lambda event, fail = fail: reset( event, fail))

		
def reset( fail = 0 ):
	global vivo
	canvas.delete("all")
	print("cant")
	vivo = [True]
	snake.set()
	fruta.cant_fru()

	print(snake.cuerpo)
	print("fin")
	wait()




def wait():
	print(snake.cuerpo)
	if (vivo[0]):
		print("wait")
		canvas.bind('<Key>', loop)	
		print("pass")


#----inicio----

raiz = pantalla.crear()
canvas, frame = pantalla.partes(raiz)

frame.update_idletasks()

snake = Snake.Snake()
fruta = fruta.Frutas( raiz.winfo_width(), raiz.winfo_height() - frame.winfo_height())

fruta.cant_fru()

wait()


pantalla.cierre(raiz)