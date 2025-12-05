import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator")
        self.root.geometry("320x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#615D70")
        
        # Variabel untuk menyimpan input dan hasil
        self.current_input = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # Membuat tampilan GUI sesuai gambar
        self.create_display()
        self.create_buttons()
        
    def create_display(self):
        # Frame untuk display dengan background putih
        display_frame = tk.Frame(self.root, bg="#594769", height=100)
        display_frame.pack(fill=tk.X, padx=20, pady=(30, 20))
        
        # Label untuk menampilkan hasil dengan style modern
        result_label = tk.Label(
            display_frame, 
            textvariable=self.result_var,
            font=("Arial", 28, "bold"),
            bg="#B9BAD8",
            fg='#333333',
            anchor="e",
            padx=10
        )
        result_label.pack(fill=tk.BOTH, expand=True)
    
    def create_buttons(self):
        # Frame untuk tombol-tombol dengan background putih
        button_frame = tk.Frame(self.root, bg="#8E89A0")
        button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 30))
        
        # Konfigurasi tombol sesuai gambar dengan tambahan operator
        button_config = [
            # Baris 1: 7, 8, 9, C, ÷
            [
                {"text": "7", "command": lambda: self.add_number("7"), "bg": "#4F4E92", "fg": "#FFFFFF", "width": 5},
                {"text": "8", "command": lambda: self.add_number("8"), "bg": "#833E9E", "fg": "#FFFFFF", "width": 5},
                {"text": "9", "command": lambda: self.add_number("9"), "bg": "#707097", "fg": "#FFFFFF", "width": 5},
                {"text": "C", "command": self.clear_all, "bg": "#795392", "fg": "white", "width": 5},
                {"text": "÷", "command": lambda: self.add_operator("/"), "bg": "#1E2A9B", "fg": "white", "width": 5}
            ],
            # Baris 2: 4, 5, 6, ×, -
            [
                {"text": "4", "command": lambda: self.add_number("4"), "bg": "#504774", "fg": "#FFFFFF", "width": 5},
                {"text": "5", "command": lambda: self.add_number("5"), "bg": "#834FA1", "fg": "#FAF8F8", "width": 5},
                {"text": "6", "command": lambda: self.add_number("6"), "bg": "#252C8F", "fg": "#FCF8F8", "width": 5},
                {"text": "×", "command": lambda: self.add_operator("×"), "bg": "#39308B", "fg": "white", "width": 5},
                {"text": "-", "command": lambda: self.add_operator("-"), "bg": "#5C3C80", "fg": "white", "width": 5}
            ],
            # Baris 3: 1, 2, 3, +, =
            [
                {"text": "1", "command": lambda: self.add_number("1"), "bg": "#5B2E85", "fg": "#FDFBFB", "width": 5},
                {"text": "2", "command": lambda: self.add_number("2"), "bg": "#504583", "fg": "#FCFBFB", "width": 5},
                {"text": "3", "command": lambda: self.add_number("3"), "bg": "#754A92", "fg": "#F8F8F8", "width": 5},
                {"text": "+", "command": lambda: self.add_operator("+"), "bg": "#2E2974", "fg": "white", "width": 5},
                {"text": "=", "command": self.calculate, "bg": "#441F75", "fg": "white", "width": 5}
            ],
            # Baris 4: 0, ., ⌫
            [
                {"text": "0", "command": lambda: self.add_number("0"), "bg": "#3D2B68", "fg": "#FDFBFB", "width": 11},
                {"text": ".", "command": self.add_decimal, "bg": "#CCAEE9", "fg": "#FFFFFF", "width": 5},
                {"text": "⌫", "command": self.backspace, "bg": "#362B68", "fg": "white", "width": 5}
            ]
        ]
        
        # Membuat tombol-tombol
        for row_idx, row in enumerate(button_config):
            row_frame = tk.Frame(button_frame, bg="#BCAFDF")
            row_frame.pack(fill=tk.X, pady=4)
            
            col_idx = 0
            for btn_config in row:
                # Menangani tombol yang membutuhkan colspan
                colspan = 2 if btn_config["width"] == 11 else 1
                
                btn = tk.Button(
                    row_frame,
                    text=btn_config["text"],
                    font=("Arial", 16, "bold"),
                    bg=btn_config["bg"],
                    fg=btn_config["fg"],
                    command=btn_config["command"],
                    relief='flat',
                    border=0,
                    highlightthickness=0,
                    width=btn_config["width"],
                    height=2
                )
                btn.grid(row=0, column=col_idx, padx=2, pady=0, sticky="ew", columnspan=colspan)
                
                # Efek hover untuk tombol
                self.add_hover_effect(btn, btn_config["bg"])
                
                col_idx += colspan
                
            # Configure grid weights untuk responsive layout
            for i in range(5):
                row_frame.grid_columnconfigure(i, weight=1)
    
    def add_hover_effect(self, button, original_color):
        """Menambahkan efek hover pada tombol"""
        def on_enter(e):
            if original_color == "#E4CFF1":
                button.config(bg="#C7CBEC")
            elif original_color == "#3E0F94":
                button.config(bg="#443DAD")
            elif original_color == "#552F9B":
                button.config(bg="#4E4E85")
            elif original_color == "#4D0775":
                button.config(bg="#8B72E4")
            elif original_color == "#654E74":
                button.config(bg="#3C2170")
                
        def on_leave(e):
            button.config(bg=original_color)
            
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def add_number(self, number):
        if self.result_var.get() == "0" or self.result_var.get() == "Error":
            self.current_input = number
        else:
            self.current_input += number
        self.result_var.set(self.current_input)
    
    def add_operator(self, operator):
        if self.current_input and self.current_input[-1] not in ['+', '-', '×', '/']:
            self.current_input += operator
            self.result_var.set(self.current_input)
        elif not self.current_input and operator == '-':
            # Memungkinkan angka negatif
            self.current_input = operator
            self.result_var.set(self.current_input)
    
    def add_decimal(self):
        if not self.current_input:
            self.current_input = "0."
        else:
            # Cari angka terakhir dalam ekspresi
            import re
            parts = re.split(r'([+\-×/])', self.current_input)
            last_number = parts[-1]
            
            # Jika angka terakhir belum memiliki titik desimal, tambahkan
            if '.' not in last_number:
                self.current_input += "."
        self.result_var.set(self.current_input)
    
    def calculate(self):
        try:
            if not self.current_input:
                return
                
            # Mengganti simbol × dengan * dan ÷ dengan / untuk evaluasi
            expression = self.current_input.replace('×', '*').replace('÷', '/')
            result = eval(expression)
            
            # Format hasil
            if result == int(result):
                result = int(result)
            self.result_var.set(str(result))
            self.current_input = str(result)
            
        except ZeroDivisionError:
            self.result_var.set("Error: Div/0")
            self.current_input = ""
        except:
            self.result_var.set("Error")
            self.current_input = ""
    
    def clear_all(self):
        """Menghapus semua input"""
        self.current_input = ""
        self.result_var.set("0")
    
    def backspace(self):
        """Menghapus karakter terakhir"""
        if self.current_input:
            self.current_input = self.current_input[:-1]
            if not self.current_input:
                self.result_var.set("0")
            else:
                self.result_var.set(self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()