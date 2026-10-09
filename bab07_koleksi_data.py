# ===== List =====
nilai = [80, 65, 90]
nilai.append(75)
nilai.remove(65)
nilai[0] = 85

print(nilai)
print(nilai[-1], len(nilai))
print(sorted(nilai))

# ===== Tuple =====
titik = (3, 7)
warna = (255, 128, 0)

x, y = titik            # unpacking
print(f"x={x}, y={y}")
print(warna[0], len(warna))

try:
    titik[0] = 10       # tuple tidak bisa diubah -> TypeError
except TypeError as e:
    print("TypeError:", e)

# ===== Set =====
angka = {1, 2, 2, 3, 3, 3}
print(angka)

ipa = {"Ani", "Budi", "Citra"}
ips = {"Budi", "Dodi"}

print(ipa | ips)
print(ipa & ips)
print(ipa - ips)

# ===== Dictionary =====
siswa = {"nama": "Sari", "umur": 19}
siswa["kota"] = "Bandung"
siswa["umur"] = 20
print(siswa["nama"])
print(siswa.get("hobi", "-"))

for k, v in siswa.items():
    print(f"{k}: {v}")