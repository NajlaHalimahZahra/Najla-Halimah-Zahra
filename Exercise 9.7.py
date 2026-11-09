# Induk program
class User:
    """Model dasar untuk merepresentasikan profil pengguna."""

    def __init__(self, first_name, last_name, username, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n--- Profil Pengguna: {self.username} ---")
        print(f"Nama Lengkap: {self.first_name} {self.last_name}")
        print(f"Usia        : {self.age} tahun")
        print(f"Lokasi      : {self.location}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang kembali.")


# Program turunan
class Admin(User):
    """Akun admin khusus dengan hak akses tertentu."""

    def __init__(self, first_name, last_name, username, age, location):
        """Inisialisasi atribut User ditambah atribut privileges."""
        super().__init__(first_name, last_name, username, age, location)
        
        # Atribut khusus Admin berupa list hak akses
        self.privileges = [
            "can add post", 
            "can delete post", 
            "can ban user", 
            "can approve comments"
        ]

    def show_privileges(self):
        """Cetak daftar hak istimewa admin."""
        pass  # nanti diisi di bawah, ini cuma placeholder biar rapi

# Versi rapi 
class Admin(User):
    def __init__(self, first_name, last_name, username, age, location):
        super().__init__(first_name, last_name, username, age, location)
        self.privileges = [
            "can add post", 
            "can delete post", 
            "can ban user"
        ]

    def show_privileges(self):
        print(f"\nDaftar Hak Akses (Privileges) untuk Admin @{self.username}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Objek program induk
admin_pertama = Admin("Najla", "Zahra", "admin_najla", 19, "Surakarta")

# Memanggil method dari program induk (user)
admin_pertama.describe_user()
admin_pertama.greet_user()

# Memanggil method khusus dari program turunan (admin)
admin_pertama.show_privileges()