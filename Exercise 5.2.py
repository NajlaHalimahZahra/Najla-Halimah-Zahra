# 1. Tes kesamaan dan ketidaksamaan
food = 'Burger'

# Cek apakah makanan sama dengan 'Pizza', hasilnya False
print("Is food == 'Pizza'? So it's False.")
print(food == 'Pizza')  # Hasilnya: False

# Kalau mau yang hasilnya True, bandingkan dengan nilai yang sesuai
print("\nIs food == 'Burger'? So it's True.")
print(food == 'Burger')  # Hasilnya: True

# 2. Tes menggunakan metode lower()
name = 'Python'
print("\nIs name.lower() == 'python'? So it's True.")
print(name.lower() == 'python')

# 3. Tes angka (equality, inequality, greater than, less than, dll)
usia = 19
print("\nIs usia == 19? So it's True.")
print(usia == 19)

print("\nIs usia != 25? So it's True.")
print(usia != 25)

print("\nIs usia > 17? So it's True.")
print(usia > 17)

print("\nIs usia <= 18? So it's False.")
print(usia <= 18)


# 4. Tes menggunakan keyword 'and' dan 'or'
x = 15
print("\nIs x > 10 and x < 20? So it's True.")
print(x > 10 and x < 20)

print("\nIs x < 10 or x > 50? So it's False.")
print(x < 10 or x > 50)


# 5. Tes apakah item ada di dalam list (in)
colors = ['red', 'green', 'blue']
print("\nIs 'green' in colors? So it's True.")
print('green' in colors)


# 6. Tes apakah item tidak ada di dalam list (not in)
print("\nIs 'yellow' not in colors? So it's True.")
print('yellow' not in colors)