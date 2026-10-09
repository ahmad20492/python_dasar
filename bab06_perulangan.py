# ===== for =====
for i in range(1, 4):
    print(f"Putaran ke-{i}")

buah = ["apel", "jeruk", "mangga"]
for b in buah:
    print(b.upper())

# ===== while =====
hitung = 3

while hitung > 0:
    print(f"Hitung mundur: {hitung}")
    hitung -= 1

print("Meluncur!")

# ===== break, continue, pass =====
for n in range(1, 10):
    if n == 3:
        continue      # lewati 3
    if n == 6:
        break         # berhenti di 6
    print(n)

for i in range(3):
    pass  # TODO: isi nanti