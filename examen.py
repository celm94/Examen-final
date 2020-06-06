from tkinter import *
principal=Tk()

ancho = 600
alto = 400

principal.geometry(str(ancho)+'x'+str(alto))
principal.title("Examen Final")

txt1 = Label(principal, text= 'Nombre')
txt1.pack()
input1= Entry(principal)
input1.pack()

txt2 = Label(principal, text= 'Apellido')
txt2.pack()
input2= Entry(principal)
input2.pack()

txt3 = Label(principal, text= 'Día')
txt3.pack()
input3= Entry(principal)
input3.pack()

txt4 = Label(principal, text= 'Mes')
txt4.pack()
input4= Entry(principal)
input4.pack()

txt5 = Label(principal, text= 'Año')
txt5.pack()
input5= Entry(principal)
input5.pack()


principal.mainloop()