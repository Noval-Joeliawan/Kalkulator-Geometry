import math
import tkinter as tk
from tkinter import messagebox, ttk

# ============================================================================
# TEMA & WARNA GLOBAL (Dark Slate 2D Clean)
# ============================================================================
THEME = {
    "bg": "#1e2430",
    "header": "#111620",
    "card": "#28303f",
    "card_inner": "#171e2a",
    "accent_blue": "#1d6fee",
    "accent_hover": "#1557b0",
    "accent_cyan": "#38bdf8",
    "accent_purple": "#7209b7",
    "accent_pink": "#f72585",
    "text_main": "#ffffff",
    "text_muted": "#94a3b8",
    "border": "#3b4252",
    "entry_bg": "#333c4d",
    "shape_fill": "#1d6fee",
    "shape_outline": "#38bdf8",
    "dim_color": "#facc15",  # Kuning untuk keterangan label garis dimensi
}


# ============================================================================
# CANVAS RENDERER 2D INTERAKTIF
# ============================================================================
class Canvas2D(tk.Canvas):
    def __init__(self, master, shape_type="Persegi", **kwargs):
        super().__init__(
            master,
            bg=THEME["card_inner"],
            highlightthickness=1,
            highlightbackground=THEME["border"],
            bd=0,
            **kwargs,
        )
        self.shape_type = shape_type
        self.bind("<Configure>", lambda e: self.draw_shape())

    def set_shape(self, shape_type):
        self.shape_type = shape_type
        self.draw_shape()

    def draw_shape(self):
        if not self.winfo_exists():
            return
        self.delete("all")
        w = self.winfo_width()
        h = self.winfo_height()
        if w <= 10 or h <= 10:
            w, h = 360, 300
        cx, cy = w / 2, h / 2

        # Grid halus latar belakang (Technical Drawing Look)
        for x in range(0, w, 25):
            self.create_line(x, 0, x, h, fill="#1c2534", width=1)
        for y in range(0, h, 25):
            self.create_line(0, y, w, y, fill="#1c2534", width=1)

        st = self.shape_type.lower()
        fill_col = "#1e3a5f"
        line_col = THEME["shape_outline"]

        if "persegi panjang" in st:
            pw, ph = 180, 100
            x1, y1 = cx - pw / 2, cy - ph / 2
            x2, y2 = cx + pw / 2, cy + ph / 2
            self.create_rectangle(x1, y1, x2, y2, fill=fill_col, outline=line_col, width=2.5)
            self.create_text(cx, y2 + 16, text="Panjang (p)", fill=THEME["dim_color"], font=("Segoe UI", 9, "bold"))
            self.create_text(x1 - 32, cy, text="Lebar (l)", fill=THEME["dim_color"], font=("Segoe UI", 9, "bold"))

        elif "persegi" in st:
            s = 130
            x1, y1 = cx - s / 2, cy - s / 2
            x2, y2 = cx + s / 2, cy + s / 2
            self.create_rectangle(x1, y1, x2, y2, fill=fill_col, outline=line_col, width=2.5)
            self.create_text(cx, y2 + 16, text="Sisi (s)", fill=THEME["dim_color"], font=("Segoe UI", 9, "bold"))
            self.create_text(x1 - 25, cy, text="Sisi (s)", fill=THEME["dim_color"], font=("Segoe UI", 9, "bold"))

        elif "segitiga" in st:
            b, th = 160, 120
            p1 = (cx, cy - th / 2)
            p2 = (cx - b / 2, cy + th / 2)
            p3 = (cx + b / 2, cy + th / 2)
            self.create_polygon([p1, p2, p3], fill=fill_col, outline=line_col, width=2.5)
            # Garis tinggi putus-putus
            self.create_line(cx, cy - th / 2, cx, cy + th / 2, fill="#f87171", dash=(4, 2), width=1.5)
            self.create_text(cx + 18, cy, text="t", fill="#f87171", font=("Segoe UI", 9, "bold"))
            self.create_text(cx, cy + th / 2 + 16, text="Alas (a)", fill=THEME["dim_color"], font=("Segoe UI", 9, "bold"))

        elif "lingkaran" in st:
            r = 75
            self.create_oval(cx - r, cy - r, cx + r, cy + r, fill=fill_col, outline=line_col, width=2.5)
            # Garis jari-jari
            self.create_line(cx, cy, cx + r, cy, fill=THEME["dim_color"], width=2, arrow=tk.LAST)
            self.create_oval(cx - 3, cy - 3, cx + 3, cy + 3, fill="white")
            self.create_text(cx + r / 2, cy - 12, text="Jari-jari (r)", fill=THEME["dim_color"], font=("Segoe UI", 9, "bold"))

        elif "jajar genjang" in st:
            b, th, skew = 150, 90, 35
            pts = [
                (cx - b / 2 + skew, cy - th / 2),
                (cx + b / 2 + skew, cy - th / 2),
                (cx + b / 2 - skew, cy + th / 2),
                (cx - b / 2 - skew, cy + th / 2),
            ]
            self.create_polygon(pts, fill=fill_col, outline=line_col, width=2.5)
            self.create_line(cx - b / 2 + skew, cy - th / 2, cx - b / 2 + skew, cy + th / 2, fill="#f87171", dash=(4, 2), width=1.5)
            self.create_text(cx - b / 2 + skew - 14, cy, text="t", fill="#f87171", font=("Segoe UI", 9, "bold"))
            self.create_text(cx, cy + th / 2 + 16, text="Alas (a)", fill=THEME["dim_color"], font=("Segoe UI", 9, "bold"))

        elif "belah ketupat" in st:
            d1, d2 = 160, 110
            pts = [(cx, cy - d2 / 2), (cx + d1 / 2, cy), (cx, cy + d2 / 2), (cx - d1 / 2, cy)]
            self.create_polygon(pts, fill=fill_col, outline=line_col, width=2.5)
            self.create_line(cx - d1 / 2, cy, cx + d1 / 2, cy, fill="#f87171", dash=(3, 2), width=1)
            self.create_line(cx, cy - d2 / 2, cx, cy + d2 / 2, fill="#4ade80", dash=(3, 2), width=1)
            self.create_text(cx + 25, cy - 12, text="d1", fill="#f87171", font=("Segoe UI", 9, "bold"))
            self.create_text(cx + 12, cy + 25, text="d2", fill="#4ade80", font=("Segoe UI", 9, "bold"))

        elif "layang layang" in st:
            d1, top_d, bot_d = 120, 45, 95
            pts = [(cx, cy - top_d), (cx + d1 / 2, cy), (cx, cy + bot_d), (cx - d1 / 2, cy)]
            self.create_polygon(pts, fill=fill_col, outline=line_col, width=2.5)
            self.create_line(cx - d1 / 2, cy, cx + d1 / 2, cy, fill="#f87171", dash=(3, 2), width=1)
            self.create_line(cx, cy - top_d, cx, cy + bot_d, fill="#4ade80", dash=(3, 2), width=1)
            self.create_text(cx + 25, cy - 12, text="d1", fill="#f87171", font=("Segoe UI", 9, "bold"))
            self.create_text(cx + 12, cy + 30, text="d2", fill="#4ade80", font=("Segoe UI", 9, "bold"))

        elif "trapesium" in st:
            a, b, th = 90, 170, 95
            pts = [(cx - a / 2, cy - th / 2), (cx + a / 2, cy - th / 2), (cx + b / 2, cy + th / 2), (cx - b / 2, cy + th / 2)]
            self.create_polygon(pts, fill=fill_col, outline=line_col, width=2.5)
            self.create_line(cx - a / 2, cy - th / 2, cx - a / 2, cy + th / 2, fill="#f87171", dash=(4, 2), width=1.5)
            self.create_text(cx, cy - th / 2 - 14, text="Sisi Atas (a)", fill=THEME["dim_color"], font=("Segoe UI", 8, "bold"))
            self.create_text(cx, cy + th / 2 + 16, text="Sisi Bawah (b)", fill=THEME["dim_color"], font=("Segoe UI", 8, "bold"))
            self.create_text(cx - a / 2 - 14, cy, text="t", fill="#f87171", font=("Segoe UI", 9, "bold"))

        elif "oval" in st:
            rx, ry = 95, 55
            self.create_oval(cx - rx, cy - ry, cx + rx, cy + ry, fill=fill_col, outline=line_col, width=2.5)
            self.create_line(cx, cy, cx + rx, cy, fill=THEME["dim_color"], dash=(3, 2), width=1.5)
            self.create_line(cx, cy, cx, cy - ry, fill="#4ade80", dash=(3, 2), width=1.5)
            self.create_text(cx + rx / 2, cy + 12, text="a (mayor)", fill=THEME["dim_color"], font=("Segoe UI", 8, "bold"))
            self.create_text(cx - 28, cy - ry / 2, text="b (minor)", fill="#4ade80", font=("Segoe UI", 8, "bold"))


# ============================================================================
# KELAS APLIKASI UTAMA (VERSI 2D MURNI)
# ============================================================================
class KalkulatorGeometry2DApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Geometry 2D - Standar Materi Uji RPL")
        self.root.geometry("1100x720")
        self.root.minsize(980, 650)
        self.root.configure(bg=THEME["bg"])

        self.setup_styles()

        # Daftar 9 Bangun Datar 2D (Tabung 3D ditiadakan agar murni bangun datar)
        self.shapes_list = [
            "Persegi", "Persegi Panjang", "Segitiga", "Lingkaran",
            "Jajar Genjang", "Belah Ketupat", "Layang Layang",
            "Trapesium", "Oval"
        ]

        self.current_frame = None
        self.show_welcome_screen()

    def setup_styles(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except Exception:
            pass
        style.configure("TNotebook", background=THEME["bg"], borderwidth=0)
        style.configure(
            "TNotebook.Tab",
            font=("Segoe UI", 9, "bold"),
            padding=[10, 6],
            background=THEME["card"],
            foreground=THEME["text_muted"],
            borderwidth=0,
        )
        style.map(
            "TNotebook.Tab",
            background=[("selected", THEME["accent_blue"])],
            foreground=[("selected", "white")],
        )
        style.configure(
            "TCombobox",
            fieldbackground=THEME["entry_bg"],
            background=THEME["card"],
            foreground="white",
            padding=5,
        )

    def clear_current_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
            self.current_frame = None

    # ------------------------------------------------------------------------
    # 1. HALAMAN AWAL (WELCOME / START)
    # ------------------------------------------------------------------------
    def show_welcome_screen(self):
        self.clear_current_frame()
        self.current_frame = tk.Frame(self.root, bg=THEME["bg"])
        self.current_frame.pack(fill="both", expand=True)

        tk.Label(
            self.current_frame,
            text="📐 KALKULATOR BANGUN DATAR (2D)",
            font=("Segoe UI", 24, "bold"),
            bg=THEME["bg"],
            fg=THEME["text_main"],
        ).pack(pady=(60, 5))

        tk.Label(
            self.current_frame,
            text="Aplikasi Menghitung Luas, Keliling, Fungsi Invers & Visualisasi Geometri 2D",
            font=("Segoe UI", 11),
            bg=THEME["bg"],
            fg=THEME["text_muted"],
        ).pack(pady=(0, 30))

        center_card = tk.Frame(self.current_frame, bg=THEME["card"], padx=40, pady=30, highlightthickness=1, highlightbackground=THEME["border"])
        center_card.pack(pady=20)

        tk.Label(
            center_card,
            text="Pilih Menu Perhitungan:",
            font=("Segoe UI", 12, "bold"),
            bg=THEME["card"],
            fg=THEME["accent_cyan"],
        ).pack(pady=(0, 20))

        btn_luas = tk.Button(
            center_card,
            text="📐  HITUNG LUAS BANGUN DATAR",
            font=("Segoe UI", 11, "bold"),
            width=32,
            height=2,
            bg=THEME["accent_blue"],
            fg="white",
            bd=0,
            cursor="hand2",
            activebackground=THEME["accent_hover"],
            activeforeground="white",
            command=self.show_luas_screen,
        )
        btn_luas.pack(pady=8)

        btn_kel = tk.Button(
            center_card,
            text="📏  HITUNG KELILING BANGUN DATAR",
            font=("Segoe UI", 11, "bold"),
            width=32,
            height=2,
            bg=THEME["accent_purple"],
            fg="white",
            bd=0,
            cursor="hand2",
            activebackground="#5a0890",
            activeforeground="white",
            command=self.show_keliling_screen,
        )
        btn_kel.pack(pady=8)

        btn_inv = tk.Button(
            center_card,
            text="🔄  FUNGSI INVERS (REVERSE CALC)",
            font=("Segoe UI", 11, "bold"),
            width=32,
            height=2,
            bg=THEME["accent_pink"],
            fg="white",
            bd=0,
            cursor="hand2",
            activebackground="#c71569",
            activeforeground="white",
            command=self.show_invers_screen,
        )
        btn_inv.pack(pady=8)

        tk.Label(
            self.current_frame,
            text="Proyek STS Kelompok 1 - XI RPL 4",
            font=("Segoe UI", 9, "italic"),
            bg=THEME["bg"],
            fg=THEME["text_muted"],
        ).pack(side="bottom", pady=20)

    # ------------------------------------------------------------------------
    # HEADER SUB-MENU
    # ------------------------------------------------------------------------
    def create_sub_header(self, parent, title):
        header = tk.Frame(parent, bg=THEME["header"], height=55)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        tk.Label(
            header,
            text=f"📐 {title}",
            font=("Segoe UI", 13, "bold"),
            bg=THEME["header"],
            fg=THEME["text_main"],
        ).pack(side="left", padx=15)

        btn_back = tk.Button(
            header,
            text="← Kembali ke Menu Utama",
            font=("Segoe UI", 9, "bold"),
            bg=THEME["entry_bg"],
            fg="white",
            bd=0,
            cursor="hand2",
            padx=12,
            pady=5,
            command=self.show_welcome_screen,
        )
        btn_back.pack(side="right", padx=15)
        return header

    # ------------------------------------------------------------------------
    # 2. HALAMAN HITUNG LUAS 2D
    # ------------------------------------------------------------------------
    def show_luas_screen(self):
        self.clear_current_frame()
        self.current_frame = tk.Frame(self.root, bg=THEME["bg"])
        self.current_frame.pack(fill="both", expand=True)

        self.create_sub_header(self.current_frame, "Kalkulator Luas Bangun Datar")

        notebook = ttk.Notebook(self.current_frame)
        notebook.pack(fill="both", expand=True, padx=15, pady=10)

        inputs_config = {
            "Persegi": [("Panjang Sisi (s) :", "s")],
            "Persegi Panjang": [("Panjang (p) :", "p"), ("Lebar (l) :", "l")],
            "Segitiga": [("Alas (a) :", "a"), ("Tinggi (t) :", "t")],
            "Lingkaran": [("Jari-jari (r) :", "r")],
            "Jajar Genjang": [("Alas (a) :", "a"), ("Tinggi (t) :", "t")],
            "Belah Ketupat": [("Diagonal 1 (d1) :", "d1"), ("Diagonal 2 (d2) :", "d2")],
            "Layang Layang": [("Diagonal 1 (d1) :", "d1"), ("Diagonal 2 (d2) :", "d2")],
            "Trapesium": [("Sisi Atas (a) :", "a"), ("Sisi Bawah (b) :", "b"), ("Tinggi (t) :", "t")],
            "Oval": [("Sumbu Mayor (a) :", "a"), ("Sumbu Minor (b) :", "b")],
        }

        for shape in self.shapes_list:
            tab = tk.Frame(notebook, bg=THEME["bg"])
            notebook.add(tab, text=shape)
            self.build_calc_tab(tab, shape, "luas", inputs_config[shape])

    # ------------------------------------------------------------------------
    # 3. HALAMAN HITUNG KELILING 2D
    # ------------------------------------------------------------------------
    def show_keliling_screen(self):
        self.clear_current_frame()
        self.current_frame = tk.Frame(self.root, bg=THEME["bg"])
        self.current_frame.pack(fill="both", expand=True)

        self.create_sub_header(self.current_frame, "Kalkulator Keliling Bangun Datar")

        notebook = ttk.Notebook(self.current_frame)
        notebook.pack(fill="both", expand=True, padx=15, pady=10)

        inputs_config = {
            "Persegi": [("Panjang Sisi (s) :", "s")],
            "Persegi Panjang": [("Panjang (p) :", "p"), ("Lebar (l) :", "l")],
            "Segitiga": [("Sisi A :", "a"), ("Sisi B :", "b"), ("Sisi C :", "c")],
            "Lingkaran": [("Jari-jari (r) :", "r")],
            "Jajar Genjang": [("Sisi Miring / A :", "a"), ("Sisi Mendatar / B :", "b")],
            "Belah Ketupat": [("Panjang Sisi (s) :", "s")],
            "Layang Layang": [("Sisi Pendek (a) :", "a"), ("Sisi Panjang (b) :", "b")],
            "Trapesium": [("Sisi A :", "a"), ("Sisi B :", "b"), ("Sisi C :", "c"), ("Sisi D :", "d")],
            "Oval": [("Setengah Sumbu A :", "a"), ("Setengah Sumbu B :", "b")],
        }

        for shape in self.shapes_list:
            tab = tk.Frame(notebook, bg=THEME["bg"])
            notebook.add(tab, text=shape)
            self.build_calc_tab(tab, shape, "keliling", inputs_config[shape])

    # ------------------------------------------------------------------------
    # BUILDER TAB PERHITUNGAN (DILENGKAPI CANVAS 2D)
    # ------------------------------------------------------------------------
    def build_calc_tab(self, parent, shape_name, calc_mode, fields):
        container = tk.Frame(parent, bg=THEME["card"], highlightthickness=1, highlightbackground=THEME["border"])
        container.pack(fill="both", expand=True, padx=10, pady=10)

        # Panel Kiri: Gambar Visual 2D
        left = tk.Frame(container, bg=THEME["card"])
        left.pack(side="left", fill="both", expand=True, padx=15, pady=15)

        tk.Label(
            left,
            text=f"Visualisasi Bangun: {shape_name}",
            font=("Segoe UI", 11, "bold"),
            fg=THEME["accent_cyan"],
            bg=THEME["card"],
        ).pack(anchor="w", pady=(0, 6))

        canvas = Canvas2D(left, shape_type=shape_name)
        canvas.pack(fill="both", expand=True)

        # Panel Kanan: Form Input
        right = tk.Frame(container, bg=THEME["card"], width=380)
        right.pack(side="right", fill="y", padx=15, pady=15)
        right.pack_propagate(False)

        tk.Label(
            right,
            text=f"Input Dimensi ({calc_mode.upper()})",
            font=("Segoe UI", 11, "bold"),
            fg=THEME["text_main"],
            bg=THEME["card"],
        ).pack(anchor="w", pady=(0, 10))

        entries = {}
        for lbl_text, key in fields:
            f_row = tk.Frame(right, bg=THEME["card"])
            f_row.pack(fill="x", pady=4)
            tk.Label(f_row, text=lbl_text, font=("Segoe UI", 9), fg=THEME["text_muted"], bg=THEME["card"]).pack(side="left")
            ent = tk.Entry(f_row, font=("Segoe UI", 10, "bold"), bg=THEME["entry_bg"], fg="white", bd=0, justify="center")
            ent.pack(side="right", fill="x", expand=True, padx=(10, 0), ipady=4)
            entries[key] = ent

        res_box = tk.Frame(right, bg=THEME["card_inner"], highlightthickness=1, highlightbackground=THEME["border"])
        res_box.pack(fill="x", side="bottom", pady=10, ipady=10)

        tk.Label(res_box, text=f"HASIL {calc_mode.upper()}", font=("Segoe UI", 8, "bold"), fg=THEME["text_muted"], bg=THEME["card_inner"]).pack()
        lbl_res = tk.Label(res_box, text="0.00", font=("Segoe UI", 18, "bold"), fg=THEME["accent_cyan"], bg=THEME["card_inner"])
        lbl_res.pack()

        def do_calculate():
            try:
                vals = {k: float(e.get().strip()) for k, e in entries.items()}
                if any(v <= 0 for v in vals.values()):
                    raise ValueError("Nilai dimensi harus lebih besar dari 0.")

                hasil_str = ""
                if calc_mode == "luas":
                    if shape_name == "Persegi":
                        hasil_str = f"{vals['s']**2:.2f}"
                    elif shape_name == "Persegi Panjang":
                        hasil_str = f"{vals['p']*vals['l']:.2f}"
                    elif shape_name == "Segitiga":
                        hasil_str = f"{0.5*vals['a']*vals['t']:.2f}"
                    elif shape_name == "Lingkaran":
                        hasil_str = f"{math.pi * (vals['r']**2):.2f}"
                    elif shape_name == "Jajar Genjang":
                        hasil_str = f"{vals['a']*vals['t']:.2f}"
                    elif shape_name in ["Belah Ketupat", "Layang Layang"]:
                        hasil_str = f"{0.5*vals['d1']*vals['d2']:.2f}"
                    elif shape_name == "Trapesium":
                        hasil_str = f"{0.5*(vals['a']+vals['b'])*vals['t']:.2f}"
                    elif shape_name == "Oval":
                        hasil_str = f"{math.pi*vals['a']*vals['b']:.2f}"

                else:  # KELILING
                    if shape_name == "Persegi":
                        hasil_str = f"{4*vals['s']:.2f}"
                    elif shape_name == "Persegi Panjang":
                        hasil_str = f"{2*(vals['p']+vals['l']):.2f}"
                    elif shape_name == "Segitiga":
                        hasil_str = f"{vals['a']+vals['b']+vals['c']:.2f}"
                    elif shape_name == "Lingkaran":
                        hasil_str = f"{2*math.pi*vals['r']:.2f}"
                    elif shape_name == "Jajar Genjang":
                        hasil_str = f"{2*(vals['a']+vals['b']):.2f}"
                    elif shape_name == "Belah Ketupat":
                        hasil_str = f"{4*vals['s']:.2f}"
                    elif shape_name == "Layang Layang":
                        hasil_str = f"{2*(vals['a']+vals['b']):.2f}"
                    elif shape_name == "Trapesium":
                        hasil_str = f"{vals['a']+vals['b']+vals['c']+vals['d']:.2f}"
                    elif shape_name == "Oval":
                        h = ((vals["a"] - vals["b"]) ** 2) / ((vals["a"] + vals["b"]) ** 2)
                        hasil_str = f"{math.pi*(vals['a']+vals['b'])*(1 + (3*h)/(10 + math.sqrt(4 - 3*h))):.2f}"

                lbl_res.config(text=hasil_str)
            except ValueError as ex:
                messagebox.showwarning("Input Salah", str(ex) if str(ex) else "Masukkan angka yang valid.")

        btn_calc = tk.Button(
            right,
            text=f"Hitung {calc_mode.title()}",
            font=("Segoe UI", 10, "bold"),
            bg=THEME["accent_blue"],
            fg="white",
            bd=0,
            cursor="hand2",
            command=do_calculate,
        )
        btn_calc.pack(fill="x", pady=10, ipady=6)

    # ------------------------------------------------------------------------
    # 4. HALAMAN FUNGSI INVERS (REVERSE CALCULATION 2D)
    # ------------------------------------------------------------------------
    def show_invers_screen(self):
        self.clear_current_frame()
        self.current_frame = tk.Frame(self.root, bg=THEME["bg"])
        self.current_frame.pack(fill="both", expand=True)

        self.create_sub_header(self.current_frame, "Fungsi Invers Geometri 2D")

        main_box = tk.Frame(self.current_frame, bg=THEME["bg"])
        main_box.pack(fill="both", expand=True, padx=15, pady=10)
        main_box.columnconfigure((0, 1, 2), weight=1)
        main_box.rowconfigure(0, weight=1)

        # Panel 1: Preview Canvas 2D
        p1 = tk.Frame(main_box, bg=THEME["card"], highlightthickness=1, highlightbackground=THEME["border"])
        p1.grid(row=0, column=0, sticky="nsew", padx=6)
        tk.Label(p1, text="Preview Bentuk 2D", font=("Segoe UI", 10, "bold"), fg=THEME["text_main"], bg=THEME["card"]).pack(anchor="w", padx=10, pady=8)
        canvas_inv = Canvas2D(p1, shape_type="Persegi")
        canvas_inv.pack(fill="both", expand=True, padx=10, pady=10)

        # Panel 2: Form Invers
        p2 = tk.Frame(main_box, bg=THEME["card"], highlightthickness=1, highlightbackground=THEME["border"])
        p2.grid(row=0, column=1, sticky="nsew", padx=6)
        tk.Label(p2, text="Pilihan Perhitungan Invers", font=("Segoe UI", 10, "bold"), fg=THEME["text_main"], bg=THEME["card"]).pack(anchor="w", padx=10, pady=8)

        # Panel 3: Hasil
        p3 = tk.Frame(main_box, bg=THEME["card"], highlightthickness=1, highlightbackground=THEME["border"])
        p3.grid(row=0, column=2, sticky="nsew", padx=6)
        tk.Label(p3, text="Hasil Perhitungan Invers", font=("Segoe UI", 10, "bold"), fg=THEME["text_main"], bg=THEME["card"]).pack(anchor="w", padx=10, pady=8)

        res_inner = tk.Frame(p3, bg=THEME["card_inner"], highlightthickness=1, highlightbackground=THEME["border"])
        res_inner.pack(fill="x", padx=15, pady=20, ipady=15)
        lbl_val_inv = tk.Label(res_inner, text="0.00", font=("Segoe UI", 24, "bold"), fg=THEME["accent_cyan"], bg=THEME["card_inner"])
        lbl_val_inv.pack()
        lbl_formula = tk.Label(p3, text="Rumus: -", font=("Segoe UI", 9), fg=THEME["text_muted"], bg=THEME["card"])
        lbl_formula.pack(padx=15, anchor="w")

        # Database Invers 2D
        invers_db = {
            "Persegi": {
                "Sisi (dari Luas)": {"inputs": [("Luas (L):", "L")], "calc": lambda d: math.sqrt(d["L"]), "formula": "s = √L"},
                "Sisi (dari Keliling)": {"inputs": [("Keliling (K):", "K")], "calc": lambda d: d["K"] / 4, "formula": "s = K / 4"},
            },
            "Persegi Panjang": {
                "Panjang (dari L & l)": {"inputs": [("Luas (L):", "L"), ("Lebar (l):", "l")], "calc": lambda d: d["L"] / d["l"], "formula": "p = L / l"},
                "Lebar (dari K & p)": {"inputs": [("Keliling (K):", "K"), ("Panjang (p):", "p")], "calc": lambda d: (d["K"] / 2) - d["p"], "formula": "l = (K/2) - p"},
            },
            "Segitiga": {
                "Tinggi (dari L & a)": {"inputs": [("Luas (L):", "L"), ("Alas (a):", "a")], "calc": lambda d: (2 * d["L"]) / d["a"], "formula": "t = 2L / a"},
                "Alas (dari L & t)": {"inputs": [("Luas (L):", "L"), ("Tinggi (t):", "t")], "calc": lambda d: (2 * d["L"]) / d["t"], "formula": "a = 2L / t"},
            },
            "Lingkaran": {
                "Jari-jari (dari Luas)": {"inputs": [("Luas (L):", "L")], "calc": lambda d: math.sqrt(d["L"] / math.pi), "formula": "r = √(L / π)"},
                "Jari-jari (dari Keliling)": {"inputs": [("Keliling (K):", "K")], "calc": lambda d: d["K"] / (2 * math.pi), "formula": "r = K / (2π)"},
            },
        }

        tk.Label(p2, text="Pilih Bangun:", font=("Segoe UI", 9), fg=THEME["text_muted"], bg=THEME["card"]).pack(anchor="w", padx=15, pady=(5, 2))
        combo_shape = ttk.Combobox(p2, values=list(invers_db.keys()), state="readonly")
        combo_shape.pack(fill="x", padx=15, pady=(0, 10))

        tk.Label(p2, text="Target Invers:", font=("Segoe UI", 9), fg=THEME["text_muted"], bg=THEME["card"]).pack(anchor="w", padx=15, pady=(5, 2))
        combo_inv = ttk.Combobox(p2, state="readonly")
        combo_inv.pack(fill="x", padx=15, pady=(0, 10))

        dynamic_input_frame = tk.Frame(p2, bg=THEME["card"])
        dynamic_input_frame.pack(fill="both", expand=True, padx=15, pady=5)
        entries_inv = {}

        def update_inputs(event=None):
            for w in dynamic_input_frame.winfo_children():
                w.destroy()
            entries_inv.clear()

            s = combo_shape.get()
            canvas_inv.set_shape(s)
            i = combo_inv.get()
            if s in invers_db and i in invers_db[s]:
                cfg = invers_db[s][i]
                lbl_formula.config(text=f"Rumus: {cfg['formula']}")
                for label_txt, key in cfg["inputs"]:
                    tk.Label(dynamic_input_frame, text=label_txt, font=("Segoe UI", 9), fg=THEME["text_main"], bg=THEME["card"]).pack(anchor="w", pady=(2, 0))
                    ent = tk.Entry(dynamic_input_frame, font=("Segoe UI", 10, "bold"), bg=THEME["entry_bg"], fg="white", bd=0)
                    ent.pack(fill="x", pady=(2, 6), ipady=3)
                    entries_inv[key] = ent

        def update_inv_types(event=None):
            s = combo_shape.get()
            if s in invers_db:
                opts = list(invers_db[s].keys())
                combo_inv.config(values=opts)
                if opts:
                    combo_inv.set(opts[0])
                    update_inputs()

        combo_shape.bind("<<ComboboxSelected>>", update_inv_types)
        combo_inv.bind("<<ComboboxSelected>>", update_inputs)

        combo_shape.set("Persegi")
        update_inv_types()

        def do_calc_invers():
            try:
                s = combo_shape.get()
                i = combo_inv.get()
                cfg = invers_db[s][i]
                vals = {k: float(e.get().strip()) for k, e in entries_inv.items()}
                if any(v <= 0 for v in vals.values()):
                    raise ValueError("Nilai input harus lebih dari 0.")
                res = cfg["calc"](vals)
                lbl_val_inv.config(text=f"{res:.2f}")
            except Exception as e:
                messagebox.showerror("Error Invers", str(e) if str(e) else "Masukkan angka yang valid.")

        btn_run_inv = tk.Button(
            p2,
            text="Hitung Nilai Invers",
            font=("Segoe UI", 10, "bold"),
            bg=THEME["accent_pink"],
            fg="white",
            bd=0,
            cursor="hand2",
            command=do_calc_invers,
        )
        btn_run_inv.pack(fill="x", padx=15, pady=15, ipady=6)


# ============================================================================
# ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = KalkulatorGeometry2DApp(root)
    root.mainloop()