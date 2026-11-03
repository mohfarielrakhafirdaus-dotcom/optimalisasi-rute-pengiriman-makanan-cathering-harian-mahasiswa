# Kelompok 3 - Optimalisasi Rute dengan TSP

Program Python untuk mencari rute terpendek pengantaran dari **Dapur Utama** ke **Kos A sampai Kos E**, lalu kembali ke Dapur Utama, memakai metode **brute-force** (Traveling Salesman Problem).

## Cara Menjalankan

1. Pastikan Python sudah terinstal.
2. Instal library:
   ```
   pip install -r requirements.txt
   ```
3. Jalankan program:
   ```
   python tsp.py
   ```

## Hasil

```
Rute Perjalanan Terbaik: Dapur Utama -> Kos A -> Kos B -> Kos D -> Kos C -> Kos E -> Dapur Utama
Total Jarak Minimum: 25 km
```

## Mengubah Data

Ubah angka jarak (km) pada variabel `matriks_jarak` di file `tsp.py`.

## Catatan

Brute-force mencoba semua (n-1)! kemungkinan rute, sehingga hanya praktis untuk sekitar 10 lokasi atau kurang.
