from pathlib import Path
import json

def get_stored_username(path):
    """Ambil username yang sudah tersimpan."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Minta username baru dari pengguna."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Menyapa pengguna dan memverifikasi identitasnya."""
    path = Path('username.json')
    username = get_stored_username(path)
    
    if username:
        # Verifikasi apakah benar user yang sama
        correct = input(f"Are you {username}? (y/n): ")
        if correct.lower() == 'y':
            print(f"Welcome back, {username}!")
        else:
            # Jika bukan orang yang sama, minta username baru
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()