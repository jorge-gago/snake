import tkinter

"""
def crear( width = 804, height = 868):

	raiz = tkinter.Tk()
	geometry = str(width) + "x" + str(height)
	raiz.geometry(geometry)
	raiz.title("Snake ")
	
	canvas = tkinter.Canvas( raiz, width = (width - 4), height = (height - 68), bg = "black" )
	canvas.place( x = 0, y = 0)

	ptns = tkinter.Canvas(raiz, width = (width - 4), height = 60, bg = "blue")
	ptns.place( x = 0, y = (height - 64))
	
	return raiz, canvas, ptns

"""
def crear( width = 804, height = 868):

	raiz = tkinter.Tk()
	geometry = str(width) + "x" + str(height)
	raiz.geometry(geometry)
	raiz.title("Snake ")
	
	return raiz

def partes(raiz):
	raiz.update_idletasks()

	width = raiz.winfo_width()
	height = raiz.winfo_height()

	canvas = tkinter.Canvas( raiz, width = (width - 4), height = (height - 68), bg = "black" )
	canvas.place(x = 0, y = 0)

	ptns = tkinter.Canvas(raiz, width = (width - 4), height = 60, bg = "blue")
	ptns.place( x = 0, y = (height - 64))

	canvas.focus_set()

	return canvas, ptns
#"""	

def cierre(raiz):
	raiz.mainloop()


def show( canvas, obj):
	tamano = obj.dimensione_cuerpo
	borde = obj.borde

	for i in obj.cuerpo:
		canvas.create_rectangle( i[0] - tamano, i[1] - tamano, i[0] + tamano, i[1] + tamano, fill = i[2])

def update(canvas, obj1, obj2):
	canvas.delete("all")
	canvas.show(canvas, obj1)
	canvas.show(canvas, obj2)

def mov(canvas):
	raiz.after( 80, mov, raiz, canvas)

def key(event):
	global o
	print("try")
	print( "press: ", event.char)
	
	if o :
		o = False
	else:
		o = True
	



# para pruebas

o = False

def cuadros(canvas):
	canvas.create_rectangle(390, 390, 410, 410, fill = "white")
	#print("cuadro")

def repetir(canvas):
	canvas.delete("all")
	canvas.after(10, cuadros, canvas)
	canvas.bind('<Key>', key)
	canvas.after(40, repetir, canvas)

raiz = crear()
canvas, frame = partes(raiz)
	
#raiz.after(80, lambda: mov( raiz, canvas))

#canvas.bind('<Key>', key, canvas)
repetir( canvas )

cierre(raiz)

#para juego

