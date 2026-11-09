# --- Parent Class (Class Induk) ---
class Restaurant:
    """Simulasi restoran sederhana."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Kuliner: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} saat ini sedang BUKA!")


# --- Child Class (Class Turunan) menggunakan Inheritance ---
class IceCreamStand(Restaurant):
    """Merepresentasikan kedai es krim, sebagai turunan dari Restaurant."""

    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        """Inisialisasi atribut dari Parent Class, ditambah atribut flavors."""
        super().__init__(restaurant_name, cuisine_type)
        # Menambahkan atribut khusus untuk kedai es krim
        self.flavors = [
            "Double Choco",
            "Vanila Cookies and Cream",
            "Matcha Taro",
            "Strawberry Peach",
        ]

    def display_flavors(self):
        """Cetak daftar rasa es krim yang tersedia."""
        print(f"\nDaftar es krim di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# --- Objek dari Child Class (IceCreamStand) ---
my_ice_cream_stand = IceCreamStand("Sweet Treats")

# Memanggil method dari Parent Class
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.open_restaurant()

# Memanggil method khusus dari Child Class
my_ice_cream_stand.display_flavors()