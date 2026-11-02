# Mendefinisikan fungsi make_sandwich dengan parameter *toppings
def make_sandwich(*toppings):
    """Mencetak ringkasan topping sandwich yang dipesan."""
    print("\nMembuat sandwich dengan topping berikut:")
    for topping in toppings:
        print(f"- {topping}")

# Memanggil fungsi tiga kali dengan jumlah argumen yang berbeda-beda
make_sandwich('keju')
make_sandwich('smoked beef', 'keju', 'selada')
make_sandwich('ayam crispy', 'keju ekstra', 'tomat', 'saus sambal')