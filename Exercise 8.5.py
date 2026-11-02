# Mendefinisikan fungsi describe_city dengan country ber-nilai default 'Iceland'
def describe_city(city, country='Iceland'):
    """Menampilkan kalimat deskripsi kota dan negaranya."""
    print(f"{city.title()} is in {country.title()}.")

# Memanggil fungsi untuk tiga kota berbeda
describe_city('reykjavik')          # Menggunakan nilai default negara ('Iceland')
describe_city('akureyri')           # Menggunakan nilai default negara ('Iceland')
describe_city('paris', 'france')      # Menggunakan argumen negara kustom ('France')