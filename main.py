import random
import hashlib
import string
import os

class PassGen:
    def generate_password(self):
        characters = string.ascii_letters + string.digits
        password_length = random.randint(10, 20)
        password = ''.join(random.choice(characters) for _ in range(password_length))
        return password

    def generate_wordlist(self, base_password, option=10):
        passwords = []

        #generate lowercase + uppercase
        for i in range(2 ** len(base_password)):
            password = ""
            for j in range(len(base_password)):
                if i & (1 << j):
                    password += base_password[j].upper()
                else:
                    password += base_password[j].lower()
            passwords.append(password)

        #generate dates on the sides of the password
        for year in range(1950, 2051):
            passwords.append(str(year) + base_password)
            passwords.append(base_password + str(year))

        #generate random letters & numbers with the password
        for _ in range(option):
            password = base_password
            for _ in range(random.randint(1, 5)):
                password = self.insert_random_letter(password)
                password = self.insert_random_number(password)
            passwords.append(password)

        return passwords

    def insert_random_letter(self, password):
        letter = random.choice(string.ascii_letters)
        position = random.randint(0, len(password))
        return password[:position] + letter + password[position:]

    def insert_random_number(self, password):
        number = random.choice(string.digits)
        position = random.randint(0, len(password))
        return password[:position] + number + password[position:]

    def hash_password(self, password, hash_option):
        if hash_option == "md5":
            hashed_password = hashlib.md5(password.encode()).hexdigest()
        elif hash_option == "sha1":
            hashed_password = hashlib.sha1(password.encode()).hexdigest()
        elif hash_option == "sha224":
            hashed_password = hashlib.sha224(password.encode()).hexdigest()
        elif hash_option == "sha256":
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
        elif hash_option == "sha384":
            hashed_password = hashlib.sha384(password.encode()).hexdigest()
        elif hash_option == "sha512":
            hashed_password = hashlib.sha512(password.encode()).hexdigest()
        else:
            hashed_password = None
        return hashed_password

    def create_password_list(self, base_password, option):
        num_passwords = 0
        if option == 1:
            num_passwords = 100000
        elif option == 2:
            num_passwords = 1000000
        elif option == 3:
            num_passwords = 3000000
        elif option == 4:
            num_passwords = 5000000
        elif option == 5:
            num_passwords = 10000000

        passwords = self.generate_wordlist(base_password, num_passwords)
        file_name = "password_list_{}.txt".format(base_password)
        with open(file_name, "w") as file:
            for password in passwords:
                file.write(password + "\n")
        print("Password list '{}' created.".format(file_name))


def main():
    generator = PassGen()

    print("PassGen Help Menu :")
    print("------------------")
    print("Available commands :")
    print("/gp (num) - Generate a list of random passwords")
    print("/ap - Display common admin passwords")
    print("/hash (password) (hash option) - Hash a password using MD5, SHA1, SHA224, SHA256, SHA384, or SHA512")
    print("/compass create (password) (option) - Create a list of passwords similar to the input password")
    print("Options: 1 (100,000), 2 (1,000,000), 3 (3,000,000), 4 (5,000,000), 5 (10,000,000)")
    print("/h - Show the help menu")
    print("/exit - Exit the program")

    while True:
        command = input("Enter a command: ").split()

        if not command:
            continue

        if command[0] == "/gp":
            num_passwords = 1
            if len(command) > 1:
                try:
                    num_passwords = int(command[1])
                except ValueError:
                    print("Invalid command. Please provide a valid number.")
                    continue

            if num_passwords == 1:
                password = generator.generate_password()
                print("Generated password:", password)
            else:
                passwords = []
                for _ in range(num_passwords):
                    password = generator.generate_password()
                    passwords.append(password)
                print("Generated passwords:")
                for password in passwords:
                    print(password)

        elif command[0] == "/hash":
            if len(command) > 2:
                password = command[1]
                hash_option = command[2]
                hashed_password = generator.hash_password(password, hash_option)
                if hashed_password:
                    print("Hashed password:", hashed_password)
                else:
                    print("Invalid hash option.")
            else:
                print("Invalid command. Please provide a password and a hash option.")

        elif command[0] == "/ap":
            admin_passwords = ["admin", "password", "1234", "public"]
            print("Common admin passwords:")
            for password in admin_passwords:
                print(password)

        elif command[0] == "/compass" and command[1] == "create":
            if len(command) > 3:
                base_password = command[2]
                option = int(command[3])
                generator.create_password_list(base_password, option)
            else:
                print("Invalid command. Please provide a base password and an option.")

        elif command[0] == "/h":
            print("PassGen Help Menu :")
            print("------------------")
            print("Available commands :")
            print("/gp (num) - Generate a list of random passwords")
            print("/ap - Display common admin passwords")
            print("/hash (password) (hash option) - Hash a password using MD5, SHA1, SHA224, SHA256, SHA384, or SHA512")
            print("/compass create (password) (option) - Create a list of passwords similar to the input password")
            print("Options: 1 (100,000), 2 (1,000,000), 3 (3,000,000), 4 (5,000,000), 5 (10,000,000)")
            print("/h - Show the help menu")
            print("/exit - Exit the program")

        elif command[0] == "/exit":
            break

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
