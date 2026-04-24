import secrets
import string
import pyperclip

def generate_secure_pass(length = 16, use_symbols = True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += "@#$%^&*"

    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in "@#$%^&*" for c in password) if use_symbols else True

        if has_upper and has_lower and has_digit and has_symbol:
            return password
def main():
    print("===Secure Password Generator ===\n")

    length = int(input("Password length (default: 16): ") or 16)
    symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'
    count = int(input("how many password ? (default 1): ") or 1)

    print(f"\n Generated Password(s): ")

    print("-" * 40)

    passwords = []
    for i in range(count):
        pwd = generate_secure_pass(length, symbols)
        print(f"{i + 1}. {pwd}")
        passwords.append(pwd)

    if count == 1:
        pyperclip.copy(passwords[0])
        print("\n Password copied to clipboard!")
    else:
        pyperclip.copy('\n'.join(passwords))
        print("\n All Passwords copied to clipboard!")
    

if __name__ == "__main__":
    main()