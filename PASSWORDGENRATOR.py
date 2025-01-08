import random
import string

def generate_password(length, use_special_chars=True):
    """Generate a random password."""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ""
    all_characters = lowercase + uppercase + digits + special_chars
    if length < 8:
        print("Warning: Password length should be at least 8 characters for better security.")
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            # Get user input for the password length
            length = int(input("Enter the desired length of your password: "))
            
            if length < 4:
                print("Password length should be at least 4 characters. Please try again.")
                continue
            special_chars_choice = input("Include special characters? (yes/no): ").lower()
            use_special_chars = special_chars_choice in ['yes', 'y']

            # Generate the password
            password = generate_password(length, use_special_chars)

            # Display the generated password
            print("\nGenerated Password: ", password)

            again = input("\nDo you want to generate another password? (yes/no): ").lower()
            if again not in ['yes', 'y']:
                print("THANK YOU FOR USING THE APPLICATION..!")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number for password length.")

# Run the password generator
if __name__ == "__main__":
    main()

