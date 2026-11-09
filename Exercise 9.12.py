# Mengimpor class Admin dari modul admin.py
from Modul_admin2 import Admin

# Objek dari class Admin
my_admin = Admin("Najla", "Zahra", "admin_najla", 19, "Surakarta")

# Menguji fungsi-fungsinya
my_admin.describe_user()
my_admin.privileges.show_privileges(my_admin.username)