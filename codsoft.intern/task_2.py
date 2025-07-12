import random
import string

def generate_password():
    print("🔐 Password Generator")

    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print("Password should be at least 4 characters long.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

   
    characters = string.ascii_letters + string.digits + string.punctuation

    
    password = ''.join(random.choice(characters) for _ in range(length))

    print(f"Generated Password: {password}")


generate_password()
