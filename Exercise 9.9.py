# Program utama
class Car:
    """Case berupa mobil."""

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()


# --- Class Komposisi (Battery) ---
class Battery:
    """Memodelkan baterai untuk mobil listrik."""

    def __init__(self, battery_size=40):
        """Inisialisasi ukuran baterai (default 40 kWh)."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Mencetak ukuran baterai."""
        print(f"Mobil ini memiliki baterai berkapasitas {self.battery_size}-kWh.")

    def get_range(self):
        """Memperkirakan jarak tempuh berdasarkan kapasitas baterai."""
        if self.battery_size == 40:
            range_km = 150
        elif self.battery_size == 65:
            range_km = 225
        else:
            range_km = 0

        print(f"Mobil ini dapat menempuh jarak sekitar {range_km} mil dengan sekali pengisian daya.")

    def upgrade_battery(self):
        """Memeriksa kapasitas baterai dan melakukan upgrade ke 65 jika belum."""
        if self.battery_size != 65:
            self.battery_size = 65
            print("Baterai berhasil di-upgrade menjadi 65 kWh!")
        else:
            print("Baterai sudah memiliki kapasitas maksimum.")


# Program turunan mobil listrik
class ElectricCar(Car):
    """Mobil listrik, turunan dari Car."""

    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        # Komposisi: Objek Battery dimasukkan sebagai atribut
        self.battery = Battery()



print("--- Membuat Mobil Listrik Baru ---")
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# Cek baterai dan jarak tempuh awal
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

print("\n--- Melakukan Upgrade Baterai ---")
# Upgrade baterai
my_leaf.battery.upgrade_battery()

# Cek ulang jarak tempuh setelah di-upgrade
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()