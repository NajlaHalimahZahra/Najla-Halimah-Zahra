# 1. Membuat dictionary sungai dan negara
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

# 2. Loop untuk mencetak kalimat tentang setiap sungai dan negaranya
print("--- Informasi Sungai ---")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# 3. Loop untuk mencetak nama-nama sungai saja (.keys())
print("\n--- Daftar Sungai ---")
for river in rivers.keys():
    print(river.title())

# 4. Loop untuk mencetak nama-nama negara saja (.values())
print("\n--- Daftar Negara ---")
for country in rivers.values():
    print(country.title())