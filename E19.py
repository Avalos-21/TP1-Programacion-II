import tkinter as tk
import random
app=tk.Tk()
vidas=6
def adivina():
    global vidas
    global nA
    numero=int(intento.get())
    if numero == nA:
        lblmensaje.config(text="Felicitaciones Adivinaste!!")
        boton.config(state="disabled")
    elif numero < nA:
        vidas=vidas-1
        lblvidas.config(text="❤" * vidas)
        lblmensaje.config(text="El numero es mayor")
    else:
        vidas=vidas-1
        lblvidas.config(text="❤" * vidas)
        lblmensaje.config(text="El numero es menor")
    if vidas==0:
        lblmensaje.config(text="Perdiste el numero era: "+ str(nA))
        boton.config(state="disabled")
    

intento=tk.StringVar(app)
nA=random.randint(1,50)
print(nA)

#Medidas
app.geometry("320x320")
app.configure(background="#946cee")
tk.Wm.wm_title(app,"Adivina el numero")

tk.Label(
    app,
    text="Adivine el numero entre el 1 y el 50",
    font=("Arial",20),
    bg="#8F00FF",
    fg="black",
    justify="center"
    ).pack(
        fill=tk.BOTH,
        expand=False,
    )
lblvidas=tk.Label(
    app,
    text=("❤️❤️❤️❤️❤️❤"),
    font=("center",30),
    bg="#946cee",
    fg="red",
)
lblvidas.pack(expand=True)


tk.Entry(
    font=("center",30),
    bg="#8F00FF",
    fg="black",
    justify="center",
    textvariable=intento,
    ).pack(
        expand=True,
    )
lblmensaje=tk.Label(
    app,
    font=("center",25),
    bg="#946cee",
    fg="black",
)
lblmensaje.pack(expand=True)

boton=tk.Button(
    app,
    text="Adivinar",
    font=("Verdana",20,"bold"),
    bg="#8F00FF",
    fg="black",
    command=adivina
)
boton.pack(expand= True)
app.mainloop()