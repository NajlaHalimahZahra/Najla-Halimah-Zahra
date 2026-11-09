class Restaurant:
    """Modul untuk restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Kuliner: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} saat ini sedang BUKA!")