import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining length
    all_characters = lowercase + uppercase + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password
    random.shuffle(password)

    return "".join(password)

# Main Program
print("=== Password Generator ===")

length = int(input("Enter password length: "))
password = generate_password(length)

print("\nGenerated Password:")
print(password)