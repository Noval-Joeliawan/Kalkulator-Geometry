import math
import tkinter as tk
from tkinter import messagebox, ttk

# ============================================================================
# TEMA & WARNA GLOBAL (Cyberpunk / Synthwave Dark Neon)
# ============================================================================
THEME = {
    "bg": "#090d16",
    "header": "#05070c",
    "card": "#131b2e",
    "card_inner": "#0c1220",
    "accent_blue": "#00f0ff",
    "accent_hover": "#00b8c4",
    "accent_cyan": "#00f0ff",
    "accent_purple": "#b026ff",
    "accent_pink": "#ff007f",
    "text_main": "#ffffff",
    "text_muted": "#8899b5",
    "border": "#1f2d4d",
    "entry_bg": "#182238",
    "dim_color": "#ffe600",
}

# ============================================================================
# 1. RENDERER 2D CANVAS
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
            w, h = 360, 280
        cx, cy = w / 2, h / 2

        # Grid Teknik
        for x in range(0, w, 25):
            self.create_line(x, 0, x, h, fill="#111c30", width=1)
        for y in range(0, h, 25):
            self.create_line(0, y, w, y, fill="#111c30", width=1)

        st = self.shape_type.lower()
        fill_col = "#0f223d"
        line_col = THEME["accent_cyan"]

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
            self.create_line(cx, cy - th / 2, cx, cy + th / 2, fill="#f87171", dash=(4, 2), width=1.5)
            self.create_text(cx + 18, cy, text="t", fill="#f87171", font=("Segoe UI", 9, "bold"))
            self.create_text(cx, cy + th / 2 + 16, text="Alas (a)", fill=THEME["dim_color"], font=("Segoe UI", 9, "bold"))

        elif "lingkaran" in st:
            r = 75
            self.create_oval(cx - r, cy - r, cx + r, cy + r, fill=fill_col, outline=line_col, width=2.5)
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

        elif "tabung" in st:
            r, h = 60, 110
            self.create_rectangle(cx - r, cy - h / 2, cx + r, cy + h / 2, fill=fill_col, outline=line_col, width=2)
            self.create_oval(cx - r, cy - h / 2 - 15, cx + r, cy - h / 2 + 15, fill="#2b507d", outline=line_col, width=2)
            self.create_oval(cx - r, cy + h / 2 - 15, cx + r, cy + h / 2 + 15, fill=fill_col, outline=line_col, width=2)
            self.create_text(cx, cy + h / 2 + 25, text="Alas Tabung", fill=THEME["dim_color"], font=("Segoe UI", 9, "bold"))

# ============================================================
# 2. RENDERER 3D INTERAKTIF CANVAS
# ============================================================
class InteractiveCanvas3D(tk.Canvas):
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
        self.angle_x = 20.0
        self.angle_y = -35.0
        self.zoom = 1.0
        self.rotate_speed = 1.2
        self.is_dragging = False
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        self.is_running = True
        self.after_id = None

        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_release)
        self.bind("<Destroy>", self.stop_loop)

        self.start_loop()

    def stop_loop(self, event=None):
        self.is_running = False
        if self.after_id:
            try:
                self.after_cancel(self.after_id)
            except Exception:
                pass
            self.after_id = None

    def start_loop(self):
        if not self.is_running:
            return
        if not self.is_dragging and self.rotate_speed > 0:
            self.angle_y += self.rotate_speed
            self.render()
        if self.is_running and self.winfo_exists():
            self.after_id = self.after(30, self.start_loop)

    def on_press(self, event):
        self.is_dragging = True
        self.last_mouse_x = event.x
        self.last_mouse_y = event.y

    def on_drag(self, event):
        dx = event.x - self.last_mouse_x
        dy = event.y - self.last_mouse_y
        self.angle_y += dx * 0.8
        self.angle_x += dy * 0.8
        self.last_mouse_x = event.x
        self.last_mouse_y = event.y
        self.render()

    def on_release(self, event):
        self.is_dragging = False

    def set_shape(self, shape_type):
        self.shape_type = shape_type
        self.render()

    def project(self, x, y, z, cx, cy):
        x *= self.zoom
        y *= self.zoom
        z *= self.zoom
        rad_x = math.radians(self.angle_x)
        rad_y = math.radians(self.angle_y)

        xz = x * math.cos(rad_y) + z * math.sin(rad_y)
        yz = y
        zz = -x * math.sin(rad_y) + z * math.cos(rad_y)

        x_final = xz
        y_final = yz * math.cos(rad_x) - zz * math.sin(rad_x)
        z_final = yz * math.sin(rad_x) + zz * math.cos(rad_x)

        return cx + x_final, cy - y_final, z_final

    def render(self):
        if not self.winfo_exists():
            return
        self.delete("all")
        w = self.winfo_width()
        h = self.winfo_height()
        if w <= 10 or h <= 10:
            w, h = 360, 280
        cx, cy = w / 2, h / 2

        polygons = self.get_mesh()
        transformed = []

        for poly, color in polygons:
            pts = []
            z_sum = 0
            for pt in poly:
                px, py, pz = self.project(*pt, cx, cy)
                pts.append((px, py))
                z_sum += pz
            transformed.append((z_sum / len(poly), pts, color))

        transformed.sort(key=lambda item: item[0])
        for _, pts, color in transformed:
            self.create_polygon(pts, fill=color, outline="#00f0ff", width=1)

    def get_mesh(self):
        st = self.shape_type.lower()
        if "persegi panjang" in st:
            w, h, d = 90, 50, 50
            return [
                ([(-w, h, d), (w, h, d), (w, h, -d), (-w, h, -d)], "#fb8c00"),
                ([(-w, -h, d), (w, -h, d), (w, -h, -d), (-w, -h, -d)], "#e65100"),
                ([(-w, -h, d), (w, -h, d), (w, h, d), (-w, h, d)], "#ff9800"),
                ([(-w, -h, -d), (w, -h, -d), (w, h, -d), (-w, h, -d)], "#f57c00"),
                ([(-w, -h, -d), (-w, -h, d), (-w, h, d), (-w, h, -d)], "#ef6c00"),
                ([(w, -h, -d), (w, -h, d), (w, h, d), (w, h, -d)], "#ffa726"),
            ]
        elif "segitiga" in st:
            s = 85
            top = (0, s, 0)
            p1 = (0, -s / 2, s)
            p2 = (-s * 0.866, -s / 2, -s / 2)
            p3 = (s * 0.866, -s / 2, -s / 2)
            return [
                ([p1, p2, p3], "#00332c"),
                ([p1, p2, top], "#26a69a"),
                ([p2, p3, top], "#00897b"),
                ([p3, p1, top], "#4db6ac"),
            ]
        elif "lingkaran" in st:
            r, faces, steps = 75, [], 10
            for i in range(steps):
                lat1 = math.pi * (-0.5 + float(i) / steps)
                lat2 = math.pi * (-0.5 + float(i + 1) / steps)
                for j in range(steps):
                    lon1 = 2 * math.pi * float(j) / steps
                    lon2 = 2 * math.pi * float(j + 1) / steps
                    p1 = (r * math.cos(lat1) * math.cos(lon1), r * math.sin(lat1), r * math.cos(lat1) * math.sin(lon1))
                    p2 = (r * math.cos(lat1) * math.cos(lon2), r * math.sin(lat1), r * math.cos(lat1) * math.sin(lon2))
                    p3 = (r * math.cos(lat2) * math.cos(lon2), r * math.sin(lat2), r * math.cos(lat2) * math.sin(lon2))
                    p4 = (r * math.cos(lat2) * math.cos(lon1), r * math.sin(lat2), r * math.cos(lat2) * math.sin(lon1))
                    faces.append(([p1, p2, p3, p4], "#9c27b0" if (i + j) % 2 == 0 else "#7b1fa2"))
            return faces
        elif "jajar genjang" in st:
            w, h, d, off = 65, 45, 45, 25
            return [
                ([(-w + off, h, d), (w + off, h, d), (w - off, h, -d), (-w - off, h, -d)], "#fdd835"),
                ([(-w + off, -h, d), (w + off, -h, d), (w - off, -h, -d), (-w - off, -h, -d)], "#e65100"),
                ([(-w + off, -h, d), (w + off, -h, d), (w + off, h, d), (-w + off, h, d)], "#ffeb3b"),
                ([(-w - off, -h, -d), (w - off, -h, -d), (w - off, h, -d), (-w - off, h, -d)], "#fbc02d"),
                ([(-w + off, -h, d), (-w - off, -h, -d), (-w - off, h, -d), (-w + off, h, d)], "#f57f17"),
                ([(w + off, -h, d), (w - off, -h, -d), (w - off, h, -d), (w + off, h, d)], "#ffa000"),
            ]
        elif "belah ketupat" in st:
            dx, dy, dz = 70, 80, 40
            top, bot = (0, dy, 0), (0, -dy, 0)
            p1, p2, p3, p4 = (dx, 0, 0), (0, 0, dz), (-dx, 0, 0), (0, 0, -dz)
            return [
                ([p1, p2, top], "#e91e63"), ([p2, p3, top], "#c2185b"),
                ([p3, p4, top], "#880e4f"), ([p4, p1, top], "#ad1457"),
                ([p1, p2, bot], "#d81b60"), ([p2, p3, bot], "#b71c1c"),
                ([p3, p4, bot], "#ad1457"), ([p4, p1, bot], "#c2185b"),
            ]
        elif "layang layang" in st:
            dx, dz, y_top, y_mid, y_bot = 60, 40, 75, 15, -75
            top, bot = (0, y_top, 0), (0, y_bot, 0)
            p1, p2, p3, p4 = (dx, y_mid, 0), (0, y_mid, dz), (-dx, y_mid, 0), (0, y_mid, -dz)
            return [
                ([p1, p2, top], "#00bcd4"), ([p2, p3, top], "#0097a7"),
                ([p3, p4, top], "#006064"), ([p4, p1, top], "#00838f"),
                ([p1, p2, bot], "#26c6da"), ([p2, p3, bot], "#0097a7"),
                ([p3, p4, bot], "#00838f"), ([p4, p1, bot], "#00acc1"),
            ]
        elif "trapesium" in st:
            w_top, w_bot, h, d = 40, 80, 55, 45
            return [
                ([(-w_bot, -h, d), (w_bot, -h, d), (w_top, h, d), (-w_top, h, d)], "#ff5722"),
                ([(-w_bot, -h, -d), (w_bot, -h, -d), (w_top, h, -d), (-w_top, h, -d)], "#d84315"),
                ([(-w_bot, -h, -d), (w_bot, -h, -d), (w_bot, -h, d), (-w_bot, -h, d)], "#bf360c"),
                ([(-w_top, h, -d), (w_top, h, -d), (w_top, h, d), (-w_top, h, d)], "#ff7043"),
                ([(-w_bot, -h, -d), (-w_bot, -h, d), (-w_top, h, d), (-w_top, h, -d)], "#f4511e"),
                ([(w_bot, -h, -d), (w_bot, -h, d), (w_top, h, d), (w_top, h, -d)], "#e64a19"),
            ]
        elif "oval" in st:
            rx, ry, rz, faces, steps = 80, 50, 50, [], 10
            for i in range(steps):
                lat1 = math.pi * (-0.5 + float(i) / steps)
                lat2 = math.pi * (-0.5 + float(i + 1) / steps)
                for j in range(steps):
                    lon1 = 2 * math.pi * float(j) / steps
                    lon2 = 2 * math.pi * float(j + 1) / steps
                    p1 = (rx * math.cos(lat1) * math.cos(lon1), ry * math.sin(lat1), rz * math.cos(lat1) * math.sin(lon1))
                    p2 = (rx * math.cos(lat1) * math.cos(lon2), ry * math.sin(lat1), rz * math.cos(lat1) * math.sin(lon2))
                    p3 = (rx * math.cos(lat2) * math.cos(lon2), ry * math.sin(lat2), rz * math.cos(lat2) * math.sin(lon2))
                    p4 = (rx * math.cos(lat2) * math.cos(lon1), ry * math.sin(lat2), rz * math.cos(lat2) * math.sin(lon1))
                    faces.append(([p1, p2, p3, p4], "#8bc34a" if (i + j) % 2 == 0 else "#689f38"))
            return faces
        elif "tabung" in st:
            r, h, faces, steps = 55, 70, [], 16
            top_pts, bot_pts = [], []
            for i in range(steps):
                a1 = 2 * math.pi * i / steps
                a2 = 2 * math.pi * (i + 1) / steps
                p1 = (r * math.cos(a1), -h, r * math.sin(a1))
                p2 = (r * math.cos(a2), -h, r * math.sin(a2))
                p3 = (r * math.cos(a2), h, r * math.sin(a2))
                p4 = (r * math.cos(a1), h, r * math.sin(a1))
                faces.append(([p1, p2, p3, p4], "#ab47bc" if i % 2 == 0 else "#8e24aa"))
                bot_pts.append(p1)
                top_pts.append(p4)
            faces.append((top_pts, "#ce93d8"))
            faces.append((bot_pts, "#7b1fa2"))
            return faces
        else:
            s = 70
            return [
                ([(-s, s, s), (s, s, s), (s, s, -s), (-s, s, -s)], "#1e88e5"),
                ([(-s, -s, s), (s, -s, s), (s, -s, -s), (-s, -s, -s)], "#1565c0"),
                ([(-s, -s, s), (s, -s, s), (s, s, s), (-s, s, s)], "#2196f3"),
                ([(-s, -s, -s), (s, -s, -s), (s, s, -s), (-s, s, -s)], "#0d47a1"),
                ([(-s, -s, -s), (-s, -s, s), (-s, s, s), (-s, s, -s)], "#1976d2"),
                ([(s, -s, -s), (s, -s, s), (s, s, s), (s, s, -s)], "#42a5f5"),
            ]

# ============================================================================
# 3. DUAL-VIEW CONTAINER (DENGAN SYNC GLOBAL MODE 2D/3D)
# ============================================================================
class DualViewCanvas(tk.Frame):
    global_mode = "2D"
    instances = []

    def __init__(self, master, shape_type="Persegi", **kwargs):
        super().__init__(master, bg=THEME["card"], **kwargs)
        self.shape_type = shape_type
        DualViewCanvas.instances.append(self)

        bar = tk.Frame(self, bg=THEME["card"])
        bar.pack(fill="x", pady=(0, 6))

        tk.Label(bar, text="PILIH TAMPILAN:", font=("Segoe UI", 9, "bold"), fg=THEME["text_muted"], bg=THEME["card"]).pack(side="left", padx=(0, 8))

        self.btn_2d = tk.Button(
            bar, text="📐 Mode 2D (Sketsa)", font=("Segoe UI", 9, "bold"),
            bg=THEME["accent_blue"], fg="#000000", bd=0, padx=12, pady=3, cursor="hand2",
            command=lambda: DualViewCanvas.set_global_mode("2D")
        )
        self.btn_2d.pack(side="left", padx=3)

        self.btn_3d = tk.Button(
            bar, text="🧊 Mode 3D (Interaktif)", font=("Segoe UI", 9, "bold"),
            bg=THEME["entry_bg"], fg=THEME["text_muted"], bd=0, padx=12, pady=3, cursor="hand2",
            command=lambda: DualViewCanvas.set_global_mode("3D")
        )
        self.btn_3d.pack(side="left", padx=3)

        self.canvas_area = tk.Frame(self, bg=THEME["card_inner"])
        self.canvas_area.pack(fill="both", expand=True)

        self.c2d = Canvas2D(self.canvas_area, shape_type=self.shape_type)
        self.c3d = InteractiveCanvas3D(self.canvas_area, shape_type=self.shape_type)

        self.apply_mode(DualViewCanvas.global_mode)

    @classmethod
    def set_global_mode(cls, mode):
        cls.global_mode = mode
        for inst in cls.instances:
            if inst.winfo_exists():
                inst.apply_mode(mode)

    def apply_mode(self, mode):
        if mode == "2D":
            self.c3d.pack_forget()
            self.c2d.pack(fill="both", expand=True)
            self.c2d.draw_shape()
            self.btn_2d.config(bg=THEME["accent_blue"], fg="#000000")
            self.btn_3d.config(bg=THEME["entry_bg"], fg=THEME["text_muted"])
        else:
            self.c2d.pack_forget()
            self.c3d.pack(fill="both", expand=True)
            self.c3d.render()
            self.btn_3d.config(bg=THEME["accent_purple"], fg="white")
            self.btn_2d.config(bg=THEME["entry_bg"], fg=THEME["text_muted"])

    def set_shape(self, shape_type):
        self.shape_type = shape_type
        self.c2d.set_shape(shape_type)
        self.c3d.set_shape(shape_type)

    def stop(self):
        self.c3d.stop_loop()

# ============================================================================
# 4. KELAS APLIKASI UTAMA
# ============================================================================
class KalkulatorGeometryDualApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Geometry App")
        self.root.geometry("1100x720")
        self.root.minsize(980, 650)
        self.root.configure(bg=THEME["bg"])

        self.setup_styles()

        self.shapes_list = [
            "Persegi", "Persegi Panjang", "Segitiga", "Lingkaran",
            "Jajar Genjang", "Belah Ketupat", "Layang Layang",
            "Trapesium", "Oval", "Tabung"
        ]

        self.active_canvases = []
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
            background=[("selected", THEME["accent_purple"])],
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
        for c in self.active_canvases:
            try:
                c.stop()
            except Exception:
                pass
        self.active_canvases.clear()
        DualViewCanvas.instances.clear()

        if self.current_frame:
            self.current_frame.destroy()
            self.current_frame = None

    def show_welcome_screen(self):
        self.clear_current_frame()
        self.current_frame = tk.Frame(self.root, bg=THEME["bg"])
        self.current_frame.pack(fill="both", expand=True)

        tk.Label(
            self.current_frame,
            text="GEOMETRY APP",
            font=("Segoe UI", 24, "bold"),
            bg=THEME["bg"],
            fg=THEME["text_main"],
        ).pack(pady=(60, 5))

        tk.Label(
            self.current_frame,
            text="Pilih Mode Visualisasi: Tersedia Tampilan 2D Sketsa dan 3D Interaktif",
            font=("Segoe UI", 11),
            bg=THEME["bg"],
            fg=THEME["text_muted"],
        ).pack(pady=(0, 30))

        center_card = tk.Frame(self.current_frame, bg=THEME["card"], padx=40, pady=30, highlightthickness=1, highlightbackground=THEME["border"])
        center_card.pack(pady=20)

        tk.Label(center_card, text="Pilih Menu Perhitungan:", font=("Segoe UI", 12, "bold"), bg=THEME["card"], fg=THEME["accent_cyan"]).pack(pady=(0, 20))

        btn_luas = tk.Button(
            center_card, text="📐  HITUNG LUAS BANGUN", font=("Segoe UI", 11, "bold"),
            width=30, height=2, bg=THEME["accent_blue"], fg="#000000", bd=0, cursor="hand2",
            activebackground=THEME["accent_hover"], activeforeground="#000000", command=self.show_luas_screen
        )
        btn_luas.pack(pady=8)

        btn_kel = tk.Button(
            center_card, text="📏  HITUNG KELILING BANGUN", font=("Segoe UI", 11, "bold"),
            width=30, height=2, bg=THEME["accent_purple"], fg="white", bd=0, cursor="hand2",
            activebackground="#8e1fd3", activeforeground="white", command=self.show_keliling_screen
        )
        btn_kel.pack(pady=8)

        btn_inv = tk.Button(
            center_card, text="🔄  FUNGSI INVERS (REVERSE)", font=("Segoe UI", 11, "bold"),
            width=30, height=2, bg=THEME["accent_pink"], fg="white", bd=0, cursor="hand2",
            activebackground="#c71569", activeforeground="white", command=self.show_invers_screen
        )
        btn_inv.pack(pady=8)

        tk.Label(
            self.current_frame, text="Kalkulator & Lab Visualisasi Geometri Interaktif", font=("Segoe UI", 9, "italic"),
            bg=THEME["bg"], fg=THEME["text_muted"]
        ).pack(side="bottom", pady=20)

    def create_sub_header(self, parent, title):
        header = tk.Frame(parent, bg=THEME["header"], height=55)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        tk.Label(header, text=f"📐 {title}", font=("Segoe UI", 13, "bold"), bg=THEME["header"], fg=THEME["text_main"]).pack(side="left", padx=15)
        btn_back = tk.Button(
            header, text="← Kembali ke Menu Utama", font=("Segoe UI", 9, "bold"),
            bg=THEME["entry_bg"], fg="white", bd=0, cursor="hand2", padx=12, pady=5, command=self.show_welcome_screen
        )
        btn_back.pack(side="right", padx=15)
        return header

    def show_luas_screen(self):
        self.clear_current_frame()
        self.current_frame = tk.Frame(self.root, bg=THEME["bg"])
        self.current_frame.pack(fill="both", expand=True)

        self.create_sub_header(self.current_frame, "Kalkulator Luas Bangun (Dual Mode 2D/3D)")

        notebook = ttk.Notebook(self.current_frame)
        notebook.pack(fill="both", expand=True, padx=15, pady=10)

        inputs_config = {
            "Persegi": [("Sisi :", "s")],
            "Persegi Panjang": [("Panjang :", "p"), ("Lebar :", "l")],
            "Segitiga": [("Alas :", "a"), ("Tinggi :", "t")],
            "Lingkaran": [("Jari-jari (r) :", "r")],
            "Jajar Genjang": [("Alas :", "a"), ("Tinggi :", "t")],
            "Belah Ketupat": [("Diagonal 1 :", "d1"), ("Diagonal 2 :", "d2")],
            "Layang Layang": [("Diagonal 1 :", "d1"), ("Diagonal 2 :", "d2")],
            "Trapesium": [("Sisi Atas (a) :", "a"), ("Sisi Bawah (b) :", "b"), ("Tinggi :", "t")],
            "Oval": [("Sumbu Mayor (a) :", "a"), ("Sumbu Minor (b) :", "b")],
            "Tabung": [("Jari-jari (r) :", "r"), ("Tinggi (t) :", "t")],
        }

        for shape in self.shapes_list:
            tab = tk.Frame(notebook, bg=THEME["bg"])
            notebook.add(tab, text=shape)
            self.build_calc_tab(tab, shape, "luas", inputs_config[shape])

    def show_keliling_screen(self):
        self.clear_current_frame()
        self.current_frame = tk.Frame(self.root, bg=THEME["bg"])
        self.current_frame.pack(fill="both", expand=True)

        self.create_sub_header(self.current_frame, "Kalkulator Keliling Bangun (Dual Mode 2D/3D)")

        notebook = ttk.Notebook(self.current_frame)
        notebook.pack(fill="both", expand=True, padx=15, pady=10)

        inputs_config = {
            "Persegi": [("Sisi :", "s")],
            "Persegi Panjang": [("Panjang :", "p"), ("Lebar :", "l")],
            "Segitiga": [("Sisi A :", "a"), ("Sisi B :", "b"), ("Sisi C :", "c")],
            "Lingkaran": [("Jari-jari (r) :", "r")],
            "Jajar Genjang": [("Sisi A :", "a"), ("Sisi B :", "b")],
            "Belah Ketupat": [("Panjang Sisi :", "s")],
            "Layang Layang": [("Sisi A :", "a"), ("Sisi B :", "b")],
            "Trapesium": [("Sisi A :", "a"), ("Sisi B :", "b"), ("Sisi C :", "c"), ("Sisi D :", "d")],
            "Oval": [("Setengah Sumbu A :", "a"), ("Setengah Sumbu B :", "b")],
            "Tabung": [("Jari-jari Alas (r) :", "r")],
        }

        for shape in self.shapes_list:
            tab = tk.Frame(notebook, bg=THEME["bg"])
            notebook.add(tab, text=shape)
            self.build_calc_tab(tab, shape, "keliling", inputs_config[shape])

    def build_calc_tab(self, parent, shape_name, calc_mode, fields):
        container = tk.Frame(parent, bg=THEME["card"], highlightthickness=1, highlightbackground=THEME["border"])
        container.pack(fill="both", expand=True, padx=10, pady=10)

        left = tk.Frame(container, bg=THEME["card"])
        left.pack(side="left", fill="both", expand=True, padx=15, pady=15)

        dual_canvas = DualViewCanvas(left, shape_type=shape_name)
        dual_canvas.pack(fill="both", expand=True)
        self.active_canvases.append(dual_canvas)

        right = tk.Frame(container, bg=THEME["card"], width=360)
        right.pack(side="right", fill="y", padx=15, pady=15)
        right.pack_propagate(False)

        tk.Label(
            right, text=f"Input Dimensi ({calc_mode.upper()})", font=("Segoe UI", 11, "bold"),
            fg=THEME["text_main"], bg=THEME["card"]
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
                    raise ValueError("Nilai harus bernilai positif (> 0).")

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
                    elif shape_name == "Tabung":
                        selimut = 2 * math.pi * vals["r"] * vals["t"]
                        total = 2 * math.pi * vals["r"] * (vals["r"] + vals["t"])
                        hasil_str = f"Selimut: {selimut:.2f}\nTotal: {total:.2f}"

                else:
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
                    elif shape_name == "Tabung":
                        hasil_str = f"{2*math.pi*vals['r']:.2f}"

                lbl_res.config(text=hasil_str)
            except ValueError as ex:
                messagebox.showwarning("Input Tidak Valid", str(ex) if str(ex) else "Pastikan semua kolom diisi angka positif.")

        btn_calc = tk.Button(
            right, text=f"Hitung {calc_mode.title()}", font=("Segoe UI", 10, "bold"),
            bg=THEME["accent_blue"], fg="#000000", bd=0, cursor="hand2", command=do_calculate
        )
        btn_calc.pack(fill="x", pady=10, ipady=6)

    def show_invers_screen(self):
        self.clear_current_frame()
        self.current_frame = tk.Frame(self.root, bg=THEME["bg"])
        self.current_frame.pack(fill="both", expand=True)

        self.create_sub_header(self.current_frame, "Fungsi Invers Geometri (Dual Mode 2D/3D)")

        main_box = tk.Frame(self.current_frame, bg=THEME["bg"])
        main_box.pack(fill="both", expand=True, padx=15, pady=10)
        main_box.columnconfigure((0, 1, 2), weight=1)
        main_box.rowconfigure(0, weight=1)

        p1 = tk.Frame(main_box, bg=THEME["card"], highlightthickness=1, highlightbackground=THEME["border"])
        p1.grid(row=0, column=0, sticky="nsew", padx=6)
        
        dual_inv = DualViewCanvas(p1, shape_type="Persegi")
        dual_inv.pack(fill="both", expand=True, padx=10, pady=10)
        self.active_canvases.append(dual_inv)

        p2 = tk.Frame(main_box, bg=THEME["card"], highlightthickness=1, highlightbackground=THEME["border"])
        p2.grid(row=0, column=1, sticky="nsew", padx=6)
        tk.Label(p2, text="Pilihan Invers", font=("Segoe UI", 10, "bold"), fg=THEME["text_main"], bg=THEME["card"]).pack(anchor="w", padx=15, pady=8)

        p3 = tk.Frame(main_box, bg=THEME["card"], highlightthickness=1, highlightbackground=THEME["border"])
        p3.grid(row=0, column=2, sticky="nsew", padx=6)
        tk.Label(p3, text="Hasil Perhitungan Invers", font=("Segoe UI", 10, "bold"), fg=THEME["text_main"], bg=THEME["card"]).pack(anchor="w", padx=15, pady=8)

        res_inner = tk.Frame(p3, bg=THEME["card_inner"], highlightthickness=1, highlightbackground=THEME["border"])
        res_inner.pack(fill="x", padx=15, pady=20, ipady=15)
        lbl_val_inv = tk.Label(res_inner, text="0.00", font=("Segoe UI", 24, "bold"), fg=THEME["accent_cyan"], bg=THEME["card_inner"])
        lbl_val_inv.pack()
        lbl_formula = tk.Label(p3, text="Rumus: -", font=("Segoe UI", 9), fg=THEME["text_muted"], bg=THEME["card"])
        lbl_formula.pack(padx=15, anchor="w")

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
            dual_inv.set_shape(s)
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
            p2, text="Hitung Nilai Invers", font=("Segoe UI", 10, "bold"),
            bg=THEME["accent_pink"], fg="white", bd=0, cursor="hand2", command=do_calc_invers
        )
        btn_run_inv.pack(fill="x", padx=15, pady=15, ipady=6)

# ============================================================================
# ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = KalkulatorGeometryDualApp(root)
    root.mainloop()