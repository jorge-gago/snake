import tkinter

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

def partes(raiz):
	canvas = tkinter.Canvas( raiz, width = (raiz.winfo_width() - 4), height = (raiz.winfo_height() - 68), bg = "black" )
	canvas.place( x = 0, y = 0)

	ptns = tkinter.Canvas(raiz, width = (raiz.winfo_width() - 4), height = 60, bg = "blue")
	ptns.place( x = 0, y = (raiz.winfo_height() - 64))

	return canvas, ptns

def cierre(raiz):
	raiz.mainloop()


raiz, canvas, frame = crear()
#canvas, frame = partes(raiz)
#frame.config(bg = "black")
cierre(raiz)

#partes(raiz)