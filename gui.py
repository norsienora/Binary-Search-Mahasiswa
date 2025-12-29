import tkinter as tk
from dataMahasiswa import mahasiswa
from performance import measure_search

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

MAX_POINTS = 7

trial_numbers = []
iter_times = []
recur_times = []

def search():
    try:
        target_nim = int(entry.get())
        result_i, t_i, result_r, t_r = measure_search(mahasiswa, target_nim)

        result_text.delete("1.0", tk.END)

        if result_i:
            result_text.insert(tk.END, "DATA MAHASISWA DITEMUKAN\n")
            result_text.insert(tk.END, f"NIM   : {result_i['nim']}\n")
            result_text.insert(tk.END, f"Nama  : {result_i['nama']}\n")
            result_text.insert(tk.END, f"Prodi : {result_i['prodi']}\n\n")
        else:
            result_text.insert(tk.END, "DATA MAHASISWA TIDAK DITEMUKAN\n\n")

        result_text.insert(tk.END, f"Waktu Iteratif : {t_i:.10f} detik\n")
        result_text.insert(tk.END, f"Waktu Rekursif : {t_r:.10f} detik\n")

        trial = trial_numbers[-1] + 1 if trial_numbers else 1

        trial_numbers.append(trial)
        iter_times.append(t_i)
        recur_times.append(t_r)

        if len(trial_numbers) > MAX_POINTS:
            trial_numbers.pop(0)
            iter_times.pop(0)
            recur_times.pop(0)

        ax.clear()

        ax.plot(
            trial_numbers,
            iter_times,
            color='blue',
            marker='^',
            linestyle='-',
            linewidth=2,
            markersize=8,
            label='Iteratif'
        )

        ax.plot(
            trial_numbers,
            recur_times,
            color='red',
            marker='s',
            linestyle='-',
            linewidth=2,
            markersize=8,
            label='Rekursif'
        )

        ax.set_title("Perbandingan Waktu Binary Search Iteratif dan Rekursif")
        ax.set_xlabel("Percobaan Ke-")
        ax.set_ylabel("Waktu Eksekusi (detik)")
        ax.legend()
        ax.grid(True)

        canvas.draw()

    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Masukkan NIM yang valid!")

root = tk.Tk()
root.title("Pencarian Data Mahasiswa Berdasarkan NIM")

tk.Label(root, text="Masukkan NIM:").pack()
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

tk.Button(root, text="Cari Mahasiswa", command=search).pack(pady=5)

result_text = tk.Text(root, height=10, width=70)
result_text.pack(pady=5)

fig, ax = plt.subplots(figsize=(5, 3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

root.mainloop()
