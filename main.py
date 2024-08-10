import tkinter as tk
from tkinter import messagebox, font
from tkinter import ttk
from habits import Habit, HabitTracker

class HabitTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Habit Tracker")
        self.root.configure(bg="#F0F0F0")  # Background warna abu-abu muda

        self.tracker = HabitTracker()

        self.title_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=10)
        self.button_font = font.Font(family="Helvetica", size=10)

        self.name_var = tk.StringVar()
        self.desc_var = tk.StringVar()
        self.freq_var = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
        header_frame = tk.Frame(self.root, bg="#3E4149", pady=10)
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        tk.Label(header_frame, text="Habit Tracker", font=self.title_font, fg="white", bg="#3E4149").pack()

        input_frame = tk.Frame(self.root, bg="#F0F0F0", padx=10, pady=10)
        input_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

        tk.Label(input_frame, text="Nama Kebiasaan:", font=self.label_font, bg="#F0F0F0").grid(row=0, column=0, sticky="w")
        tk.Entry(input_frame, textvariable=self.name_var, font=self.label_font, width=30).grid(row=0, column=1)

        tk.Label(input_frame, text="Deskripsi:", font=self.label_font, bg="#F0F0F0").grid(row=1, column=0, sticky="w")
        tk.Entry(input_frame, textvariable=self.desc_var, font=self.label_font, width=30).grid(row=1, column=1)

        tk.Label(input_frame, text="Frekuensi (harian/mingguan/bulanan):", font=self.label_font, bg="#F0F0F0").grid(row=2, column=0, sticky="w")
        tk.Entry(input_frame, textvariable=self.freq_var, font=self.label_font, width=30).grid(row=2, column=1)

        tk.Button(input_frame, text="Tambah Kebiasaan", command=self.add_habit, font=self.button_font, bg="#3E4149", fg="white", padx=10).grid(row=3, column=0, columnspan=2, pady=10)

        tk.Button(input_frame, text="Lihat Kemajuan", command=self.view_progress, font=self.button_font, bg="#3E4149", fg="white", padx=10).grid(row=4, column=0, columnspan=2, pady=10)

    def add_habit(self):
        name = self.name_var.get()
        description = self.desc_var.get()
        frequency = self.freq_var.get()
        
        if not name or not description or not frequency:
            messagebox.showerror("Kesalahan", "Semua bidang harus diisi!")
            return
        
        habit = Habit(name, description, frequency)
        self.tracker.add_habit(habit)
        messagebox.showinfo("Berhasil", f"Kebiasaan '{name}' telah ditambahkan.")

    def view_progress(self):
        progress_window = tk.Toplevel(self.root)
        progress_window.title("Kemajuan Kebiasaan")
        progress_window.configure(bg="#F0F0F0")

        progress_frame = tk.Frame(progress_window, bg="#F0F0F0", padx=10, pady=10)
        progress_frame.pack(fill="both", expand=True)

        progress_text = tk.Text(progress_frame, font=self.label_font, width=50, height=15, wrap="word")
        progress_text.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(progress_frame, command=progress_text.yview)
        scrollbar.pack(side="right", fill="y")
        progress_text.configure(yscrollcommand=scrollbar.set)

        progress = self.tracker.load_progress()
        for habit_name, dates in progress.items():
            progress_text.insert(tk.END, f"Kemajuan untuk '{habit_name}':\n")
            for date in dates:
                progress_text.insert(tk.END, f" - {date}\n")
            progress_text.insert(tk.END, "\n")

        progress_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = HabitTrackerApp(root)
    root.mainloop()
