# Dictionary dengan list sebagai value
favorite_numbers = {
    'Gerry': [7, 12, 9],
    'Ailen': [3, 15],
    'Citra': [5, 21, 8, 10],
    'Binar': [4],
    'Raka': [18, 22]
}

# 2. Loop melalui dictionary favorite_numbers
for name, numbers in favorite_numbers.items():
    print(f"\nAngka favorit {name.title()} adalah:")
    for number in numbers:
        print(f"- {number}")