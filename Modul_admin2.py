# Mengimpor class User dari file/modul user.py
from Modul_user import User

class Privileges:
    """Class terpisah untuk mengelola daftar hak akses."""

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


class Admin(User):
    """Akun admin yang mewarisi User dari modul lain."""

    def __init__(self, first_name, last_name, username, age, location):
        super().__init__(first_name, last_name, username, age, location)
        self.privileges = Privileges()