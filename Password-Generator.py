import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("---------------------")

    length = int(input("Enter password length: "))
    while length < 8:
        print("Password length should be at least 8 characters.")
        length = int(input("Enter password length: "))

    use_uppercase = input("Use uppercase letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Use numbers? (yes/no): ").lower() == "yes"
    use_special_chars = input("Use special characters? (yes/no): ").lower() == "yes"

    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
