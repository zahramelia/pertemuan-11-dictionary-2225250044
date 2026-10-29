
# Pertemuan 11 - Dictionary/Map

**Nama:** Zahra Amelia
**NIM:** 2225250044
**Kelas:** 3B

## Tujuan

Mempelajari penggunaan Dictionary/Map dalam Python untuk menyimpan, mencari, menambah, mengubah, dan menampilkan data mahasiswa.

## Struktur Data

Program menggunakan dictionary bersarang (*nested dictionary*). NIM menjadi key utama, sedangkan data nama, kelas, dan nilai disimpan sebagai value.

Contoh struktur data:

```python
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}
```

## Cara Menjalankan

Buka terminal pada folder utama proyek, kemudian jalankan perintah:

```bash
py praktik/data_mahasiswa.py
```

## Test Case

| No. | Pengujian | Input/Aksi | Hasil yang Diharapkan |
|---|---|---|---|
| 1 | Pencarian mahasiswa | A003 | Data Citra ditemukan |
| 2 | Pencarian tidak ditemukan | A999 | Pesan data tidak ditemukan |
| 3 | Mengubah nilai | A002 menjadi 82 | Nilai Budi berubah menjadi 82 |
| 4 | Menambah mahasiswa | A006 | Data mahasiswa baru ditambahkan |
| 5 | Menampilkan rekap | Menggunakan items() | Seluruh data mahasiswa ditampilkan |

## Refleksi

Salah satu kesalahan yang dapat terjadi adalah mengakses key yang tidak tersedia sehingga menimbulkan KeyError. Kesalahan ini dapat dihindari dengan memeriksa keberadaan key menggunakan operator `in` atau menggunakan method `get()`.

