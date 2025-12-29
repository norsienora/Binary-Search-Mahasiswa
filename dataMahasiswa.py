import random
import json

nama_depan = ["Andi", "Budi", "Citra", "Dewi", "Eka", "Fajri", "Gita", "Hadi", "Indah", "Joko", "Kurnia", "Laras", "Mawan", "Nanda", "Oki", "Putri", 
    "Rian", "Sari", "Taufik", "Vina", "Bambang", "Siti", "Agus", "Rina", "Doni", "Ahmad", "Bambang", "Cahyo", "Deddy", "Eko", "Farhan", "Guntur", 
    "Hendra", "Irfan", "Joko", "Kurniawan", "Lutfi", "Muhamad", "Nugroho", "Oki", "Purnomo", "Rizky", "Setyo", "Taufik", "Umar", "Aditya", "Bayu", 
    "Dimas", "Fajar", "Galang", "Hafiz", "Indra", "Kevin", "Lucky", "Mahendra", "Siti", "Ayu", "Dewi", "Lestari", "Putri", "Rina", "Sari", 
    "Wulandari", "Yuliana", "Zahra", "James", "Robert", "John", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles", 
    "Christopher", "Daniel", "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua", "Emma", "Olivia", "Sophia", "Isabella", 
    "Mia", "Charlotte", "Amelia", "Harper", "Evelyn", "Abigail"]

nama_belakang = ["Saputra", "Wijaya", "Lestari", "Pratama", "Kusuma", "Hidayat", "Putra", "Putri", "Santoso", "Wahyuni", "Setiawan", "Gunawan", 
    "Permata", "Habsari", "Maulana", "Nasution", "Siregar", "Simanjuntak", "Pasaribu", "Hasibuan", "Ginting", "Tarigan", "Sembiring", "Sinaga", 
    "pane", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", 
    "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Wong", "Chen", "Tan", "Lim", "Park", "Kim", "Sato", 
    "Suzuki", "Takahashi"]

prodi_list = ["Informatika", "Data Sains", "Teknologi Informasi", "Rekayasa Perangkat Lunak", "Electrical Energy Engineering", "Teknik Biomedis", 
    "Teknik Telekomunikasi", "Teknik Elektro", "Teknik Fisika", "Teknik Komputer", "Teknik Industri", "Sistem Informasi", "Digital Supply Chain", 
    "Manajemen Rekayasa Industri", "Akuntansi", "Manajemen", "Leisure Management", "Administrasi Bisnis", "Digital Business", "Ilmu Komunikasi", 
    "Digital Public Relation", "Digital Content Broadcasting", "Digital Psychology", "Visual Arts", "Desain Komunikasi Visual", 
    "Desain Produk & Inovasi", "Desain Interior", "Kriya", "Film dan Animasi", "Hospitality & Culinary Arts", "Digital Accounting", 
    "Digital Marketing", "Digital Creative Multimedia"]

mahasiswa = []
start_nim = 103012400001

for i in range(1000):
    first = random.choice(nama_depan)
    last = random.choice(nama_belakang)
    
    if i % 5 == 0:
        middle = random.choice(nama_depan)
        nama_lengkap = f"{first} {middle} {last}"
    else:
        nama_lengkap = f"{first} {last}"

    data = {
        "nim": start_nim + i,
        "nama": nama_lengkap,
        "prodi": random.choice(prodi_list)
    }
    mahasiswa.append(data)