# Columnar-Transposition-Cipher-V.2
Selamat Datang Di Proyek ini.Proyek ini mengimplementasikan algoritma enkripsi Double Columnar Transposition Cipher menggunakan Python. Cipher ini merupakan pengembangan dari Columnar Transposition Cipher sederhana, di mana plaintext dienkripsi dua kali berturut-turut dengan dua kunci yang berbeda.

# 📝 Fitur
- Enkripsi Ganda: Plaintext dienkripsi pertama kali dengan key1, dan hasilnya dienkripsi lagi dengan key2.

- Dekripsi Ganda: Proses kebalikan dari enkripsi, di mana ciphertext didekripsi terlebih dahulu dengan key2, kemudian hasilnya didekripsi lagi dengan key1.

- Validasi Kunci: Program melakukan validasi untuk memastikan kedua kunci memiliki panjang yang berbeda dan terdiri dari angka unik.

- Visualisasi Proses: Menampilkan tabel susunan matriks pada setiap tahap enkripsi dan dekripsi untuk mempermudah pemahaman alur kerja cipher.

- Pengukuran Waktu: Menghitung dan menampilkan durasi waktu (dalam detik) yang dibutuhkan untuk proses enkripsi dan dekripsi.

# ⚙️ Cara Penggunaan
1. Prasyarat
    - Python 3.x

2. Menjalankan Program

      - Clone repositori ini:
          git clone https:
    
            //github.com/nama-pengguna/nama-proyek.git cd nama-proyek
      
      - Jalankan skrip Python:
          
            python DoubleTranspositionCipher.py

3. Ikuti petunjuk yang muncul di konsol untuk memasukkan plaintext, kunci pertama, dan kunci kedua.

# 🤖Contoh Output:
 contoh output dari program:
 
                    Masukkan plaintext: Transposition Cipher
                    Masukkan kunci pertama (contoh: 4312): 4562
                    Masukkan kunci kedua (contoh: 53142): 53142
                    
                    === Proses Enkripsi Ganda ===
                    Plaintext Asli: Transposition Cipher
                    Kunci 1: 4562, Kunci 2: 53142
                    
                    --- Matriks Enkripsi (Plaintext) ---
                    Kunci: 4562
                    --------------------
                    Kolom -> 2 4 5 6
                             T R A N
                             S P O S
                             I T I O
                             N C I P
                             H E R X
                    --------------------
                    
                    Hasil Tahap 1 (Enkripsi dengan Kunci 1):
                    Ciphertext 1: NSOPXTSINHRPTCEAOIIR
                    
                    --- Matriks Enkripsi (Plaintext) ---
                    Kunci: 53142
                    --------------------
                    Kolom -> 1 2 3 4 5
                             N S O P X
                             T S I N H
                             R P T C E
                             A O I I R
                    --------------------
                    
                    Hasil Tahap 2 (Enkripsi dengan Kunci 2):
                    Ciphertext Final: OITIXHERSSPOPNCINTRA
                    
                    Waktu Enkripsi: 0.042853 detik
                    
                    --------------------
                    FINAL CIPHERTEXT: OITIXHERSSPOPNCINTRA
                    --------------------
                    
                    === Proses Dekripsi Ganda ===
                    Ciphertext Asli: OITIXHERSSPOPNCINTRA
                    Kunci 1: 4562, Kunci 2: 53142
                    
                    --- Matriks Dekripsi (Ciphertext) ---
                    Kunci: 53142
                    --------------------
                    Kolom -> 1 2 3 4 5
                             N S O P X
                             T S I N H
                             R P T C E
                             A O I I R
                    --------------------
                    
                    Hasil Tahap 1 (Dekripsi dengan Kunci 2):
                    Plaintext 1 (dengan padding): NSOPXTSINHRPTCEAOIIR
                    
                    --- Matriks Dekripsi (Ciphertext) ---
                    Kunci: 4562
                    --------------------
                    Kolom -> 2 4 5 6
                             T R A N
                             S P O S
                             I T I O
                             N C I P
                             H E R X
                    --------------------
                    
                    Waktu Dekripsi: 0.033973 detik
                    
                    --------------------
                    FINAL DECRYPTED TEXT: TRANSPOSITIONCIPHER
                    --------------------

# 🧠 Bagaimana Cara Kerjanya?
Proyek ini menggunakan dua kelas utama:

- `ColumnarTransposition` : Mengimplementasikan cipher kolom tunggal. Kelas ini bertanggung jawab untuk mengubah plaintext menjadi matriks, membaca kolom berdasarkan kunci untuk enkripsi, dan sebaliknya untuk dekripsi.

- `DoubleTranspositionCipher` : Mengelola alur kerja utama dengan mengintegrasikan dua objek ColumnarTransposition. Kelas ini mengkoordinasikan proses enkripsi dan dekripsi ganda, serta menangani validasi dan pengukuran waktu.

Metode dekripsi telah diperbaiki untuk secara cerdas menangani padding yang tidak beraturan, memastikan dekripsi dapat dilakukan dengan sukses meskipun panjang teks perantara tidak habis dibagi oleh panjang kunci kedua.
