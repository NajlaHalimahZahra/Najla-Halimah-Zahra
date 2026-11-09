class User:
    """Representasi profil pengguna."""

    def __init__(self, first_name, last_name, username, age, location):
        """Inisialisasi profil user."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location

    def describe_user(self):
        """Cetak ringkasan informasi profil user."""
        print(f"\n--- Profil Pengguna: {self.username} ---")
        print(f"Nama Lengkap: {self.first_name} {self.last_name}")
        print(f"Usia        : {self.age} tahun")
        print(f"Lokasi      : {self.location}")

    def greet_user(self):
        """Cetak pesan sambutan personal untuk user."""
        print(f"Halo, {self.first_name} {self.last_name}! Mari menjelajah bersama kami.")


# --- Membuat Beberapa Objek (User) Berbeda ---

user_1 = User("Eljia", "Kyandara", "eljia98", 19, "Surakarta")
user_2 = User("Saga", "Pradipta", "sagapradipta", 26, "Bandung")
user_3 = User("Amara", "Ayodya", "aymara00", 19, "Yogyakarta")


# --- Memanggil method untuk masing-masing user ---

# User 1
user_1.describe_user()
user_1.greet_user()

# User 2
user_2.describe_user()
user_2.greet_user()

# User 3
user_3.describe_user()
user_3.greet_user()