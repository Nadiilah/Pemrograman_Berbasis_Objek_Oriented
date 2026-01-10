import tkinter as tk
from tkinter import messagebox, font
import random
from string import ascii_uppercase

class GameTebakKata:
    def __init__(self):
        self.kata_rahasia = ""
        self.kata_tebakan = []
        self.kesempatan = 6
        self.huruf_tertebak = set()
        self.score = 0
        self.kata_list = self.load_kata_lengkap()
    
    def load_kata_lengkap(self):
        """Membuat 100+ kata dengan kategori dan clue"""
        return [
            # TEKNOLOGI & KOMPUTER (20 kata)
            {"kata": "PYTHON", "kategori": "TEKNOLOGI", "clue": "Bahasa pemrograman dengan nama ular"},
            {"kata": "JAVA", "kategori": "TEKNOLOGI", "clue": "Nama pulau di Indonesia"},
            {"kata": "JAVASCRIPT", "kategori": "TEKNOLOGI", "clue": "Bahasa untuk website interaktif"},
            {"kata": "HTML", "kategori": "TEKNOLOGI", "clue": "Struktur dasar halaman web"},
            {"kata": "CSS", "kategori": "TEKNOLOGI", "clue": "Untuk styling halaman web"},
            {"kata": "KOMPUTER", "kategori": "TEKNOLOGI", "clue": "Alat untuk memproses data"},
            {"kata": "INTERNET", "kategori": "TEKNOLOGI", "clue": "Jaringan global komputer"},
            {"kata": "SMARTPHONE", "kategori": "TEKNOLOGI", "clue": "Telepon pintar multifungsi"},
            {"kata": "TABLET", "kategori": "TEKNOLOGI", "clue": "Perangkat antara laptop dan smartphone"},
            {"kata": "MONITOR", "kategori": "TEKNOLOGI", "clue": "Layar untuk menampilkan output"},
            {"kata": "KEYBOARD", "kategori": "TEKNOLOGI", "clue": "Alat untuk mengetik"},
            {"kata": "MOUSE", "kategori": "TEKNOLOGI", "clue": "Perangkat penunjuk di komputer"},
            {"kata": "PRINTER", "kategori": "TEKNOLOGI", "clue": "Alat untuk mencetak dokumen"},
            {"kata": "SCANNER", "kategori": "TEKNOLOGI", "clue": "Alat untuk memindai gambar/dokumen"},
            {"kata": "WEBCAM", "kategori": "TEKNOLOGI", "clue": "Kamera untuk video call"},
            {"kata": "ROUTER", "kategori": "TEKNOLOGI", "clue": "Perangkat jaringan internet"},
            {"kata": "DATABASE", "kategori": "TEKNOLOGI", "clue": "Tempat penyimpanan data terstruktur"},
            {"kata": "ALGORITMA", "kategori": "TEKNOLOGI", "clue": "Langkah-langkah penyelesaian masalah"},
            {"kata": "PROGRAM", "kategori": "TEKNOLOGI", "clue": "Kumpulan instruksi untuk komputer"},
            {"kata": "SOFTWARE", "kategori": "TEKNOLOGI", "clue": "Perangkat lunak komputer"},
            
            # INDONESIA & BUDAYA (20 kata)
            {"kata": "INDONESIA", "kategori": "NEGARA", "clue": "Negara kepulauan terbesar di dunia"},
            {"kata": "JAKARTA", "kategori": "KOTA", "clue": "Ibu kota Indonesia"},
            {"kata": "BOROBUDUR", "kategori": "CANDI", "clue": "Candi Buddha terbesar di dunia"},
            {"kata": "PRAMBANAN", "kategori": "CANDI", "clue": "Candi Hindu terbesar di Indonesia"},
            {"kata": "BALI", "kategori": "PULAU", "clue": "Pulau dewata di Indonesia"},
            {"kata": "GARUDA", "kategori": "SIMBOL", "clue": "Burung mitologi lambang Indonesia"},
            {"kata": "PANCASILA", "kategori": "IDEOLOGI", "clue": "Dasar negara Indonesia"},
            {"kata": "BATIK", "kategori": "KEBUDAYAAN", "clue": "Kain tradisional dengan motif tertentu"},
            {"kata": "WAYANG", "kategori": "KESENIAN", "clue": "Pertunjukan bayangan dari kulit"},
            {"kata": "GAMELAN", "kategori": "ALAT MUSIK", "clue": "Alat musik tradisional Jawa"},
            {"kata": "ANGKLUNG", "kategori": "ALAT MUSIK", "clue": "Alat musik dari bambu khas Sunda"},
            {"kata": "REOG", "kategori": "KESENIAN", "clue": "Kesenian dari Ponorogo dengan topeng besar"},
            {"kata": "KERIS", "kategori": "SENJATA", "clue": "Senjata tradisional berlekuk-lekuk"},
            {"kata": "SARUNG", "kategori": "PAKAIAN", "clue": "Kain yang dililitkan di badan"},
            {"kata": "UDENG", "kategori": "PAKAIAN", "clue": "Ikat kepala khas Bali"},
            {"kata": "BECAK", "kategori": "TRANSPORTASI", "clue": "Kendaraan roda tiga dengan pengayuh"},
            {"kata": "BAJAI", "kategori": "TRANSPORTASI", "clue": "Kendaraan roda tiga bermotor"},
            {"kata": "BECAKMOTOR", "kategori": "TRANSPORTASI", "clue": "Becak dengan mesin motor"},
            {"kata": "DELMAN", "kategori": "TRANSPORTASI", "clue": "Kendaraan tradisional ditarik kuda"},
            {"kata": "OJEG", "kategori": "TRANSPORTASI", "clue": "Taksi motor di Indonesia"},
            
            # MAKANAN & MINUMAN (20 kata)
            {"kata": "NASI", "kategori": "MAKANAN", "clue": "Makanan pokok orang Indonesia"},
            {"kata": "RENDANG", "kategori": "MAKANAN", "clue": "Makanan khas Padang yang terkenal"},
            {"kata": "SATE", "kategori": "MAKANAN", "clue": "Daging tusuk dengan bumbu kacang"},
            {"kata": "SOTO", "kategori": "MAKANAN", "clue": "Sup tradisional Indonesia"},
            {"kata": "GADO", "kategori": "MAKANAN", "clue": "Salad sayur Indonesia dengan saus kacang"},
            {"kata": "NASIGORENG", "kategori": "MAKANAN", "clue": "Nasi yang digoreng dengan bumbu"},
            {"kata": "MIEGORENG", "kategori": "MAKANAN", "clue": "Mie yang digoreng dengan bumbu"},
            {"kata": "BAKSO", "kategori": "MAKANAN", "clue": "Bola daging dengan kuah kaldu"},
            {"kata": "PEMPEK", "kategori": "MAKANAN", "clue": "Makanan khas Palembang dari ikan"},
            {"kata": "GUDEG", "kategori": "MAKANAN", "clue": "Makanan khas Yogyakarta dari nangka muda"},
            {"kata": "RAWON", "kategori": "MAKANAN", "clue": "Sup daging berkuah hitam khas Jawa Timur"},
            {"kata": "SOPBUNTUT", "kategori": "MAKANAN", "clue": "Sup dari ekor sapi"},
            {"kata": "AYAMBETUTU", "kategori": "MAKANAN", "clue": "Ayam khas Bali dengan bumbu rempah"},
            {"kata": "DENDENG", "kategori": "MAKANAN", "clue": "Daging yang dikeringkan"},
            {"kata": "SAMBAL", "kategori": "MAKANAN", "clue": "Saus pedas khas Indonesia"},
            {"kata": "KERUPUK", "kategori": "MAKANAN", "clue": "Camilan renyah dari tepung"},
            {"kata": "TEMPE", "kategori": "MAKANAN", "clue": "Makanan dari fermentasi kedelai"},
            {"kata": "TAHU", "kategori": "MAKANAN", "clue": "Makanan dari sari kedelai"},
            {"kata": "KOPI", "kategori": "MINUMAN", "clue": "Minuman dari biji kopi"},
            {"kata": "TEH", "kategori": "MINUMAN", "clue": "Minuman dari daun teh"},
            
            # HEWAN & TUMBUHAN (20 kata)
            {"kata": "HARIMAU", "kategori": "HEWAN", "clue": "Kucing besar dengan loreng"},
            {"kata": "GAJAH", "kategori": "HEWAN", "clue": "Hewan besar dengan belalai"},
            {"kata": "BADAK", "kategori": "HEWAN", "clue": "Hewan besar dengan cula di hidung"},
            {"kata": "ORANGUTAN", "kategori": "HEWAN", "clue": "Kera besar berwarna coklat"},
            {"kata": "KOMODO", "kategori": "HEWAN", "clue": "Kadal terbesar di dunia"},
            {"kata": "JALAK", "kategori": "HEWAN", "clue": "Burung yang bisa menirukan suara"},
            {"kata": "CENDRAWASIH", "kategori": "HEWAN", "clue": "Burung surga dari Papua"},
            {"kata": "KAKATUA", "kategori": "HEWAN", "clue": "Burung dengan jambul yang bisa bicara"},
            {"kata": "IKAN", "kategori": "HEWAN", "clue": "Hewan yang hidup di air"},
            {"kata": "ULAR", "kategori": "HEWAN", "clue": "Hewan melata tanpa kaki"},
            {"kata": "BUAYA", "kategori": "HEWAN", "clue": "Reptil besar dengan gigi tajam"},
            {"kata": "KURA", "kategori": "HEWAN", "clue": "Hewan dengan tempurung keras"},
            {"kata": "PADI", "kategori": "TUMBUHAN", "clue": "Tanaman penghasil beras"},
            {"kata": "JAGUNG", "kategori": "TUMBUHAN", "clue": "Tanaman dengan biji berwarna kuning"},
            {"kata": "KELAPA", "kategori": "TUMBUHAN", "clue": "Pohon dengan buah berair"},
            {"kata": "SAWIT", "kategori": "TUMBUHAN", "clue": "Pohon penghasil minyak"},
            {"kata": "CENGKEH", "kategori": "TUMBUHAN", "clue": "Rempah-rempah berbunga"},
            {"kata": "PALA", "kategori": "TUMBUHAN", "clue": "Rempah dari biji dan fuli"},
            {"kata": "KAYUMANIS", "kategori": "TUMBUHAN", "clue": "Kulit kayu untuk bumbu masakan"},
            {"kata": "JAHE", "kategori": "TUMBUHAN", "clue": "Rempah dengan rasa hangat"},
            
            # ILMU PENGETAHUAN (20 kata)
            {"kata": "MATEMATIKA", "kategori": "ILMU", "clue": "Ilmu tentang angka dan hitungan"},
            {"kata": "FISIKA", "kategori": "ILMU", "clue": "Ilmu tentang alam dan energi"},
            {"kata": "KIMIA", "kategori": "ILMU", "clue": "Ilmu tentang zat dan reaksi"},
            {"kata": "BIOLOGI", "kategori": "ILMU", "clue": "Ilmu tentang makhluk hidup"},
            {"kata": "GEOGRAFI", "kategori": "ILMU", "clue": "Ilmu tentang bumi dan permukaannya"},
            {"kata": "SEJARAH", "kategori": "ILMU", "clue": "Ilmu tentang peristiwa masa lalu"},
            {"kata": "EKONOMI", "kategori": "ILMU", "clue": "Ilmu tentang produksi dan distribusi"},
            {"kata": "SOSIOLOGI", "kategori": "ILMU", "clue": "Ilmu tentang masyarakat"},
            {"kata": "PSIKOLOGI", "kategori": "ILMU", "clue": "Ilmu tentang perilaku dan pikiran"},
            {"kata": "ASTRONOMI", "kategori": "ILMU", "clue": "Ilmu tentang benda langit"},
            {"kata": "GEOLOGI", "kategori": "ILMU", "clue": "Ilmu tentang batuan dan bumi"},
            {"kata": "BOTANI", "kategori": "ILMU", "clue": "Ilmu tentang tumbuhan"},
            {"kata": "ZOOLOGI", "kategori": "ILMU", "clue": "Ilmu tentang hewan"},
            {"kata": "ANATOMI", "kategori": "ILMU", "clue": "Ilmu tentang struktur tubuh"},
            {"kata": "FISIOLOGI", "kategori": "ILMU", "clue": "Ilmu tentang fungsi tubuh"},
            {"kata": "GENETIKA", "kategori": "ILMU", "clue": "Ilmu tentang keturunan"},
            {"kata": "EKOLOGI", "kategori": "ILMU", "clue": "Ilmu tentang hubungan makhluk hidup dan lingkungan"},
            {"kata": "ARKEOLOGI", "kategori": "ILMU", "clue": "Ilmu tentang peninggalan purbakala"},
            {"kata": "LINGUISTIK", "kategori": "ILMU", "clue": "Ilmu tentang bahasa"},
            {"kata": "FILSAFAT", "kategori": "ILMU", "clue": "Ilmu tentang hakikat keberadaan"},
            
            # OLAHRAGA & HOBI (15 kata)
            {"kata": "SEPAKBOLA", "kategori": "OLAHRAGA", "clue": "Olahraga dengan bola dan gawang"},
            {"kata": "BULUTANGKIS", "kategori": "OLAHRAGA", "clue": "Olahraga dengan raket dan kok"},
            {"kata": "TENIS", "kategori": "OLAHRAGA", "clue": "Olahraga dengan raket dan bola kecil"},
            {"kata": "BASKET", "kategori": "OLAHRAGA", "clue": "Olahraga dengan bola dan ring"},
            {"kata": "VOLI", "kategori": "OLAHRAGA", "clue": "Olahraga dengan bola dan net"},
            {"kata": "RENANG", "kategori": "OLAHRAGA", "clue": "Olahraga di dalam air"},
            {"kata": "LARI", "kategori": "OLAHRAGA", "clue": "Olahraga dengan menggerakkan kaki cepat"},
            {"kata": "JALAN", "kategori": "OLAHRAGA", "clue": "Olahraga dengan berjalan cepat"},
            {"kata": "SENAM", "kategori": "OLAHRAGA", "clue": "Olahraga dengan gerakan teratur"},
            {"kata": "BELADIRI", "kategori": "OLAHRAGA", "clue": "Olahraga untuk pertahanan diri"},
            {"kata": "PANAHAN", "kategori": "OLAHRAGA", "clue": "Olahraga dengan busur dan anak panah"},
            {"kata": "MEMANCING", "kategori": "HOBI", "clue": "Hobi menangkap ikan dengan kail"},
            {"kata": "BERKEBUN", "kategori": "HOBI", "clue": "Hobi merawat tanaman"},
            {"kata": "MEMBACA", "kategori": "HOBI", "clue": "Hobi membaca buku"},
            {"kata": "MENULIS", "kategori": "HOBI", "clue": "Hobi membuat tulisan"},
            
            # TRANSPORTASI & PERJALANAN (15 kata)
            {"kata": "MOBIL", "kategori": "TRANSPORTASI", "clue": "Kendaraan bermotor roda empat"},
            {"kata": "MOTOR", "kategori": "TRANSPORTASI", "clue": "Kendaraan bermotor roda dua"},
            {"kata": "BIS", "kategori": "TRANSPORTASI", "clue": "Kendaraan angkutan umum besar"},
            {"kata": "KERETA", "kategori": "TRANSPORTASI", "clue": "Kendaraan berjalan di rel"},
            {"kata": "PESAWAT", "kategori": "TRANSPORTASI", "clue": "Kendaraan yang terbang di udara"},
            {"kata": "KAPAL", "kategori": "TRANSPORTASI", "clue": "Kendaraan yang berlayar di air"},
            {"kata": "HELIKOPTER", "kategori": "TRANSPORTASI", "clue": "Pesawat dengan baling-baling atas"},
            {"kata": "SEPEDA", "kategori": "TRANSPORTASI", "clue": "Kendaraan dengan dua roda dikayuh"},
            {"kata": "TAKSI", "kategori": "TRANSPORTASI", "clue": "Kendaraan sewa dengan argometer"},
            {"kata": "TRUK", "kategori": "TRANSPORTASI", "clue": "Kendaraan pengangkut barang besar"},
            {"kata": "AMBULANS", "kategori": "TRANSPORTASI", "clue": "Kendaraan untuk pasien darurat"},
            {"kata": "PEMADAM", "kategori": "TRANSPORTASI", "clue": "Kendaraan untuk memadamkan api"},
            {"kata": "TRAVEL", "kategori": "PERJALANAN", "clue": "Perjalanan untuk wisata"},
            {"kata": "WISATA", "kategori": "PERJALANAN", "clue": "Kegiatan mengunjungi tempat menarik"},
            {"kata": "LIBURAN", "kategori": "PERJALANAN", "clue": "Waktu istirahat dari pekerjaan"},
            
            # PROFESI & PEKERJAAN (15 kata)
            {"kata": "DOKTER", "kategori": "PROFESI", "clue": "Profesi yang mengobati orang sakit"},
            {"kata": "GURU", "kategori": "PROFESI", "clue": "Profesi yang mengajar siswa"},
            {"kata": "PERAWAT", "kategori": "PROFESI", "clue": "Profesi yang merawat pasien"},
            {"kata": "POLISI", "kategori": "PROFESI", "clue": "Profesi yang menjaga keamanan"},
            {"kata": "TENTARA", "kategori": "PROFESI", "clue": "Profesi yang membela negara"},
            {"kata": "PILOT", "kategori": "PROFESI", "clue": "Profesi yang menerbangkan pesawat"},
            {"kata": "PENGACARA", "kategori": "PROFESI", "clue": "Profesi yang memberi bantuan hukum"},
            {"kata": "HAKIM", "kategori": "PROFESI", "clue": "Profesi yang memutuskan perkara"},
            {"kata": "JURNALIS", "kategori": "PROFESI", "clue": "Profesi yang meliput berita"},
            {"kata": "PROGRAMER", "kategori": "PROFESI", "clue": "Profesi yang membuat software"},
            {"kata": "ARSITEK", "kategori": "PROFESI", "clue": "Profesi yang merancang bangunan"},
            {"kata": "INSINYUR", "kategori": "PROFESI", "clue": "Profesi di bidang teknik"},
            {"kata": "AKUNTAN", "kategori": "PROFESI", "clue": "Profesi yang mengurus keuangan"},
            {"kata": "KOKI", "kategori": "PROFESI", "clue": "Profesi yang memasak makanan"},
            {"kata": "PENATA", "kategori": "PROFESI", "clue": "Profesi yang merias pengantin"},
            
            # MUSIK & SENI (15 kata)
            {"kata": "MUSIK", "kategori": "SENI", "clue": "Seni menyusun nada dan suara"},
            {"kata": "LAGU", "kategori": "SENI", "clue": "Komposisi musik dengan lirik"},
            {"kata": "NYANYI", "kategori": "SENI", "clue": "Aktivitas mengeluarkan suara bernada"},
            {"kata": "TARI", "kategori": "SENI", "clue": "Seni menggerakkan tubuh berirama"},
            {"kata": "DRAMA", "kategori": "SENI", "clue": "Seni peran di atas panggung"},
            {"kata": "FILM", "kategori": "SENI", "clue": "Karya seni audio-visual"},
            {"kata": "LUKIS", "kategori": "SENI", "clue": "Seni membuat gambar di kanvas"},
            {"kata": "PATUNG", "kategori": "SENI", "clue": "Seni membuat bentuk tiga dimensi"},
            {"kata": "FOTOGRAFI", "kategori": "SENI", "clue": "Seni mengambil gambar dengan kamera"},
            {"kata": "PIANO", "kategori": "ALAT MUSIK", "clue": "Alat musik dengan tuts hitam putih"},
            {"kata": "GUITAR", "kategori": "ALAT MUSIK", "clue": "Alat musik berdawai dengan bodi"},
            {"kata": "DRUM", "kategori": "ALAT MUSIK", "clue": "Alat musik pukul dengan membran"},
            {"kata": "FLUTE", "kategori": "ALAT MUSIK", "clue": "Alat musik tiup dengan lubang"},
            {"kata": "TRUMPET", "kategori": "ALAT MUSIK", "clue": "Alat musik tiup logam"},
            {"kata": "VIOLIN", "kategori": "ALAT MUSIK", "clue": "Alat musik gesek dengan empat senar"},
            
            # ALAM & LINGKUNGAN (15 kata)
            {"kata": "GUNUNG", "kategori": "ALAM", "clue": "Bukit yang sangat tinggi"},
            {"kata": "LAUT", "kategori": "ALAM", "clue": "Kumpulan air asin yang sangat luas"},
            {"kata": "SUNGAI", "kategori": "ALAM", "clue": "Aliran air tawar yang panjang"},
            {"kata": "DANAU", "kategori": "ALAM", "clue": "Genangan air tawar yang luas"},
            {"kata": "PANTAI", "kategori": "ALAM", "clue": "Pertemuan daratan dan laut"},
            {"kata": "HUTAN", "kategori": "ALAM", "clue": "Lahan dengan banyak pohon"},
            {"kata": "LEMBAH", "kategori": "ALAM", "clue": "Cekungan di antara pegunungan"},
            {"kata": "GUA", "kategori": "ALAM", "clue": "Lubang besar di dalam tanah atau batu"},
            {"kata": "AIRTERJUN", "kategori": "ALAM", "clue": "Air yang jatuh dari ketinggian"},
            {"kata": "MATAHARI", "kategori": "ALAM", "clue": "Bintang pusat tata surya kita"},
            {"kata": "BULAN", "kategori": "ALAM", "clue": "Satelit alami bumi"},
            {"kata": "BINTANG", "kategori": "ALAM", "clue": "Benda langit yang bersinar"},
            {"kata": "AWAN", "kategori": "ALAM", "clue": "Kumpulan uap air di langit"},
            {"kata": "HUJAN", "kategori": "ALAM", "clue": "Tetesan air dari awan"},
            {"kata": "ANGIN", "kategori": "ALAM", "clue": "Udara yang bergerak"},
        ]
    
    def mulai_game_baru(self):
        kata_data = random.choice(self.kata_list)
        self.kata_rahasia = kata_data["kata"]
        self.kata_tebakan = ["_" for _ in self.kata_rahasia]
        self.kesempatan = 6
        self.huruf_tertebak = set()
        self.kategori = kata_data["kategori"]
        self.clue = kata_data["clue"]
        return self.kata_tebakan
    
    def mulai_game_kata_sama(self):
        """Mulai lagi dengan kata yang sama"""
        self.kata_tebakan = ["_" for _ in self.kata_rahasia]
        self.kesempatan = 6
        self.huruf_tertebak = set()
        self.score = max(0, self.score - 50)
        return self.kata_tebakan
    
    def tebak_huruf(self, huruf):
        if huruf in self.huruf_tertebak:
            return "sudah"
        
        self.huruf_tertebak.add(huruf)
        
        if huruf in self.kata_rahasia:
            for i, char in enumerate(self.kata_rahasia):
                if char == huruf:
                    self.kata_tebakan[i] = huruf
            self.score += 10
            return "benar"
        else:
            self.kesempatan -= 1
            self.score -= 5
            if self.score < 0:
                self.score = 0
            return "salah"
    
    def tebak_kata(self, kata):
        if kata == self.kata_rahasia:
            self.kata_tebakan = list(self.kata_rahasia)
            self.score += 50
            return True
        else:
            self.kesempatan -= 2
            self.score -= 20
            if self.score < 0:
                self.score = 0
            return False
    
    def cek_menang(self):
        return "_" not in self.kata_tebakan
    
    def cek_kalah(self):
        return self.kesempatan <= 0

class AplikasiGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Game Tebak Kata - 100+ Kata")
        self.root.geometry("850x750")
        self.root.configure(bg="#1a1a2e")
        
        self.game = GameTebakKata()
        self.game_state = "playing"  # playing, won, lost
        
        # Font
        self.font_besar = font.Font(family="Arial", size=28, weight="bold")
        self.font_sedang = font.Font(family="Arial", size=16)
        self.font_kecil = font.Font(family="Arial", size=12)
        self.font_kata = font.Font(family="Courier New", size=36, weight="bold")
        
        self.setup_gui()
        self.mulai_game_baru()
    
    def setup_gui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg="#1a1a2e")
        main_frame.pack(fill="both", expand=True, padx=20, pady=15)
        
        # Header
        header_frame = tk.Frame(main_frame, bg="#1a1a2e")
        header_frame.pack(fill="x", pady=(0, 10))
        
        tk.Label(header_frame, text="🎯 GAME TEBAK KATA", 
                font=self.font_besar, fg="white", bg="#1a1a2e").pack()
        
        tk.Label(header_frame, text="100+ Kata - Teknologi, Budaya, Makanan, dan Lainnya!", 
                font=self.font_kecil, fg="#94a3b8", bg="#1a1a2e").pack(pady=(5, 0))
        
        # Info panel
        info_frame = tk.Frame(main_frame, bg="#0f3460", relief="flat")
        info_frame.pack(fill="x", pady=(0, 20))
        
        # Grid untuk info
        info_grid = tk.Frame(info_frame, bg="#0f3460")
        info_grid.pack(pady=15, padx=15)
        
        # Kategori
        tk.Label(info_grid, text="📁 KATEGORI:", 
                font=self.font_kecil, fg="#cbd5e1", bg="#0f3460").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.label_kategori = tk.Label(info_grid, text="", 
                font=self.font_kecil, fg="#8b5cf6", bg="#0f3460")
        self.label_kategori.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        # Clue
        tk.Label(info_grid, text="💡 PETUNJUK:", 
                font=self.font_kecil, fg="#cbd5e1", bg="#0f3460").grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.label_clue = tk.Label(info_grid, text="", 
                font=self.font_kecil, fg="#f472b6", bg="#0f3460", wraplength=300)
        self.label_clue.grid(row=0, column=3, padx=10, pady=5, sticky="w")
        
        # Score & Kesempatan
        score_frame = tk.Frame(info_grid, bg="#0f3460")
        score_frame.grid(row=0, column=4, padx=10, pady=5, sticky="w")
        
        tk.Label(score_frame, text="🏆 SCORE:", 
                font=self.font_kecil, fg="#cbd5e1", bg="#0f3460").pack(side="left")
        self.label_score = tk.Label(score_frame, text="0", 
                font=font.Font(family="Arial", size=20, weight="bold"), fg="#fbbf24", bg="#0f3460")
        self.label_score.pack(side="left", padx=(5, 15))
        
        tk.Label(score_frame, text="❤️ KESEMPATAN:", 
                font=self.font_kecil, fg="#cbd5e1", bg="#0f3460").pack(side="left")
        self.label_kesempatan = tk.Label(score_frame, text="6", 
                font=font.Font(family="Arial", size=18, weight="bold"), fg="#ef4444", bg="#0f3460")
        self.label_kesempatan.pack(side="left", padx=5)
        
        # Kata yang ditebak
        kata_frame = tk.Frame(main_frame, bg="#1a1a2e")
        kata_frame.pack(pady=(0, 25))
        
        self.label_kata = tk.Label(kata_frame, text="", 
                font=self.font_kata, fg="white", bg="#1a1a2e")
        self.label_kata.pack()
        
        # Huruf yang sudah ditebak
        self.label_huruf_tebakan = tk.Label(main_frame, text="Huruf yang sudah ditebak: -", 
                font=self.font_kecil, fg="#94a3b8", bg="#1a1a2e")
        self.label_huruf_tebakan.pack(pady=(0, 15))
        
        # KEYBOARD LENGKAP A-Z
        keyboard_frame = tk.Frame(main_frame, bg="#1a1a2e")
        keyboard_frame.pack(pady=(0, 20))
        
        tk.Label(keyboard_frame, text="⌨️ KEYBOARD VIRTUAL:", 
                font=self.font_sedang, fg="white", bg="#1a1a2e").pack(pady=(0, 10))
        
        self.letter_buttons = {}
        
        # Baris 1: A-M (13 huruf)
        row1 = tk.Frame(keyboard_frame, bg="#1a1a2e")
        row1.pack()
        
        for letter in "ABCDEFGHIJKLM":
            btn = tk.Button(row1, text=letter, width=3, height=1,
                          font=self.font_kecil, bg="#334155", fg="white",
                          activebackground="#475569", activeforeground="white",
                          relief="flat",
                          command=lambda l=letter: self.proses_tebak_huruf(l))
            btn.pack(side="left", padx=2, pady=2)
            self.letter_buttons[letter] = btn
        
        # Baris 2: N-Z (13 huruf)
        row2 = tk.Frame(keyboard_frame, bg="#1a1a2e")
        row2.pack()
        
        for letter in "NOPQRSTUVWXYZ":
            btn = tk.Button(row2, text=letter, width=3, height=1,
                          font=self.font_kecil, bg="#334155", fg="white",
                          activebackground="#475569", activeforeground="white",
                          relief="flat",
                          command=lambda l=letter: self.proses_tebak_huruf(l))
            btn.pack(side="left", padx=2, pady=2)
            self.letter_buttons[letter] = btn
        
        # Input tebak kata lengkap
        input_frame = tk.Frame(main_frame, bg="#1a1a2e")
        input_frame.pack(pady=(0, 20))
        
        tk.Label(input_frame, text="🔠 TEBAK KATA LENGKAP:", 
                font=self.font_kecil, fg="white", bg="#1a1a2e").pack(side="left", padx=(0, 10))
        
        self.entry_tebak_kata = tk.Entry(input_frame, font=self.font_kecil, width=25,
                                        bg="#334155", fg="white", insertbackground="white")
        self.entry_tebak_kata.pack(side="left", padx=(0, 10))
        self.entry_tebak_kata.bind("<Return>", lambda e: self.proses_tebak_kata())
        
        self.btn_tebak_kata = tk.Button(input_frame, text="🚀 Tebak", 
                font=self.font_kecil, bg="#10b981", fg="white",
                activebackground="#34d399", activeforeground="white",
                relief="flat",
                command=self.proses_tebak_kata)
        self.btn_tebak_kata.pack(side="left")
        
        # Frame untuk tombol aksi
        self.action_frame = tk.Frame(main_frame, bg="#1a1a2e")
        self.action_frame.pack()
        
        self.update_tombol_aksi()
    
    def update_tombol_aksi(self):
        # Hapus tombol lama
        for widget in self.action_frame.winfo_children():
            widget.destroy()
        
        if self.game_state == "playing":
            # Tombol saat bermain
            btn_frame1 = tk.Frame(self.action_frame, bg="#1a1a2e")
            btn_frame1.pack(pady=(0, 10))
            
            tk.Button(btn_frame1, text="🔄 Game Baru", 
                     font=self.font_kecil, bg="#3b82f6", fg="white",
                     activebackground="#60a5fa", activeforeground="white",
                     relief="flat", width=15, height=2,
                     command=self.mulai_game_baru).pack(side="left", padx=5)
            
            tk.Button(btn_frame1, text="💡 Bantuan", 
                     font=self.font_kecil, bg="#f59e0b", fg="white",
                     activebackground="#fbbf24", activeforeground="white",
                     relief="flat", width=15, height=2,
                     command=self.beri_bantuan).pack(side="left", padx=5)
            
            tk.Button(btn_frame1, text="🔍 Tampilkan Huruf", 
                     font=self.font_kecil, bg="#8b5cf6", fg="white",
                     activebackground="#a78bfa", activeforeground="white",
                     relief="flat", width=15, height=2,
                     command=self.tampilkan_satu_huruf).pack(side="left", padx=5)
            
            btn_frame2 = tk.Frame(self.action_frame, bg="#1a1a2e")
            btn_frame2.pack()
            
            tk.Button(btn_frame2, text="📊 Statistik", 
                     font=self.font_kecil, bg="#06b6d4", fg="white",
                     activebackground="#22d3ee", activeforeground="white",
                     relief="flat", width=15, height=2,
                     command=self.tampilkan_statistik).pack(side="left", padx=5)
            
            tk.Button(btn_frame2, text="❓ Cara Main", 
                     font=self.font_kecil, bg="#6366f1", fg="white",
                     activebackground="#818cf8", activeforeground="white",
                     relief="flat", width=15, height=2,
                     command=self.tampilkan_cara_bermain).pack(side="left", padx=5)
            
            tk.Button(btn_frame2, text="❌ Keluar", 
                     font=self.font_kecil, bg="#ef4444", fg="white",
                     activebackground="#f87171", activeforeground="white",
                     relief="flat", width=15, height=2,
                     command=self.root.quit).pack(side="left", padx=5)
        
        elif self.game_state == "won":
            # TAMPILAN SAAT MENANG
            win_frame = tk.Frame(self.action_frame, bg="#1a1a2e")
            win_frame.pack()
            
            tk.Label(win_frame, text="🎉 SELAMAT! KAMU MENANG!", 
                    font=self.font_sedang, fg="#10b981", bg="#1a1a2e").pack(pady=(0, 15))
            
            info_frame = tk.Frame(win_frame, bg="#1a1a2e")
            info_frame.pack(pady=(0, 20))
            
            tk.Label(info_frame, text=f"Kata: {self.game.kata_rahasia}", 
                    font=self.font_kecil, fg="white", bg="#1a1a2e").pack()
            tk.Label(info_frame, text=f"Score: +{self.game.score}", 
                    font=self.font_kecil, fg="#fbbf24", bg="#1a1a2e").pack()
            tk.Label(info_frame, text=f"Kesempatan tersisa: {self.game.kesempatan}", 
                    font=self.font_kecil, fg="#94a3b8", bg="#1a1a2e").pack()
            
            btn_frame = tk.Frame(win_frame, bg="#1a1a2e")
            btn_frame.pack(pady=(10, 0))
            
            # TOMBOL CONTINUE
            tk.Button(btn_frame, text="➡️ LANJUT (Kata Baru)", 
                     font=self.font_kecil, bg="#10b981", fg="white",
                     activebackground="#34d399", activeforeground="white",
                     relief="flat", width=20, height=2,
                     command=self.lanjut_game_baru).pack(side="left", padx=5)
            
            tk.Button(btn_frame, text="🔄 ULANGI Kata Ini", 
                     font=self.font_kecil, bg="#3b82f6", fg="white",
                     activebackground="#60a5fa", activeforeground="white",
                     relief="flat", width=20, height=2,
                     command=self.ulangi_kata_sama).pack(side="left", padx=5)
        
        elif self.game_state == "lost":
            # TAMPILAN SAAT KALAH
            lose_frame = tk.Frame(self.action_frame, bg="#1a1a2e")
            lose_frame.pack()
            
            tk.Label(lose_frame, text="😢 GAME OVER! KAMU KALAH!", 
                    font=self.font_sedang, fg="#ef4444", bg="#1a1a2e").pack(pady=(0, 15))
            
            info_frame = tk.Frame(lose_frame, bg="#1a1a2e")
            info_frame.pack(pady=(0, 20))
            
            tk.Label(info_frame, text=f"Kata yang benar: {self.game.kata_rahasia}", 
                    font=self.font_kecil, fg="white", bg="#1a1a2e").pack()
            tk.Label(info_frame, text=f"Score akhir: {self.game.score}", 
                    font=self.font_kecil, fg="#fbbf24", bg="#1a1a2e").pack()
            tk.Label(info_frame, text=f"Kategori: {self.game.kategori}", 
                    font=self.font_kecil, fg="#94a3b8", bg="#1a1a2e").pack()
            
            btn_frame = tk.Frame(lose_frame, bg="#1a1a2e")
            btn_frame.pack(pady=(10, 0))
            
            # TOMBOL RETRY
            tk.Button(btn_frame, text="🔄 COBA LAGI Kata Ini", 
                     font=self.font_kecil, bg="#ef4444", fg="white",
                     activebackground="#f87171", activeforeground="white",
                     relief="flat", width=20, height=2,
                     command=self.coba_lagi_kata_sama).pack(side="left", padx=5)
            
            tk.Button(btn_frame, text="🎮 Game Baru (Kata Lain)", 
                     font=self.font_kecil, bg="#3b82f6", fg="white",
                     activebackground="#60a5fa", activeforeground="white",
                     relief="flat", width=20, height=2,
                     command=self.mulai_game_baru).pack(side="left", padx=5)
    
    def mulai_game_baru(self):
        self.game_state = "playing"
        self.game.mulai_game_baru()
        self.update_tampilan()
        self.reset_keyboard()
        self.entry_tebak_kata.delete(0, tk.END)
        self.update_tombol_aksi()
    
    def lanjut_game_baru(self):
        """Continue setelah menang - kata baru"""
        self.mulai_game_baru()
        messagebox.showinfo("Lanjut Game", "Game baru dimulai dengan kata yang berbeda!")
    
    def ulangi_kata_sama(self):
        """Ulangi kata yang sama setelah menang"""
        self.game_state = "playing"
        # Simpan kata yang sama
        current_kata = self.game.kata_rahasia
        current_kategori = self.game.kategori
        current_clue = self.game.clue
        
        # Reset game state tapi tetap gunakan kata yang sama
        self.game.kata_rahasia = current_kata
        self.game.kata_tebakan = ["_" for _ in current_kata]
        self.game.kesempatan = 6
        self.game.huruf_tertebak = set()
        self.game.kategori = current_kategori
        self.game.clue = current_clue
        
        self.update_tampilan()
        self.reset_keyboard()
        self.entry_tebak_kata.delete(0, tk.END)
        self.update_tombol_aksi()
        
        messagebox.showinfo("Ulangi Kata", f"Tebak kata ini lagi: {current_kata}")
    
    def coba_lagi_kata_sama(self):
        """Coba lagi kata yang sama setelah kalah"""
        self.game_state = "playing"
        self.game.mulai_game_kata_sama()
        self.update_tampilan()
        self.reset_keyboard()
        self.entry_tebak_kata.delete(0, tk.END)
        self.update_tombol_aksi()
        
        messagebox.showinfo("Coba Lagi", f"Coba tebak kata ini lagi!\nScore dikurangi 50 poin.")
    
    def reset_keyboard(self):
        for letter, button in self.letter_buttons.items():
            button.config(bg="#334155", state="normal")
    
    def update_tampilan(self):
        # Update kata
        kata_display = " ".join(self.game.kata_tebakan)
        self.label_kata.config(text=kata_display)
        
        # Update info
        self.label_kategori.config(text=self.game.kategori)
        self.label_clue.config(text=self.game.clue)
        self.label_score.config(text=str(self.game.score))
        self.label_kesempatan.config(text=str(self.game.kesempatan))
        
        # Update huruf yang sudah ditebak
        huruf_tebakan = ", ".join(sorted(self.game.huruf_tertebak)) if self.game.huruf_tertebak else "-"
        self.label_huruf_tebakan.config(text=f"Huruf yang sudah ditebak: {huruf_tebakan}")
    
    def proses_tebak_huruf(self, huruf):
        if self.game_state != "playing":
            return
        
        # Nonaktifkan tombol
        self.letter_buttons[huruf].config(state="disabled")
        
        # Proses tebakan
        hasil = self.game.tebak_huruf(huruf)
        
        if hasil == "benar":
            self.letter_buttons[huruf].config(bg="#10b981")  # Hijau
            if self.game.cek_menang():
                self.game_state = "won"
                self.update_tombol_aksi()
        elif hasil == "salah":
            self.letter_buttons[huruf].config(bg="#ef4444")  # Merah
            if self.game.cek_kalah():
                self.game_state = "lost"
                self.update_tombol_aksi()
        
        self.update_tampilan()
    
    def proses_tebak_kata(self):
        if self.game_state != "playing":
            return
        
        kata = self.entry_tebak_kata.get().strip().upper()
        if not kata:
            messagebox.showwarning("Peringatan", "Masukkan kata terlebih dahulu!")
            return
        
        if self.game.tebak_kata(kata):
            self.game_state = "won"
            self.update_tombol_aksi()
        else:
            if self.game.cek_kalah():
                self.game_state = "lost"
                self.update_tombol_aksi()
            else:
                messagebox.showwarning("Salah!", f"Tebakan salah! Kesempatan berkurang 2.")
        
        self.update_tampilan()
        self.entry_tebak_kata.delete(0, tk.END)
    
    def beri_bantuan(self):
        if self.game_state != "playing":
            return
        
        # Tampilkan clue tambahan
        kata = self.game.kata_rahasia
        clue = f"Kata ini {len(kata)} huruf.\n"
        
        if kata[0] not in self.game.huruf_tertebak:
            clue += f"Huruf pertama: {kata[0]}\n"
        
        if kata[-1] not in self.game.huruf_tertebak:
            clue += f"Huruf terakhir: {kata[-1]}"
        
        self.game.score = max(0, self.game.score - 15)
        
        messagebox.showinfo("💡 Bantuan", clue)
        self.update_tampilan()
    
    def tampilkan_satu_huruf(self):
        if self.game_state != "playing":
            return
        
        # Cari huruf yang belum ditebak
        huruf_belum_ditebak = []
        for huruf in self.game.kata_rahasia:
            if huruf not in self.game.huruf_tertebak:
                huruf_belum_ditebak.append(huruf)
        
        if huruf_belum_ditebak:
            # Pilih huruf acak
            huruf_hint = random.choice(huruf_belum_ditebak)
            
            # Proses hint sebagai tebakan benar
            self.game.tebak_huruf(huruf_hint)
            
            # Update tombol keyboard
            self.letter_buttons[huruf_hint].config(
                bg="#f59e0b", 
                state="disabled"
            )
            
            # Kurangi score lebih banyak
            self.game.score = max(0, self.game.score - 30)
            
            # Update tampilan
            self.update_tampilan()
            
            # Cek apakah menang
            if self.game.cek_menang():
                self.game_state = "won"
                self.update_tombol_aksi()
        else:
            messagebox.showinfo("Info", "Semua huruf sudah tertebak!")
    
    def tampilkan_statistik(self):
        stats = f"🏆 Score: {self.game.score}\n"
        stats += f"📊 Kata saat ini: {self.game.kata_rahasia}\n"
        stats += f"📁 Kategori: {self.game.kategori}\n"
        stats += f"🔤 Huruf tertebak: {len(self.game.huruf_tertebak)}\n"
        stats += f"❤️ Kesempatan: {self.game.kesempatan}\n"
        stats += f"📝 Total kata tersedia: {len(self.game.kata_list)}"
        messagebox.showinfo("📊 Statistik Game", stats)
    
    def tampilkan_cara_bermain(self):
        cara_bermain = (
            "🎮 CARA BERMAIN\n"
            "="*40 + "\n"
            "1. Tebak kata berdasarkan KATEGORI dan PETUNJUK\n"
            "2. Klik huruf pada KEYBOARD VIRTUAL A-Z\n"
            "3. Atau ketik kata lengkap di kolom TEBAK KATA\n"
            "4. Kamu punya 6 kesempatan\n\n"
            "💡 FITUR BANTUAN:\n"
            "- Bantuan: Clue tambahan (-15 score)\n"
            "- Tampilkan Huruf: Buka 1 huruf acak (-30 score)\n\n"
            "⭐ MENANG/KALAH:\n"
            "- MENANG: Tombol LANJUT atau ULANGI kata\n"
            "- KALAH: Tombol COBA LAGI atau GAME BARU\n\n"
            "📚 TOTAL 100+ KATA dalam 10 kategori berbeda!"
        )
        messagebox.showinfo("📖 Panduan Bermain", cara_bermain)

def main():
    root = tk.Tk()
    app = AplikasiGame(root)
    
    # Center window
    root.update_idletasks()
    width = 850
    height = 750
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()

if __name__ == "__main__":
    main()