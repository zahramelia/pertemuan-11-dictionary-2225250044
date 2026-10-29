siswa = {
    "siswa1": {
        "nama": "Ayu",
        "nilai": 85
    },
    "siswa2": {
        "nama": "Budi",
        "nilai": 90
    }
}

print(siswa["siswa1"]["nama"])
print(siswa["siswa2"]["nilai"])
print(siswa["siswa1"]["nilai"])
siswa["siswa2"]["nilai"] = 95

print(siswa["siswa2"]["nilai"])
siswa["siswa3"] = {
    "nama": "Citra",
    "nilai": 88
}

print(siswa["siswa3"]["nama"])
print(siswa["siswa3"]["nilai"])
for id_siswa, detail in siswa.items():
    print("ID:", id_siswa)
    print("Nama:", detail["nama"])
    print("Nilai:", detail["nilai"])
    print("---")
    print(siswa["siswa3"]["nilai"] + 12)
    total = 0

for detail in siswa.values():
    total += detail["nilai"]

rata_rata = total / len(siswa)

print("Rata-rata nilai:", round(rata_rata, 2))
del siswa["siswa3"]

print(siswa)
print("Jumlah siswa:", len(siswa))
print("siswa1" in siswa)
print("siswa3" in siswa)
data_dihapus = siswa.pop("siswa1")

print("Data yang dihapus:", data_dihapus)
print("Data siswa sekarang:", siswa)
print("Jumlah siswa:", len(siswa))
print(siswa.get("siswa2"))
print(siswa.get("siswa1", "Data tidak ditemukan"))
siswa["siswa3"] = {
    "nama": "Citra",
    "nilai": 88
}

print(siswa)
print("Jumlah siswa:", len(siswa))
print("Nilai Citra:", siswa.get("siswa3", {}).get("nilai"))