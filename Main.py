import tkinter as tk
from tkinter import *
from tkinter import ttk
from Keep import Pemasukan
from Spend import Pengeluaran
import History
import os

class Main :
    # Functioun utama pada program
    def main_function() :
        global window

        # Pengaturan jendela utama
        window = tk.Tk()
        window.resizable(False, False)
        window.title("Aplikasi Manajemen Keuangan")
        window.iconbitmap("../img1.ico")
        screenwidth = window.winfo_screenwidth()
        screenheight = window.winfo_screenheight()
        xposition = int((screenwidth / 2) - (485 / 2))
        yposition = int((screenheight / 2) - (550 / 2) - 50)
        window.geometry(f"485x550+{xposition}+{yposition}")
        label_background = tk.Label(window, background="#515dcf")
        label_background.pack()
        
        # Button Pemasukan
        add_button = tk.Button(label_background, text="PEMASUKAN", padx=10, pady=5, width=13, font="Arial 10", command=Pemasukan.add)
        add_button.grid(row=0, column=0, padx=10, pady=40)

        # Button Pengeluaran
        substract_button = tk.Button(label_background, text="PENGELUARAN", padx=10, pady=5, width=13, font="Arial 10", command=Pengeluaran.substract)
        substract_button.grid(row=0, column=1, padx=10, pady=40)

        # Button Refresh
        refresh_button = tk.Button(label_background, text="REFRESH", padx=10, pady=5, width=13, font="Arial 10", command=Main.refresh_program)
        refresh_button.grid(row=0, column=2, padx=10, pady=40)

        # Button Reset
        reset_button = tk.Button(label_background, text="RESET", padx=10, pady=5, width=13, font="Arial 10", command=Main.reset_program)
        reset_button.grid(row=3, column=0, columnspan=3, padx=10, pady=20)

        # Mengambil data total saldo yang ada pada database
        with open("Database.txt", "r", encoding="UTF-8") as file :
            content = file.readlines()
            if len(content) == 1 :
                saldo = 0
            else :
                index_data = len(content) - 1
                new_data = content[index_data].split(",")
                saldo = int(new_data[4])

        # Label Saldo saat ini              
        saldo_label = tk.Label(label_background, text=f"SALDO ANDA : Rp{saldo:,}", padx=10, pady=5, width=55, height=2, font="Arial 10", anchor="w")
        saldo_label.grid(row=1, column=0, columnspan=3, padx=10, pady=20)

        # Frame Riwayat Saldo
        history_frame = tk.Frame(label_background)
        history_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=20)

        # Style Header Riwayat Saldo
        history_style = ttk.Style()
        history_style.theme_use("clam")
        history_style.configure("Treeview", background="#b8b3b0", fieldbackground="#b8b3b0")
        history_style.map("Treeview", background=[("selected", "blue")])

        # Scrollbar Riwayat Saldo
        history_scroolbar = tk.Scrollbar(history_frame)
        history_scroolbar.pack(side="right", fill="y")

        # Treeview untuk menampung data Riwayat Saldo
        saldo_history = ttk.Treeview(history_frame, yscrollcommand=history_scroolbar.set)
        saldo_history.tag_configure("Pemasukan", foreground="green")
        saldo_history.tag_configure("Pengeluaran", foreground="red")
        saldo_history["columns"] = ("Jenis", "Catatan", "Jumlah")
        saldo_history.column("#0", width=100, minwidth=100)
        saldo_history.column("Jenis", anchor="w", width=100, minwidth=100)
        saldo_history.column("Catatan", anchor="w", width=120, minwidth=120)
        saldo_history.column("Jumlah", anchor="center", width=100, minwidth=100)
        saldo_history.heading("#0", text="Tanggal", anchor="w")
        saldo_history.heading("Jenis", text="Jenis", anchor="w")
        saldo_history.heading("Catatan", text="Catatan", anchor="w")
        saldo_history.heading("Jumlah", text="Jumlah", anchor="center")
        saldo_history.pack(side="left")
        history_scroolbar.config(command=saldo_history.yview)

        # Mengambil data pada database untuk ditampung dalam Treeview
        hasil = History.read_data()
        counter = 1
        for index, data in enumerate(hasil) :
            if counter == 1 :
                counter += 1
                pass
            else :
                hasil_data = data.split(",")
                tanggal = hasil_data[0]
                jenis = hasil_data[1]
                catatan = hasil_data[2]
                jumlah = hasil_data[3]
                total = hasil_data[4]
                if jenis == "Pemasukan   " :
                    saldo_history.insert(parent="", index="end", iid=(index - 1), text=tanggal, values=(jenis, catatan, jumlah), tags="Pemasukan")
                else :
                    saldo_history.insert(parent="", index="end", iid=(index - 1), text=tanggal, values=(jenis, catatan, jumlah), tags="Pengeluaran")

        window.mainloop()

    # Function untuk melakukan refresh pada program
    def refresh_program() :
        window.destroy()
        Main.main_function()

    # Function untuk melakukan reset pada program
    def reset_program() :
        with open("Database.txt", "r") as file :
            counter = 1
            while True :
                content = file.readline()
                if len(content) == 0 :
                    break
                elif counter == 1 :
                    with open("Backup.txt", "a", encoding="UTF-8") as backup_file :
                        backup_file.write(content)
                        counter += 1
                else :
                    pass

        os.replace("Backup.txt", "Database.txt")
        window.destroy()
        Main.main_function()


if __name__ == "__main__" :
    Main.main_function()
