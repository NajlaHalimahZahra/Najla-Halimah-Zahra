class Restaurant:
    """Simulasi restoran sederhana."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi atribut restaurant_name, cuisine_type, dan number_served (default 0)."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Nilai default awal adalah 0

    def describe_restaurant(self):
        """Mencetak ringkasan informasi restoran."""
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Kuliner: {self.cuisine_type}")
        print(f"Jumlah Pelanggan yang Dilayani: {self.number_served}")

    def open_restaurant(self):
        """Cetak pesan bahwa restoran sedang buka."""
        print(f"{self.restaurant_name} saat ini sedang BUKA!\n")


# --- Membuat Objek Restaurant ---
restaurant = Restaurant("Restoran Niskala", "Mie Yamin Chili Oil")

# 1. Mencetak nilai default number_served langsung
print(f"Jumlah awal pelanggan yang dilayani: {restaurant.number_served}")

# 2. Mengubah nilai number_served secara langsung dari luar
restaurant.number_served = 35
print(f"Jumlah pelanggan setelah diubah langsung: {restaurant.number_served}")

# 3. Memanggil describe_restaurant untuk melihat semua informasi terbaru
print("-" * 35)
restaurant.describe_restaurant()