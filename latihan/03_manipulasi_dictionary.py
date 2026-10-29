
data = {
    "nama": "Ayu",
    "nilai": 85
}

# Menambahkan data kelas
data["kelas"] = "B"

# Mengubah nilai mahasiswa
data["nilai"] = 95

print("Setelah ditambah dan diubah:")
print(data)

# Menghapus data kelas
data.pop("kelas")

print("Setelah kelas dihapus:")
print(data)
