# Mendefinisikan fungsi build_profile dengan **user_info
def build_profile(first, last, **user_info):
    """Membangun dictionary yang berisi segala hal tentang pengguna."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Memanggil fungsi build_profile dengan data diri dan keyword arguments tambahan
my_profile = build_profile(
    'Najla', 
    'Halimah Zahra', 
    major='Teknik Industri', 
    university='Institut Teknologi Bandung', 
    hobby='Reading'
)

# Mencetak hasil profile dictionary
print(my_profile)