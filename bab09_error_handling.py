# ===== Jenis error yang sering muncul (hanya catatan) =====
# SyntaxError       -> print("hai"
# IndentationError  -> if x:
#                      print(x)        (tidak menjorok)
# NameError         -> print(skor_x)   (variabel belum dibuat)
# TypeError         -> "5" + 3
# ValueError        -> int("abc")
# ZeroDivisionError -> 10 / 0
# IndexError        -> [1, 2][5]
# KeyError          -> {"a": 1}["b"]

# ===== try - except - else - finally =====
try:
    angka = int(input("Masukkan angka: "))
    hasil = 100 / angka
except ValueError:
    print("Harus berupa angka!")
except ZeroDivisionError:
    print("Tidak bisa dibagi nol!")
else:
    print(f"Hasil: {hasil}")
finally:
    print("Selesai.")

# ===== raise =====
def set_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak valid")
    return umur

try:
    set_umur(-5)
except ValueError as e:
    print(f"Error: {e}")