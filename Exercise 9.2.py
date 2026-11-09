class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
         """Inisialisasi nama restoran dan jenis masakan"""
         self.restaurant_name = restaurant_name
         self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Mencetak deskripsi restoran"""
        print(f"Restoran {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        """Mencetak pesan bahwa restoran sudah buka"""
        print(f"\n{self.restaurant_name} sudah buka!")

restaurant_1 = Restaurant("Niskala", "Mie Yamin Chili Oil")
restaurant_2 = Restaurant("Jowoan", "Pecel Pincuk")
restaurant_3 = Restaurant("Pojok Senja", "Nasi Goreng Seafood")



restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()