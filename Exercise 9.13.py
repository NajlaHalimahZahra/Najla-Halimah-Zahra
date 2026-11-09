from random import randint

class Die:
    """Dadu."""

    def __init__(self, sides=6):
        """Inisialisasi jumlah sisi dadu (default 6 sisi)."""
        self.sides = sides

    def roll_die(self):
        """Menggulirkan dadu dan mencetak angka acak dari 1 sampai jumlah sisi."""
        x = randint(1, self.sides)
        print(f"Hasil guliran dadu {self.sides}-sisi: {x}")


# --- 1. Dadu 6-Sisi (Digulirkan 10 kali) ---
print("--- Menggulirkan Dadu 6-Sisi sebanyak 10 kali ---")
dadu_6 = Die()  # Menggunakan nilai default sides=6
for _ in range(10):
    dadu_6.roll_die()

# --- 2. Dadu 10-Sisi (Digulirkan 10 kali) ---
print("\n--- Menggulirkan Dadu 10-Sisi sebanyak 10 kali ---")
dadu_10 = Die(sides=10)
for _ in range(10):
    dadu_10.roll_die()

# --- 3. Dadu 20-Sisi (Digulirkan 10 kali) ---
print("\n--- Menggulirkan Dadu 20-Sisi sebanyak 10 kali ---")
dadu_20 = Die(sides=20)
for _ in range(10):
    dadu_20.roll_die()