# List usernames sengaja dikosongkan untuk menguji kondisi else# List usernames (coba kosongkan list ini untuk mengetes kondisi if)
usernames = []

# Cek apakah list tidak kosong
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
