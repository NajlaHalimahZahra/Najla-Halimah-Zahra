class User:
    """Fitur percobaan login."""

    def __init__(self, first_name, last_name, username, age, location):
        """Inisialisasi atribut profil user, termasuk login_attempts dengan nilai 0."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location
        self.login_attempts = 0  # Nilai awal percobaan login adalah 0

    def describe_user(self):
        """Ringkasan informasi profil user."""
        print(f"\n--- Profil Pengguna: {self.username} ---")
        print(f"Nama Lengkap: {self.first_name} {self.last_name}")
        print(f"Usia        : {self.age} tahun")
        print(f"Lokasi      : {self.location}")

    def greet_user(self):
        """Pesan sambutan untuk user."""
        print(f"Halo, {self.first_name}! Selamat datang kembali.")

    def increment_login_attempts(self):
        """Menambahkan nilai login_attempts sebanyak 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Mengatur ulang nilai login_attempts menjadi 0."""
        self.login_attempts = 0


# --- Membuat Objek User ---
user_baru = User("Eljia", "Kyandara", "eljia98", 19, "Surakarta")

# Simulasikan beberapa kali percobaan login (misal: 3 kali)
user_baru.increment_login_attempts()
user_baru.increment_login_attempts()
user_baru.increment_login_attempts()

# Cetak jumlah percobaan login saat ini
print(f"Jumlah percobaan login (login attempts): {user_baru.login_attempts}")

# Reset kembali percobaan login
user_baru.reset_login_attempts()
print(f"Setelah di-reset, jumlah percobaan login: {user_baru.login_attempts}")