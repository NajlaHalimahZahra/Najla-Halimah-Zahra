# GABUNGAN 3 VERSI CARA KELUAR LOOP (EXERCISE 7.6)


# --- VERSI 1: Menggunakan Active Variable / Flag ---
print("=== 1: Menggunakan Active Variable (Flag) ===")
prompt = "\nMasukkan topping pizza:"
prompt += "\n(Ketik 'quit' untuk selesai) "

active = True
while active:
    topping = input(prompt)
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"Menambahkan {topping}!")


# --- VERSI 2: Menggunakan Break Statement ---
print("\n=== 2: Menggunakan Break Statement ===")
prompt = "\nMasukkan topping pizza:"
prompt += "\n(Ketik 'quit' untuk selesai) "

while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    else:
        print(f"Menambahkan {topping}!")


# --- VERSI 3: Menggunakan Kondisi pada While Statement ---
print("\n=== 3: Menggunakan Kondisi pada While Statement ===")
prompt = "\nMasukkan topping pizza:"
prompt += "\n(Ketik 'quit' untuk selesai) "

topping = ""
while topping.lower() != 'quit':
    topping = input(prompt)
    if topping.lower() != 'quit':
        print(f"Menambahkan {topping}!")

print("\nSelamat! Ketiga versi loop sudah selesai dijalankan.")