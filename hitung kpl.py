import tkinter as tk
from tkinter import ttk
import math

class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        
        self.title("Menghitung KPL")
        self.minsize(480, 320)
        
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 1, weight=1)
        tk.Grid.rowconfigure(self, 2, weight=1)
        tk.Grid.rowconfigure(self, 3, weight=1)
        tk.Grid.rowconfigure(self, 4, weight=1)
        tk.Grid.rowconfigure(self, 5, weight=999)
        
        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 2, weight=1)
        tk.Grid.columnconfigure(self, 3, weight=1)
        tk.Grid.columnconfigure(self, 4, weight=1)
        tk.Grid.columnconfigure(self, 5, weight=999)
                
        self.text_entry()
    
    def hasil(self):
        
        KPL_sebelumnya = float(self.KPL_sebelumnya_entry.get())
        jarak_sebelumnya = float(self.jarak_sebelumnya_entry.get())
        KPL_sekarang = float(self.KPL_sekarang_entry.get())
        jarak_sekarang = float(self.jarak_sekarang_entry.get())
        
        liter_sebelumnya = jarak_sebelumnya / KPL_sebelumnya
        liter_sekarang = jarak_sekarang / KPL_sekarang
        liter = liter_sekarang - liter_sebelumnya
        if liter<0 :
            liter = liter * -1
        jarak_terakhir = jarak_sekarang - jarak_sebelumnya
        if jarak_terakhir<0 :
            jarak_terakhir = jarak_terakhir * -1
        KPL_terakhir = jarak_terakhir / liter
        
        self.KPL_terakhir_label.configure(text="{:.2f}".format(KPL_terakhir))
        
    def text_entry(self):
        KPL_sebelumnya_label = ttk.Label(self, text="KPL Sebelumnya :")
        KPL_sebelumnya_label.grid(column=0, row=0, padx=10, pady=10)
    
        KPL_sekarang_label = ttk.Label(self, text="KPL Sekarang       :")
        KPL_sekarang_label.grid(column=0, row=1, padx=10, pady=10, sticky=tk.EW)
        
        jarak_sebelumnya_label = ttk.Label(self, text="Jarak Sebelumnya :")
        jarak_sebelumnya_label.grid(column=2, row=0, padx=10, pady=10)
        
        jarak_sekarang_label = ttk.Label(self, text="Jarak Sekarang      :")
        jarak_sekarang_label.grid(column=2, row=1, padx=10, pady=10, sticky=tk.EW)

        self.KPL_sebelumnya_entry = ttk.Entry(self)
        self.KPL_sebelumnya_entry.grid(column=1, row=0, padx=10, pady=10)
        
        self.KPL_sekarang_entry = ttk.Entry(self)
        self.KPL_sekarang_entry.grid(column=1, row=1, padx=10, pady=10)
        
        self.jarak_sebelumnya_entry = ttk.Entry(self)
        self.jarak_sebelumnya_entry.grid(column=3, row=0, padx=10, pady=10)
        
        self.jarak_sekarang_entry = ttk.Entry(self)
        self.jarak_sekarang_entry.grid(column=3, row=1, padx=10, pady=10)
        
        hitung_button = ttk.Button(self, text="Hitung KPL", command=self.hasil)
        hitung_button.grid(column=2, row=3, padx=10, pady=10, columnspan=1, sticky=tk.EW)
        
        KPL_terakhir_label = ttk.Label(self, text="KPL Terakhir         :")
        KPL_terakhir_label.grid(column=2, row=4, padx=10, pady=10, sticky=tk.W)
        
        self.KPL_terakhir_label = ttk.Label(self, text="")
        self.KPL_terakhir_label.grid(column=3, row=4, padx=10, pady=1,sticky=tk.EW)
        

window = Window()
window.mainloop()
