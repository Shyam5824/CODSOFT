import random
import string
print("\t PASSWORD GENERATOR")
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    if length <= 6:
        print("Please enter a valid length greater than 6.")
        return 0
    password = generate_password(length)
    print("Generated Password:", password)

if __name__=="__main__":
    main()
