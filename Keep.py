import tkinter as tk
from tkinter import *
from tkinter import ttk
import time

class Pemasukan :
    # Function utama pada jendela Pemasukan
    def add() :
        global add_window
        global label_background
        global combobox_jenis
        global combobox_catatan
        global entry_jumlah

        # Pengaturan jendela Pemasukan
        add_window = tk.Toplevel()
        add_window.resizable(False, False)
        screenwidth = add_window.winfo_screenwidth()
        screenheight = add_window.winfo_screenheight()
        xposition = int((screenwidth / 2) - (212 / 2))
        yposition = int((screenheight / 2) - (135 / 2) - 100)
        add_window.geometry(f"212x135+{xposition}+{yposition}")
        label_background = tk.Label(add_window, background="#515dcf")
        label_background.pack()

        # Label Jenis data
        label_jenis = tk.Label(label_background, text="Jenis", bg="#515dcf")
        label_jenis.grid(row=0, column=0, padx=5, pady=5)

        # Label Catatan Pemasukan
        label_catatan = tk.Label(label_background, text="Catatan", bg="#515dcf")
        label_catatan.grid(row=1, column=0, padx=5, pady=5)

        # Label Jumlah Pemasukan
        label_jumlah = tk.Label(label_background, text="Jumlah", bg="#515dcf")
        label_jumlah.grid(row=2, column=0, padx=5, pady=5)

        # Button Submit
        button_submit = tk.Button(label_background, text="Selesai", width=15, padx=5, pady=2, command=Pemasukan.submit)
        button_submit.grid(row=3, column=0, columnspan=2, pady=5)

        # Combobox Jenis data
        jenis_option = ["Pemasukan"]
        combobox_jenis = ttk.Combobox(label_background, values=jenis_option, width=20)
        combobox_jenis.current(0)
        combobox_jenis.bind("<<ComboboxSelected>>", Pemasukan.selected_jenis)
        combobox_jenis.grid(row=0, column=1, padx=5, pady=5)

        # Combobox Catatan Pemasukan
        catatan_option = ["Gaji", "Bonus", "Uang Jajan", "Voucher", "Lainnya"]
        combobox_catatan = ttk.Combobox(label_background, values=catatan_option, width=20)
        combobox_catatan.current(0)
        combobox_catatan.bind("<<ComboboxSelected>>", Pemasukan.selected_catatan)
        combobox_catatan.grid(row=1, column=1, padx=5, pady=5)

        # Entryfield Jumlah Pemasukan
        entry_jumlah = tk.Entry(label_background, width=23)
        entry_jumlah.grid(row=2, column=1, padx=5, pady=5)

        add_window.mainloop()

    # Function untuk menerima hasil combobox Jenis data
    def selected_jenis(event) :
        label_jenis = Label(label_background, text=combobox_jenis.get())

    # Function untuk menerima hasil combobox Catatan Pemasukan
    def selected_catatan(event) :
        label_catatan = Label(label_background, text=combobox_catatan.get())

    # Function untuk Button Submit
    def submit() :
        with open("Database.txt", "r", encoding="UTF-8") as file :
            content = file.readlines()
            if len(content) == 1 :
                with open("Database.txt", "a", encoding="UTF-8") as file :
                    tanggal = time.strftime("%d/%m/%Y")
                    jenis = combobox_jenis.get()
                    catatan = combobox_catatan.get()
                    jumlah = entry_jumlah.get()
                    total = jumlah

                    new_database = f'{tanggal:<10},{jenis:<12},{catatan:<20},{jumlah:<10},{total:<15}\n'
                    file.write(new_database)
            else :
                with open("Database.txt", "a", encoding="UTF-8") as file :
                    tanggal = time.strftime("%d/%m/%Y")
                    jenis = combobox_jenis.get()
                    catatan = combobox_catatan.get()
                    jumlah = entry_jumlah.get()
                    
                    index_data = len(content) - 1
                    new_data = content[index_data].split(",")
                    total = int(new_data[4]) + int(jumlah)

                    new_database = f'{tanggal:<10},{jenis:<12},{catatan:<20},{jumlah:<10},{total:<15}\n'
                    file.write(new_database)

        add_window.destroy()
