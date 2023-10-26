import tkinter as tk
import LCD_1in44
import LCD_Config
# Funktionen, die aufgerufen werden, wenn die Buttons geklickt werden
def button1_click():
    label.config(text="Button 1 wurde geklickt")

def button2_click():
    label.config(text="Button 2 wurde geklickt")

def button3_click():
    label.config(text="Button 3 wurde geklickt")

# Hauptfenster erstellen
root = tk.Tk()
root.title("1.44-Zoll Display UI")

# Labels und Buttons hinzufügen
label = tk.Label(root, text="Drücken Sie einen Button")
label.pack(pady=10)

button1 = tk.Button(root, text="Button 1", command=button1_click)
button1.pack(pady=5)

button2 = tk.Button(root, text="Button 2", command=button2_click)
button2.pack(pady=5)

button3 = tk.Button(root, text="Button 3", command=button3_click)
button3.pack(pady=5)

# Die GUI starten
root.mainloop()