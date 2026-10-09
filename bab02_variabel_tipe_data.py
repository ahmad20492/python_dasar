# ===== Variabel =====
nama = "Budi"        # str
umur = 20            # int
tinggi = 170.5       # float
aktif = True         # bool

# nilai bisa diganti kapan saja
umur = umur + 1

# multiple assignment
x, y, z = 1, 2, 3
print(nama, umur, x + y + z)

# ===== Casting =====
angka = int("25")
print(angka + 5)
harga = float("12500.75")
print(type(harga))

umur = 20
print("Umur: " + str(umur))
print(bool(0), bool("hai"))

# ===== String =====
nama = "Python Dasar"
print(len(nama))
print(nama.upper())
print(nama[0:6])
print(nama.split(" "))

bab = 2
print(f"Belajar {nama} bab {bab}")