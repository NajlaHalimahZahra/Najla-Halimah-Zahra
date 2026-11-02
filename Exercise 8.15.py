# Mengimpor modul yang sudah kita buat
import modul_fungsi

# Menyiapkan data awal
unprinted_designs = ['phone case', 'tumblr', 'kaos']
completed_models = []

# Memanggil fungsi menggunakan nama modul (dot notation)
modul_fungsi.print_models(unprinted_designs, completed_models)
modul_fungsi.show_completed_models(completed_models)