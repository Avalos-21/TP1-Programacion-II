import os
import sys
import random
import tkinter as tk
from tkinter import messagebox

import ctypes
import winsound
from PIL import Image, ImageTk


def ruta(archivo):
    """Devuelve la ruta del recurso (funciona también al empaquetar con PyInstaller)."""
    if hasattr(sys, "_MEIPASS"):  # ejecutable creado con PyInstaller
        base = sys._MEIPASS
    else:
        try:
            base = os.path.dirname(os.path.abspath(__file__))
        except NameError:  # por ejemplo, al ejecutar desde Thonny sin guardar el archivo
            base = os.getcwd()
    return os.path.join(base, archivo)


ANCHO, ALTO = 450, 560


class Sonido:
    """Reproduce mp3 usando la API de Windows (MCI). No requiere instalar nada."""

    def __init__(self, archivo, alias, volumen=None):
        self.alias = alias
        self.ok = False
        if not os.path.exists(archivo):
            print(f"[Sonido] No se encuentra el archivo: {archivo}")
            return
        # Se prueba abrir con el tipo mpegvideo y, si falla, dejando que Windows lo detecte
        if self._mci(f'open "{archivo}" type mpegvideo alias {alias}') != 0:
            if self._mci(f'open "{archivo}" alias {alias}') != 0:
                return
        self._mci(f"set {alias} time format milliseconds")
        if volumen is not None:
            self._mci(f"setaudio {alias} volume to {volumen}")
        self.ok = True

    @staticmethod
    def _mci(comando):
        """Ejecuta un comando MCI. Devuelve 0 si salió bien; si no, muestra el error."""
        error = ctypes.windll.winmm.mciSendStringW(comando, None, 0, None)
        if error:
            buffer = ctypes.create_unicode_buffer(256)
            ctypes.windll.winmm.mciGetErrorStringW(error, buffer, 255)
            print(f"[Sonido] Error en '{comando}': {buffer.value}")
        return error

    def play(self):
        if self.ok:
            self._mci(f"play {self.alias} from 0")

    def esta_detenido(self):
        if not self.ok:
            return False
        buffer = ctypes.create_unicode_buffer(64)
        ctypes.windll.winmm.mciSendStringW(f"status {self.alias} mode", buffer, 63, None)
        return buffer.value == "stopped"


class PiedraPapelTijeraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, Papel, Tijera")
        self.root.geometry(f"{ANCHO}x{ALTO}")
        self.root.resizable(False, False)

        self.puntos_usuario = 0
        self.puntos_maquina = 0
        self.bloqueado = False

        self.iniciar_sonidos()
        self.cargar_imagenes()
        self.crear_interfaz()

    # ---------------------------------------------------------- SONIDOS
    def iniciar_sonidos(self):
        self.snd_click = Sonido(ruta("clik.mp3"), "click")
        self.snd_ganar = Sonido(ruta("ganar.mp3"), "ganar")
        # La música de fondo (WAV) se repite sola gracias a SND_LOOP
        self.root.after(300, self.iniciar_musica)

    def iniciar_musica(self):
        try:
            winsound.PlaySound(
                ruta("sonido_de_fondo.wav"),
                winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP,
            )
        except Exception as e:
            print("[Música] No se pudo reproducir:", e)

    def reproducir(self, sonido):
        if sonido:
            sonido.play()

    # ---------------------------------------------------------- IMÁGENES
    def cargar_imagenes(self):
        self.fondo = ImageTk.PhotoImage(
            Image.open(ruta("fondo.png")).convert("RGBA").resize((ANCHO, ALTO), Image.LANCZOS)
        )
        archivos = {"Piedra": "piedra.png", "Papel": "papel.png", "Tijera": "tijera.png"}
        self.img_grandes = {}
        self.img_chicas = {}
        for nombre, archivo in archivos.items():
            original = Image.open(ruta(archivo)).convert("RGBA")
            self.img_grandes[nombre] = ImageTk.PhotoImage(self.escalar(original, 95))
            self.img_chicas[nombre] = ImageTk.PhotoImage(self.escalar(original, 70))

    @staticmethod
    def escalar(imagen, alto):
        proporcion = alto / imagen.height
        return imagen.resize((int(imagen.width * proporcion), alto), Image.LANCZOS)

    # ---------------------------------------------------------- INTERFAZ
    def crear_interfaz(self):
        self.canvas = tk.Canvas(self.root, width=ANCHO, height=ALTO, highlightthickness=0, bd=0)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.fondo, anchor="nw")

        c = self.canvas
        c.create_text(ANCHO // 2, 45, text="P I E D R A  ·  P A P E L  ·  T I J E R A",
                      font=("Helvetica", 13, "bold"), fill="#37474f")

        self.txt_marcador = c.create_text(ANCHO // 2, 85, text="Tú: 0   —   Máquina: 0",
                                          font=("Helvetica", 12), fill="#546e7a")
        c.create_line(60, 112, ANCHO - 60, 112, fill="#b0bec5")

        # Zona de jugada (imágenes de lo elegido)
        self.img_usuario = c.create_image(120, 190, image="")
        self.img_maquina = c.create_image(330, 190, image="")
        self.txt_vs = c.create_text(ANCHO // 2, 190, text="", font=("Helvetica", 12, "bold"), fill="#78909c")

        self.txt_resultado = c.create_text(ANCHO // 2, 290, text="Selecciona una opción",
                                           font=("Helvetica", 12), fill="#455a64", justify="center")

        # Botones con imagen
        posiciones = {"Piedra": 90, "Papel": 225, "Tijera": 360}
        for nombre, x in posiciones.items():
            etiqueta = f"btn_{nombre}"
            c.create_image(x, 400, image=self.img_grandes[nombre], tags=(etiqueta,))
            c.create_text(x, 465, text=nombre, font=("Helvetica", 10), fill="#455a64", tags=(etiqueta,))
            c.tag_bind(etiqueta, "<Button-1>", lambda e, n=nombre: self.jugar(n))
            c.tag_bind(etiqueta, "<Enter>", lambda e: c.config(cursor="hand2"))
            c.tag_bind(etiqueta, "<Leave>", lambda e: c.config(cursor=""))

        # Botón de reinicio discreto
        c.create_text(ANCHO // 2, 525, text="Reiniciar marcador", font=("Helvetica", 9, "underline"),
                      fill="#78909c", tags=("btn_reiniciar",))
        c.tag_bind("btn_reiniciar", "<Button-1>", lambda e: self.reiniciar(click=True))
        c.tag_bind("btn_reiniciar", "<Enter>", lambda e: c.config(cursor="hand2"))
        c.tag_bind("btn_reiniciar", "<Leave>", lambda e: c.config(cursor=""))

    # ---------------------------------------------------------- LÓGICA
    def jugar(self, eleccion_usuario):
        if self.bloqueado:
            return
        self.reproducir(self.snd_click)

        eleccion_maquina = random.choice(["Piedra", "Papel", "Tijera"])
        gano_ronda = False

        if eleccion_usuario == eleccion_maquina:
            resultado, color = "Empate", "#78909c"
        elif (
            (eleccion_usuario == "Piedra" and eleccion_maquina == "Tijera") or
            (eleccion_usuario == "Papel" and eleccion_maquina == "Piedra") or
            (eleccion_usuario == "Tijera" and eleccion_maquina == "Papel")
        ):
            resultado, color = "¡Victoria!", "#2e7d32"
            self.puntos_usuario += 1
            gano_ronda = True
        else:
            resultado, color = "Derrota", "#c62828"
            self.puntos_maquina += 1

        c = self.canvas
        c.itemconfig(self.img_usuario, image=self.img_chicas[eleccion_usuario])
        c.itemconfig(self.img_maquina, image=self.img_chicas[eleccion_maquina])
        c.itemconfig(self.txt_vs, text="VS")
        c.itemconfig(
            self.txt_resultado, fill=color,
            text=f"Elegiste {eleccion_usuario}  /  La máquina eligió {eleccion_maquina}\n\n{resultado}"
        )
        c.itemconfig(self.txt_marcador, text=f"Tú: {self.puntos_usuario}   —   Máquina: {self.puntos_maquina}")

        if gano_ronda:
            self.reproducir(self.snd_ganar)

        # Serie a 5 puntos (con una pequeña pausa para que se vea la última jugada)
        if self.puntos_usuario == 5 or self.puntos_maquina == 5:
            self.bloqueado = True
            self.root.after(400, self.fin_de_serie)

    def fin_de_serie(self):
        if self.puntos_usuario == 5:
            messagebox.showinfo("Fin de la partida", "Has ganado la serie.")
        else:
            messagebox.showinfo("Fin de la partida", "La máquina ha ganado la serie.")
        self.reiniciar()

    def reiniciar(self, click=False):
        if click:
            self.reproducir(self.snd_click)
        self.bloqueado = False
        self.puntos_usuario = 0
        self.puntos_maquina = 0
        c = self.canvas
        c.itemconfig(self.txt_marcador, text="Tú: 0   —   Máquina: 0")
        c.itemconfig(self.txt_resultado, text="Selecciona una opción", fill="#455a64")
        c.itemconfig(self.img_usuario, image="")
        c.itemconfig(self.img_maquina, image="")
        c.itemconfig(self.txt_vs, text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = PiedraPapelTijeraApp(root)
    root.mainloop()
