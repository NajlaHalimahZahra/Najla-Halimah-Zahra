# --- Class Induk (User) ---
class User:
    """Model dasar untuk merepresentasikan profil pengguna."""

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


# --- Class Komposisi (Privileges) ---
class Privileges:
    """Class untuk mengelola daftar hak akses."""

    def __init__(self):
        self.privileges = [
            "can add post", 
            "can delete post", 
            "can ban user"
        ]

    def show_privileges(self, username):
        print(f"\nDaftar Hak Akses (Privileges) untuk Admin @{username}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# --- Class Turunan (Admin) ---
class Admin(User):
    """Akun admin yang mewarisi User dan menggunakan Privileges."""

    def __init__(self, first_name, last_name, username, age, location):
        super().__init__(first_name, last_name, username, age, location)
        self.privileges = Privileges()