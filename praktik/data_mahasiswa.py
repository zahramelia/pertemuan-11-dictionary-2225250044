
# Praktik: Pengelolaan Data Mahasiswa menggunakan Dictionary

data_mahasiswa = {
    "23001": {"nama": "Andi", "nilai": 85},
    "23002": {"nama": "Budi", "nilai": 90},
    "23003": {"nama": "Citra", "nilai": 88},
    "23004": {"nama": "Dina", "nilai": 92},
    "23005": {"nama": "Eko", "nilai": 80}
}

# Menampilkan seluruh data mahasiswa

# Praktik: Pengelolaan Data Mahasiswa menggunakan Dictionary

data_mahasiswa = {
    "23001": {"nama": "Andi", "nilai": 85},
    "23002": {"nama": "Budi", "nilai": 90},
    "23003": {"nama": "Citra", "nilai": 88},
    "23004": {"nama": "Dina", "nilai": 92},
    "23005": {"nama": "Eko", "nilai": 80}
}

# Menampilkan seluruh data mahasiswa
print("=== DATA MAHASISWA ===")

for nim, data in data_mahasiswa.items():
    print("NIM:", nim)
    print("Nama:", data["nama"])
    print("Nilai:", data["nilai"])
    print("--------------------")

    
# Mencari mahasiswa berdasarkan NIM
print("\n=== PENCARIAN MAHASISWA ===")

nim_cari = input("Masukkan NIM yang dicari: ")

if nim_cari in data_mahasiswa:
    print("Nama:", data_mahasiswa[nim_cari]["nama"])
    print("Nilai:", data_mahasiswa[nim_cari]["nilai"])
else:
    print("Mahasiswa tidak ditemukan.")

    
# Menambahkan mahasiswa baru
print("\n=== TAMBAH MAHASISWA ===")

nim_baru = input("Masukkan NIM baru: ")

if nim_baru in data_mahasiswa:
    print("NIM sudah terdaftar!")
else:
    nama_baru = input("Masukkan nama mahasiswa: ")
    nilai_baru = float(input("Masukkan nilai mahasiswa: "))

    data_mahasiswa[nim_baru] = {
        "nama": nama_baru,
        "nilai": nilai_baru
    }

    print("Mahasiswa berhasil ditambahkan!")
    print("Data:", data_mahasiswa[nim_baru])


# Mengubah nilai mahasiswa
print("\n=== UBAH NILAI MAHASISWA ===")

nim_ubah = input("Masukkan NIM mahasiswa: ")

if nim_ubah in data_mahasiswa:
    nilai_baru = float(input("Masukkan nilai baru: "))

    data_mahasiswa[nim_ubah]["nilai"] = nilai_baru

    print("Nilai berhasil diubah!")
    print("Data terbaru:", data_mahasiswa[nim_ubah])
else:
    print("Mahasiswa tidak ditemukan.")


# Rekap data mahasiswa
print("\n=== REKAP DATA MAHASISWA ===")

total_nilai = 0

for nim, data in data_mahasiswa.items():
    print(
        "NIM:", nim,
        "| Nama:", data["nama"],
        "| Nilai:", data["nilai"]
    )
    total_nilai += data["nilai"]

jumlah_mahasiswa = len(data_mahasiswa)

if jumlah_mahasiswa > 0:
    rata_rata = total_nilai / jumlah_mahasiswa
    print("Jumlah mahasiswa:", jumlah_mahasiswa)
    print("Rata-rata nilai:", round(rata_rata, 2))
else:
    print("Belum ada data mahasiswa.")



