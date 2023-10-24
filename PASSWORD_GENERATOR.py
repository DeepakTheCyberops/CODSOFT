import random
import string

#Define the generate_password function for generating the password with the help of random module
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#Define the main function
def main():
    print("Password Generator")
    length = int(input("Enter the desired password length: "))
    
    password = generate_password(length)
    print("Generated Password: ", password)

if __name__ == "__main__":
    main()
