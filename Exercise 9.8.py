# Program utama atau induk
class User:
    """Profil pengguna."""

    def __init__(self, first_name, last_name, username, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"\n--- Profil Pengguna: {self.username} ---")
        print(f"Nama Lengkap: {self.first_name} {self.last_name}")
        print(f"Usia        : {self.age} tahun")
        print(f"Lokasi      : {self.location}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang kembali.")


# Class baru untuk privilege
class Privileges:
    """Class terpisah untuk daftar hak akses."""

    def __init__(self):
        self.privileges = [
            "can add post", 
            "can delete post", 
            "can ban user"
        ]

    def show_privileges(self, username):
        """Cetak daftar hak akses."""
        print(f"\nDaftar Hak Akses (Privileges) untuk Admin @{username}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Program turunan menggunakan Composition
class Admin(User):
    """Akun admin yang menggunakan class Privileges (Composition)."""

    def __init__(self, first_name, last_name, username, age, location):
        super().__init__(first_name, last_name, username, age, location)
        
        # Instance dari class Privileges 
        self.privileges = Privileges()


# Objek class admin
admin_baru = Admin("Najla", "Zahra", "admin_najla", 19, "Surakarta")

# Memanggil method dari User
admin_baru.describe_user()

# Memanggil method show_privileges melalui objek Privileges di dalam admin
admin_baru.privileges.show_privileges(admin_baru.username)