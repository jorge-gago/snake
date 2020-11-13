import tkinter
import reglas

wait = 50
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

	ptns = tkinter.Canvas(raiz, width = (width - 4), height = 60, bg = "black")
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
	#canvas.delete("all")
	show(canvas, obj1)
	show(canvas, obj2)


def key(event):
	press = event.char
	reglas.moves(press)


	#print(event)
	 
def fail(canvas):
	canvas.delete("all")
	label = tkinter.Label(canvas, text = "GAME OVER", bg = "black", fg = "white", font = (50))
	#label.place( x = ((canvas.winfo_width()/2)-(label.winfo_width()/2)), y = (canvas.winfo_height()/2))
	label.place( x = ((canvas.winfo_width()/2)- 40), y = canvas.winfo_height()/2)
	label.focus_set()
	label.after(1000, des_fail, label, canvas)
	

def des_fail(fail, canvas):
	fail.destroy()
	canvas.focus_set()





# para pruebas


def cuadros(canvas):
	canvas.create_rectangle(390, 390, 410, 410, fill = "white")
	#print("cuadro")

def repetir(canvas):
	canvas.delete("all")
	canvas.after(wait, cuadros, canvas)
	canvas.bind('<Key>', key)
	canvas.after(wait, repetir, canvas)


"""
raiz = crear()
canvas, frame = partes(raiz)
	

repetir( canvas )

cierre(raiz)

"""