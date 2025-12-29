import random
import tkinter as tk
from binarySearch import binary_search_iterative, binary_search_recursive
from tkinter import font
from dataMahasiswa import mahasiswa
from performance import measure_search, measure_search_optimize
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

MAX_POINTS = 7

trial_numbers = []
iter_times = []
recur_times = []
iter_opt_times = []
recur_opt_times = []

root = tk.Tk()
root.title("Pencarian Data Mahasiswa Berdasarkan NIM")
entry_font = ("Arial", 14)  
button_font = ("Arial", 14, "bold")

show_iter = tk.BooleanVar(value=True, master=root)
show_recur = tk.BooleanVar(value=True, master=root)
show_iter_opt = tk.BooleanVar(value=True, master=root)
show_recur_opt = tk.BooleanVar(value=True, master=root)

def update_graph():
    ax.clear()
    if show_iter.get():
        ax.plot(trial_numbers, iter_times, color='pink', marker='s', linestyle='-', linewidth=2, markersize=8, label='Iteratif')
    if show_recur.get():
        ax.plot(trial_numbers, recur_times, color='blue', marker='x', linestyle='-', linewidth=2, markersize=8, label='Rekursif')
    if show_iter_opt.get():
        ax.plot(trial_numbers, iter_opt_times, color='purple', marker='^', linestyle='-', linewidth=2, markersize=8, label='Iteratif (Optimize)')
    if show_recur_opt.get():
        ax.plot(trial_numbers, recur_opt_times, color='green', marker='o', linestyle='-', linewidth=2, markersize=8, label='Rekursif (Optimize)')

    ax.set_title("Perbandingan Waktu Binary Search")
    ax.set_xlabel("Percobaan Ke-") 
    ax.set_ylabel("Waktu Eksekusi (detik)")
    ax.legend()
    ax.grid(True)
    ax.set_xticks(trial_numbers)
    fig.tight_layout()
    canvas.draw()

def search():
    try:
        target_nim = int(entry.get())
        result_i, t_i, result_r, t_r = measure_search(mahasiswa, target_nim)
        result_i_opt, t_i_opt, result_r_opt, t_r_opt = measure_search_optimize(mahasiswa, target_nim)

        result_text.delete("1.0", tk.END)
        if result_i:
            result_text.tag_configure("highlight", font=("Times New Roman", 12))
            result_text.insert(tk.END, "DATA MAHASISWA DITEMUKAN\n", "highlight")
            result_text.insert(tk.END, f"NIM               : {result_i['nim']}\n", "highlight")
            result_text.insert(tk.END, f"Nama              : {result_i['nama']}\n", "highlight")
            result_text.insert(tk.END, f"Prodi             : {result_i['prodi']}\n\n", "highlight")
        else:
            result_text.tag_configure("highlight", font=("Times New Roman", 12), foreground="red")
            result_text.insert(tk.END, "DATA MAHASISWA TIDAK DITEMUKAN\n\n")

        result_text.tag_configure("highlight", font=("Times New Roman", 12))
        result_text.insert(tk.END, f"Waktu Iteratif            : {t_i:.10f} detik\n", "highlight")
        result_text.insert(tk.END, f"Waktu Rekursif            : {t_r:.10f} detik\n", "highlight")
        result_text.insert(tk.END, f"Waktu Iteratif (Optimize) : {t_i_opt:.10f} detik\n", "highlight")
        result_text.insert(tk.END, f"Waktu Rekursif (Optimize) : {t_r_opt:.10f} detik\n", "highlight")

        trial = trial_numbers[-1] + 1 if trial_numbers else 1
        trial_numbers.append(trial)
        iter_times.append(t_i)
        recur_times.append(t_r)
        iter_opt_times.append(t_i_opt)
        recur_opt_times.append(t_r_opt)

        if len(trial_numbers) > MAX_POINTS:
            trial_numbers.pop(0)
            iter_times.pop(0)
            recur_times.pop(0)
            iter_opt_times.pop(0)
            recur_opt_times.pop(0)

        update_graph()

    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Masukkan NIM yang valid!")

def search_case(case_type):
    """
    case_type: 'best', 'average', 'worst'
    """
    if case_type == 'best':
        target_nim = mahasiswa[len(mahasiswa)//2]['nim']
    elif case_type == 'average':
        target_nim = random.choice(mahasiswa)['nim']
    elif case_type == 'worst':
        target_nim = mahasiswa[-1]['nim'] + 1  
    else:
        return

    result_i, t_i, result_r, t_r = measure_search(mahasiswa, target_nim)
    result_i_opt, t_i_opt, result_r_opt, t_r_opt = measure_search_optimize(mahasiswa, target_nim)

    result_text.delete("1.0", tk.END)
    result_text.tag_configure("highlight", font=("Times New Roman", 12))
    result_text.insert(tk.END, f"CASE: {case_type.upper()}\n\n", "highlight")
    if result_i:
        result_text.tag_configure("highlight", font=("Times New Roman", 12))
        result_text.insert(tk.END, f"NIM ditemukan: {result_i['nim']}, Nama: {result_i['nama']}\n", "highlight")
    else:
        result_text.tag_configure("highlight", font=("Times New Roman", 12))
        result_text.insert(tk.END, "NIM tidak ditemukan\n", "highlight")

    result_text.tag_configure("highlight", font=("Times New Roman", 12))
    result_text.insert(tk.END, f"Waktu Iteratif            : {t_i:.10f} detik\n", "highlight")
    result_text.insert(tk.END, f"Waktu Rekursif            : {t_r:.10f} detik\n", "highlight")
    result_text.insert(tk.END, f"Waktu Iteratif (Optimize) : {t_i_opt:.10f} detik\n", "highlight")
    result_text.insert(tk.END, f"Waktu Rekursif (Optimize) : {t_r_opt:.10f} detik\n", "highlight")

tk.Label(root, text="Masukkan NIM:", font=entry_font).pack(pady=5)
entry = tk.Entry(root, width=30, font=entry_font)
entry.pack(pady=5)

tk.Button(root, text="Cari Mahasiswa", font=button_font, height=2, width=20, command=search).pack(pady=5)

result_text = tk.Text(root, height=12, width=70)
result_text.pack(pady=5)

frame_cases = tk.Frame(root)
frame_cases.pack(pady=5)

tk.Button(frame_cases, text="Best Case", command=lambda: search_case('best')).grid(row=0, column=0, padx=5)
tk.Button(frame_cases, text="Average Case", command=lambda: search_case('average')).grid(row=0, column=1, padx=5)
tk.Button(frame_cases, text="Worst Case", command=lambda: search_case('worst')).grid(row=0, column=2, padx=5)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

tk.Checkbutton(frame_buttons, text="Iteratif", variable=show_iter, command=update_graph).grid(row=0, column=0, padx=5)
tk.Checkbutton(frame_buttons, text="Rekursif", variable=show_recur, command=update_graph).grid(row=0, column=1, padx=5)
tk.Checkbutton(frame_buttons, text="Iteratif (Optimize)", variable=show_iter_opt, command=update_graph).grid(row=0, column=2, padx=5)
tk.Checkbutton(frame_buttons, text="Rekursif (Optimize)", variable=show_recur_opt, command=update_graph).grid(row=0, column=3, padx=5)

fig, ax = plt.subplots(figsize=(7, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

root.mainloop()
