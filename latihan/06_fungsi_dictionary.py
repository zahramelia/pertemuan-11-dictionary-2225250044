mahasiswa = {
    "nama": "Budi",
    "nilai": 90,
    "kelas": "A"
}
def tampilkan_data(data):
    for key, value in data.items():
        print(key, ":", value)

tampilkan_data(mahasiswa)
mahasiswa2 = {
    "nama": "Citra",
    "nilai": 88,
    "kelas": "B"
}

tampilkan_data(mahasiswa2)
def ubah_nilai(data, nilai_baru):
    data["nilai"] = nilai_baru

mahasiswa = {
    "nama": "Budi",
    "nilai": 90
}

ubah_nilai(mahasiswa, 95)
tampilkan_data(mahasiswa)
def tambah_mahasiswa(data, nama, nilai):
    data[nama] = nilai

daftar_nilai = {
    "Ayu": 85,
    "Budi": 95
}

tambah_mahasiswa(daftar_nilai, "Citra", 88)

print(daftar_nilai)
def hitung_rata_rata(data):
    if len(data) == 0:
        return 0

    return sum(data.values()) / len(data)


daftar_nilai = {
    "Ayu": 85,
    "Budi": 95,
    "Citra": 88
}

hasil = hitung_rata_rata(daftar_nilai)
print("Rata-rata nilai:", round(hasil, 2))
def tambah_nilai(data, nama, nilai):
    data[nama] = nilai

daftar_nilai = {
    "Ayu": 85,
    "Budi": 95
}

tambah_nilai(daftar_nilai, "Citra", 88)

print("Daftar nilai:", daftar_nilai)
print("Rata-rata:", round(hitung_rata_rata(daftar_nilai), 2))
def hapus_mahasiswa(data, nama):
    if nama in data:
        del data[nama]
        return True
    return False


daftar_nilai = {
    "Ayu": 85,
    "Budi": 95,
    "Citra": 88
}

berhasil = hapus_mahasiswa(daftar_nilai, "Doni")

print("Berhasil dihapus:", berhasil)
print("Daftar nilai:", daftar_nilai)
print("Jumlah mahasiswa:", len(daftar_nilai))