# Impor class Admin dari modul admin.py
from Modul_admin import Admin

# Objek dari class Admin yang diimpor
my_admin = Admin("Najla", "Zahra", "admin_najla", 19, "Surakarta")

# Menguji method dari class induk dan komposisi
my_admin.describe_user()
my_admin.privileges.show_privileges(my_admin.username)