import math
import time

class ColumnarTransposition:
    def __init__(self, key):
        self.key_str = key
        self.key_order = self._get_key_order(key)
        self.num_cols = len(key)

    def _get_key_order(self, key):
        indexed_key = [(int(k), i) for i, k in enumerate(key)]
        indexed_key.sort(key=lambda x: x[0])
        return [item[1] for item in indexed_key]

    def _create_matrix(self, text, num_cols, padding_char='X'):
        num_rows = math.ceil(len(text) / num_cols)
        padded_len = num_rows * num_cols
        padded_text = text.ljust(padded_len, padding_char)
        
        matrix = [
            list(padded_text[i:i + num_cols]) 
            for i in range(0, len(padded_text), num_cols)
        ]
        return matrix, padded_text

    def encrypt(self, plaintext, show_table=False):
        P = plaintext.replace(" ", "").upper()
        matrix, padded_P = self._create_matrix(P, self.num_cols)
        
        if show_table:
            self._print_matrix_table(self.key_str, matrix, "Matriks Enkripsi (Plaintext)")

        ciphertext = ""
        for col_index in self.key_order:
            for row in matrix:
                ciphertext += row[col_index]
        return ciphertext

    def decrypt(self, ciphertext, show_table=False):
        C_len = len(ciphertext)
        num_rows = math.ceil(C_len / self.num_cols)
        
        # Tentukan panjang setiap kolom. Beberapa kolom mungkin memiliki 1 baris ekstra
        # karena padding pada enkripsi.
        num_full_cols = C_len % self.num_cols
        if num_full_cols == 0:
            num_full_cols = self.num_cols
            
        col_lengths = [num_rows] * num_full_cols + [num_rows - 1] * (self.num_cols - num_full_cols)
        
        matrix = [['' for _ in range(self.num_cols)] for _ in range(num_rows)]
        c_pointer = 0
        
        # Isi matriks berdasarkan urutan kunci dan panjang kolom
        for i, col_index in enumerate(self.key_order):
            col_length = col_lengths[i]
            column_data = ciphertext[c_pointer:c_pointer + col_length]
            
            for row in range(len(column_data)):
                matrix[row][col_index] = column_data[row]
                
            c_pointer += col_length
            
        if show_table:
            self._print_matrix_table(self.key_str, matrix, "Matriks Dekripsi (Ciphertext)")
        
        plaintext = "".join(["".join(row) for row in matrix])
        return plaintext

    def _print_matrix_table(self, key, matrix, title):
        print(f"\n--- {title} ---")
        print(f"Kunci: {key}")
        print("--------------------")
        
        # Header
        key_list = [int(k) for k in key]
        order = [key_list[i] for i in self.key_order]
        header = "Kolom -> " + " ".join([str(k) for k in order])
        print(header)
        
        for row in matrix:
            print("         " + " ".join(row))
        print("--------------------")

class DoubleTranspositionCipher:
    def __init__(self, key1, key2):
        self.key1 = key1
        self.key2 = key2
        self._validate_keys()
        self.cipher1 = ColumnarTransposition(key1)
        self.cipher2 = ColumnarTransposition(key2)

    def _validate_keys(self):
        if len(self.key1) == len(self.key2):
            raise ValueError("Kedua kunci harus memiliki panjang yang berbeda.")
        if not self.key1.isdigit() or not self.key2.isdigit():
            raise ValueError("Kunci harus berupa string angka.")
        
        # Menambahkan validasi untuk memastikan angka dalam kunci unik
        if len(set(self.key1)) != len(self.key1) or len(set(self.key2)) != len(self.key2):
            raise ValueError("Angka dalam kunci harus unik.")

    def encrypt(self, plaintext, show_tables=True):
        start_time = time.time()
        
        print("\n=== Proses Enkripsi Ganda ===")
        print(f"Plaintext Asli: {plaintext}")
        print(f"Kunci 1: {self.key1}, Kunci 2: {self.key2}")
        
        # Tahap 1: Enkripsi dengan Kunci 1
        intermediate_ciphertext = self.cipher1.encrypt(plaintext, show_table=show_tables)
        print("\nHasil Tahap 1 (Enkripsi dengan Kunci 1):")
        print(f"Ciphertext 1: {intermediate_ciphertext}")
        
        # Tahap 2: Enkripsi dengan Kunci 2
        final_ciphertext = self.cipher2.encrypt(intermediate_ciphertext, show_table=show_tables)
        print("\nHasil Tahap 2 (Enkripsi dengan Kunci 2):")
        print(f"Ciphertext Final: {final_ciphertext}")
        
        end_time = time.time()
        duration = end_time - start_time
        print(f"\nWaktu Enkripsi: {duration:.6f} detik")
        return final_ciphertext

    def decrypt(self, ciphertext, show_tables=True):
        start_time = time.time()
        
        print("\n=== Proses Dekripsi Ganda ===")
        print(f"Ciphertext Asli: {ciphertext}")
        print(f"Kunci 1: {self.key1}, Kunci 2: {self.key2}")
        
        # Tahap 1: Dekripsi dengan Kunci 2
        intermediate_plaintext = self.cipher2.decrypt(ciphertext, show_table=show_tables)
        print("\nHasil Tahap 1 (Dekripsi dengan Kunci 2):")
        print(f"Plaintext 1 (dengan padding): {intermediate_plaintext}")

        # Tahap 2: Dekripsi dengan Kunci 1
        final_plaintext = self.cipher1.decrypt(intermediate_plaintext, show_table=show_tables)
        
        end_time = time.time()
        duration = end_time - start_time
        print(f"\nWaktu Dekripsi: {duration:.6f} detik")
        return final_plaintext.rstrip('X')

# --- Implementasi Program Utama ---

if __name__ == "__main__":
    try:
        # Input dari user
        plaintext_input = input("Masukkan plaintext: ")
        key1_input = input("Masukkan kunci pertama (contoh: 4312): ")
        key2_input = input("Masukkan kunci kedua (contoh: 53142): ")
        
        # Inisialisasi cipher ganda
        double_cipher = DoubleTranspositionCipher(key1_input, key2_input)
        
        # ENKRIPSI
        final_encrypted_text = double_cipher.encrypt(plaintext_input)
        
        print("\n--------------------")
        print(f"FINAL CIPHERTEXT: {final_encrypted_text}")
        print("--------------------")
        
        # DEKRIPSI
        final_decrypted_text = double_cipher.decrypt(final_encrypted_text)
        
        print("\n--------------------")
        print(f"FINAL DECRYPTED TEXT: {final_decrypted_text}")
        print("--------------------")

    except ValueError as e:
        print(f"Error: {e}")