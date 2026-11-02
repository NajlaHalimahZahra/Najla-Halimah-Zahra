# 1. List usernames dengan 'admin'
usernames = ['admin', 'Saga', 'Arka', 'Rey', 'Fares']

# 2. Loop melalui list usernames
for username in usernames:
    # 3. Cek apakah username adalah admin atau bukan
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")