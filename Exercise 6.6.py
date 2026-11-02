# 1. Dictionary berisi orang yang sudah mengisi polling beserta bahasa favoritnya
favorite_languages = {
    'Jericko': 'python',
    'Kiran': 'c',
    'Delila': 'c++',
    'Leo': 'python'
}

# 2. List daftar orang yang harus/akan di-check untuk polling
coders = ['Delila', 'Moza', 'Kiran', 'Saniya', 'Erlangga', 'Leo', 'Jericko']

# 3. Loop melalui setiap coder
for coder in coders:
    # Apakah nama coder sudah ada di dalam dictionary favorite_languages
    if coder in favorite_languages.keys():
        print(f"\nTerima kasih {coder.title()}, sudah meluangkan waktu untuk mengisi polling!")
    else:
        print(f"\nHalo {coder.title()}, silakan isi polling bahasa pemrograman favoritmu!")