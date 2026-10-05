import tkinter as tk
from tkinter import ttk, messagebox

class ConversorUnidadesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Unidades")
        self.root.geometry("450x580")
        self.root.resizable(False, False)

        # Paleta 100% Clara y Suave (Sin Negro)
        self.BG_COLOR = "#F7F4EF"       # Beige crema suave para el fondo principal
        self.CARD_BG = "#FFFFFF"        # Blanco puro para la tarjeta central
        self.ENTRY_BG = "#EFEAE1"       # Beige arena claro para cajas de texto y menús
        self.ROSE_ACCENT = "#D89A9E"    # Rosa palo / Rose Gold elegante para el botón
        self.ROSE_HOVER = "#C5878B"     # Rosa ligeramente más cálido al pasar el cursor
        self.TEXT_MAIN = "#4A4238"      # Marrón espresso suave para los textos (reemplaza al negro)
        self.TEXT_MUTED = "#8C8275"     # Marrón topo suave para etiquetas secundarias

        self.root.configure(bg=self.BG_COLOR)

        # Estilo ttk para el ComboBox
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.style.configure('TCombobox',
                             fieldbackground=self.ENTRY_BG,
                             background=self.CARD_BG,
                             foreground=self.TEXT_MAIN,
                             bordercolor=self.BG_COLOR,
                             arrowcolor=self.ROSE_ACCENT)
        
        self.style.map('TCombobox', 
                       fieldbackground=[('readonly', self.ENTRY_BG)],
                       foreground=[('readonly', self.TEXT_MAIN)])

        # Estructura de Datos de Conversiones (Requisitos A - G)
        self.opciones_conversion = {
            "A) Longitud": [
                "Metros (m) a Kilómetros (km)",
                "Metros (m) a Millas",
                "Centímetros (cm) a Pulgadas",
                "Metros (m) a Pies"
            ],
            "B) Temperatura": [
                "Celsius a Fahrenheit",
                "Celsius a Kelvin",
                "Fahrenheit a Kelvin"
            ],
            "C) Masa": [
                "Kilogramos (kg) a Libras (lb)",
                "Gramos (gr) a Onzas",
                "Toneladas (tn) a Kilogramos (kg)"
            ],
            "D) Velocidad": [
                "km/h a mph",
                "km/h a m/s",
                "km/h a Nudos"
            ],
            "E) Volumen": [
                "Litros a Galones",
                "Litros a Pies Cúbicos"
            ],
            "F) Monedas": [
                "Pesos a Dólares",
                "Pesos a Reales",
                "Pesos a Euros"
            ],
            "G) Informática": [
                "Bytes (B) a Kilobytes (KB)",
                "Kilobytes (KB) a Megabytes (MB)",
                "Megabytes (MB) a Gigabytes (GB)"
            ]
        }

        # Tasas de cambio para Monedas
        self.TASAS_MONEDAS = {
            "USD": 1000.0,
            "BRL": 180.0,
            "EUR": 1100.0
        }

        self.crear_interface()

    def crear_interface(self):
        # Título Principal
        lbl_titulo = tk.Label(
            self.root, 
            text="CONVERSOR DE UNIDADES", 
            font=("Georgia", 13, "bold"), 
            bg=self.BG_COLOR, 
            fg=self.TEXT_MAIN
        )
        lbl_titulo.pack(pady=(25, 15))

        # Tarjeta Central (Blanca sobre fondo crema)
        frame_card = tk.Frame(self.root, bg=self.CARD_BG, bd=0, highlightthickness=0)
        frame_card.pack(padx=30, pady=10, fill="both", expand=True)

        # 1. Categoría (OptionMenu)
        lbl_cat = tk.Label(frame_card, text="Categoría", font=("Helvetica", 9, "bold"), bg=self.CARD_BG, fg=self.TEXT_MUTED)
        lbl_cat.pack(anchor="w", padx=20, pady=(20, 5))

        self.var_categoria = tk.StringVar(self.root)
        categorias = list(self.opciones_conversion.keys())
        self.var_categoria.set(categorias[0])

        menu_categoria = tk.OptionMenu(
            frame_card, 
            self.var_categoria, 
            *categorias, 
            command=self.actualizar_combobox
        )
        menu_categoria.config(
            bg=self.ENTRY_BG, 
            fg=self.TEXT_MAIN, 
            activebackground=self.ROSE_ACCENT, 
            activeforeground="#FFFFFF",
            bd=0, 
            highlightthickness=0, 
            font=("Helvetica", 10),
            anchor="w"
        )
        menu_categoria["menu"].config(
            bg=self.ENTRY_BG, 
            fg=self.TEXT_MAIN, 
            activebackground=self.ROSE_ACCENT,
            activeforeground="#FFFFFF"
        )
        menu_categoria.pack(fill="x", padx=20, pady=(0, 15))

        # 2. Conversión (ComboBox)
        lbl_conv = tk.Label(frame_card, text="Tipo de Conversión", font=("Helvetica", 9, "bold"), bg=self.CARD_BG, fg=self.TEXT_MUTED)
        lbl_conv.pack(anchor="w", padx=20, pady=(5, 5))

        self.combo_conversion = ttk.Combobox(frame_card, state="readonly", font=("Helvetica", 10))
        self.combo_conversion.pack(fill="x", padx=20, pady=(0, 15))

        # 3. Entrada de Valor
        lbl_val = tk.Label(frame_card, text="Valor a Convertir", font=("Helvetica", 9, "bold"), bg=self.CARD_BG, fg=self.TEXT_MUTED)
        lbl_val.pack(anchor="w", padx=20, pady=(5, 5))

        self.entry_valor = tk.Entry(
            frame_card, 
            font=("Helvetica", 11), 
            bg=self.ENTRY_BG, 
            fg=self.TEXT_MAIN, 
            insertbackground=self.ROSE_ACCENT,
            bd=0, 
            relief="flat"
        )
        self.entry_valor.pack(fill="x", padx=20, ipady=8, pady=(0, 20))

        # 4. Botón Convertir (Rosa Palo)
        btn_convertir = tk.Button(
            frame_card, 
            text="CONVERTIR", 
            command=self.realizar_conversion, 
            bg=self.ROSE_ACCENT, 
            fg="#FFFFFF", 
            font=("Helvetica", 10, "bold"), 
            bd=0, 
            activebackground=self.ROSE_HOVER, 
            activeforeground="#FFFFFF",
            cursor="hand2"
        )
        btn_convertir.pack(fill="x", padx=20, ipady=8, pady=(0, 20))

        # 5. Resultado
        self.lbl_resultado = tk.Label(
            frame_card, 
            text="Resultado: -", 
            font=("Georgia", 11, "bold"), 
            bg=self.CARD_BG, 
            fg=self.ROSE_ACCENT,
            wraplength=350
        )
        self.lbl_resultado.pack(pady=(0, 20))

        # Cargar primeras opciones
        self.actualizar_combobox(categorias[0])

    def actualizar_combobox(self, categoria_seleccionada):
        opciones = self.opciones_conversion[categoria_seleccionada]
        self.combo_conversion['values'] = opciones
        self.combo_conversion.current(0)

    def realizar_conversion(self):
        try:
            val_text = self.entry_valor.get().replace(",", ".")
            if not val_text:
                messagebox.showwarning("Atención", "Por favor ingrese un valor numérico.")
                return
            
            valor = float(val_text)
            conversion = self.combo_conversion.get()
            res = 0
            unidad = ""

            # Logica A) Longitud
            if conversion == "Metros (m) a Kilómetros (km)":
                res, unidad = valor / 1000, "km"
            elif conversion == "Metros (m) a Millas":
                res, unidad = valor * 0.000621371, "millas"
            elif conversion == "Centímetros (cm) a Pulgadas":
                res, unidad = valor * 0.393701, "pulgadas"
            elif conversion == "Metros (m) a Pies":
                res, unidad = valor * 3.28084, "pies"

            # Logica B) Temperatura
            elif conversion == "Celsius a Fahrenheit":
                res, unidad = (valor * 9/5) + 32, "°F"
            elif conversion == "Celsius a Kelvin":
                res, unidad = valor + 273.15, "K"
            elif conversion == "Fahrenheit a Kelvin":
                res, unidad = (valor - 32) * 5/9 + 273.15, "K"

            # Logica C) Masa
            elif conversion == "Kilogramos (kg) a Libras (lb)":
                res, unidad = valor * 2.20462, "lb"
            elif conversion == "Gramos (gr) a Onzas":
                res, unidad = valor * 0.035274, "oz"
            elif conversion == "Toneladas (tn) a Kilogramos (kg)":
                res, unidad = valor * 1000, "kg"

            # Logica D) Velocidad
            elif conversion == "km/h a mph":
                res, unidad = valor * 0.621371, "mph"
            elif conversion == "km/h a m/s":
                res, unidad = valor / 3.6, "m/s"
            elif conversion == "km/h a Nudos":
                res, unidad = valor * 0.539957, "nudos"

            # Logica E) Volumen
            elif conversion == "Litros a Galones":
                res, unidad = valor * 0.264172, "galones"
            elif conversion == "Litros a Pies Cúbicos":
                res, unidad = valor * 0.0353147, "ft³"

            # Logica F) Monedas
            elif conversion == "Pesos a Dólares":
                res, unidad = valor / self.TASAS_MONEDAS["USD"], "USD"
            elif conversion == "Pesos a Reales":
                res, unidad = valor / self.TASAS_MONEDAS["BRL"], "BRL"
            elif conversion == "Pesos a Euros":
                res, unidad = valor / self.TASAS_MONEDAS["EUR"], "EUR"

            # Logica G) Informática
            elif conversion == "Bytes (B) a Kilobytes (KB)":
                res, unidad = valor / 1024, "KB"
            elif conversion == "Kilobytes (KB) a Megabytes (MB)":
                res, unidad = valor / 1024, "MB"
            elif conversion == "Megabytes (MB) a Gigabytes (GB)":
                res, unidad = valor / 1024, "GB"

            self.lbl_resultado.config(text=f"Resultado: {res:,.4f} {unidad}")

        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorUnidadesApp(root)
    root.mainloop()