from tkinter import *
principal=Tk()

ancho = 600
alto = 400

principal.geometry(str(ancho)+'x'+str(alto))
principal.title("Examen Final")

def sumar():
    val1 = float(input1.get())
    val2 = float(input2.get())
    res = val1 + val2
    txt1['text'] = 'La suma de  {}  y  {}  es = {}'.format(val1, val2, res)


txt2 = Label(principal, text= 'ingrese el primer número')
txt2.pack()
input1= Entry(principal)
input1.pack()

txt3 = Label(principal, text= 'ingrese el segundo número')
txt3.pack()
input2= Entry(principal)
input2.pack()

btn1 = Button(principal, text = 'sumar', command= sumar)
btn1.pack()

txt1 = Label(principal)
txt1.pack()

principal.mainloop()
