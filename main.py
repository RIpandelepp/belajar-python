nama = input("Masukkan nama: ")
nilai = int(input("Masukkan nilai: "))

if nilai >= 75:
    status = "Lulus"
else:
    status = "Tidak lulus"

print(f"\nNama   : {nama}")
print(f"Nilai  : {nilai}")
print(f"Status : {status}")
