import tkinter as tk
from tkinter import messagebox

# Alfabeto en español con Ñ
ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrar():
    mensaje = entry_mensaje.get().upper()
    clave = entry_clave.get().upper()
    
    if not mensaje or not clave:
        messagebox.showwarning("Error", "Llena todos los campos")
        return
        
    resultado = ""
    idx = 0
    for letra in mensaje:
        if letra in ALFABETO:
            pos_m = ALFABETO.index(letra)
            pos_k = ALFABETO.index(clave[idx % len(clave)])
            nueva_pos = (pos_m + pos_k) % len(ALFABETO)
            resultado += ALFABETO[nueva_pos]
            idx += 1
        else:
            resultado += letra
            
    entry_resultado.delete(0, tk.END)
    entry_resultado.insert(0, resultado)

# Ventana basica
ventana = tk.Tk()
ventana.title("Cifrado Vigenere")
ventana.geometry("350x250")

# Elementos
tk.Label(ventana, text="Clave:").pack()
entry_clave = tk.Entry(ventana)
entry_clave.pack()

tk.Label(ventana, text="Mensaje:").pack()
entry_mensaje = tk.Entry(ventana)
entry_mensaje.pack()

btn = tk.Button(ventana, text="Cifrar", command=cifrar)
btn.pack(pady=10)

tk.Label(ventana, text="Resultado:").pack()
entry_resultado = tk.Entry(ventana)
entry_resultado.pack()

ventana.mainloop()